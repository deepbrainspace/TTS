#!/bin/bash
set -e  # Exit on any error

# Download models first
mkdir -p models
python3 scripts/download_models.py

# Stop any existing containers
docker compose down --remove-orphans

# Start docker containers
docker compose up --build -d

echo -e "\nSetup complete! The TTS service should be available at http://localhost:5002"
