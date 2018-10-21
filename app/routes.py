from flask import render_template
from app import app

@app.route('/')
@app.route('/index') #decorators
def index():
    user = {"username": "Kasia"}
    posts = [
        {
            'author': {"username": 'Kath'},
            'body': "It's a beautiful day"
        },
        {
            'author': {"username": 'Marco'},
            'body': "I like trains"
        }
    ]
    return render_template('index.html', title="Kcht's blog", user=user, posts = posts)
