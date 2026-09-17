from pathlib import Path

from flask import Flask, abort, redirect, request, send_from_directory
from whitenoise import WhiteNoise
import os

BASE_DIR = Path(__file__).resolve().parent
ROOT_FILES = {
    'about.html',
    'Andrew_Mweene_Resume.pdf',
    'index.html',
    'projects.html',
    'script.js',
    'styles.css',
}
IMAGE_EXTENSIONS = {'.gif', '.jpeg', '.jpg', '.png', '.webp'}
SECURITY_HEADERS = {
    'Content-Security-Policy': (
        "default-src 'self'; "
        "base-uri 'self'; object-src 'none'; frame-ancestors 'none'; "
        "script-src 'self'; style-src 'self' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com; "
        "img-src 'self' https://cdn.simpleicons.org https://images.credly.com; "
        "connect-src 'self'; form-action 'self' mailto:"
    ),
    'Strict-Transport-Security': 'max-age=63072000; includeSubDomains; preload',
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Permissions-Policy': 'camera=(), microphone=(), geolocation=()',
}

flask_app = Flask(__name__, static_folder=None)


@flask_app.before_request
def redirect_http_requests():
    if os.getenv('FORCE_HTTPS') == '1' and request.headers.get('X-Forwarded-Proto', 'https') == 'http':
        return redirect(request.url.replace('http://', 'https://', 1), code=308)


@flask_app.after_request
def add_security_headers(response):
    for name, value in SECURITY_HEADERS.items():
        response.headers[name] = value
    return response


def add_static_security_headers(headers, path, url_prefix):
    for name, value in SECURITY_HEADERS.items():
        headers[name] = value

# First define routes, THEN wrap with WhiteNoise
@flask_app.route('/')
def home():
    return send_from_directory(BASE_DIR, 'index.html')


@flask_app.route('/<path:path>')
def serve_file(path):
    requested = Path(path)
    if any(part.startswith('.') for part in requested.parts):
        abort(404)
    if requested.parts and requested.parts[0] == 'images':
        if requested.suffix.lower() not in IMAGE_EXTENSIONS:
            abort(404)
    elif path not in ROOT_FILES:
        abort(404)
    full_path = (BASE_DIR / requested).resolve()
    if BASE_DIR not in full_path.parents or not full_path.is_file():
        abort(404)
    return send_from_directory(BASE_DIR, requested.as_posix())

# Wrap Flask app with WhiteNoise AFTER routes are defined
app = WhiteNoise(
    flask_app,
    root=str(BASE_DIR),
    index_file='index.html',
    add_headers_function=add_static_security_headers,
)

# Required for Render
if __name__ == '__main__':
    flask_app.run()
