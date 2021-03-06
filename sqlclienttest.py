import MySQLdb as db
from json import loads

# based on https://gist.github.com/kirang89/7161185

HOST = ''
PASSWORD = ''
PORT = 3306
USER = ''
DB = ''
url_id = ''

with open('server0.json') as serverfile:
    data = loads(serverfile.read())
    HOST = data['ip']
    PASSWORD = data['pass']
    USER = data['user']
    DB = data['db']

try:
    connection = db.Connection(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=DB)
    dbhandler = connection.cursor()
    dbhandler.execute("SELECT href FROM {}".format(url_id))
    result = dbhandler.fetchall()
    test_thing = [x[0] for x in result]
    print(test_thing[0])
except Exception as e:
    print(e)

finally:
    connection.close()
