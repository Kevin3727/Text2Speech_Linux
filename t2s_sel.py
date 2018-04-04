#!/usr/bin/env python3

import os
import time
from copy import copy
import subprocess
import signal

# Initialization
prev_read_ = os.popen('xsel').read()
p_ = None

try:
    # loop until stops
    while True:
        read_ = os.popen('xsel').read()
        if read_ != prev_read_:
            if p_ != None:
                if p_.poll() == None:
                    os.kill(p_.pid, signal.SIGTERM)
            p_ = subprocess.Popen(['./t2s_speech.py', read_], stdout=subprocess.PIPE)
        time.sleep(0.2)
        prev_read_ = copy(read_)

except KeyboardInterrupt:
    if p_ != None:
        if p_.poll() == None:
            os.kill(p_.pid, signal.SIGTERM)
    pass
