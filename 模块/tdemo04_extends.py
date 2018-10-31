from flask import Flask
from flask import render_template

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("temp_demo04_extends_son.html")
if __name__ == '__main__':
    app.run()