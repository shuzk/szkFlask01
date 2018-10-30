from flask import Flask
app=Flask(__name__)
@app.route("/demo02")
def index():
    return "helldsao"
@app.route("/user/<user_id>")
def user(user_id):
    return "fdjsa%s"%user_id
@app.route("/user_info/<int:user_id>")
def user_info(user_id):
    return "adfdsafsds%d"%user_id
if __name__ == '__main__':
    app.run()