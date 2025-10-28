# Flask Form Page — README

This README is for a small Flask project that includes an HTML form page. It explains how to set up, run, and understand the folder structure and main functionality.

---

## 📌 Project Purpose

A simple web form page that collects user input (like name, email, message), processes it on the server, and displays a result. It demonstrates Flask basics like routing, Jinja2 templating, and form handling.

## 🔧 Features

* HTML form submission using POST
* Basic server-side validation
* Redirect or Thank You page after successful submission
* Uses Jinja2 templates (templates/)
* Static files for CSS/JS in static/

## 🧰 Requirements

* Python 3.8+
* pip (Python package manager)

> Optional but recommended: create a virtual environment using `python -m venv venv` and activate it with `source venv/bin/activate` (Linux/macOS) or `venv\\Scripts\\activate` (Windows).

## 📦 Installation

1. Clone or open the project folder:

   ```bash
   git clone <repo-url>
   cd flask-form-page
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Linux / macOS
   source venv/bin/activate
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

> The `requirements.txt` file usually includes `Flask` and optionally `Flask-WTF` or `python-dotenv`.

## 🏁 Run the App

To start the development server:

```bash
export FLASK_APP=app.py        # Linux / macOS
set FLASK_APP=app.py           # Windows (cmd)
flask run
```

Or simply run:

```bash
python app.py
```

Then open your browser at: `http://127.0.0.1:5000/`

## 📂 Folder Structure

```
flask-form-page/
├─ app.py                # Flask app and routes
├─ requirements.txt
├─ templates/
│  ├─ base.html
│  ├─ form.html          # Form page
│  └─ success.html       # Thank-you / result page
├─ static/
│  ├─ css/
│  │  └─ style.css
│  └─ js/
│     └─ main.js
└─ README.md
```

## app.py — Overview

* `from flask import Flask, render_template, request, redirect, url_for, flash`
* `/` route — GET: shows form, POST: processes form data
* If valid, redirects to `success.html` using `redirect(url_for('success'))`

> Using `Flask-WTF` makes field validation and CSRF protection easier.

## 🔒 Security Notes

* Never keep `debug=True` in production.
* Always validate user input server-side to prevent XSS/SQL injection.
* Keep sensitive data (like `SECRET_KEY`) in a `.env` file and add `.env` to `.gitignore`.

## 🚀 Deployment

* For small apps, you can use Heroku, Render, or Vercel.
* For production, set `FLASK_ENV=production` and use a WSGI server like Gunicorn:

  ```bash
  pip install gunicorn
  gunicorn -w 4 app:app
  ```

## 🧪 Testing

* Manual: open form in browser and submit test data.
* Automated: write unit tests with `pytest` to test routes and validation.

## ⚙️ Common Issues

* **TemplateNotFound**: ensure `templates/` folder is in the same directory as `app.py`, and filenames match.
* **Static files not loading**: use correct syntax — `{{ url_for('static', filename='css/style.css') }}`.
* **Form data is None**: ensure `<form method="POST">` and each field has a proper `name` attribute.

## 💡 Future Improvements

* Add better form validation with `Flask-WTF`.
* Save submissions to a database (SQLite/Postgres).
* Improve UI using Bootstrap or Tailwind CSS.

## 🤝 Contributing

Feel free to fork the repo and open a Pull Request. Please open an issue first to discuss your proposed changes.

## 📄 License

You may include any license that fits your project — for example, MIT.

---

If you share your `app.py` and `templates/form.html`, I can update this README with exact project-specific details (dependencies, run commands, etc.).
