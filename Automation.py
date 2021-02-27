# This python code will notify you about your schedule
from time import sleep
from plyer import notification
import datetime
import webbrowser
import sys
import json

def show_notification(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "icon.ico",
        timeout = 10
    )


def events_automation():

    with open('events_today.json') as f:
        events = json.load(f)

    print(events)
    
    if events != None or len(events)>0:

        current_time = datetime.datetime.now().time()
        time_compare1 = current_time.hour*3600 + current_time.minute*60 + current_time.second

        for event in events:

            start_time_hour, start_time_minute, start_time_second =  map(int,event['start_time'].split(':'))
            title = event['summary']
            link = event['url']
            time_compare2 = start_time_hour*3600 + start_time_minute*60 + start_time_second

            if time_compare2 >= time_compare1:

                sleepTime = time_compare2-time_compare1
                time_left = 0
                
                if sleepTime>120:
                    sleepTime -= 120
                    time_left = 2
                else:
                    time_left = "less than 2 minutes"

                sleep(sleepTime)
                message = f"You have next meet in {time_left} minutes. Related link will be opened in browser."
                show_notification(title = title, message = message)
                sleep(10)
                webbrowser.open(link)

            else:
                continue 

    show_notification(title = "Event Automation is closing", message= "No extra task has been found. If you felt any problem please re-check your events. You can also report issues.")
    sys.exit()


if __name__ == "__main__":
    events_automation()