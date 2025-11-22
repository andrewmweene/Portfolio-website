# app.py — works perfectly on Render, Railway, Fly.io
from flask import Flask, send_from_directory, abort
from whitenoise import WhiteNoise
import os

# Create Flask app
app = Flask(__name__)

# Serve all static files from the root folder
app = WhiteNoise(app, root='.', index_file='index.html')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    if os.path.isfile(path):
        return send_from_directory('.', path)
    else:
        # Fallback to index.html for SPA-style routing (optional)
        return send_from_directory('.', 'index.html')

# Required for Render
if __name__ == '__main__':
    app.run()
