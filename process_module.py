from input_module import take_input
from music import *
from timeANDdate_module import get_time, get_date, get_day
from database import *
from output_module import output
from internet import check_internet_connection, check_on_wikipedia
import assistance_details
from web import close_browser, open_facebook, open_google


def process(query):

    if "play" in query and "music" not in query:
        answer = get_answer_from_memory("play specific")

    elif "set volume" in query:
        answer = get_answer_from_memory("set volume")
    else:
        answer = get_answer_from_memory(query)

    # ----------------------------------------------------------

    # change name
    if answer == "change name":
        output("Okay! what do you want to call me?")
        temp = take_input()
        if temp == assistance_details.name:
            return "can't change. I think you're happy with my old name"
        else:
            update_name(temp)
            assistance_details.name = temp
            return "Now you can call me " + temp

    # -----------------------------------------------------------

    # speech mode on
    elif answer == "speech mode on":
        speech_on()

    # speech mode off
    elif answer == "speech mode off":
        speech_off()

    # --------------------------------------------------------------

    # PA name
    elif answer == "your name":
        return ("I am "+assistance_details.name)

    # ------------------------------------------------------------

    # Current Time Details
    elif answer == "get time details":
        return ("Time is " + get_time())


    # Today's Day details
    elif answer == "week day details":
        return ("Today is " + get_day())

    # Today's Date details
    elif answer == "todays date details":
        return (str(get_date()))

    # ------------------------------------------------------------

    # open facebook
    elif answer == "open facebook":
        open_facebook()
        return "opening facebook"

    # open google/browser
    elif answer == "open google":
        open_google()
        return "opening google"

    # close google/browser
    elif answer == "close browser":
        close_browser()
        return "your current browser is closed"
    
    # check internet connection
    elif answer == "check internet connection":
        if check_internet_connection():
            return "Internet is Connected"

        else:
            return "Internet is NOT Connected"

    # ------------------------------------------------------------

    # play song
    elif answer == "play music":
        play_music()
        return "playing music"

    # pause/stop music
    elif answer == "pause music" or answer == "stop music":
        pause_music()
        return "paused"

    # volume up music
    elif answer == "volume up":
        volume_up()
        return "increased"
    
    # volume down music
    elif answer == "volume down":
        volume_down()
        return "decreased"

    # next song
    elif answer == "next song":
        next_song()
        return "playing next"

    # previous song
    elif answer == "previous song":
        previous_song()
        return "playing previous"

    elif answer == "play specific":
        return play_specific_song(query)

    elif answer == "set volume":
        return set_volume(query)


    # ------------------------------------------------------------

    # teach PA and search on wikipedia
    else:

        # search on wikipedia
        output("Don't know this one should I search on web")
        ans = take_input()
        if "yes" in ans:
            
            answer = check_on_wikipedia(query)
            if answer != "":
                output("Here is what I found on Web")
                return answer
        else:

            # teach PA
            output("can you please tell me what it means?")
            ans = take_input()
            if "it means" in ans:
                ans = ans.replace("it means", "")
                ans = ans.strip()

                value = get_answer_from_memory(ans)
                if value == "":
                    return "can't help with this one"

                else:
                    insert_question_and_answer(query, value)
                    return "Thanks I will remember it for the next time"
            else:
                return "can't help with this one"

