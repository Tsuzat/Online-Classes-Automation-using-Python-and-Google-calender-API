from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def CheckUser():
    
    print("\t--> AUTHORIZING USER")
    ################## AUTHENTICATION ######################################
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    print("\t--> AUTHORIZATION COMPLETED")

    ########################################################################
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('\t--> Fetching data from google Calendar server')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    
    #todays date
    date_today = now[:10]
    events_today = []

    other_events = []
    
    if not events:
        print('\t--> No upcoming events found.')
    
    for event in events:

        start = event['start'].get('dateTime', event['start'].get('date'))
        
        end = event['end'].get('dateTime', event['end'].get('date'))
        
        if date_today in start[:10]:
            
            d1 = {} #storing fetched data in a dictionary
            
            d1['start_time'] = re.search(r'\d{2}:\d{2}:\d{2}',start).group()
            d1['end_time'] = re.search(r'\d{2}:\d{2}:\d{2}',end).group()
            d1['summary'] = event['summary'] if 'summary' in event else 'No Title'

            #Getting meet/hangoutLink
            if 'hangoutLink' in event: #if link is in hangoutLink
                d1['url'] = event['hangoutLink']
            elif 'description' in event: #if link is in description
                d1['url'] = re.search(r'https://meet.google.com/\D{3}-\D{4}-\D{3}',event['description']).group()
            else: #can't find the link.
                d1['url'] = None
            
            # appending the fetched data in events_today
            events_today.append(d1)
        
        '''#storing other_events
        else:
            d2 = {} #storing data in a dictionary
            
            d2['start'] = start
            d2['end'] = end
            d2['summary'] = event['summary']
            
            #Getting meet/hangoutLink
            if 'hangoutLink' in event: #if link is in hangoutLink
                d2['url'] = event['hangoutLink']
            elif 'description' in event: #if link is in description
                d2['url'] = re.search(r'https://meet.google.com/\D{3}-\D{4}-\D{3}',event['description']).group()
            else: #can't find the link.
                d2['url'] = None
            
            # appending the fetched data in events_today
            other_events.append(d2)'''

    '''print("Other Events============>")
    for i in other_events:
        print(i)'''
            
    return events_today

if __name__ == '__main__':
    comming_events = CheckUser()
    if comming_events:
        print("TODAY'S EVENTS =============================>")
        for commingEvents in comming_events:
            print(commingEvents)
    else:
        print("--> No events found for today. FREE DAY I GUESS.")