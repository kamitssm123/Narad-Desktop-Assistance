from timeANDdate_module import get_hours
from output_module import output
from datetime import date
from database import get_last_seen, update_last_seen



def greet():


    # previous date
    previous_date = get_last_seen()


    # todays date
    today_date = str(date.today())
    update_last_seen(today_date)

    if previous_date == today_date:
        output("Welcome Back, Amit")

    else:
        hour = int(get_hours())
        
        if hour >= 4 and hour <12:
            output("Good Morning, Amit")

        elif hour >= 12 and hour < 16:
            output("Good Afternoon, Amit")

        else:
            output("Good Evening, Amit")


