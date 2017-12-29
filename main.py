from flask import Flask, render_template, redirect
import mysql_wrapper as mysql
app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    num = mysql.get_url_amt()
    return render_template('index.html', num=num)

@app.route("/new")
def new():
    return render_template('new.html')

@app.route("/new/<string:url>/<string:date>")
def generate(url, date):
    gen_url_id = ""
    if date == "":
        gen_url_id = mysql.new_url(url)
    else:
        gen_url_id = mysql.new_url(url, date)

    if gen_url_id==None:
        redirect("/error")
    else:
        redirect("/details/new/{}".format(gen_url_id))



@app.route("/details/new/<string:url_id>")
def created(url_id):
    
    render_template('new_url.html', url_id=url_id, date=)

@app.route("/details/<string:url_id>")
def details(url_id):
    return render_template('details.html')

@app.route('/404')
def page_not_found():
    return "404 PAGE NOT FOUND"

@app.route("/<string:url_id>")
def redir(url_id):
    return redirect(mysql.get_href_from_db(url_id))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)
