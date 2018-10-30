from flask import Flask, jsonify

app=Flask(__name__)
@app.route("/")
def index():
    return "hello"
@app.route("/demo01")
def demo1():
    json_dict={
        "user_id":111,
        "user_name":"laowang"
    }
    return jsonify(json_dict)
if __name__ == '__main__':
    app.run()