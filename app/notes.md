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

## End of 2023-05-27

The file `indicator.py` properly controls the shell side LED indicator; it
is currently connected to the blue/aft LED, with a 330 kOhm resistor in
series. It properly sets the blinking status based on the text that is in
`/tmp/audiostatus`.

The file `audiostream.py` writes the `STARTUP` status to the status file.