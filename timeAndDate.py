import datefinder
from datetime import datetime,timedelta
import re

def create_event(start_time_str, summary, duration1=1,duration2=0, url=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration1,minutes=duration2)
    
    event = {
        'start_time': re.search(r'\d{2}:\d{2}:\d{2}',start_time.isoformat()).group(),
        'end_time': re.search(r'\d{2}:\d{2}:\d{2}',end_time.isoformat()).group(),
        'summary': summary,
        'url': url
    }
    return event