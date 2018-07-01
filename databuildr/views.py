"""
Routes and views for the flask application.
"""

from flask import render_template
from databuildr import app
from databuildr import globalvars

content = globalvars.GlobalVars.content
#content = {
#    'layout': {
#        'title': 'data.buildr(...)',
#        'name': 'Michael Hoovler',
#        'email':'architect@databuildr.com',
#        'phone':'(434) 270-0548',
#        'year': datetime.now().year
#    },
#    'index': {
#        'title': 'Datavangelism',
#        'tagline': 'Opposing information entropy through the power of Charismatic Datavangelism.'
#    },
#    'dirs': {
#        'images': 'static/images/',
#        'css': 'static/content/',
#        'fonts': 'static/fonts/',
#        'scripts': 'static/scripts/',
#        'templates': 'templates/'
#    },
#    'links': {
#        'medium': 'https://medium.com/@architect_85019',
#        'twitter': 'https://twitter.com/hoovlernaut'
#    },
#    'images': {
#        'mainImage': 'dataPuzzle.png'    
#    }
#}

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        content=content
    )

@app.route('/portfolio')
def portfolio():
    """renders the experience page."""
    return render_template(
        'portfolio.html',
        content=content
    )