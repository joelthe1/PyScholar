#!/usr/bin/python
import time
import sys
import socket
import os
import errno
import json
import subprocess
import re
import random

def ensure_path(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

path = sys.argv[1]
with open(path) as rfile:
    data = json.load(rfile)
    ctr=0
    wfile = open('../data/run2/scraped_results_1.csv', 'a')
    for pub in data: # till 237 and started from 500
        try:
            ctr += 1
            print pub['id']
            res = subprocess.check_output("python pyscholar.py -t -p \"{0}\" --csv".format(pub['title']), shell=True);

            #wfile.write(str(pub['id']) + '||')
#            res = res[:-1]
#            res = res.replace('\n', '\n'+str(pub['id'])+'||')
            wfile.write(res)
            time.sleep(random.randrange(1,4))
#            if ctr %20:
#                time.sleep(rand)
        except Exception:
            print 'An error occured. ', sys.exc_info()

