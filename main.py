from flask import Flask
import couchdb
from json import loads
app = Flask(__name__)
db_server = '' # change this to mysql
with open('server0.json') as f:
    db_server = loads(f.read())
couch = couchdb.Server('http://{}:5984/'.format(db_server))
