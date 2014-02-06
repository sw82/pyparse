#!/usr/bin/python

import os
from xml.dom import minidom
import sqlite3 

#db stuff
connection = sqlite3.connect("cb.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS cb (
	filename TEXT, name TEXT, vorname TEXT, richtig INTEGER)""")

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

for filename in os.listdir(xmlfolder):
	tmpfile = xmlfolder + "/" + filename
	xmldoc = minidom.parse(tmpfile)
	itemlist = xmldoc.getElementsByTagName('item')
	print len(itemlist)
	#print itemlist[0].attributes['name'].value
	for s in itemlist :
		print s.attributes['name'].value

	#copy stuff to db

	werte = {"filename" : filename, 
         "name" : "", "vorname" : "", "richtig" : "" } 

	sql = "INSERT INTO cebit VALUES (:filename, :name, :vorname, :richtig)" 
	cursor.execute(sql, werte)

	connection.commit()

	#move file to archive
	destination = xmlarchivefolder + "/" + filename;
	os.rename(tmpfile, destination)
