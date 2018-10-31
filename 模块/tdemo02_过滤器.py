from flask import Flask
from flask import render_template

app=Flask(__name__)

def do_listreverse(li):
    temp_li=list(li)
    temp_li.reverse()
    return temp_li
app.add_template_filter(do_listreverse,"lireverse")

@app.template_filter("aa")
def do_listreverse(li):
    temp_li=list(li)
    temp_li.reverse()
    t=str(temp_li)
    print(t)
    return t

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