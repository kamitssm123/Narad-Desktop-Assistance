from datetime import datetime

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H Hours %M Minutes")
    return current_time


def get_hours():
    now = datetime.now()
    return (now.strftime("%H"))

def get_day():
    now = datetime.now()
    today_day = now.strftime("%A")
    return today_day

def get_date():
    now = datetime.now()
    today_date = now.strftime("%B %d %Y")
    return today_date
