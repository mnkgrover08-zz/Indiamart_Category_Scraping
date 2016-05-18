#!/usr/bin/env python
import requests
import re
import os
import smtplib
import unicodedata
import urllib
import types
import csv
import sys
import time
import datetime
import math
import json
import urllib
from time import sleep
from bs4 import BeautifulSoup
import xlrd
import MySQLdb

dictionary = [ 199,336,34,798,228,23,426 ]

for dic in dictionary:
	url = "http://mapi.indiamart.com/wservce/im/category/"
	headers = {'Accept-Encoding':'gzip','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Content-Length':129,'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A0001 Build/LMY48B)','Host':'mapi.indiamart.com'}
	payload = {'mtype':'scat','mid':dic,'token':'Your Token','modid':'ANDROID','flname':'','gluserid':'your User Id','app_version_no':'5.4','from':0,'to':500}
	urlData = requests.post(url,data=payload,headers=headers)
	jsonData = json.loads(urlData.text)
	if 'mcats' in jsonData:
		mcats = jsonData['mcats']
		if 'mcat' in mcats:
			mcatarray = mcats['mcat']
			for data in mcatarray:
				identity = data['id']
				name = data['name']
				fname = data['name']
				prodmaptotal = data['prod-map-total']
				category = 'Paper'
				database = MySQLdb.connect (host="localhost", user = "root", passwd = "your paasword", db = "indiamart")
				cursor = database.cursor()
				database.set_character_set('utf8')
				cursor.execute('SET NAMES utf8;')
				cursor.execute('SET CHARACTER SET utf8;')
				cursor.execute('SET character_set_connection=utf8;')

				# Create the INSERT INTO sql query
				query = """INSERT INTO categories (cat_id,cat_name,fname,prodmaptotal,category) VALUES (%s, %s, %s, %s, %s)"""

				# Assign values from each row
				values = ( identity , name , fname , prodmaptotal , category )

				# Execute sql Query
				cursor.execute(query, values)

				# Close the cursor
				cursor.close()

				# Commit the transaction
				database.commit()

				# Close the database connection
				database.close()

				print name
	else:
		continue			


