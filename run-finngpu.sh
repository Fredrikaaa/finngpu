#!/bin/bash

# Set up logging and directories
LOG_DIR=~/finngpu/logs
LOG_FILE="${LOG_DIR}/finngpu_$(date +\%Y-\%m-\%d).log"
LISTINGS_DIR=~/finngpu/listings
SCRIPT_DIR=~/finngpu
VENV_DIR="$SCRIPT_DIR/venv"

# Analysis files
CURRENT_ANALYSIS="$LISTINGS_DIR/analysis_$(date +\%Y-\%m-\%d).csv"
PREVIOUS_ANALYSIS="$LISTINGS_DIR/analysis_$(date -d "yesterday" +\%Y-\%m-\%d).csv"
LAST_KNOWN_GOOD="$LISTINGS_DIR/last_known_good.csv"

# Email configuration
EMAIL_TO="fredrik2401@gmail.com"
EMAIL_SUBJECT_PREFIX="[FinnGPU]"

# Required Python packages
REQUIRED_PACKAGES=(
    "beautifulsoup4"
    "pandas"
    "requests"
    "tqdm"
)

# Required system packages
SYSTEM_PACKAGES=(
    "python3-full"
    "python3-venv"
)

# Analysis settings
MAX_DEALS_TO_SHOW=5             # Maximum number of deals to show in notification

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to send email
send_email() {
    local subject="$1"
    local body="$2"
    local priority="$3"  # normal or high

    # Add timestamp to email body
    local dated_body="Report Time: $(date '+%Y-%m-%d %H:%M:%S')\nServer: $(hostname)\n\n${body}"
    
    # Create email headers
    local headers=""
    if [ "$priority" == "high" ]; then
        headers="Subject: $subject\nX-Priority: 1\n\n"
    else
        headers="Subject: $subject\n\n"
    fi

    # Log the email
    log "EMAIL - $subject: $body"
    
    # Send the email using msmtp
    {
        echo -e "$headers"
        echo -e "$dated_body"
    } | msmtp "$EMAIL_TO"
    
    if [ $? -eq 0 ]; then
        log "Email sent successfully to $EMAIL_TO"
    else
        log "ERROR: Failed to send email"
    fi
}

# Function to analyze changes in GPU deals
analyze_changes() {
    local current="$1"
    local previous="$2"
    local max_deals="$3"

    # Check if current file exists
    if [ ! -f "$current" ]; then
        log "ERROR: Current analysis file not found"
        return 1
    fi

    # If no previous analysis exists, save current as last known good and exit
    if [ ! -f "$previous" ]; then
        cp "$current" "$LAST_KNOWN_GOOD"
        log "No previous analysis found. Saving current as baseline."
        send_email \
            "$EMAIL_SUBJECT_PREFIX Initial GPU Analysis" \
            "First run completed. Saved baseline for future comparison." \
            "normal"
        return 0
    fi

    # Create temporary files for processing
    local temp_dir=$(mktemp -d)
    local current_top="$temp_dir/current_top.csv"
    local previous_top="$temp_dir/previous_top.csv"

    # Extract headers and top entries from both files
    head -n $((max_deals + 1)) "$current" > "$current_top"
    head -n $((max_deals + 1)) "$previous" > "$previous_top"

    # Compare files
    if ! diff -q "$current_top" "$previous_top" >/dev/null; then
        # Files are different, analyze the changes
        log "Detected changes in top GPU deals"
        
        # Create email message
        local message="New GPU Deals Detected\n\nTop $max_deals current best deals:\n\n"
        
        # Add comparison with previous analysis
        message+="Changes from previous analysis:\n"
        diff --suppress-common-lines -y "$previous_top" "$current_top" | \
            grep -v "model,price" > "$temp_dir/diff_output.txt" || true
        
        if [ -s "$temp_dir/diff_output.txt" ]; then
            message+="$(cat "$temp_dir/diff_output.txt")\n\n"
        fi
        
        message+="Current top deals:\n\n"
        
        # Add current top deals
        while IFS=, read -r model price fps price_per_fps url; do
            # Skip header line
            if [[ "$model" != "model" ]]; then
                # Format price and metrics nicely
                price_formatted=$(printf "%.0f" "$price")
                fps_formatted=$(printf "%.1f" "$fps")
                priceperfps_formatted=$(printf "%.2f" "$price_per_fps")
                
                message+="Model: $model\n"
                message+="Price: ${price_formatted} NOK\n"
                message+="FPS (1440p): $fps_formatted\n"
                message+="Price/FPS: $priceperfps_formatted NOK\n"
                message+="URL: $url\n\n"
            fi
        done < "$current_top" | head -n $(((max_deals * 6)))

        # Send email notification
        send_email \
            "$EMAIL_SUBJECT_PREFIX New GPU Deals Available" \
            "$message" \
            "normal"

        # Update last known good
        cp "$current" "$LAST_KNOWN_GOOD"
    else
        log "No significant changes in GPU deals"
    fi

    # Cleanup
    rm -rf "$temp_dir"
}

# Function to check if a package is installed in the system
check_system_package() {
    dpkg -l "$1" &>/dev/null
    return $?
}

# Function to ensure system dependencies are installed
ensure_system_dependencies() {
    log "Checking system dependencies..."
    
    local PACKAGES_TO_INSTALL=()

    # Check which packages need to be installed
    for package in "${SYSTEM_PACKAGES[@]}"; do
        if ! check_system_package "$package"; then
            PACKAGES_TO_INSTALL+=("$package")
        else
            log "$package is already installed"
        fi
    done

    # Install missing packages if any
    if [ ${#PACKAGES_TO_INSTALL[@]} -ne 0 ]; then
        log "Installing missing system packages: ${PACKAGES_TO_INSTALL[*]}"
        sudo apt-get update
        sudo apt-get install -y "${PACKAGES_TO_INSTALL[@]}"
        if [ $? -ne 0 ]; then
            log "ERROR: Failed to install system packages"
            exit 1
        fi
    fi
}

# Function to setup virtual environment
setup_venv() {
    # Check if venv already exists
    if [ ! -d "$VENV_DIR" ]; then
        log "Creating virtual environment..."
        python3 -m venv "$VENV_DIR"
        if [ $? -ne 0 ]; then
            log "ERROR: Failed to create virtual environment"
            exit 1
        fi
    fi

    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    if [ $? -ne 0 ]; then
        log "ERROR: Failed to activate virtual environment"
        exit 1
    fi
    log "Virtual environment activated"

    # Upgrade pip in virtual environment
    log "Upgrading pip..."
    pip install --upgrade pip
    if [ $? -ne 0 ]; then
        log "ERROR: Failed to upgrade pip"
        exit 1
    fi

    # Install required packages in virtual environment
    log "Installing required Python packages..."
    for package in "${REQUIRED_PACKAGES[@]}"; do
        log "Installing $package..."
        pip install "$package"
        if [ $? -ne 0 ]; then
            log "ERROR: Failed to install $package"
            exit 1
        fi
    done
}

# Main script execution
cd "$SCRIPT_DIR" || {
    log "ERROR: Could not change to script directory $SCRIPT_DIR"
    exit 1
}

# Ensure system dependencies are installed
ensure_system_dependencies

# Setup and activate virtual environment
setup_venv

# Run the main script
log "Starting FinnGPU script"
python finngpu.py \
    -b blacklist.txt \
    -w whitelist.txt \
    2>&1 | tee -a "$LOG_FILE"

FINNGPU_EXIT_CODE=${PIPESTATUS[0]}

# Check if the script ran successfully
if [ $FINNGPU_EXIT_CODE -eq 0 ]; then
    # Move the generated CSV file to listings directory
    newest_csv=$(ls -t finn_gpu_listings_*.csv 2>/dev/null | head -n1)
    if [ -n "$newest_csv" ]; then
        mv "$newest_csv" "$LISTINGS_DIR/"
        log "Successfully moved $newest_csv to $LISTINGS_DIR"
        
        # Run analysis on the new data
        log "Running GPU analysis"
        python gpu_analysis.py \
            -f "$LISTINGS_DIR/$newest_csv" \
            -p "1440p-ultra-performance.csv" \
            -c "$CURRENT_ANALYSIS" \
            2>&1 | tee -a "$LOG_FILE"
        
        if [ $? -eq 0 ]; then
            # Analyze changes and send notifications if needed
            analyze_changes \
                "$CURRENT_ANALYSIS" \
                "$PREVIOUS_ANALYSIS" \
                "$MAX_DEALS_TO_SHOW"
        else
            log "ERROR: GPU analysis script failed"
            send_email \
                "$EMAIL_SUBJECT_PREFIX ERROR - Analysis Failed" \
                "The GPU analysis script failed to complete. Check the logs for more details." \
                "high"
        fi
    else
        log "WARNING: No CSV file was generated"
        send_email \
            "$EMAIL_SUBJECT_PREFIX WARNING - No Data" \
            "No CSV file was generated during the GPU listing collection" \
            "high"
    fi
else
    log "ERROR: FinnGPU script failed with exit code $FINNGPU_EXIT_CODE"
    send_email \
        "$EMAIL_SUBJECT_PREFIX ERROR - Script Failed" \
        "The FinnGPU script failed to complete with exit code $FINNGPU_EXIT_CODE" \
        "high"
fi

# Deactivate virtual environment
deactivate
log "Virtual environment deactivated"

log "Script execution completed"
