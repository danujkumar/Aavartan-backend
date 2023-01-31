from dataclasses import dataclass
from pickletools import read_uint1
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pytz
import json

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("aavartan.json", scope)
opener = gspread.authorize(creds)
sheet = opener.open("Aavartan")

# return number of rows in a sheet
def rows(work):
    wks = sheet.worksheet(work)
    return len(wks.get_all_records())

# return all records of a sheet
def allRec(work):
    wks = sheet.worksheet(work)
    return wks.get_all_records()

# checks if this mail already exists
def check_mail(mail):
    record = {}
    wks = sheet.worksheet("users")
    data = wks.get_all_records()

    for i in data:
        if i['email'] == mail:
            record['email'] = i['email']
            record['name'] = i['full_name']
            record['college'] = i['college']
            # record['roll'] = i['roll']
            record['phone'] = i['phone']
            record['password'] = i['password']
            return record
    return False

# adds this user to the sheet
def addUser(data):
    if check_mail(data['email']):
        return 2

    wks = sheet.worksheet("users")
    n = rows('users')
    n += 2

    UTC = pytz.utc
    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    dt_Kl = datetime.now(timeZ_Kl)
    utc_Kl = dt_Kl.astimezone(UTC)
    dt = dt_Kl.strftime('%d-%m-%Y %H:%M:%S')

    try:
        wks.update_cell(n, 1, data['email'])
        wks.update_cell(n, 2, data['name'])
        wks.update_cell(n, 3, data['college'])
        # wks.update_cell(n, 4, data['roll'])
        wks.update_cell(n, 4, data['phno'])
        wks.update_cell(n, 5, data['password'])
        wks.update_cell(n, 6, str(dt))
        # account created
        return 1
    except:
        # server error
        return 0

def login(data):
    record = check_mail(data['email'])
    if record == False:
        return -2

    pwd = record['password']
    pwd = str(pwd)

    if (data['password'] == pwd):
        # logged in
        record = json.dumps(record)
        return record
    else:
        # wrong password
        return -1


def register(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    print(wks)
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['team_name'])
        wks.update_cell(n, 2, data['team_leader_name'])
        wks.update_cell(n, 3, data['team_leader_mail'])
        wks.update_cell(n, 4, data['college_name'])

        size = len(data) - 5;
        size = size / 2;
        
        i = 1
        cell = 5
        while i <= size:
            wks.update_cell(n, cell, data['name' + str(i)])
            wks.update_cell(n, cell + 1, data['phone' + str(i)])
            cell += 2
            i += 1;

        return 1
    except:
        # server error
        return 0