from flask import Flask, render_template, redirect, send_from_directory, url_for
from random import choice
import mysql_wrapper as mysql
import os
import chtimer
app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    num = mysql.get_url_amt()
    tagline = choice(["Killable urls.", "Terminate a link with ease.", "Click to kill.", "Urls with expiration dates."])
    otherline = choice(["the slaughter of young-links", "killable urls", "killable urls", "killable urls", "killable urls", "killable urls", "killable urls", "links with expiration dates", "links with expiration dates", "links with expiration dates", "links with expiration dates", "links with expiration dates"])
    execute = "The link to be killed."
    return render_template('index.html', num=num, tagline=tagline, otherline=otherline, execute=execute)

@app.route("/new")
def new():
    return render_template('new.html')

@app.route("/new/<string:url>")
def generate(url):
    gen_url_id = mysql.new_url(url)
    if gen_url_id==None:
        redirect("/error")
    else:
        redirect("/details/new/{}".format(gen_url_id))

@app.route("/new/<string:url>/<string:date>")
def generate_main(url, date):
    gen_url_id = mysql.new_url(url, date)
    if gen_url_id==None:
        redirect("/error")
    else:
        redirect("/details/new/{}".format(gen_url_id))

@app.route("/k")
def killed():
    return "Url was terminated"

@app.route("/details/new/<string:url_id>")
def created(url_id):
    killdate = mysql.get_url_killdate(url_id)
    otherline = choice(["the slaughter of young-links", "killable urls", "killable urls", "killable urls", "killable urls", "killable urls", "killable urls", "links with expiration dates", "links with expiration dates", "links with expiration dates", "links with expiration dates", "links with expiration dates"])
    render_template('details.html', url_id=url_id, date=killdate, otherline=otherline)

@app.route("/details/<string:url_id>")
def details(url_id):
    return render_template('details.html')

@app.route('/404')
def page_not_found():
    return "404 PAGE NOT FOUND"

@app.route("/<string:url_id>")
def redir(url_id):
    killdate = mysql.get_url_killdate(url_id)

    return redirect(mysql.get_href_from_db(url_id))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/buttons.css')
def buttons():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'buttons.css', mimetype='text/css')

@app.route('/marketing.css')
def marketing():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'marketing.css', mimetype="text/css")

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
