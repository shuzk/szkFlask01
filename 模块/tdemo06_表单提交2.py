from flask import Flask
from flask import flash
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"


@app.route("/register", methods=["post", "get"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一样")
        else:
            print(username, password, password2, "这里省略了注册")
            return "success"
    return render_template("temp_demo06_表单提交2.html")


if __name__ == '__main__':
    app.run()
