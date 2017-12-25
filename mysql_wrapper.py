import MySQLdb as db
from json import loads

DBHOST = ''
PASSWD = ''
DBPORT = 3306
DBUSER = ''
DB = ''
jsonfile = 'server0.json'
with open(jsonfile) as serverfile:
    data = loads(serverfile.read())
    DBHOST = data['ip']
    PASSWD = data['pass']
    DBUSER = data['user']
    DB = data['db']


def get_href_from_db(url_id='XD1'):
    try:
        connection = db.Connection(host=DBHOST,port=3306,user=DBUSER,passwd=PASSWD,db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute("SELECT href FROM {}".format(url_id))
        result = dbhandler.fetchall()
        return extract_href(result)
    except Exception as e:
        print(e)
        return 'https://github.com/chand1012/killableurls'

def extract_href(tup):
    test_thing = [x[0] for x in tup]
    return test_thing[0]
