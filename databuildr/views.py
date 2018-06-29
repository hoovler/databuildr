"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from databuildr import app

templates = {
    'index': {
        'file':'index.html',
        'title': 'Datavangelist Home'
    }
}

directories = {
    'imageDir': 'static/images/',
    'cssDir': 'static/content/',
    'fontDir': 'static/fonts/',
    'scriptDir': 'static/scripts/',
    'templateDir': 'templates/'
}

siteMeta = {
    'title': 'data.buildr(...)',
    'author': {
        'name': 'Michael Hoovler',
        'email':'architect@databuildr.com',
        'phone':'(434) 270-0548'
    }
}

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        templates['index']['file'],
        title=templates['index']['title'],
        year=datetime.now().year,
        values=siteMeta,
        dirs=directories
    )

#@app.route('/experience')
#def experience():
#    """Renders the experience page."""
#    return render_template(
#        pathTo['experience'],
#        title='Experience',
#        year=datetime.now().year,
#        message='experience'
#    )