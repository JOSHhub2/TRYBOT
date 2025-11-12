#!/bin/bash

# Check if app.py exists
if [ -f "app.py" ]; then
    echo "Starting app.py..."
    python3 app.py
# Else check if bot.py exists
elif [ -f "bot.py" ]; then
    echo "Starting bot.py..."
    python3 bot.py
else
    echo "No bot file found!"
    exit 1
fi
