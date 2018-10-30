from flask import Flask
from flask import request

app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
@app.route("/index1/<varindex>",methods=["GET","POST"])
def index1(varindex):
    return "asfda%s"%request.method
if __name__ == '__main__':
    app.run()