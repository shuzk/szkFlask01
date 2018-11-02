from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

@app.route('/')
def admin_home():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/publish')
def publish():
    return 'publish'

if __name__=='__main__':
    app.run()