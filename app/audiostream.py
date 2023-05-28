""" audiostream: play an online audio stream and monitor its status

    Eric M. Jackson
    start of work 2023-05-27

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
"""

import sys, os

# CONSTANTS
STATUSFILE = '/tmp/audiostatus'

# KTUS Tower/Ops
# https://www.liveatc.net/hlisten.php?mount=ktus&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus?nocache=2023052803395933640" type="audio/mp3" controls="controls" autoplay="true">
#STREAMURL = 'https://s1-fmt2.liveatc.net/ktus'

# KTUS Del/Gnd/Twr/App
# https://www.liveatc.net/hlisten.php?mount=ktus2&icao=ktus
# <audio id="player2" crossorigin="anonymous" preload="none" src="https://s1-bos.liveatc.net/ktus2?nocache=2023052803382740287" type="audio/mp3" controls="controls" autoplay="true">
STREAMURL = 'https://s1-bos.liveatc.net/ktus2'

def writeStatus(status, path):
    try:
        with open(path, mode='w', encoding='utf-8-sig') as file:
            file.write(status)
    except IOError:
        print("Could not create {}".format(path))
        return(1)
    return 0

def main():
    """load appropriate audio stream and monitor status"""
    status = 'STARTUP'

    writeStatus(status, STATUSFILE)

    # TODO: check WiFi/internet status? if down, then switch to error?

    # Connect to audio stream at STREAMURL
    # On successful connection, status = 'CONNECTED'
    # If stream disconnects, status = 'ERROR' while try to reconnect
    #status = 'CONNECTED'
    #status = 'ERROR'
    #writeStatus(status, STATUSFILE)


if __name__ == "__main__":
    main()