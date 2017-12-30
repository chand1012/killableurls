import MySQLdb as db
from json import loads
from random import choice
from chtimer import *
import datetime

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

def get_tomorrow():
    a = datetime.datetime.now()
    b = a + datetime.timedelta(1,0)
    return to_chstring(b)


def get_url_killdate(url_id):
    try:
        connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute("SELECT killdate FROM {}".format(url_id))
        result = dbhandler.fetchall()
        return extract_first(result)
    except Exception as e:
        print(e)
        return 'DATE NOT FOUND'

def generate_url_id(chars=6, custom=None):
    urls = []
    uid = ""
    try:
        connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
        dbhandler = connection.cursor()
        dbhandler.execute("SHOW TABLES")
        for table in dbhandler:
            urls += [table]
        while True:
            if custom==None:
                uid = ''.join(choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(chars))
            else:
                uid = custom
            if uid in urls and custom==None:
                pass
            elif uid in urls and custom!=None:
                return 1
                break
            else:
                return uid
                break
    except Exception as e:
        print(e)
        return None


def new_url(url, killdate=get_tomorrow(), killclicks=0, surl="/404", gen_length=6, custom=None):
    url_id = generate_url_id(gen_length, custom) # increase the char amount in production, or just make it increase when we need more
    if not "http" in url:
        url = "http://" + url

    if str(type(url_id))=="<class 'str'>":
        try:
            connection = db.Connection(host=DBHOST,port=DBPORT,user=DBUSER,passwd=PASSWD,db=DB)
            dbhandler = connection.cursor()
            query = "CREATE TABLE {} (href VARCHAR(2000), killdate CHAR(16), killclicks INT(12), alturl VARCHAR(2000))".format(url_id) #possibly add a way to save the IP
            dbhandler.execute(query)
            query = "INSERT INTO %s VALUES('%s', '%s', %d, '%s')" % (url_id, url, killdate, killclicks, surl)
            dbhandler.execute(query)
            connection.commit()
            return url_id
        except Exception as e:
            print(e)
            return None
    elif url_id==1:
        print("Custom url already taken!")
        return 1
    else:
        print("Url generator errored out, they're gonna have to retry.")
        return None
