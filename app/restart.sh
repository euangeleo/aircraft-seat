#!/usr/bin/bash

mkdir /tmp/audiostream
echo '5' > /tmp/audiostream/audiochannel
echo '100' > /tmp/audiostream/audiovolume

sudo systemctl start audiostream.service
sleep 5
sudo systemctl start indicator.service
