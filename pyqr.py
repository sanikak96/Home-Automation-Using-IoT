import pyqrcode
import sys
import socket

def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('google.com', 0))
    return s.getsockname()[0]
a=getNetworkIp()

url = pyqrcode.create(a)
url.svg('qr.svg', scale=8)

