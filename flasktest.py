from flask import Flask, redirect, render_template
from to_html import *
app = Flask(__name__, static_url_path="")
url_dict = {"1":"http://google.com/","2":"http://github.com/"}
@app.route("/")
def index():
    return html_to_str("html/test.html")

@app.route("/<string:url_id>")
def redir(url_id):
    return redirect(url_dict[url_id])

if __name__=="__main__":
    app.run(host="127.0.0.1",port=8080)
