""" audiostream: play an online audio stream and monitor its status

    Eric M. Jackson
    start of work 2023-05-27

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
    -- This file will be run daily at 6am via CRON/anacron/something, and
       it should run until 10pm, at which time it will change the status to
       the appropriate overnight status ('STARTUP') and exit
"""
# IMPORTS
import vlc
import time

# CONSTANTS
STATUSFILE = '/tmp/audiostatus'

# KTUS Tower/Ops
# https://www.liveatc.net/hlisten.php?mount=ktus&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus?nocache=2023052803395933640" type="audio/mp3" controls="controls" autoplay="true">
#STREAMURL = 'https://s1-fmt2.liveatc.net/ktus'
# From playlist file (available at https://www.liveatc.net/search/?icao=ktus)
#STREAMURL = '/tmp/ktus.pls'  # Doesn't seem to actually play with python-vlc commands?
#STREAMURL = 'https://www.liveatc.net/play/ktus.pls' # maybe this requires media_player.playlist_play()?
# URL taken from the playlist file:
#STREAMURL = 'http://d.liveatc.net/ktus'

# KTUS Del/Gnd/Twr/App
# https://www.liveatc.net/hlisten.php?mount=ktus2&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus2?nocache=2023052803382740287" type="audio/mp3" controls="controls" autoplay="true">
#STREAMURL = 'https://s1-bos.liveatc.net/ktus2'
#STREAMURL = 'http://d.liveatc.net/ktus2'

# KUAZ Jazz 89.1 HD-2
STREAMURL = 'https://hls.azpm.org/fj-stream/128k/fjazz128.m3u8'

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
    """
    load appropriate audio stream to play during one day

    Connect to audio stream at STREAMURL
    Thanks, https://stackoverflow.com/questions/46758360/how-to-play-streaming-audio-from-internet-radio-on-python-3-5-3?
    API doc: https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Instance-class.html
    Lots of good info: https://www.geeksforgeeks.org/python-vlc-mediaplayer-getting-media/
    and vlc --help
    """

    status = 'STARTUP'
    writeStatus(status, STATUSFILE)

    # TODO: check WiFi/internet status? if down, then switch to error?

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(STREAMURL)
    while time.localtime()[3] < 22:  # while it's before 10pm
        if not player.is_playing():
            if status != 'ERROR':  # logical check first, to reduce writes to flash
                status = 'ERROR'
                writeStatus(status, STATUSFILE)

            player.set_media(media)
            player_status = player.play()
            player.audio_set_volume(100)
            if player_status == 0:
                status = 'CONNECTED'
                writeStatus(status, STATUSFILE)
        else:
            if status != 'CONNECTED':  # logical check first, to reduce writes to flash
                status = 'CONNECTED'
                writeStatus(status, STATUSFILE)
        time.sleep(2)

    player.stop()
    status = 'STARTUP'
    writeStatus(status, STATUSFILE)
    exit(0)


if __name__ == "__main__":
    main()
