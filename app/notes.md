# Notes regarding programming

I want to have a Python script load an online audio stream, and control one
shell side LED to indicate the status of this stream: slow flash during
boot and startup, solid on for connected, and fast flashing if there's an
error. My initial thinking was to use a microservices approach, so I could
have one thread managing the LED, and another thread managing the audio
stream. I started working on gRPC, but eventually determined that this
was far more than I needed for this project.

A simpler approach will be to have one Python script that handles the audio
connection, and will update the status by writing to a file. A second Python
script will read from this file every two seconds, command the light to light
appropriately for those two seconds according to the state in the file, then
re-check the file, etc,

Further reflection indicates that (1) I don't need the audio running 24 hours
a day, 7 days a week. If the connection is shut off overnight, this might
allow for a bit of error-checking (the connection will be reset every 24 hours).
I'm assuming that the live streaming URL for LiveATC audio does not
change every day or every several days, so using one constant URL won't cause
problems. If this assumption turns out not to be valid, I can have a third Python
script that scrapes the URL for LiveATC each morning before 5 (run as a CRON job?),
to get that day's streaming URL. This URL can be written to a file. The
audio-playing Python script can be run at 6am (again, via CRON?), first reading
in the URL, and then connecting to it. At 10om each day, the connection can be
closed and the script terminated. I could build the audio streaming script to read
the URL from a file, so that if I need to change it, I can do so easily. (I'll
also need to validate the URL each day, since I think otherwise this would be
a security hole.)

## End of 2023-05-27

The file `indicator.py` properly controls the shell side LED indicator; it
is currently connected to the blue/aft LED, with a 330 kOhm resistor in
series. It properly sets the blinking status based on the text that is in
`/tmp/audiostatus`.

The file `audiostream.py` writes the `STARTUP` status to the status file.

## End of 2023-06-07

I now have `audiostream.py` set up to use python-vlc. I'm not sure if it's
working, though. Maybe have to fiddle a bit in a REPL to make sure it's working?

## Middle of 23-06-11

The `audiostream.py` file is now properly using python-vlc. I couldn't
get it to work using the LiveATC *playlist*, but it seems to work fine if I
use the URL that is provided in that playlist. Rather than have that script
have to parse the playlist to get the URL, I've just hard-coded it in. If
this becomes a problem, I can change it.

Now that I'm shutting down the playing of the stream overnight, do I need to
add a fourth status, something like "overnight hold"? Will a blinking light
be disturbing if someone is ever sleeping in that room? The blue LED is pretty
dim, so I don't think so.

So, if the code part is working well enough now, then I need to focus on
getting it set up to run via CRON or something comparable.

Run on startup: indicator.py (should remain always running)
Run daily at 6am: audiostream.py (will run daily until 10pm)

Guide for running things on RasPi on startup: https://www.sparkfun.com/news/2779

```
sudo nano /etc/rc.local
```
Just before the exit 0 line, add the following:
```
/usr/bin/python3 /home/<username>/<path>/indicator.py &
```

Guide for setting up cron jobs: https://pimylifeup.com/cron-jobs-and-crontab/

crontab -e
0 6 * * * /home/<username>/<path>/audiostream.py

## Middle of 23-06-17

The .rclocal and cron approach doesn't seem to have worked well. The audio script doesn't seem
to be starting daily, and I can't tell whether the indicator script is running (the LED is on,
but I don't know if the GPIO pins would default to "off", or would remain "on", if that script
stopped). The light status doesn't seem to be changing properly when I change the status in
the file, and ps -A | grep python3 doesn't turn up any processes.

I don't want to have two instances of the audio stream running, and although I could add a check
to the script at the beginning (when executed, first check whether there's another script by
this name running, and if it is, then end), the easier way to ensure that would be to use
systemd.

Following the systemd section on https://www.sparkfun.com/news/2779 and 
https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-3-systemd

I'll use these files:

/lib/systemd/system/indicator.service
```quote
[Unit]
Description=Use an LED to indicate the audio status
After=boot-complete.target

[Service]
ExecStart=/usr/bin/python3 /home/seb/GitHub/aircraft-seat/app/indicator.py
Restart=always
RestartSec=4s
KillMode=process
TimeoutSec=infinity

[Install]
WantedBy=boot-complete.target
```

/lib/systemd/system/audiostream.service
```quote
[Unit]
Description=stream audio to the headphones
After=network-online.target

[Service]
ExecStart=/usr/bin/python3 /home/seb/GitHub/aircraft-seat/app/audiostream.py
Restart=always
RestartSec=5s
KillMode=process
TimeoutSec=infinity

[Install]
WantedBy=network-online.target
```

then

sudo systemctl daemon-reload
sudo systemctl enable indicator.service
sudo systemctl enable audiostream.service
sudo reboot

## End of 23-06-18

The systemd solution sorta works, though the services don't seem to be starting on boot. I can start
them manually, but the audiostream.service doesn't seem to be writing the status to /tmp. I found
this page (https://blog.oddbit.com/post/2012-11-05-fedora-private-tmp/) which suggests that systemd
services *may* be using private directories in /tmp. I don't *see* one that looks like it's private,
but let me force that setting to be false and see if it helps.

Hmm, for reasons I don't yet know, it appears that the audiostream.py file, when run as a systemd
service, isn't writing to /tmp/audiostatus, even when the "private temp" setting is set to false.
Is this likely a permissions issue? What user is the systemd process being run as, and what
permissions does it have?

Also, as the system is set up now, it's not running as I intended: I intended the audio stream
to shut off daily at 10pm, and restart daily at 6pm, while the indicator should remain on at all
times. However, the restarting value for the audiostream service means that it'll keep
restarting the service after 10pm, even though each time it does, the service will shut itself
off--until 12:00am, at which time the script will allow itself to not shut off, since it's now
(again) "before" 10pm. Need to adjust this, if I really want my intended behavior.

## 23-06-29

Okay, using systemd to restart the audio streaming service if it ever stopped was not a good
solution for keeping the audio off overnight. It also meant that the streaming would start again
at midnight, rather than 6am. However, systemd offers timers!

https://wiki.archlinux.org/title/systemd/Timers

This may be a good option to restart the service daily at 6am, and let the script stop itself
daily at 10pm.