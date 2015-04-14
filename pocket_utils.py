import os
import sys
import re
from pocket import Pocket
import time

def pck_time_filename():
    return '.pck_lasttimestamp'

def set_timestamp():
    stamp = time.time()
    c = open(pck_time_filename(), 'w+')
    c.write("{0:.15f}".format(stamp))
    return stamp

def last_timestamp():
    if (os.path.isfile(pck_time_filename())):
        c = open(pck_time_filename(), 'r')
        time = c.read()
        if (time):
            return float(time)
    return 0

def get_consumer_key():
    return "25938-52f1a7be9eed9b54abd1e0f4"

def get_request_token():
    consumer_key = get_consumer_key()
    request_token = Pocket.get_request_token(consumer_key = consumer_key)
    auth_url = Pocket.get_auth_url(code=request_token)
    os.system('open "{0}"'.format(auth_url))
    time.sleep(5)

    return request_token

def get_pocket_instance():
    user_credentials = Pocket.get_credentials(consumer_key = get_consumer_key(), code = get_request_token())
    access_token = user_credentials['access_token']
    pocket = Pocket(get_consumer_key(), access_token)

    return pocket

if __name__ == "__main__":
    print last_timestamp()
