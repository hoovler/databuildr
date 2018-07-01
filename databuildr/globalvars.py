from datetime import datetime

class GlobalVars:
    """Builds and sets the content of the databuildR website pages"""
    content = {
        'layout': {
            'title': 'data.buildr(...)',
            'name': 'Michael Hoovler',
            'email':'architect@databuildr.com',
            'phone':'(434) 270-0548',
            'year': datetime.now().year
        },
        'index': {
            'title': 'Datavangelism',
            'tagline': 'Opposing information entropy through the power of Charismatic Datavangelism.',
            'opener': ''
        },
        'dirs': {
            'images': 'static/images/',
            'css': 'static/content/',
            'fonts': 'static/fonts/',
            'scripts': 'static/scripts/',
            'templates': 'templates/'
        },
        'links': {
            'medium': 'https://medium.com/@architect_85019',
            'twitter': 'https://twitter.com/hoovlernaut'
        },
        'images': {
            'mainImage': 'dataPuzzle.png'    
        }
    }