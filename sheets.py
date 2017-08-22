import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds"]
cred = ServiceAccountCredentials.from_json_keyfile_name('apis/piMeasures-9539a6a7828c.json', scope)
client = gspread.authorize(cred)

sheet = client.open('piMeasuresSheet').sheet1

measures = sheet.get_all_records()
print(measures)