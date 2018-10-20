from app import app

@app.route('/')
@app.route('/index') #decorators
def index():
    return "Hello, world!"
