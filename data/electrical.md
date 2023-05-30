# Airplane seats: electrical

Pair of Sicma Aero Majesty 1606 seats (first class 767-300)

## Raw electrical

Electrical items include:
* two small indicator lights (LED?) on right outer shell (about 6 inches above floor), one green one blue
* two white LED reading lights (each module with 18 LEDs) on a flexible gooseneck extending from upper front of central pillar
* two in-flight entertainment passenger control units (PCUs) on center armrest
* electrical/electronics boxes discussed in following section

### Reading lights

Observations
* Two wires plus a grounding strap going to each light, through center pillar
* These wires are attached to the PGA electronic controller box under left seat
* back of each reading light module includes a momentary on/off switch and a momentary intensity switch
* wires indicate "12V DC" and a S/N
* Testing:
  * lights come on at 8V, seem reasonably bright at 12V [photo](../media/101-reading-light.jpg), and brighter still at 15V (but didn't keep it at 15V long)
  * Provide power, then push the "on/off" button that is on the back of the module to turn the light on
  * intensity switch cycles between full, mid, low, mid, full ...
  * LEFT SIDE light: Red is positive, brown is ground
  * RIGHT SIDE light: could not see color of wires due to heatshrink

### Seat shell side lights

Observations
* two wires going to each (LED?) light.
* blue is aft, green is forward.
* green light has brown wire (+5V), red wire (GROUND); wired into PGA Electronics recliner control box.
* blue light has blue/white wire (+5V), white wire (GROUND); wired into Astronics power supply box. (...*I think*. I disconnected these at the shell before I fully identified where each wire went. The pair of wires that went to the Astronics box match the white & blue/white wires that are attached to the blue light)
* Same voltage level? [green](../media/102-green-light.jpg) was drawing at 4.5V, [blue](../media/103-blue-light.jpg) at 4.9V
* These lights can be illuminated reasonably bright from the 5V GPIO pins on the Raspberry Pi.

### Center armrest in-flight entertainment controls

Observations
* The controllers in the armrests are marked: PCU (passenger control unit?) MFR P/N RD-AX6530-E1 S/N 00871 MFG DATE 08 '9(1?) Matsushita Electric Industrial Co, Ltd.
* Fasteners: There is one fastener holding each PCU in place. It appears to be a 2.5mm hex-head screw, but perhaps because the interior of the head was somewhat worn, a Torx T10 worked best for moving it.
* There is a fixed lip on the rear side of the PCU that hooks into the aperture that the PCU sits in; when the screw fastener is loosened and the tongue rotates into the body of the PCU, that end of the PCU (the front end, away from a passenger) can be pulled/rotated outward, and the rearward end can be slid forward and out of the aperture in the armrest. ([video loosening/tightening fastener](../media/221-PCU-latch-loosen-tighten.m4v), [video removing PCU](../media/222-PCU-panel-remove-insert.m4v)) 
* NOTE: The controls that are on the IFE panel are: volume up; volume down; channel up; channel down; light toggle; attendant call; attendant call clear;
* LEFT SEAT PCU: five conductors going to each unit (the connector has space for six conductors, but one conductor appears not to have contacts in the receptacle; there is no friction/resistance to a test pin when it is inserted), three conductors going out to audio jack
* audio jack is two-bayonet style, not 1/8" stereo
* Checks were done using digital multimeter
* Output connector has five conductors going to headphone jack; Top to bottom, they are:
  * x (no wire/not used)
  * x (no wire/not used)
  * red wire, connects to "red" channel (right audio channel) in audio out jack
  * white wire, connects to "white" channel (left audio channel) in audio out jack
  * pink/orange wire, connects to ground in audio out jack
* Input connector has six conductors coming from SEB; from top to bottom (when unit is in passenger orientation) all wires are white with colored stripes: 1 yellow, 2 red, 3 green, 4 blue, 5 white w/ numbers, 6 black
  * yel: 28 ohms to audio ground
  * red: right audio jack direct connection
  * grn: left audio jack direct connection
  * blu: no connection to audio ground, audio left, audio right
  * wht: feels like no contact in jack
  * blk: audio ground
* Screen printing on SEB (below) suggests that these conductors should include (1) left audio, (2) right audio, (3) (common?) ground, (4) PCU power, (5) PCU data. Which is which?
* Tested power configurations:
  * yel 6V, blk ground, panel lights up brightly (all buttons backlit), 7-seg displays "E"
  * blu 6V, blk ground, no indicators
  * blu 6V, yel ground, panel lights up dimly (mainly "light on" button), 7-seg displays "6"
  * blu 6V, yel ground, blk ground, panel lights up brightly (all buttons backlit), 7-seg displays "6"
* CONCLUSION: yel: data, red: right audio, grn: left audio, blk: ground, blu: power
* PCU buttons are back-lit
* pushing buttons (volume up, volume down, channel up, channel down, light, attendant call, attendant clear) has no response on panel. Pushing volume buttons while playing an audio signal appears to have no effect on audio signal. Also tried channel up/down, light on, attendant call/clear; there was no change in the audio that was playing and no change in what was displayed on the 7-segment display. Maybe these momentary buttons just send a signal to the underseat SEB, which is responsible for processing the response? Is it [something like this](https://electronics.stackexchange.com/questions/38417/how-do-volume-control-headphones-work#:~:text=Inside%20the%20phone%20there%20will,which%20button%20is%20being%20pressed.)?
* Have not yet tried altering the resistance on yellow conductor

## Electronics boxes

* underseat electronics boxes (left to right):
  * under left seat: PGA Electronic PN: P78621B470 "ECU Electronic Control Unit (FCBE)"
  * under center: Boeing / Matsushita "Seat Electronics Box RD-AX4406"
  * under right seat: Astronics "AC In-Seat Power Supply P/N 3E2Y8/1191-8" , PGA Electronic P80437-M01 Rev A (also just a power supply, for ECU?)

### PGA ECU
* Date 26/10/06 (Oct 26 2006)
* Software version V32.352
* Paraeter version VP010
* Connections: 1x power (J1)? 2x ?? (J2, J3), 4 others?
* There is something (a breaker?) on the forward-facing side (where all connectors are) labeled "5". Is this a 5-amp fuse/breaker?
* This is the box that controls seat position based on input from two "keyboards" on the center armrest. It has many wires coming out and connecting to the many actuator motors around the seat.

### Matsushita SEB
* Two connectors at rear of box (left/right): small coax plus five pins
* One connector at front of box, connected to two cables that head into the central armrest
* Interpretation: this looks like it receives an RF signal over coax, plus five other pins, from one connector on rear, and passes the same signal on to daisy chain to the next seat via the other connector on rear, while also passing a 24-pin output (via connector at front, not all conductors are used) to the IFE control panels ("Passenger Control Units") for this pair of seats. If the neighboring box (power box under right seat) is representative, the input goes into the left connector, and the output to next seat is from right connector.
* Although here *is* a light control on the PCU panels, this appears to *not* run the gooseneck reading lights. (Maybe the PCU buttons control a light placed in the cabin ceiling?)
* There are screen-printed labels between the two PC boards: (see photos)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x 1 2 3 4 x x x (1: L R) x x x x G? B5 5 8 G (AC: x x) (AC: x x)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x (ATT CON: 1 2 3 4) +5V (4: L R) (1: L R) (2: L R) (3: L R) x x x x x x x x x
* There are screen-printed labels on the 24-pin outputs: (see photos)(CORY 71771 CB24R-3 R5SCB24R-3 9809)
(DATA: 1 2 3 4) (POWER: 1 2 3 4) (4: R L) (?: L R) (L R) (L R) (L R) GND
* The 1 2 3 4 likely refer to seats, not audio channels, since the largest number of seats in a row is hypotheticaly four (in a center section; that way, the same box could be used everywhere, and just wired up differently depending on the number of seats); the L and R then refer to left/right channel. (NOT left/right seat, which would then be specific to just a pair of seats)
* Wiring has six conductors to each passenger control unit in the armrest, but only five are used? **Data (what format is this signal?), Power (5V?), Ground, audio left, audio right?**
* My arbitrary pinout numbers: ([photo](../media/217-IFE-box-cable.jpg), [annotated photo](../media/218-IFE-box-cable-pins.jpg))

| connector pin number from image | connects to PCU wire         | best guess function    |
|---------------------------------|------------------------------|------------------------|
| 1                               | right, white (2nd from top)  | no connection in jack? |
| 2                               | left, white (5th from top)   | no connection in jack? |
| 3                               | left, red (2nd from top)     | right channel audio    |
| 4                               | right, red (5th from top)    | right channel audio    |
| 5                               | left, blue (4th from top)    | 5V power               |
| 7                               | left, black (6th from top)   | ground                 |
| 8                               | right, black (1st from top)  | ground                 |
| 11                              | left, green (3rd from top)   | left channel audio     |
| 13                              | right, green (4th from top)  | left channel audio     |
| 14                              | (no connection found)        |                        |
| 15                              | right, blue (3rd from top)   | 5V power               |
| 17                              | (no connection found)        |                        |
| 21                              | left, yellow (1st from tope) | data?                  |
| 22                              | right, yellow (6th from top) | data?                  |


**PLAN**
* I think the easiest thing will be to simply bypass this box; otherwise, I think I'd have to encode multiple audio streams into the RF input to pass ***to*** this box, and I'm not sure how to do that in the way that this box expects. I also don't know what kind of power this box expects, or what kinds of input & output it expects on the non-coax pins.
* Replace this box with a single Raspberry Pi. RasPi can output one audio stream; I think GPIO header can't easily be used for a second audio stream, so if I want the left and right seat panel to have different feeds, I think I'd need two RasPis.
* Use the green or blue seat shell LEDs as status indicators for the RPi connection? (one LED is run by the PGA ECU, but I think I could choose either LED to be for either purpose now.)
  * Blue is dimmer than green, so maybe have solid blue indicate status up/OK. slow flashing for "booting"? rapid flashing for "problem"? Number of flashes could indicate sub-problem, but would require users to have a look-up table in order to get useful information just from the flashing.
* See [code](../app/notes.md)

### Astronics in-seat power supply

* Labels on 2 rear connectors: no labels
* Left is 6 pin male, right is six pin female
* Interpreation of two rear connetors: Same as PGA box? (ie, one is input, one is output, daisy chained to next row of seats?)
* Interpretation of purpose: power supply for passenger 110V60Hz outlets? with an LED on the side of the seat shell as a status indicator?
* Can I simply wire the front outlets into a wall mains power source?
* in-line connectors to the EmPower outlets are [Molex Micro-Fit 3.0 43025](https://www.digikey.com/en/products/detail/molex/0430250800/252499). However, I think I can keep this back-of-seat-to-front-of-seat wiring, and just provide wall power by replacing the connector that would have gone to this box. (Looks like a computer serial connector).

### PGA Electronics, power supply for ECU?

* Labels on 2 rear connectors:
  * Left: "X1 INPUT 115V 400Hz", six pin male 
  * Right: "X3 OUTPUT next SEAT", six pin female
* Two front outputs: insulated wire, no connector. (Is this simply power for the ECU under the left seat? Cannot follow wiring to make sure.
* Interpretation: power is daisy-chained from one row of seats to the next?
* What does this box output? If it converts 115V400Hz AC power into something else (24/27/29V DC?) for the ECU, then could I simply replace it with a different wall power converter (110V60Hz AC to 27V DC)?
* Unfortunately, photos of the inside of this box suggest all it does is create a place to daisy-chain to the next seat, while putting a 5A breaker in between the power supply and the actual PGA ECU under the left seat: [photo](../media/232-PGA-ECU-inside.jpg)
