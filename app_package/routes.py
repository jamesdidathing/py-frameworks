from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app_package import app
from app_package.forms import LoginForm
from app_package.models import User

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)