# Current plan

* In-flight entertainment, brainstorming ideas:
  * find a small FM radio with presets, and wire pre-sets in to the previous IFE box?
  * Use Raspberry Pi to pull Internet radio streams based on which channel is selected on IFE seat arm panel?
  * Run separate source directly into 1/8in stereo jack (in which case pabel is non-functional)?

## Plan Number 1 (NOW DEPRECATED)
*Summary* Provide all inputs just as they would be on the aircraft. This includes inflight entertainment (audio only) encoded over RF coax input, and input AC power (at 115V400Hz) to all power boxes.
*Difficulties*
* Providing 115V400Hz power via a frequency adapter is economically infeasible. I paid US$400 for the pair of seats, and I'm not paying [US$1400](https://www.powerstream.com/1-phase-frequency-converter-60Hz-to-400hz-500w.htm) to convert wall power (110V60Hz) to proper input for the seats; best budget would be US$150 or less. (Maybe find a salvage frequency converter? Build one from parts?)
* Providing multiple audio signals encoded over RF (by some protocol that I don't currently know) exceeds what I'm able to do on my own.

## Plan Number 2 (CURRENTLY WORKING)
*Summary* Determine the power or signals that would be *output* from each electronics box, and provide those through some other means.

### RECLINER FUNCTIONS
* Does the PGA Electronic box simply convert 115V400Hz to 24/27/29 VDC for the motors and controllers? Converters (110V60Hz to 24VDC or 28 VDC can be found in the ideal budget range; just need to know the current draw/wattage.)
  * How can I figure out what type of power was provided, without having access to any wiring/electronics documentation for this box? Standard home recliners appear to commonly use 24-29V. (For one example, see [this EE StackExchange post](https://electronics.stackexchange.com/questions/568350/different-output-for-recliner-power-supply-safe-to-use-25v-2-5a-to-a-29v-2a).)
### FRONT OF SEAT POWER OUTLETS
* The Astronics power box appears to convert 115V400Hz to 110V60Hz for the front-side EmPower outlets. There is also a smaller-gauge line that goes from this box to one of the LEDs on the side of the seat shell; was this simply a status or power indicator? Current plan is to remove the Astronics box entirely and wire mains power to the seat-front outlets without modification. The seat shell LED will be wired to the Raspberry Pi (running in-flight entertainment) as a status indicator.
### GOOSENECK LED READING LIGHTS
* Does the Matsushita SEB provide DC power to the reading lights? No, they're wired to the PGA Electronics box.
  * ANSWER: reading lights take 12V DC; at least that makes them look reasonably bright, and the wire itself says it's rated for 12V. This power was coming from the PGA Electronic box (which I guessed powered the recliner controls). This seems consistent with that box working with "low" (12-28) voltage power. I had planned to provide power for the reading lights from a wall wart power supply--but this looks like I could simply leave them connected to the PGA box if I can get that one properly powered.
### IN-FLIGHT ENTERTAINMENT
* Does the Matsushita SEB provide line-level stereo audio signal to the armrest? Does the armrest control panel (PCU =? "passenger control unit") adjust volume, or does it just send volume up / down signals to the SEB to control volume in the signal?
  * PARTIAL ANSWER: Found power, ground, and audio inputs to PCU; volume buttons on the PCU don't seem to adjust volume on their own, so I conclude that the SEB was sending full-output audio levels (ie, not line level) to the PCU, and the PCU was sending volume up/down signals to the SEB. I plan to provide audio from a Raspberry Pi. If I can figure out what those signals were, sent from the PCU to the SEB, I could possibly decode them with the Raspberry Pi and have the PCU buttons still control volume, maybe audio source, maybe other things.
* What signals does the armrest control panel send to the SEB for audio channel up / down?
* What signals does the SEB send to the armrest control panel to determine channel number as shown on the 7-segent display? Some voltage on one of the conductors? Some resistance on one of the conductors?
* What signal is sent for the attendant call / attendant clear buttons?
* PLAN:
  * I can provide a stereo audio signal from a Raspberry Pi. Interesting signals could be various internet radio stations (like in-flight radio stations), or even [live ATC chatter from KTUS](https://s1-fmt2.liveatc.net/ktus2).
  * If I can decode the signals from the volume or channel buttons, I could implement some kind of control for the RasPi. Otherwise, it would be at a fixed volume and fixed channel/source.
  * It looks like one RasPi could provide only one audio signal, so I may simply need to wire the same signal to both PCUs (ie, to the left and right seat audio jacks)--or buy a second RasPi.
  * Use blue & green seat shell LEDs as indicators from the RasPi? or leave green LED as power indicator for PGA ECU?

## Task list
* clean upholstery
* dust/clean upper/outer and inner/under
  * DONE!
* re-glue center armrest top panel (this must wait until I'm sure I don't need access to the center console for any wiring/rewiring work)
* move upstairs -- I NEED TO DISASSEMBLE TO GET IT IN THE DOOR AND UP THE STAIRS
  * DONE! Its dimensions now allow moving up the stairs
* build a frame so it won't tip forward when both seats are reclining? CHECK CENTER OF MASS RELATIVE TO FRONT/REAR FEET WITH TWO PAX
* power supply to FRONT OUTLETS (use mains power 110V60Hz)
* power supply to READING LIGHTS (12V from PGA Electronics box (recliner controls)?
* power supply to MOTORS (INPUT: hard to get 115V400Hz into first PGA box? easier to get 24/27/29 VDC into second PGA box?)
