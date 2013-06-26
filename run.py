#!/usr/bin/env python 
import os,sys
import subprocess


# this script should control everything
if (len(sys.argv) < 3):
    print "expected 2 arguments, user@ip-address of raspberry pi and port number!"
    print "example: run.py pi@192.168.1.152 5001"
    exit(1)

client_ip = sys.argv[1]
port = int(sys.argv[2])


# get ip address of host 
if sys.platform == "darwin":
    server_ip = subprocess.check_output("/sbin/ifconfig | /usr/bin/grep 'inet '| /usr/bin/grep -v '127.0.0.1' | /usr/bin/cut -d' ' -f2 | /usr/bin/head -1 | /usr/bin/awk {'printf(\"%s\", $1)'}", shell=True)
else:
    server_ip = subprocess.check_output("/sbin/ifconfig | /bin/grep 'inet addr:'| /bin/grep -v '127.0.0.1' | /usr/bin/cut -d: -f2 | /usr/bin/head -1 | /usr/bin/awk {'printf(\"%s\", $1)'}", shell=True)

print "My IP:", server_ip

run_path = os.path.dirname(os.path.realpath(__file__))
client_script = run_path + "/pi/socket_client.py " 
host_script = run_path + "/host/socket_server.py " + str(port)

# here should start the server script
print "Running ", host_script, "..."
os.system(host_script + " &> /dev/null &") 

# start the pi script
print "Running ", client_script, "..."
#ssh_proc = subprocess.Popen(['ssh', '-o','StrictHostKeyChecking=no',  'paul@127.0.0.1',  '<<\'ENDSSH\'', 'python', '<', client_script ], stdin=subprocess.PIPE)
ssh_proc = subprocess.Popen(['ssh', '-o','StrictHostKeyChecking=no',  'paul@127.0.0.1',  '<<\'ENDSSH\'', 'echo raspberry | sudo -Sv &&  ls '], stdin=subprocess.PIPE)
ssh_proc.communicate()[0]
#print foo
