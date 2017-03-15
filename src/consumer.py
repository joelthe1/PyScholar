#!/usr/bin/python
import time
import sys
import socket
import os
import errno
import json
import subprocess
import re

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
    wfile = open('scraped_results.csv', 'a')
    for pub in data[238:]: # till 237 and started from 500
        try:
            ctr += 1
            print pub['id']
            res = subprocess.check_output("python pyscholar.py -t -p \"{0}\" --csv".format(pub['title']), shell=True);

            #wfile.write(str(pub['id']) + '||')
            res = res[:-1]
            res = res.replace('\n', '\n'+str(pub['id'])+'||')
            wfile.write(res)
            if len(res) > 5:
                wfile.write(res[1:] + '\n')
            if ctr %20:
                time.sleep(30)
        except Exception:
            print 'An error occured. ', sys.exc_info()

