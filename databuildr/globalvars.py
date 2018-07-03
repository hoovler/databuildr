from datetime import datetime

import numpy as np
import pandas as pd
import csv, os, glob

dirs = {
    'images': 'static' + os.sep + 'images' + os.sep,
    'css': 'static' + os.sep + 'content' + os.sep,
    'fonts': 'static' + os.sep + 'fonts' + os.sep,
    'scripts': 'static' + os.sep + 'scripts' + os.sep,
    'csv': 'static' + os.sep + 'text' + os.sep,
    'templates': 'templates' + os.sep
}
    
expFilenames = {
    'job': 'jobs.csv',
    'rol': 'roles.csv',
    'ach': 'achievements.csv',
    'res': 'responsibilities.csv'
}

currentDir = os.getcwd() + os.sep + 'databuildr' + os.sep

class GlobalVars:
    """Builds and sets the content of the databuildR website pages"""
    

    #files = (currentDir + dirs['csv'] + value for value in expFilenames.values())
    files = dict(zip(expFilenames.keys(), (currentDir + dirs['csv'] + value for value in expFilenames.values())))
    #files = dict(zip(expFilenames.keys(), (dirs['csv'] + value for value in expFilenames.values())))


    #filePaths = glob.glob('E:\\dev\\code\\personal\\git\\databuildr\\databuildr\\databuildr\\static\\text\\' + '*.csv')

    
    jobs = pd.read_csv(files['job'])
    roles = pd.read_csv(files['rol'])
    responsibilities = pd.read_csv(files['res'])
    achievements = pd.read_csv(files['ach'])

    df = pd.merge(jobs, roles, on='job_id')
    
    #exp = np.array(jobs)

    
    # Getting current working directory:
    # os.getcwd()

    # Getting script's directory:
    # os.path.dirname(os.path.realpath(__file__))

    skills = {'Software Engineering', 'Data Engineering'}
    content = {
        'layout': {
            'title': 'Datavangelism',
            'name': 'Michael Hoovler',
            'email':'architect@databuildr.com',
            'phone':'(434) 270-0548',
            'year': datetime.now().year
        },
        'index': {
            'title': 'Data BuildR, LLC',
            'tagline': 'Opposing information entropy through the power of Charismatic Datavangelism.',
            'opener': 'Building secure, efficient, data-driven and informed environments in the healthcare industry, federal government, ' +
                'and private sector since 2005 with unrivaled creativity, adept analysis, and an inimitable calling and life-long commitment ' +
                'to solve problems, create technical solutions, and unearth objective truths from pristine, raw information.',
            'block1': {
                'title': 'Professional Tradecraft',
                'section1': {
                    'title': roles.get('position_title')[1],
                    'summary': roles.get('descr_role')[1]
                },
                'section2': {
                    'title': roles.get('position_title')[2],
                    'summary': roles.get('descr_role')[2]
                }
                ,
                'section3': {
                    'title': roles.get('position_title')[3],
                    'summary': roles.get('descr_role')[3]
                }
                ,
                'section4': {
                    'title': roles.get('position_title')[4],
                    'summary': roles.get('descr_role')[4]
                }
            }
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
            'mainImage': 'binary-full.png'    
        }
    }