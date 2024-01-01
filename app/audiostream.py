""" audiostream: play an online audio stream and monitor its status

    Eric M. Jackson
    start of work 2023-05-27

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
    -- This file will be run daily at 6am, and it should run until
       10pm, at which time it will change the status to the
       appropriate overnight status ('STARTUP') and exit
"""
# IMPORTS
import vlc
import time
import constants as cs
# in use: cs.STATUSFILE, cs.VOLUMEFILE, cs.CHANNELFILE, cs.STREAMURLS

# FUNCTIONS
def writeStatus(status, path):
    '''Put the status of the streamer'''
    try:
        with open(path, mode='w', encoding='utf-8-sig') as file:
            file.write(status)
        return 0
    except IOError:
        print("Could not create {}".format(path))
        return 1

def readChannel(path):
    '''Get the audio stream channel (integer 1 to 6)'''
    try:
        with open(path, mode='r', encoding='utf-8-sig') as file:
            firstline = file.read().strip()
            if (1 <= int(firstline) <= 6):
                return int(firstline)
            else:
                print("audiochannel file is not channel 1-6: {}".format(firstline))
                return 0
    except IOError:
        print("Could not read {}".format(path))
        return 0


def readVolume(path):
    '''Get the audio volume (integer 0 to 100)'''
    try:
        with open(path, mode='r', encoding='utf-8-sig') as file:
            firstline = file.read().strip()
            if (0 <= int(firstline) <= 100):
                return int(firstline)
            else:
                print("audiovolume file is not in range 0-100: {}".format(firstline))
                return 0
    except IOError:
        print("Could not read {}".format(path))
        return 0


def startPlayer(instance, URL, audiovolume=100):
    player = instance.media_player_new()
    media = instance.media_new(URL)
    player.set_media(media)
    player_status = player.play()
    player.audio_set_volume(audiovolume)
    return player, player_status

def setStatus(status, newstatus):
    if newstatus != status: # logical check first, to reduce writes to flash
        status = newstatus
        writeStatus(status, cs.STATUSFILE)
    return status

def main():
    """
    load appropriate audio stream to play based on channel selection

    Connect to audio stream from STREAMURLS based on the channel given in /tmp/audiochannel
    Thanks, https://stackoverflow.com/questions/46758360/how-to-play-streaming-audio-from-internet-radio-on-python-3-5-3?
    API doc: https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Instance-class.html
    Lots of good info: https://www.geeksforgeeks.org/python-vlc-mediaplayer-getting-media/
    and vlc --help
    """

    status = 'STARTUP'
    writeStatus(status, cs.STATUSFILE)
    audiovolume = readVolume(cs.VOLUMEFILE) or 100
    channel = readChannel(cs.CHANNELFILE) or 1

    instance = vlc.Instance()
    player, playerStatus = startPlayer(instance, cs.STREAMURLS[channel], audiovolume)
    if playerStatus == 0:
        status = setStatus(status, 'CONNECTED')
    else:
        status = setStatus(status, 'ERROR')

    while time.localtime()[3] < 22:  # while it's before 10pm
        # TODO: check WiFi/internet status? if down, then switch to error?

        nowChannel = readChannel(cs.CHANNELFILE)
        if nowChannel != channel:
            channel = nowChannel
            status = setStatus(status, 'STARTUP')
            player.stop()
            player, playerStatus = startPlayer(instance, cs.STREAMURLS[channel])
            if playerStatus == 0:
                status = setStatus(status, 'CONNECTED')
            else:
                status = setStatus(status, 'ERROR')

        nowVolume = readVolume(cs.VOLUMEFILE)
        if nowVolume != audiovolume:
            audiovolume = nowVolume
            player.audio_set_volume(audiovolume)

        if not player.is_playing():
            status = setStatus(status, 'ERROR')
            player.stop()
            player, playerStatus = startPlayer(instance, cs.STREAMURLS[channel])
            if playerStatus == 0:
                status = setStatus(status, 'CONNECTED')
            else:
                status = setStatus(status, 'ERROR')
        else:
            status = setStatus(status, 'CONNECTED')
        time.sleep(2)

    player.stop()
    status = setStatus(status, 'STARTUP')
    exit(0)


if __name__ == "__main__":
    main()
