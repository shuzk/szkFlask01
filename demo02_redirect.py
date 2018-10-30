from flask import Flask
from flask import redirect
from flask import url_for

app=Flask(__name__)
@app.route("/")
def index():
    return "hello"

@app.route("/index02/<user>")
def index2(user):
    return "hello222%s"%user

@app.route("/redirect01",methods=["get","put"])
def redirect1():
    return redirect("https://www.baidu.com")
@app.route("/redirect02",methods=['get'])
def redirect2():
    return redirect(url_for("index"))
@app.route("/redirect03")
def redirect3():
    return redirect(url_for("index2",user="3333"))
if __name__ == '__main__':
    app.run()