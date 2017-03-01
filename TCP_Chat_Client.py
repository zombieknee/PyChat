import sys
from Tkinter import *
# from Tkinter.simpledialog import *
import threading
import socket
import time
import select
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

root = Tk()
root.withdraw()

def send(*stuff):
	txt = textline.get()
	textline.delete(0,len(txt))
	msg = "CHAT:",myname,":",txt
	totalBytes = len(message)
	totalBytes += 1
	words = ("%05d"%totalBytes,":",message).encode("utf-8")
	sock.send(words)

root.title("User: Test Connected To: 127.0.0.1")
root.deiconify()
root.mainloop()