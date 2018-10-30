from flask import Flask
app=Flask(__name__)
@app.before_first_request
def before_first_request():
    print("fjdsajfdl")
@app.route("/")
def index():
    return "hello"
@app.before_request
def before_request():
    print("before request")
@app.after_request
def after_request(response):
    print("after_request111")
    return response
@app.teardown_request
def teardown_request(e):
    print("teardown_request")
if __name__ == '__main__':
    app.run()