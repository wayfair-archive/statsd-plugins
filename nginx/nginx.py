#!/usr/bin/env python

import httplib
import time
import socket

class UdpSender(object):
        def __init__(self, port, address):
                self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.client.connect((address, port))

        def send(self, message):
                self.client.send(message)


while(True):
        conn = httplib.HTTPConnection("your.domain.com")
        conn.request("GET","/nginx_status")
        response = conn.getresponse()
        data = response.read()
        data = data.split("\n")
        # replace 0000 with statsd listening port and x.x.x.x with ip for statsd host
        snd = UdpSender(0000, 'x.x.x.x')  
        activeconns = data[0].split()[-1]
        readstate = data[3].split()[1]
        writestate = data[3].split()[3]
        openstate = data[3].split()[5]
        val = "nginx.activeconns:%s|c" % str(activeconns)
        snd.send(val)
        snd.send("nginx.read:%s|c" % str(readstate))
        snd.send("nginx.write:%s|c" % str(writestate))
        snd.send("nginx.open:%s|c" % str(openstate))
        snd = None
        time.sleep(5)
