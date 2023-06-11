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