""" indicator: flash an LED with a pattern to indicate the current audio state.

    Eric M. Jackson
    start of work 2023-05-27

    ASSUMPTIONS:
    -- Status file will have the status written on the first line
    -- Valid status is 'STARTUP', 'CONNECTED', or 'ERROR'
"""

import sys, os
from gpiozero import LED
from time import sleep

# CONSTANTS
STATUSFILE = '/tmp/audiostatus'
led = LED(2)

def StartupState():
    """
    Flash the LED indicator in a pattern indicating start-up state.
    Run for 2 seconds, then return
    """
    led.on
    sleep(1)
    lef.off
    sleep(1)
    return 0

def ConnectedState():
    """
    Flash the LED indicator in a pattern indicating connected state
    Run for 2 seconds, then return
    """
    led.on
    sleep(2)
    return 0

def ErrorState():
    """
    Flash the LED indicator in a pattern indicating error state
    Run for 2 seconds, then return
    """
    for _ in range(10)
        led.on
        sleep(0.2)
        lef.off
        sleep(0.2)
    return 0

def main():
    """indefinite loop to read and indicate the current audio state"""
    while True:
        try:
            with open(STATUSFILE, mode='r', encoding='utf-8-sig') as file:
                firstline = file.read().strip()
        except IOError:
            print("Could not read {}".format(STATUSFILE))
            exit(1)

        # Each function should take about 2 seconds then return
        if firstline == 'STARTUP':
            exitStatus = StartupState()
        else if firstline == 'CONNECTED':
            exitStatus = ConnectedState()
        else:
            exitStatus = ErrorState()

if __name__ == "__main__":
    main()