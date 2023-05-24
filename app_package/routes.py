from app_package import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello"

@app.route('/welcome')
def welcome():
    return "Welcome!"