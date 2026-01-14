#!/bin/bash
# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p ~/.streamlit/

# Create Streamlit config file
echo "\
[server]\n\nheadless = true\nport = $PORT\nenableCORS = false\n\n" > ~/.streamlit/config.toml
