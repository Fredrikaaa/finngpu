#!/bin/bash

# Set the base directory to the script's parent directory for relative paths
BASE_DIR="$(dirname "$(dirname "$(realpath "$0")")")"
FINNGPU_WWW="/var/www/finngpu"  # Web directory
DATA_DIR="$FINNGPU_WWW/data"    # Data directory now inside finngpu
ANALYSIS_FILE="$FINNGPU_WWW/analysis.csv"
PREV_ANALYSIS_FILE="$FINNGPU_WWW/analysis_prev.csv"
CURRENT_ANALYSIS="$ANALYSIS_FILE"
VENV_DIR="$BASE_DIR/.venv"
EMAIL="email@mail.com"
REQUIREMENTS="$BASE_DIR/requirements.txt"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check dependencies
DEPENDENCIES=("python3" "mail")
for dep in "${DEPENDENCIES[@]}"; do
    if ! command_exists "$dep"; then
        echo "Error: '$dep' is not installed. Please install it and rerun the script."
        exit 1
    fi
done

# Set web directory permissions early
sudo chown -R $USER:gpudata "$FINNGPU_WWW"
sudo chmod -R 775 "$FINNGPU_WWW"

# Function to setup virtual environment
setup_venv() {
    # Check if venv already exists
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
        source "$VENV_DIR/bin/activate"
        echo "Installing requirements..."
        pip install -r "$REQUIREMENTS"
    else
        source "$VENV_DIR/bin/activate"
    fi
}

setup_venv

# Create directories if they don't exist
mkdir -p "$DATA_DIR"

# Find the newest CSV file in the data directory
newest_csv=$(ls -t "$DATA_DIR"/*.csv 2>/dev/null | head -n 1)

# Check if the newest CSV file exists
if [[ -z "$newest_csv" ]]; then
    echo "Error: No CSV file found in $DATA_DIR."
    exit 1
fi

# Run finngpu.py with blacklist and whitelist parameters
cd "$BASE_DIR"
python3 finngpu.py -b blacklist.txt -w whitelist.txt

# Run price_analysis.py with the specified parameters
python3 price_analysis.py -f "$newest_csv" -p "$BASE_DIR/1440p-ultra-performance.csv" -c "$CURRENT_ANALYSIS" --min-fps 10

# Run csv_to_html.py
cd "$FINNGPU_WWW"
echo "Generating HTML table..."
python3 csv_to_html.py

# Modified permissions section (remove sudo)
chgrp gpudata "$ANALYSIS_FILE" "$FINNGPU_WWW/table.html"
chmod 664 "$ANALYSIS_FILE" "$FINNGPU_WWW/table.html"

# Check for differences in top ten ads
if [[ -f "$ANALYSIS_FILE" ]]; then
    # If previous analysis exists, compare it
    if [[ -f "$PREV_ANALYSIS_FILE" ]]; then
        # Extract top ten ads (excluding the header) from current and previous analysis files
        CURRENT_TOP_TEN=$(head -n 11 "$ANALYSIS_FILE" | tail -n 10)
        PREV_TOP_TEN=$(head -n 11 "$PREV_ANALYSIS_FILE" | tail -n 10)

        # Compare the top ten entries
        if [[ "$CURRENT_TOP_TEN" != "$PREV_TOP_TEN" ]]; then
            # If there are changes, send email notification
            echo "Top 10 ads have changed. Sending notification."
            #mail -s "GPU Price/Performance Update" "$EMAIL" < "$ANALYSIS_FILE"
        else
            echo "No changes in the top 10 ads."
        fi
    else
        echo "Previous analysis file not found. Skipping comparison."
    fi

    # Update the previous analysis file with the current run's output
    cp "$ANALYSIS_FILE" "$PREV_ANALYSIS_FILE"
else
    echo "Current analysis file not found. Exiting."
    exit 1
fi
