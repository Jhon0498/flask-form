# Flask Web Form

A simple web form application developed with **Flask** as part of my web development studies.

The project is based on concepts from the **Flasky** application and focuses on creating forms, handling user input, managing sessions, and organizing a Flask application using templates and routes.

## Technologies

* Python
* Flask
* Flask-Bootstrap
* Flask-WTF
* WTForms
* HTML5
* Bootstrap
* Jinja2

## Project Structure

```text
flask-form/
├── static/
│   └── favicon.ico
├── templates/
│   ├── base.html
│   └── index.html
├── .gitignore
├── app.py
├── forms.py
├── routes.py
└── requirements.txt
```

## Features

* Web form for entering a user's name
* Form validation using WTForms
* Session management with Flask
* Flash messages
* Bootstrap-based interface
* Reusable HTML templates using Jinja2
* Custom favicon

## How It Works

The application starts in `app.py`, where the Flask application and Bootstrap are initialized.

The form is defined in `forms.py` using Flask-WTF and WTForms. The `NameForm` class contains a required name field and a submit button.

The application routes are defined in `routes.py`. The submitted name is stored in the Flask session, allowing the application to display the user's name on the page.

The HTML interface is organized into reusable templates:

* `base.html` provides the main page structure and navigation.
* `index.html` extends the base template and displays the form.

## Installation

Clone the repository:

```bash
git clone https://github.com/Jhon0498/flask-form.git
```

Navigate to the project directory:

```bash
cd flask-form
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and access:

```text
http://127.0.0.1:5000
```

## Learning Goals

This project was created to practice:

* Flask application structure
* Routing
* HTML templates
* Jinja2
* Flask sessions
* Form handling
* Form validation
* Bootstrap integration
* Git and GitHub workflow

## Author

**Jhonatan**

GitHub: [Jhon0498](https://github.com/Jhon0498)

## Status

This is a study project and may receive improvements as I continue learning Flask and web development.
