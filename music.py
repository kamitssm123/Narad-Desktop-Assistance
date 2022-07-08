import os
import file_search

music_path = "/home/machine/Music"

def play_music():
    os.system("rhythmbox-client --play")

def stop_music():
    os.system("rhythmbox-client --pause")

def pause_music():
    os.system("rhythmbox-client --pause")

def volume_up():
    os.system("rhythmbox-client --volume-up")

def volume_down():
    os.system("rhythmbox-client --volume-down")

def next_song():
    os.system("rhythmbox-client --next")

def previous_song():
    os.system("rhythmbox-client --previous")

def play_specific_song(song_name):
    song_name = song_name.replace('play', '')
    file_search.set_root(music_path)
    song = file_search.searchFile(song_name)

    try:
        song_uri = song[0]
        command = 'rhythmbox-client --play-uri="' + song_uri + '"'
        os.system(command)
        return "playing" + song_name

    except:
        return "No music found named " + song_name

def set_volume(value):
    value = value.replace('set volume to', '')
    value = value.replace('%', '')
    value.split()
    value = int(value)/100
    command = 'rhythmbox-client --set-volume ' + str(value) 
    os.system(command)
    return "done"


