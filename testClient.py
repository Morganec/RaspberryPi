import socket
import os
from datetime import datetime
import subprocess
import time , sys


def getBluetoothMacAddr():
    try:
        output= subprocess.check_output("hciconfig").decode('utf-8')
        bdaddr= output.split('\n')[1].split("\t")[1].split(" ")[2]
        return bdaddr
    except Exception as e:
        print(e)
        return "00:00:00:00:00:00"


hote = "192.168.1.114"
port = 8080

def connectAndClose():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((hote, port))
	print "Connection on {}".format(port)
	hostname = socket.gethostname()
	dateDuJour = datetime.now()
	dateDuJourStr = str(dateDuJour)
	bltadress = str(getBluetoothMacAddr())
	sock.send(hostname+","+dateDuJourStr+","+bltadress)
	print "Close"
	sock.close()

while 1:
	connectAndClose()
	if len(sys.argv) >= 2:
		time.sleep(float(sys.argv[1]))
	else:
		time.sleep(10)
