from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import int
from future import standard_library
standard_library.install_aliases()
import datetime

#this is my custom timer lib

queue = {}

def to_datetime(convertstring):
    # string format: "24:00 12/31/2017" or "24:00_12/31/2017"
    # will be converted to utc later
    hr = int(convertstring[:2])
    mt = int(convertstring[3:5])
    mth = int(convertstring[5:8])
    d = int(convertstring[9:11])
    yr = int(convertstring[12:])
    if hr==0 and mt==0:
        return datetime.datetime(yr, mth, d)
    else:
        return datetime.datetime(yr, mth, d, hr, mt)

def to_chstring(convertdate): # http://strftime.org
    return convertdate.strftime("%H:%M %m/%d/%Y")

def execute_all(funcs):
    for f in funcs:
        f()

def get_today():
    return to_chstring(datetime.datetime.now())

def add_queue(stime, func):
    queue.update({stime:func})

def update_queue():
    del_items=[]
    currenttime = datetime.datetime.now()
    for stime, func in queue.items():
        if to_datetime(stime) <= currenttime:
            func()
            del_items += [stime]
    for thing in del_items:
        del queue[thing]

'''
if you want to break the loop when the queue is finished,
use this snippet:
if not bool(chtimer.queue):
    break

this will terminate the loop when the queue is empty
'''
