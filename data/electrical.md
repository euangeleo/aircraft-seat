# Airplane seats: electrical

Pair of Sicma Aero Majesty 1606 seats (first class 767-300)

## Raw electrical

Electrical items include:
* two small indicator lights (LED?) on right outer shell (about 6 inches above floor), one green one blue
* two white LED reading lights on a flexible gooseneck extending from upper front of central pillar
* two in-flight entertainment passenger control units on center armrest
* electrical/electronics boxes discussed in following section

### Reading lights

Observations
* Two wires plus a grounding strap going to each light, through center pillar
* back of light head includes a momentary on/off switch and a momentary intensity switch
* wires indicate "12V DC" and a S/N
* Testing:
  * lights come on at 8V, seem reasonably bright at 12V, and brighter still at 15V (but didn't keep it at 15V long)
  * Provide power, then push on/off to turn on
  * intensity switch cycles between full, mid, low, mid, full ...
  * LEFT SIDE light: Red is positive, brown is ground
  * RIGHT SIDE light: could not see color of wires due to heatshrink

### Attendant call lights

Observations
* two wires going to each light
* blue is aft, green is forward
* green light has brown wire (+5V), red wire (GROUND)
* blue light has blue/white wire (+5V), white wire (GROUND)
* Same power supply, green was drawing at 4.5V, blue at 4.9V

### Center armrest in-flight entertainment controls

Observations
* six wires going to each unit
* three wires coming out of the unit, going to headphone jack (two bayonet style)
* LEFT PCU: from top to bottom (when unit is in passenger orientation) all wires are white with colored stripes: 1 orange (or yellow?), 2 red, 3 green, 4 blue, 5 white w/ numbers, 6 black
* GROUND is third wire from top (white with green stripe)
* POWER is fourth wire from top (white with blue stripe)
* display comes on dimly at 5V, looks normally bright at 12V
* channel indicator came on with "6" on 7-seg display
* buttons are back-lit
* pushing buttons (volume up, volume down, channel up, channel down, light, attendant call, attendant clear) has no response on panel --> cannot test for volume without having an audio signal to test, but did test for channel, light, attendant call; maybe these momentary buttons just send a signal to the underseat SEB to process the response?

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
* This is the box that controls seat position based on input from two "keyboards" on the center armrest

### Matsushita SEB
* Two connectors at rear of box (left/right): coax plus five pins
* One connector at front of box, connected two two cables that head into the central armrest
* Interpretation: this looks like it receives an RF signal over coax, plus five other pins, from one connector on rear, and passes the same signal on to daisy chain to the next seat via the other connector on rear, while also passing a 24-pin output (via connector at front, not all conductors are used) to the IFE control panels for this pair of seats. If the neighboring box (power box under right seat) is representative, the input goes into the left connector, and the output to next seat is from right connector.
* I think this handles just the In Flight Entertainment (ie, audio only), not the 120V AC outlets. The diameter of the conductors seems too small for the power draw you might have on a power socket. Need to check the wiring to make sure.
* This *might* run the reading lights (I note that there *is* a light control on the IFE panel; does this control these reading lights, or a light placed in the cabin ceiling?), but if so, I suspect it's providing 5V to them, not anything more powerful.
* There are screen-printed labels between the two PC boards: (see photos)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x 1 2 3 4 x x x (1: L R) x x x x G? B5 5 8 G (AC: x x) (AC: x x)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x (ATT CON: 1 2 3 4) +5V (4: L R) (1: L R) (2: L R) (3: L R) x x x x x x x x x
* There are screen-printed labels on the 24-pin outputs: (see photos)(CORY 71771 CB24R-3 R5SCB24R-3 9809)
(DATA: 1 2 3 4) (POWER: 1 2 3 4) (4: R L) (?: L R) (L R) (L R) (L R) GND
* The 1 2 3 4 likely refer to seats, not audio channels, since the largest number of seats in a row is hypotheticaly four (in a center section; that way, the same box could be used everywhere, and just wired up differently depending on the number of seats); the L and R then refer to left/right channel. (NOT left/right seat, which would then be specific to just a pair of seats)
* Six conductors to each passenger control unit in the armrest? **Data (what format is this signal?), Power (5V), Ground, audio left, audio right, attendant call?**

* The output from this box is simpler, in terms of conductors in the receptacle. 
* I think the easiest thing will be to simply bypass this box; otherwise, I think I'd have to encode multiple audio streams into the RF input, and I'm not sure how to do that in the way that this box expects


* The controlers in the armrests are marked: PCU (passenger control unit?) MFR P/N RD-AX6530-E1 S/N 00871 MFG DATE 08 '9(1?) Matsushita Electric Industrial Co, Ltd.
* There are just six pins that go in to each controller, and three conductors that leave each controller to the headphone jack; I should be able to provide power and signal to those six pins for each side.

* NOTE: The controls that are on the IFE panel are: volume up; volume down; channel up; channel down; light toggle; attendant call; attendant call clear;

### Astronics in-seat power supply

* Labels on 2 rear connectors: no labels
* Left is 6 pin male, right is six pin female
* Interpreation of connetors: Same as PGA box? (daisy chained to next row of seats?)
* Interpretation of purpose: power supply for passenger 110V60Hz outlets?
* Can I simply wire the front outlets into a wall mains power source?

### PGA Electronics, power supply for ECU?

* Labels on 2 rear connectors:
* Left: "X1 INPUT 115V 400Hz", six pin male 
* Right: "X3 OUTPUT next SEAT", six pin female
* Two front outputs: insulated wire, no connector. (Is this simply power for the ECU under the left seat? Cannot follow wiring to make sure.
* Interpretation: power is daisy-chained from one row of seats to the next?
* What does this box output? If it converts 115V400Hz AC power into something else (27V DC?) for the ECU, then could I simply replace it with a different wall power converter (110V60Hz AC to 27V DC)?
