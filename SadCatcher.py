import os
import pyttsx3
engine = pyttsx3.init()

os.environ['SPOTIPY_CLIENT_ID'] = 'b7853f9173184630bb167909d35b39e2'
os.environ['SPOTIPY_CLIENT_SECRET'] = '89a4062f80e3434f805bce9334af307f'

import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials

def sendamessage(playlistname):
    print("need to send a message to " + str(playlistname[1]))
    engine.say("need to send a message to " + str(playlistname[1]))
    engine.runAndWait()

playlist1 = ['spotify:playlist:2P0AHxkTi9EDfWJvHIoHEH','lucia']
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
        w.write(songtotal['total'])
        w.close()
        f = open("playlist1number.txt","r")
        storedtotal = int(f.read())
        sendamessage(playlist1)
        
    if storedtotal == newtotal:
        print("no change")
        time.sleep(5)
        
  


