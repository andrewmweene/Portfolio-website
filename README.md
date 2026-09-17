# Andrew Buumba Mweene Portfolio

Personal portfolio website for Andrew Buumba Mweene, a Software Engineer from Zambia.

Live site: [portfolio-website-vezc.onrender.com](https://portfolio-website-vezc.onrender.com)

## Overview

This is a small static portfolio served by Flask and WhiteNoise. The frontend uses semantic HTML, plain CSS, and a small vanilla JavaScript file for the responsive navigation menu. There is no frontend framework, database, authentication system, or build step.

The site includes:

- Responsive hero section with Andrew's profile photo
- About section and verified technology stack
- Credly certification cards for Cisco IT Essentials and CCNA: Introduction to Networks
- Projects and GitHub links
- What I do section
- Contact details and a mailto contact form
- Security headers and restricted static-file serving

## Project Structure

| File or directory | Purpose |
| --- | --- |
| `index.html` | Main portfolio page |
| `about.html` | About page |
| `projects.html` | Projects page |
| `styles.css` | Shared responsive styling and design tokens |
| `script.js` | Mobile navigation behavior |
| `app.py` | Flask/WhiteNoise application and security configuration |
| `images/` | Local portfolio images |
| `Andrew_Mweene_Resume.pdf` | Downloadable resume |
| `requirements.txt` | Pinned Python runtime dependencies |
| `SECURITY.md` | Vulnerability reporting instructions |
| `.env.example` | Environment variable template |
| `.github/dependabot.yml` | Weekly Python dependency update checks |

## Local Development

### Requirements

- Python 3.10 or newer
- A modern web browser

### Setup

Create and activate a virtual environment, then install the pinned dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS/Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Start the development server:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

For a production-style local server, use Gunicorn where available:

```bash
gunicorn app:app
```

## Deployment

The project is configured for a Python web service such as Render. Use this production start command:

```bash
gunicorn app:app
```

Set this environment variable in the hosting provider:

```text
FORCE_HTTPS=1
```

The Flask app redirects forwarded HTTP requests to HTTPS and adds security headers to dynamic and static responses.

## Contact Form

The contact form currently uses the browser's `mailto:` handler and sends messages to `mweeeneandrew8@gmail.com`. It does not store submissions on the server.

The form includes browser-side required fields and length limits. A server-backed form service, server-side validation, rate limiting, and CAPTCHA protection can be added later if a hosted submission endpoint is selected.

## External Services

The frontend loads only the following third-party assets:

- Google Fonts for typography
- Simple Icons CDN for technology logos
- Credly-hosted badge images for certification cards
- GitHub and Credly links opened by the user

Credly badge image cards link to the public credential pages:

- [IT Essentials](https://www.credly.com/badges/e8e0aeeb-ae2d-4df3-a3a3-36916996ca5f/public_url)
- [CCNA: Introduction to Networks](https://www.credly.com/badges/5b10764f-748f-4ac2-ae83-530f49ada7c8/public_url)

## Security

The Flask layer restricts public file access to known HTML, CSS, JavaScript, resume, and image files. Hidden paths and unsupported file types return `404` responses.

Configured response headers include Content Security Policy, Strict Transport Security, X-Content-Type-Options, X-Frame-Options, Referrer Policy, and Permissions Policy.

See [SECURITY.md](SECURITY.md) for private vulnerability reporting instructions. Do not commit `.env` files or credentials; use `.env.example` as the configuration reference.
