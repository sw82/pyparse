#!/usr/bin/python

import os, datetime
from xml.dom import minidom

#db stuff
import sqlite3 
connection = sqlite3.connect("cb.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cb (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	filename TEXT, name TEXT, vorname TEXT, richtig INTEGER, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""")

#folder which contains all xml files
xmlfolder 	= "xml";
xmlarchivefolder = "archive";

# create folders
if not os.path.exists(xmlfolder):
    os.makedirs(xmlfolder)
if not os.path.exists(xmlarchivefolder):
    os.makedirs(xmlarchivefolder)

# parse each file in xmlfolder, put it to db and mv the file to archive
print os.listdir(xmlfolder);

# read file
for filename in os.listdir(xmlfolder):
	tmpfile = xmlfolder + "/" + filename
	xmldoc = minidom.parse(tmpfile)

	#get name
	xmlTagName	= xmldoc.getElementsByTagName('name')[0].toxml()
	xmlDataName	= xmlTagName.replace('<name>','').replace('</name>','')
	print "Name: " + xmlDataName

	#get email
	xmlTagEmail	= xmldoc.getElementsByTagName('email')[0].toxml()
	xmlDataEmail= xmlTagEmail.replace('<email>','').replace('</email>','')
	print "Email: " + xmlDataEmail

	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	#TODO get right amount of answers and add this too


	#copy stuff to db
	werte = { "filename" : filename, "timestamp" : now, 
         "name" : xmlDataName, "email" : xmlDataEmail, "richtig" : "0" } 
	sql = "INSERT INTO cb VALUES ( :filename, :name, :email, :richtig, :timestamp)" 
	cursor.execute(sql, werte)
	connection.commit()




	#TODO move file to archive
	#destination = xmlarchivefolder + "/" + filename;
	#os.rename(tmpfile, destination)
