""" indicator: flash an LED with a pattern to indicate the current audio state.

    Eric M. Jackson
    start of work 2023-05-27
    v 1.0 2023-06-04
    v 1.1 2023-12-31 work with constants file; changed settings path to /tmp/audiostream

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
"""

# following https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
#from gpiozero import LED
import RPi.GPIO as GPIO
from time import sleep
import constants as cs
# in use: cs.PINNUM, cs.STATUSFILE

def led_on(pinnum=cs.PINNUM):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pinnum, GPIO.OUT)
    GPIO.output(pinnum, GPIO.HIGH)
    return


def led_off(pinnum=cs.PINNUM):
    GPIO.output(pinnum, GPIO.LOW)
    return


def StartupState():
    """
    Flash the LED indicator in a pattern indicating start-up state.
    Run for 2 seconds, then return
    """
    led_on()
    sleep(1)
    led_off()
    sleep(1)
    return 0


def ConnectedState():
    """
    Flash the LED indicator in a pattern indicating connected state
    Run for 2 seconds, then return
    """
    led_on()
    sleep(2)
    return 0


def ErrorState():
    """
    Flash the LED indicator in a pattern indicating error state
    Run for 2 seconds, then return
    """
    for _ in range(10):
        led_on()
        sleep(0.2)
        led_off()
        sleep(0.2)
    return 0


def main():
    """indefinite loop to read and indicate the current audio state"""
    while True:
        try:
            with open(cs.STATUSFILE, mode='r', encoding='utf-8-sig') as file:
                firstline = file.read().strip()
        except IOError:
            print("Could not read {}".format(cs.STATUSFILE))
            exit(1)

        # Each function should take about 2 seconds then return
        if firstline == 'STARTUP':
            exitStatus = StartupState()
        elif firstline == 'CONNECTED':
            exitStatus = ConnectedState()
        else:   # assume anything else results in ERROR state
            exitStatus = ErrorState()

if __name__ == "__main__":
    main()