import os
import wikipedia
def check_internet_connection():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        return True
    else:
        return False

def check_on_wikipedia(query):
    query = query.lower()
    query = query.replace("who is", "")
    query = query.replace("what is", "")
    query = query.replace("do you know", "")
    query = query.replace("tell me about", "")

    query = query.strip()

    try:
        data = wikipedia.summary(query, sentences=1)
        return data
    except Exception as e:
        return ""
