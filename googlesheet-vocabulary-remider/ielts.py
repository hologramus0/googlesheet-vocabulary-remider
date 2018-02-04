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
	sheet = client.open("IELTS Notes")
	
	pharaphase = sheet.worksheet('Pharapharse').get_all_records()
	vocabulary = sheet.worksheet('Vocabulary').get_all_records()
	sentences = sheet.worksheet('Sentences').get_all_records()
	
	#print (worksheet)
	
	 
	# Extract and print all of the values
	#list_of_hashes = sheet.get_all_records()
	now =  datetime.datetime.now()
	last_update = (now.replace(microsecond=0))
	

	
	kwargs =  {'use_multipliers': True, 'comma_multiplier': 2.0, 'stop_multiplier': 2.5 }
	for dict in pharaphase:
		print ('[Pharapharse] INFO: U/%s   [S]/%d\n\n' %(	last_update, len(pharaphase)))
		
		
		with Halo(dict['original'], spinner="dots2"):
			time.sleep(10)
			# Run time consuming work here
			#typewrite(, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )

		typewrite(dict['original'], max_time=1, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['pharapharse'], max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>", max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>" + '.'* 50, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['examples'], max_time=100, min_time=None, base=0.075, end='\n', ** kwargs )
		time.sleep(10)
		os.system('cls')  # on windows
	
	
	for dict in vocabulary:
		print ('[Vocabulary] INFO: U/%s   [S]/%d\n\n' %(	last_update, len(vocabulary)))
		
		
		with Halo(dict['word'], spinner="dots2"):
			time.sleep(10)
			# Run time consuming work here
			#typewrite(, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )

		typewrite(dict['word'], max_time=1, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['meaning'], max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>", max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>" + '.'* 50, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['examples'], max_time=100, min_time=None, base=0.075, end='\n', ** kwargs )
		time.sleep(10)
		os.system('cls')  # on windows
	
	for dict in sentences:
		print ('[Sentences] INFO: U/%s   [S]/%d\n\n' %(	last_update, len(sentences)))
		
		
		with Halo(dict['sentence'], spinner="dots2"):
			time.sleep(10)
			# Run time consuming work here
			#typewrite(, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )

		typewrite(dict['sentence'], max_time=1, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['meaning'], max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>", max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(">>" + '.'* 50, max_time=30, min_time=None, base=0.075, end='\n', ** kwargs )
		typewrite(dict['examples'], max_time=100, min_time=None, base=0.075, end='\n', ** kwargs )
		time.sleep(10)
		os.system('cls')  # on windows