
# importing libraries 
  
import requests 
from bs4 import BeautifulSoup 
from tabulate import tabulate 
import os
import time
import numpy as np 
import matplotlib.pyplot as plt 
from textmagic.rest import TextmagicRestClient
def covids():

	extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 
	URL = 'https://www.mohfw.gov.in/'
	  
	SHORT_HEADERS = ['SNo', 'State','Indian-Confirmed', 
	                 'Foreign-Confirmed','Cured','Death'] 
	  
	response = requests.get(URL).content 
	soup = BeautifulSoup(response, 'html.parser') 
	header = extract_contents(soup.tr.find_all('th')) 

	stats = [] 
	all_rows = soup.find_all('tr') 
	x = [] 
	for row in all_rows: 
	    stat = extract_contents(row.find_all('td')) 

	    if stat: 
	        if len(stat) == 5: 
	            # last row 
	            x = stat
	            stat = ['', *stat]
	            print(stat)  
	            stats.append(stat) 
	        elif len(stat) == 6: 
	            stats.append(stat) 
	  
	stats[-1][1] = "Total Cases"
	print(x) 
	stats.remove(stats[-1])
	p = "\nTotal Confirmed cases (Indian National): " +str(x[1]) + "\nTotal Confirmed cases ( Foreign National ): " + str(x[2]) +  "\nCured/Discharged/Migrated: " + str(x[3]) +  "\nDeath: " + str(x[4])
	objects = []
	print(p) 
	for row in stats : 
	    objects.append(row[1])  
	  
	y_pos = np.arange(len(objects)) 

	performance = [] 
	for row in stats : 
	    performance.append(int(row[2]) + int(row[3])) 
	  
	table = tabulate(stats, headers=SHORT_HEADERS) 
	print(table)
	url = "https://www.fast2sms.com/dev/bulk"
	payload = "sender_id=FSTSMS&message=" + p +  "&language=english&route=p&numbers=7411884965,7478572471"
	headers = {
	'authorization': "MHwCFq9yWVJ6a4B3TRmzEkZ8P5biGuetc7jOIsSLQXgv1KUdfAMytOViR785wvSuj2Qcb1dmeKHWrD3A",
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache",
	}
	response = requests.request("POST", url, data=payload, headers=headers)
	print(response.text)

def wait():
	print("Wait...for next cycle")
	time.sleep(10)

while True:
	covids()
	wait()
