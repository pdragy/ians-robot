#!/usr/bin/env python 
import os,sys
import subprocess


# this script should control everything
if (len(sys.argv) != 3):
    print "expected 2 arguments, user@ip-address of raspberry pi and port number!"
    print "example: run.py pi@192.168.1.152 5001"
    exit(1)

client_ip = sys.argv[1]
port = int(sys.argv[2])
if sys.platform == "darwin":
    server_ip = subprocess.check_output("/sbin/ifconfig | /usr/bin/grep 'inet '| /usr/bin/grep -v '127.0.0.1' | /usr/bin/cut -d' ' -f2 | /usr/bin/head -1 | /usr/bin/awk {'printf(\"%s\", $1)'}", shell=True)
else:
    server_ip = subprocess.check_output("/sbin/ifconfig | /bin/grep 'inet addr:'| /bin/grep -v '127.0.0.1' | /usr/bin/cut -d: -f2 | /usr/bin/head -1 | /usr/bin/awk {'printf(\"%s\", $1)'}", shell=True)
#ssh_proc = Popen(['ssh', '-f', '-N', '-L', local_forward, local_user_host], stdin=PIPE, stdout=PIPE)

print server_ip
