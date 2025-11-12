from flask import Flask, render_template
import subprocess, os

app = Flask(__name__)
process = None

@app.route('/')
def home():
    status = "✅ Running" if process and process.poll() is None else "❌ Stopped"
    return render_template('index.html', status=status)

@app.route('/start')
def start_bot():
    global process
    if not process or process.poll() is not None:
        process = subprocess.Popen(['python3', 'bot.py'])
    return "Bot started!"

@app.route('/stop')
def stop_bot():
    global process
    if process:
        process.terminate()
        process = None
    return "Bot stopped!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
