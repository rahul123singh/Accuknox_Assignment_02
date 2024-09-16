#!/bin/bash

# Define directories
SOURCE_DIR="/d/Accuknox_Assignment"
BACKUP_DIR="/d/Backup_Files"
LOG_FILE="$BACKUP_DIR/backup_report.log"

# Timestamp for the backup folder and log entry
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Create a new directory for the backup with timestamp
BACKUP_PATH="$BACKUP_DIR/backup_$(date +"%Y%m%d_%H%M%S")"
mkdir -p "$BACKUP_PATH"

# Start logging
echo "[$timestamp] Starting backup from $SOURCE_DIR to $BACKUP_PATH" >> "$LOG_FILE"

# Copy files from source to backup directory
cp -r "$SOURCE_DIR"/* "$BACKUP_PATH/" >> "$LOG_FILE" 2>&1

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "[$timestamp] Backup successful! Backup stored at: $BACKUP_PATH" >> "$LOG_FILE"
else
    echo "[$timestamp] Backup failed." >> "$LOG_FILE"
fi

# Add a new line for readability in the log file
echo "" >> "$LOG_FILE"
