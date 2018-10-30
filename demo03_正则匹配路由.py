from werkzeug.routing import BaseConverter
from flask import Flask

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegexConverter,self).__init__(url_map)
        self.regex=args[0]
app=Flask(__name__)
app.url_map.converters['re']=RegexConverter
@app.route('/user/<re("[0-9]{3}"):user_id>')
def user_info(user_id):
    return "user_id=%s"%user_id

@app.route("/")
def index():
    return "hello fa"
if __name__ == '__main__':
    app.run()