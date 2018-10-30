from flask import Flask
from flask import make_response
from flask import request

app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
@app.route("/cookie")
def set_cookie():
    resp=make_response("afdsadfasf")
    resp.set_cookie("username","itcast",max_age=3600)
    return resp
@app.route("/request")
def resp_cookie():
    resp=request.cookies.get("username")
    return resp
if __name__ == '__main__':
    app.run()