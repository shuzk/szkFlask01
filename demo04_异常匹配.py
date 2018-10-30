from flask import Flask
from flask import abort

app=Flask(__name__)
@app.route("/")
def index():
    print(11)
    # a=4/0
    abort(401)
    return "hello"
@app.errorhandler(404)
def a(e):
    # abort(200)
    return "404错误"
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return "除数不能为0"
if __name__ == '__main__':
    app.run()