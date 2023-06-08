""" audiostream: play an online audio stream and monitor its status

    Eric M. Jackson
    start of work 2023-05-27

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
    -- This file will be run daily at 6am via CRON/anacron/something
"""
# IMPORTS
import sys, os
import vlc
import time

# CONSTANTS
STATUSFILE = '/tmp/audiostatus'

# KTUS Tower/Ops
# https://www.liveatc.net/hlisten.php?mount=ktus&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus?nocache=2023052803395933640" type="audio/mp3" controls="controls" autoplay="true">
#STREAMURL = 'https://s1-fmt2.liveatc.net/ktus'

# KTUS Del/Gnd/Twr/App
# https://www.liveatc.net/hlisten.php?mount=ktus2&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus2?nocache=2023052803382740287" type="audio/mp3" controls="controls" autoplay="true">
#STREAMURL = 'https://s1-bos.liveatc.net/ktus2'
# From playlist file (available at https://www.liveatc.net/search/?icao=ktus)
#STREAMURL = 'http://d.liveatc.net/ktus'
# But wait--can't media players just open the playlist file?
#STREAMURL = '/tmp/ktus.pls'
STREAMURL = 'https://www.liveatc.net/play/ktus.pls'

# FUNCTIONS
def writeStatus(status, path):
    try:
        with open(path, mode='w', encoding='utf-8-sig') as file:
            file.write(status)
        return 0
    except IOError:
        print("Could not create {}".format(path))
        return(1)

def main():
    """load appropriate audio stream and monitor status"""
    status = 'STARTUP'
    writeStatus(status, STATUSFILE)

    # TODO: check WiFi/internet status? if down, then switch to error?

    # Connect to audio stream at STREAMURL
    # Thanks, https://stackoverflow.com/questions/46758360/how-to-play-streaming-audio-from-internet-radio-on-python-3-5-3?
    # API doc: https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Instance-class.html
    # and vlc --help
    instance = vlc.Instance('--input-repeat=-1', '--no-fullscreen')
    player = instance.media_player_new()
    player.set_media(instance.media_new(STREAMURL))
    '''
    if player.play():  # Does this return something that I can interpret as a logical value?
        status = 'CONNECTED'
        writeStatus(status, STATUSFILE)
    else:
        status = 'ERROR'
        writeStatus(status, STATUSFILE)
    '''
    player.play()
    status = 'CONNECTED'
    writeStatus(status, STATUSFILE)
    time.sleep(57600) # 6am to 10pm is 16 hrs = 57600 sec
    player.stop()
    status = 'STARTUP'
    writeStatus(status, STATUSFILE)
    exit(0)

    # If stream disconnects, status = 'ERROR' while try to reconnect
    #status = 'CONNECTED'
    #status = 'ERROR'
    #writeStatus(status, STATUSFILE)


if __name__ == "__main__":
    main()