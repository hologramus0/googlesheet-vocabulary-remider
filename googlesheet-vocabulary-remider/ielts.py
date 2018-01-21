import gspread
from typewriter import typewrite
from oauth2client.service_account import ServiceAccountCredentials
from halo import Halo
import time 
import os
import datetime 


while True:
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
	client = gspread.authorize(creds)
	 
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open("IELTS Pharses").sheet1
	 
	# Extract and print all of the values
	list_of_hashes = sheet.get_all_records()
	#print(list_of_hashes)
	now =  datetime.datetime.now()
	last_update = (now.replace(microsecond=0))

	kwargs =  {'use_multipliers': True, 'comma_multiplier': 2.0, 'stop_multiplier': 2.5 }
	for dict in list_of_hashes:
		print ('INFO: U/%s   [S]/%d\n\n' %(	last_update, len(list_of_hashes)))
		
		
		with Halo(dict['orginal'], spinner="dots2"):
			time.sleep(10)
			# Run time consuming work here
			#typewrite(, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )

		typewrite(dict['orginal'], max_time=1, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['parapharse'], max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>", max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>" + '.'* 50, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['examples'], max_time=100, min_time=None, base=0.075, end='\n', ** kwargs )
		time.sleep(10)
		os.system('cls')  # on windows