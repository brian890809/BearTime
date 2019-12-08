from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from textprocessing import *
from datetime import datetime, timedelta
from collections import defaultdict

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def days_in_range(start, end, daysDict):
    # Convert your start/end dates
    start_d = datetime.strptime(start, '%Y-%m-%dT%H:%M:%SZ')
    end_d = datetime.strptime(end, '%Y-%m-%dT%H:%M:%SZ')

    # Now iterate over the days between those two dates, adding
    # an arbitrary value to the 'day' key of our dict
    for i in range((end_d - start_d).days + 1):
        day_name = '{0:%A}'.format(start_d + timedelta(days=i))
        daysDict[day_name].append(i)
    return daysDict

def find_date_from_a_week(date):
    day = int(date[len(date) - 2:len(date)])
    lst = []
    for i in range(day, day + 7):
        if i > 31 and (int(date[5:7]) == 1 or int(date[5:7]) == 3 or int(date[5:7]) == 5 or int(date[5:7]) == 7 or int(date[5:7]) == 8 or int(date[5:7]) == 10 or int(date[5:7]) == 12):
            if int(date[5:7]) == 12:
                lst.append(str(int(date[0:4]) + 1) + "-01-" + str(i - 31))
            else:
                lst.append(date[0:5] + str(int(date[5:7]) + 1) + "-" + str(i - 31))
        elif int(date[0:4]) % 4 == 0 and int(date[5:7]) == 2 and i > 29:
            lst.append(date[0:5] + str(int(date[5:7]) + 1) + "-" + str(i - 29))
        elif int(date[5:7]) == 2 and i > 28:
            lst.append(date[0:5] + str(int(date[5:7]) + 1) + "-" + str(i - 28))
        elif i > 30 and (int(date[5:7]) == 4 or int(date[5:7]) == 6 or int(date[5:7]) == 9 or int(date[5:7]) == 11):
            lst.append(date[0:5] + str(int(date[5:7]) + 1) + "-" + str(i - 30))
        else:
            lst.append(date[0:len(date) - 2] + str(i))
    return lst


def ret_date_time(date):
    index = 0
    for s in date:
        if s is not ' ':
            index += 1
        else:
            return date[0:index], date[index + 2:]

def generate_weekday_lst(weekday):
    lst = []
    for i in range(weekday, weekday + 7):
        if i > 6:
            lst.append(i - 7)
        else:
            lst.append(i)
    return lst

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    """if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)"""
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials (1).json', SCOPES)
            creds = flow.run_local_server("127.0.0.1")
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    """now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])"""

    #Extract data from textprocessing
    data = main_func(inpramesh) #Later, instead of impful we will connect it to web to read data from there
    print(data)
    current_date,time = ret_date_time(str(datetime.today()))
    dates_till_six_days = find_date_from_a_week(current_date)
    weekdays = generate_weekday_lst(datetime.today().weekday())
    dictionary_of_weekdays = {'M':0, 'Tu':1, 'W':2, 'Th':3, 'F':4}
    dictionary_of_dates = {}
    for i in range(len(weekdays)):
        dictionary_of_dates[weekdays[i]] = dates_till_six_days[i]





    #Adding an Event to Calendar
    for d in data:
        if 'TBA' not in d and 'TBA' not in d[1]:
            for days in d[1]:
                start_time = ""
                end_time = ""
                if d[2][len(d[2]) - 1] == 'P' and d[2][:2] != "12":
                    #print(d[2][:2])
                    get_colon_index = 0
                    while d[2][get_colon_index] is not ":":
                        get_colon_index += 1
                    start_time = str(int(d[2][:get_colon_index]) + 12) + d[2][get_colon_index:len(d[2]) - 1] + ":00"
                else:
                    start_time = d[2][:len(d[2]) - 1] + ":00"

                if d[3][len(d[3]) - 1] == 'P' and d[3][:2] != "12":
                    get_colon_index = 0
                    while d[3][get_colon_index] is not ":":
                        get_colon_index += 1
                    end_time = str(int(d[3][:get_colon_index]) + 12) + d[3][get_colon_index:len(d[3]) - 1] + ":00"
                else:
                    end_time = d[3][:len(d[3]) - 1] + ":00"

                event = {
                      'summary': d[0],
                      'location': None,
                      'description': None,
                      'start': {
                        'dateTime': dictionary_of_dates[dictionary_of_weekdays[days]] + "T" + start_time,
                        'timeZone': 'America/Los_Angeles',
                      },
                      'end': {
                        'dateTime': dictionary_of_dates[dictionary_of_weekdays[days]] + "T" + end_time,
                        'timeZone': 'America/Los_Angeles',
                      },
                      'recurrence': [
                        'RRULE:FREQ=WEEKLY;UNTIL=20191220T235959Z'#COUNT=1'
                      ],
                      'attendees': [
                        {'email': 'raneshprasad@gmail.com'},
                        {'email': 'raneshprasad@gmail.com'},
                      ],
                      'reminders': {
                        'useDefault': False,
                        'overrides': [
                          {'method': 'email', 'minutes': 24 * 60},
                          {'method': 'popup', 'minutes': 10},
                        ],
                      },
                    }

                event = service.events().insert(calendarId='primary', body=event).execute()
                print('Event created: %s' % event.get('htmlLink'))



if __name__ == '__main__':
    main()
