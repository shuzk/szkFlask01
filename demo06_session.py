from flask import Flask
from flask import redirect
from flask import session
from flask import url_for

app=Flask(__name__)
app.secret_key="jflsad"
@app.route("/")
def index():
    return session.get("username")
@app.route("/index1")
def index1():
    session['username']='itcast'
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()