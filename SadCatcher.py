import os
import pyttsx3
engine = pyttsx3.init()

os.environ['SPOTIPY_CLIENT_ID'] = 'INSERT HERE'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'INSERT HERE'

import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

def sendamessage(playlistname):
    print("need to send a message to " + str(playlistname[1]))
    engine.say("need to send a message to " + str(playlistname[1]))
    engine.runAndWait()

playlist1 = ['spotify:playlist:URI','NAME']
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

f = open("playlist1number.txt","r")
storedtotal = int(f.read())

#NUMBER OF SONGS IN THE PLAYLIST
while True:
    songtotal = spotify.playlist_items(playlist1[0],fields='total')
    newtotal = int(float(songtotal["total"]))

    if storedtotal != newtotal:
        print("not the same as last run")
        f.close()
        w = open("playlist1number.txt","w")
        w.write(str(songtotal['total']))
        w.close()
        f = open("playlist1number.txt","r")
        storedtotal = int(f.read())
        sendamessage(playlist1)
        
    if storedtotal == newtotal:
        print("no change")
        time.sleep(5)
        
  


