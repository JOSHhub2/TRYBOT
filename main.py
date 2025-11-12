from flask import Flask, request, redirect, send_from_directory, render_template
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploaded"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Serve upload page
@app.route("/")
def index():
    return render_template("index.html")

# Handle file upload
@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files.get("file")
    if file and file.filename.endswith(".py"):
        filepath = os.path.join(UPLOAD_FOLDER, "app.py")
        file.save(filepath)

        # Kill previous running app.py if exists
        subprocess.call("pkill -f uploaded/app.py", shell=True)

        # Run new uploaded app.py
        subprocess.Popen(["python3", filepath])

        return f"File uploaded and running: {file.filename}"
    return "Invalid file"

if __name__ == "__main__":
    # If uploaded app.py exists, run it, otherwise run main.py default logic
    uploaded_path = os.path.join(UPLOAD_FOLDER, "app.py")
    if os.path.exists(uploaded_path):
        subprocess.Popen(["python3", uploaded_path])
    app.run(host="0.0.0.0", port=10000)
