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
* Does the PGA Electronic box under the right seat simply convert 115V400Hz to 24/27/29 VDC for the motors and controllers? Converters (110V60Hz to 24VDC or 28 VDC can be found in the ideal budget range; just need to know the current draw/wattage.) ***No, it looks like I'll need to provide 115V400Hz if I want to use existing hardware to control the recliner functions. This also includes the 12V taking lights.***
  * Standard home recliners appear to commonly use 24-29V. (For one example, see [this EE StackExchange post](https://electronics.stackexchange.com/questions/568350/different-output-for-recliner-power-supply-safe-to-use-25v-2-5a-to-a-29v-2a).)
  * I have a 28V power supply. Can I build a DC to AC converter?
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
### FEET
* The brackets that these seats stand on are separated fairly widely side to side, and somewhat wide front to back. However, they are designed to be secured to the floor of a plane. This poses at least two problems when using them in a home:
  * This concentrates the weight of the seats (somewhere around 280 lbs, as listed on the registration plate on one of the seats) on four very small points, which may damage the carpet in a home.
  * When in fully-flat configuration, this places the center of gravity of the seats far forward relative to the front foot, and they have a tendency to tip forward.
* SOLUTION to both problems: Using 1x4 wooden boards, create rails to set the feet of the seats into.
  * This spreads out the weight of the seats over a larger surface area of the floor, hopefully reducing damage to carpet or the padding beneath.
  * Extending the boards to the front of the seats enlarges the footprint of the seats, and helps move the center of gravity not so far in front of thsi footprint
  * Extending the boards to the rear of the seats will allow adding some counterweight, to move the effective center of gravity even farther back.
  * This has a side benefit of making the seats slightly easier to push around on a carpet floor.
* DESIGN and BUILD:
  * I had some scrap 1x4 boards I could use
  * I cut two lengths of 36 inches, which was enough to extend 1.5 inches in front of the front feet (can't extend too far in front, otherwise the boards will be in the way for people sitting down in the seats), and about 9 inches behind the rear feet. This is enough length to allow putting a counterweight on each board, without needing to keep the seats too far from the wall of the room.
  * The pattern of the front feet is two circles, with centers 1" apart, each of 0.75" diameter. ([photo1](media/301-foot-bracket-front-measurements-1.jpg), [photo2](media/302-foot-bracket-front-measurements-2.jpg)) I decided to drill holes into the boards for these feet to fit into. (There is a threaded ring on these feet that is of wider diameter, which can be tightened down so that the weight from the front feet is transferred to the board, not simply going straight into the carpet. With my tools, I couldn't make these holes *not* go all the way through the boards.)
  * The rear feet are more elongated and can rest on top of the board. In order to keep the rear feet from popping up off the board when the seats are front-loaded, I bought 1" conduit brackets and screwed them down over these feet. ([photo](media/304-foot-bracket-rear.jpg))
  * The completed boards are shown in [this photo](media/303-foot-bracket-in_prog.jpg)
  * Once the seats were placed on the boards and the rear brackets screwed into place, I placed a 25lb weight (conveniently in the form of an unused kettlebell) on the rear part of the board, to help keep the seats from tipping forward in the fully-reclined position. ([photo](media/305-foot-bracket-overall.jpg))

## Task list
* clean upholstery
* dust/clean upper/outer and inner/under -- DONE
* re-glue center armrest top panel (this must wait until I'm sure I don't need access to the center console for any wiring/rewiring work)
* move upstairs -- DONE

* build a frame so it won't tip forward when both seats are reclining -- DONE
  * two boards -- DONE
  * 1in conduit brackets to secure rear feet to board -- DONE
  * drill holes for forward feet bolts -- DONE
* power supply to FRONT OUTLETS (use mains power 110V60Hz) -- DONE
* power supply to READING LIGHTS (12V from PGA Electronics box (recliner controls)?
* power supply to MOTORS (INPUT: hard to get 115V400Hz into first PGA box? easier to get 24/27/29 VDC into second PGA box?)
* wiring harness from RasPi to IFE connector -- in progress
* RasPi software -- in progress
