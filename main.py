from flask import Flask, render_template, redirect
import mysql_wrapper as mysql
app = Flask(__name__, static_url_path="")
mysql.get_server_info('server0.json')

@app.route("/<string:url_id>")
def redir(url_id):
    return redirect(mysql.get_href_from_db(url_id))

if __name__=="__main__":
    app.run(host="192.168.1.13",port=8080)
