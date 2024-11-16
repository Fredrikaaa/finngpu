#!/bin/bash

# Set the base directory to the script's parent directory for relative paths
BASE_DIR="$(dirname "$(dirname "$(realpath "$0")")")"
DATA_DIR="$BASE_DIR/data"
ANALYSIS_FILE="$BASE_DIR/analysis.csv"
PREV_ANALYSIS_FILE="$BASE_DIR/analysis_prev.csv"
CURRENT_ANALYSIS="$ANALYSIS_FILE"  # Output file for price analysis
VENV_DIR="$BASE_DIR/venv"
EMAIL="email@mail.com"

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check dependencies
DEPENDENCIES=("python3" "mail") # Add "mail" if using mail to notify
for dep in "${DEPENDENCIES[@]}"; do
    if ! command_exists "$dep"; then
        echo "Error: '$dep' is not installed. Please install it and rerun the script."
        exit 1
    fi
done

# Function to setup virtual environment
setup_venv() {
    # Check if venv already exists
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
        if [ $? -ne 0 ]; then
            echo "ERROR: Failed to create virtual environment"
            exit 1
        fi
    fi

    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to activate virtual environment"
        exit 1
    fi
    echo "Virtual environment activated"

    # Upgrade pip in virtual environment
    echo "Upgrading pip..."
    pip install --upgrade pip
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to upgrade pip"
        exit 1
    fi

    # Install required packages in virtual environment
    echo "Installing required Python packages..."
    for package in "${REQUIRED_PACKAGES[@]}"; do
        echo "Installing $package..."
        pip install "$package"
        if [ $? -ne 0 ]; then
            echo "ERROR: Failed to install $package"
            exit 1
        fi
    done
}
setup_venv
# Find the newest CSV file in the data directory
newest_csv=$(ls -t "$DATA_DIR"/*.csv | head -n 1)

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
sudo chgrp gpudata "$ANALYSIS_FILE"
sudo chmod 664 "$ANALYSIS_FILE"
python3 /var/www/finngpu/csv_to_html.py
sudo chgrp gpudata /var/www/finngpu/table.html
sudo chmod 664 /var/www/finngpu/table.html


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
            mail -s "GPU Price/Performance Update" "$EMAIL" < "$ANALYSIS_FILE"
        else
            echo "No changes in the top 10 ads."
        fi
    else
        echo "Previous analysis file not found. Skipping comparison."
    fi

    # Update the previous analysis file with the current run’s output
    cp "$ANALYSIS_FILE" "$PREV_ANALYSIS_FILE"
else
    echo "Current analysis file not found. Exiting."
    exit 1
fi
