import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

def writeTemp(temp):
	scope = ["https://spreadsheets.google.com/feeds"]
	cred = ServiceAccountCredentials.from_json_keyfile_name('apis/piMeasures-9539a6a7828c.json', scope)
	client = gspread.authorize(cred)

	sheet = client.open('piMeasuresSheet').sheet1
	row = [str(time.asctime()), str(temp)]

	print('writing')
	sheet.insert_row(row)
	print('wrote')