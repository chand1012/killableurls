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
        connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute("SELECT href FROM {}".format(url_id))
        result = dbhandler.fetchall()
        return extract_first(result)
    except Exception as e:
        print(e)
        return '/404'

def extract_first(tup):
    thing = [x[0] for x in tup]
    return thing[0]

def get_url_amt():
    try:
        connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute('SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = "{}"'.format(DB))
        result = dbhandler.fetchall()
        return extract_first(result)
    except Exception as e:
        print(e)
        return None

'''
def generate_url_id(chars=6):


def new_url(url):
'''
