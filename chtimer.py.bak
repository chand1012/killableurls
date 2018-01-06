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
    return datetime.datetime(yr, mth, d, hr, mt)

def to_chstring(convertdate): # http://strftime.org
    return convertdate.strftime("%H:%M %m/%d/%Y")

def execute_all(funcs):
    for f in funcs:
        f()

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
