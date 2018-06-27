"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from databuildr import app

pathTo = {
    'index': 'index.html',
    'experience': 'experience.html',
    'education': 'education.html',
    'skills': 'skills.html',
    'contact': 'contact.html',
    'sidebar': 'snippets/sidebar.html'
}

contactInfo = {
    'email':'architect@databuildr.com',
    'phone':'(434) 270-0548'
}

emailAddress = contactInfo['email']

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        pathTo['index'],
        title='Home Page',
        year=datetime.now().year
    )

@app.route('/experience')
def experience():
    """Renders the experience page."""
    return render_template(
        pathTo['experience'],
        title='Experience',
        year=datetime.now().year,
        message='experience'
    )

@app.route('/education')
def education():
    """Renders the about page."""
    return render_template(
        pathTo['education'],
        title='Education',
        year=datetime.now().year,
        message='education'
    )

@app.route('/skills')
def skills():
    """Renders the skills page."""
    return render_template(
        pathTo['skills'],
        title='Skills',
        year=datetime.now().year,
        message='skills'
    )

@app.route('/portfolio')
def portfolio():
    """Renders the portfolio page."""
    return render_template(
        'portfolio.html',
        title='Portfolio',
        year=datetime.now().year,
        message='A sample of my work...'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        pathTo['contact'],
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/snippets/sidebar')
def sidebar():
    """Renders the sidebar."""
    return render_template(
        pathTo['sidebar'],
        year=datetime.now().year,
        contact=contactInfo
    )