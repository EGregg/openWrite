#!/usr/bin/env python3
import os


credentialsFile = 'storedCredentials.txt'

#creates credentials file if not present
def configPresent():
	try:
	        open(credentialsFile,'r')
	except:
		open(credentialsFile,'w')

#asks for username and password to be written to credentials file
def configWriter():
	username = input('create username: ')
	password = input('create password: ')
	fd = open(credentialsFile,"w")
	fd.write("%s:%s" % (username,password))

#reads credentials file for user info, creates if not present
#stores
def configReader():
	with open(credentialsFile) as f:
		if os.stat(credentialsFile).st_size == 0:
			configWriter()
		
		credentials = [x.strip().split(':') for x in f.readlines()]
		for p in credentials:
			username = p[0]
			password = p[1]

		return username,password
		

#first check to see if the file is present
configPresent()

#then read through the file and store the username as username and password as password
configReader()

#sets the username and password for use out of the function
config_username, config_password = configReader()
#print (config_username)
#print (config_password)
