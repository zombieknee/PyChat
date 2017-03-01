import sys
import Tkinter
import datetime
import socket
import time
import random
import threading
import select

ClientList = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(("0.0.0.0",31337)) #temporary for connections to local host

so.listen(5)

