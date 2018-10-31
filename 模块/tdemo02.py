from flask import Flask
from flask import render_template

app=Flask(__name__)
@app.route("/")
def index():
    a=1
    b="fjdsa"
    c=[1,2]
    d={1:2,"fd":4}
    return render_template("temp_demo02.html",
                           aa=a,bb=b,cc=c,dd=d)
if __name__ == '__main__':
    app.run()