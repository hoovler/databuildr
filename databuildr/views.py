"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from databuildr import app

contactInfo = {

    'email':'architect@databuildr.com',
    'phone':'(434) 270-0548',
    'address': {
        'street': '109 Mallard Lane',
        'city':'Stanardsville',
        'state':'VA',
        'zip':'22973'
    }
}

emailAddress = contactInfo['email']

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        sidebar=sidebar()
    )

@app.route('/experience')
def experience():
    """Renders the about page."""
    return render_template(
        'experience.html',
        title='Experience',
        year=datetime.now().year,
        message='experience'
    )

@app.route('/education')
def education():
    """Renders the about page."""
    return render_template(
        'education.html',
        title='Education',
        year=datetime.now().year,
        message='education'
    )

@app.route('/skills')
def skills():
    """Renders the about page."""
    return render_template(
        'skills.html',
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
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/snippets/sidebar')
def sidebar():
    """Renders the sidebar."""
    return render_template(
        'snippets/sidebar.html',
        year=datetime.now().year,
        contact=contactInfo,
    )