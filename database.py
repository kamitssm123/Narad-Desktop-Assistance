import sqlite3
from tabnanny import check
from internet import check_internet_connection


def create_connection():

    connection = sqlite3.connect("memory.db")
    return connection



def get_questions_and_answers():

    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM questionAndanswer")

    return cur.fetchall()



def insert_question_and_answer(question, answer):
    con = create_connection()
    cur = con.cursor()

    # insert into tablename values('question', 'answer')
    query = "INSERT INTO questionAndanswer values('"+question+"', '"+answer+"')"
    cur.execute(query)
    con.commit()




def get_answer_from_memory(question):
    rows = get_questions_and_answers()
    answer = ""
    for row in rows:
        if row[0].lower() in question.lower():
            answer = row[1]
            break

    return answer

def get_name():
    con = create_connection()
    cur = con.cursor()

    # insert into tablename values('question', 'answer')
    query = "select value from memory where name = 'assistance_name'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_name(new_name):
    con = create_connection()
    cur = con.cursor()

   
    query = "update memory set value = '"+new_name+"' where name = 'assistance_name'"
    cur.execute(query)
    con.commit()



def get_last_seen():
    con = create_connection()
    cur = con.cursor()

    # insert into tablename values('question', 'answer')
    query = "select value from memory where name = 'last_seen_date'"
    cur.execute(query)
    return cur.fetchall()[0][0]


def update_last_seen(last_seen_date):
    con = create_connection()
    cur = con.cursor()

   
    query = "update memory set value = '"+last_seen_date+"' where name = 'last_seen_date'"
    cur.execute(query)
    con.commit()

def speech_mode():
    con = create_connection()
    cur = con.cursor()

    query = "select value from memory where name = 'speech_mode'"
    cur.execute(query)
    status = cur.fetchall()[0][0]
    if status == "on":
        return True
    else:
        return False

def speech_on():
    if check_internet_connection():
        con = create_connection()
        cur = con.cursor()

        query = "update memory set value = 'on' where name = 'speech_mode'"
        cur.execute(query)
        con.commit()
        return "Speech Mode Enabled"
    else:
        return "Turn on your internet connection"


def speech_off():
    con = create_connection()
    cur = con.cursor()

   
    query = "update memory set value = 'off' where name = 'speech_mode'"
    cur.execute(query)
    con.commit()
    return "Speech Mode Disabled"

