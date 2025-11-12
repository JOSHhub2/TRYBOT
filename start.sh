#!/bin/bash

# If uploaded app.py exists, run it
if [ -f "uploaded/app.py" ]; then
    echo "Running uploaded app.py..."
    python3 uploaded/app.py
else
    echo "No uploaded app.py, running default main.py"
    python3 main.py
fi
