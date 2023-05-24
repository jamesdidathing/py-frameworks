from flask import render_template, flash, redirect
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
    # render_template will render the html to the page
    return render_template('index.html', title='Home', user=user, posts=posts)


# 'POST' method is sending data/whatever from the browser to the server, 'GET' is the 
# other way around.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)