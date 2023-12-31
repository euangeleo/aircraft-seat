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

# CONSTANTS
STATUSFILE = '/tmp/audiostatus'
CHANNELFILE = '/tmp/audiochannel'
STREAMURLS = {1:'https://slcr.me/SLCR1',                     # rock, St Louis Classic Rock Preservation Society
              2:'https://slcr.me/SLCR66',                    # oldies, SLCR Route 66
              3:'https://kexp.streamguys1.com/kexp64.aac',   # pop, KEXP Seattle
              4:'http://cast1.torontocast.com:1650/stream',  # jazz, Jazz Radio Network
              5:'https://kbaq.streamguys1.com/kbaq_mp3_128', # classical, KBAQ (Phoenix)
              6:'http://d.liveatc.net/ktus'}                # ATC, KTUS


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

def startPlayer(instance, URL):
    player = instance.media_player_new()
    media = instance.media_new(URL)
    player.set_media(media)
    player_status = player.play()
    player.audio_set_volume(100)
    return player, player_status

def setStatus(status, newstatus):
    if newstatus != status: # logical check first, to reduce writes to flash
        status = newstatus
        writeStatus(status, STATUSFILE)
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
    writeStatus(status, STATUSFILE)
    channel = readChannel(CHANNELFILE)

    instance = vlc.Instance()
    player, playerStatus = startPlayer(instance, STREAMURLS[channel])
    if playerStatus == 0:
        status = setStatus(status, 'CONNECTED')
    else:
        status = setStatus(status, 'ERROR')

    while time.localtime()[3] < 22:  # while it's before 10pm
        # TODO: check WiFi/internet status? if down, then switch to error?

        nowChannel = readChannel(CHANNELFILE)
        if nowChannel != channel:
            channel = nowChannel
            status = setStatus(status, 'STARTUP')
            player.stop()
            player, playerStatus = startPlayer(instance, STREAMURLS[channel])
            if playerStatus == 0:
                status = setStatus(status, 'CONNECTED')
            else:
                status = setStatus(status, 'ERROR')

        if not player.is_playing():
            status = setStatus(status, 'ERROR')
            player.stop()
            player, playerStatus = startPlayer(instance, STREAMURLS[channel])
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
