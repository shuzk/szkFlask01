from werkzeug.routing import BaseConverter
from flask import Flask
app=Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegexConverter,self).__init__(url_map)
        self.regex=args[0]


@app.route("/")
def index():
    return "hello fa"
if __name__ == '__main__':
    app.run()