from _curses import flash

from flask import Flask
from flask import render_template
from flask import request

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("temp_demo04_extends_son.html")
@app.route("/include")
def include():
    return render_template("temp_demo05_include.html")
@app.route('/demo1', methods=["get", "post"])
def demo1():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"

    return render_template('login.html')
if __name__ == '__main__':
    app.run()