#!/bin/bash
# main.sh
# This script runs main.py for four target hosts (one on each continent)
# and saves the output to separate text files.
# It uses the 'timeout' command to stop the ping after a fixed duration (10 seconds).

# Adjust the Python command if needed. For Windows, if using Git Bash, try "py -3" instead of "python3".
PYTHON_CMD="py -3"  # Change this if necessary (e.g., "python3" or "python") 

echo "Pinging facebook.com .. *** START **** Test "
timeout 10 $PYTHON_CMD main.py facebook.com
echo "Pinging facebook.com .. *** COMPLETE **** Test"

# North America (e.g., google.com)
echo "Pinging google.com (North America)..."
timeout 10 $PYTHON_CMD main.py google.com > output_google.txt
echo "Output for google.com saved in output_google.txt"

# Europe (e.g., bbc.co.uk)
echo "Pinging bbc.co.uk (Europe)..."
timeout 10 $PYTHON_CMD main.py bbc.co.uk > output_bbc.txt
echo "Output for bbc.co.uk saved in output_bbc.txt"

# Asia (e.g., baidu.com)
echo "Pinging baidu.com (Asia)..."
timeout 10 $PYTHON_CMD main.py baidu.com > output_baidu.txt
echo "Output for baidu.com saved in output_baidu.txt"

# South America (e.g., uol.com.br)
echo "Pinging uol.com.br (South America)..."
timeout 10 $PYTHON_CMD main.py uol.com.br > output_uol.txt
echo "Output for uol.com.br saved in output_uol.txt"

echo "All pings completed."
