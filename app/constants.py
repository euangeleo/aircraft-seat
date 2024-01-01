# CONSTANTS
STATUSFILE = '/tmp/audiostream/audiostatus'
VOLUMEFILE = '/tmp/audiostream/audiovolume'
CHANNELFILE = '/tmp/audiostream/audiochannel'
STREAMURLS = {1:'https://slcr.me/SLCR1',                     # rock, St Louis Classic Rock Preservation Society
              2:'https://slcr.me/SLCR66',                    # oldies, SLCR Route 66
              3:'https://kexp.streamguys1.com/kexp64.aac',   # pop, KEXP Seattle
              4:'http://cast1.torontocast.com:1650/stream',  # jazz, Jazz Radio Network
              5:'https://kbaq.streamguys1.com/kbaq_mp3_128', # classical, KBAQ (Phoenix)
              6:'http://d.liveatc.net/ktus'}                # ATC, KTUS

PINNUM = 14 # This pin is directly below the 5V out and ground pin on RPi header that I'm also using