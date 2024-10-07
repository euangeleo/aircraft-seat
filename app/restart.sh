#!/usr/bin/bash

mkdir /tmp/audiostream
echo '5' > /tmp/audiostream/audiochannel
echo '100' > /tmp/audiostream/audiochannel

sudo systemctl start indicator.service
sudo systemctl start audiostream.service
