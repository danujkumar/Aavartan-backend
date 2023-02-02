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


def blindCode(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    print(wks)
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['yos'])
        wks.update_cell(n, 7, data['branch'])
        wks.update_cell(n, 8, data['hackerrank'])
        return 1
    except:
        # server error
        return 0

def bow(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    print(wks)
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['course'])
        wks.update_cell(n, 7, data['yos'])
        wks.update_cell(n, 8, data['branch'])
        return 1
    except:
        # server error
        return 0

def hydrolift(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['yos'])
        wks.update_cell(n, 7, data['branch'])
        return 1
    except:
        # server error
        return 0

def shipwreck(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['yos'])
        wks.update_cell(n, 7, data['branch'])
        return 1
    except:
        # server error
        return 0

def scavengerhunt(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['team_name'])
        wks.update_cell(n, 2, data['leader_name'])
        wks.update_cell(n, 3, data['leader_mail'])
        wks.update_cell(n, 4, data['leader_whatsapp'])
        wks.update_cell(n, 5, data['leader_college'])
        wks.update_cell(n, 6, data['leader_number'])
        wks.update_cell(n, 7, data['leader_branch'])
        wks.update_cell(n, 8, data['yos'])
        wks.update_cell(n, 9, data['mem2'])
        wks.update_cell(n, 10, data['mem3'])
        wks.update_cell(n, 11, data['mem4'])
        return 1
    except:
        # server error
        return 0


def codetag(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['team_name'])
        wks.update_cell(n, 2, data['leader_name'])
        wks.update_cell(n, 3, data['leader_mail'])
        wks.update_cell(n, 4, data['leader_whatsapp'])
        wks.update_cell(n, 5, data['leader_college'])
        wks.update_cell(n, 6, data['leader_number'])
        wks.update_cell(n, 7, data['leader_branch'])
        wks.update_cell(n, 8, data['yos'])
        wks.update_cell(n, 9, data['mem2'])
        wks.update_cell(n, 10, data['mem3'])
        return 1
    except:
        # server error
        return 0


def treasurehunt(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['team_name'])
        wks.update_cell(n, 2, data['leader_name'])
        wks.update_cell(n, 3, data['leader_mail'])
        wks.update_cell(n, 4, data['leader_whatsapp'])
        wks.update_cell(n, 5, data['leader_college'])
        wks.update_cell(n, 6, data['leader_number'])
        wks.update_cell(n, 7, data['leader_branch'])
        wks.update_cell(n, 8, data['yos'])
        wks.update_cell(n, 9, data['mem2'])
        wks.update_cell(n, 10, data['mem3'])
        wks.update_cell(n, 11, data['mem4'])
        # wks.update_cell(n, 12, data['mem5'])
        return 1
    except:
        # server error
        return 0


def animatrix(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['yos'])
        wks.update_cell(n, 7, data['branch'])
        return 1
    except:
        # server error
        return 0

def robotrek(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['mail'])
        wks.update_cell(n, 2, data['leader_name'])
        wks.update_cell(n, 3, data['leader_number'])
        wks.update_cell(n, 4, data['leader_mail'])
        wks.update_cell(n, 5, data['name2'])
        wks.update_cell(n, 6, data['name3'])
        wks.update_cell(n, 7, data['name4'])
        return 1
    except:
        # server error
        return 0

def circuitrix(data):
    print(data)
    wks = sheet.worksheet(data['event'])
    n = rows(data['event'])
    n += 2

    try:
        wks.update_cell(n, 1, data['name'])
        wks.update_cell(n, 2, data['mail'])
        wks.update_cell(n, 3, data['phone'])
        wks.update_cell(n, 4, data['whatsapp'])
        wks.update_cell(n, 5, data['college'])
        wks.update_cell(n, 6, data['yos'])
        wks.update_cell(n, 7, data['branch'])
        return 1
    except:
        # server error
        return 0