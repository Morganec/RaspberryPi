#!/usr/bin/python

import socket
import sqlite3
#from influxdb import InfluxDBClient

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
#client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
def insert(hostname,adressIP,dateEnvoi,bltAdress):
	conn = sqlite3.connect('bddSqlLite.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS connection(hostname text,adressip text, dateConnection text, bluetoothAdress text)''')
	c.execute("INSERT INTO connection(rowId,hostname,adressip, dateConnection, bluetoothAdress) VALUES ( NULL,?, ? ,?,?);",[str(hostname), str(adressIP),str(dateEnvoi),str(bltAdress)])
	conn.commit()
	conn.close()

while True:
        sock.listen(100)
        client, address = sock.accept()
        print "{} connected".format( address )
        

        response = client.recv(255)
        if response != "":
            splitResp = response.split(",",2)
            insert(splitResp[0],address[0],splitResp[1],splitResp[2])

        
print "Close"


client.close()
sock.close()