from flask import Flask, send_from_directory
try:
    from flask_frozen import Freezer
except Exception:
    Freezer = None

app = Flask(__name__, static_folder='.')

# Serve all your HTML files
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_page(path):
    return send_from_directory('.', path)

# Optional: auto-generate static build
freezer = Freezer(app) if Freezer is not None else None

if __name__ == '__main__':
    if freezer is not None:
        # Use Freezer to generate static build
        freezer.run(debug=True)
    else:
        # Frozen-Flask not installed: run the normal Flask dev server instead
        print("Warning: 'Frozen-Flask' not installed. Running Flask dev server.\nInstall with: python -m pip install Frozen-Flask")
        app.run(debug=True)