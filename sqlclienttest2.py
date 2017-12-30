import mysql_wrapper as mysql
from json import loads
import MySQLdb as db
MHOST = ''
DBHOST = ''
PASSWD = ''
DBPORT = 3306
DBUSER = ''
DB = ''
jsonfile = 'server0.json'
with open(jsonfile) as serverfile:
    data = loads(serverfile.read())
    MHOST = data['domain']
    DBHOST = data['ip']
    PASSWD = data['pass']
    DBUSER = data['user']
    DB = data['db']


url = "http://example.com"
killdate = mysql.get_tomorrow()
killclicks = 0
surl = "/404"
url_id = "AMm30j"
#url_id = mysql.generate_url_id()


connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
dbhandler = connection.cursor()
#query = "CREATE TABLE {} (href VARCHAR(2000), killdate CHAR(16), killclicks INT(12), alturl VARCHAR(2000))".format(url_id) #possibly add a way to save the IP
#dbhandler.execute(query)
query = "INSERT INTO %s VALUES('%s', '%s', %d, '%s')" % (url_id, url, killdate, killclicks, surl)
dbhandler.execute(query)
connection.commit()
