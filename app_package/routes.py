from flask import render_template
from app_package import app
from app_package.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'James'}    # this is a mock user

    # Here we are creating mock posts for our page from different users
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'My favourite recipe is Lasagne :)'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The soup recipe needs more salt..'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)