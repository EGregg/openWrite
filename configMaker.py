#!/usr/bin/env python3
import os


credentialsFile = 'storedCredentials.txt'

def config_present():
	try:
	        open(credentialsFile,'r')
	except:
		open(credentialsFile,'w')

def config_writer():
	username = input('create username: ')
	password = input('create password: ')
	fd = open(credentialsFile,"w")
	fd.write("%s:%s" % (username,password))

def config_read():
	with open(credentialsFile) as f:
		credentials = [x.strip().split(':') for x in f.readlines()]
		#if the file is empty then to run config_writer

	for username,password in credentials:
		print (username, password)

config_present()
config_read()
