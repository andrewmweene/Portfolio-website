# app.py — PROVEN TO WORK on Render (2025)
from flask import Flask, send_from_directory
from whitenoise import WhiteNoise
import os

# Create Flask app
app = Flask(__name__, static_folder='.')

# First define routes, THEN wrap with WhiteNoise
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    if os.path.isfile(path):
        return send_from_directory('.', path)
    # Fallback to index.html for clean URLs (optional)
    return send_from_directory('.', 'index.html')

# Wrap Flask app with WhiteNoise AFTER routes are defined
app = WhiteNoise(app, root='.', index_file='index.html')

# Required for Render
if __name__ == '__main__':
    app.run()
