from app import app
from flask import render_template, url_for, redirect


@app.route('/')
@app.route('/index')
def index():
    data = {
        'name': 'Tara',
        'location': 'Coding Temple'
    }

    locations = ['Boston', 'Chicago', 'Washington D.C.']

    return render_template('index.html', data=data, locations=locations)


@app.route('/class')
def class_data():
    persons = {
        1: {
            'name': 'Connor',
            'instructor': True
        },
        2: {
            'name': 'Tara',
            'instructor': False
        },
        3: {
            'name': 'Fiona',
            'instructor': False
        },
        4: {
            'name': 'Chet',
            'instructor': False
        },
        5: {
            'name': 'Tyler',
            'instructor': False
        },
        6: {
            'name': 'Todd',
            'instructor': False
        }
    }

    return render_template('class.html', persons=persons)


@app.route('/language')
def language_data():
    language_lst = ['Python', 'CSS3', 'HTML5', 'Javascript', 'SQL']
    descriptions = {
        'Python': 'An interpreted high-level programming language for general-purpose programming.',
        'CSS3': 'The latest evolution of the Cascading Style Sheets language and aims at extending CSS2.1.',
        'HTML5': 'A markup language used for structuring and presenting content on the World Wide Web.',
        'Javascript': 'A lightweight interpreted or JIT-compiled programming language with first-class functions.',
        'SQL': 'A domain-specific language used in programming and designed for managing data held in a relational database management system.'
    }

    return render_template('language.html', languages=language_lst, descriptions=descriptions)


@app.route('/redirecting')
def my_redirect():
    return redirect(url_for('index'))
