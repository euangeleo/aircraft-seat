# Airplane seats

## Purchase information
SELLER: Whale Tail Sales
URL: https://whaletailsales.com/products/first-class-airline-seats

## Provenance and identifying information
tag:

```
AERSALE
PARTS REMOVAL AND IDENTIFICATION TAG
Registration No: N281AS
MSN: 28132
Part no: 1606211-011
Service order/operation no: 3140/18001
Serial no: 07-00020
Nomenclature/panel no: Pax seat
Location removed from: Main cabin
Removed by initials/badge no/date: JB501450 03/04/21
```
Information about N281AS:
https://www.planespotters.net/airframe/boeing-767-300-n281as-aersale-inc/rm08ke
Boeing 767-300
last air carrier: El Al, registered 4X-EAM, Daliat El Carmel / דאלית אל כרמל
First Class interior photo (similar):
https://www.airliners.net/photo/El-Al-Israel-Airlines/Boeing-767-330-ER/2801977


```
SEAT DOCUMENTATION PLATE:
Zodiac Seats France
MFG DATE 01/2007
WEIGHT 281,0 lb
elsewhere
277 lb
```

Seat Model: Sicma Aero 1606211

## Notes
* two seats
* left side looks like it was wall-facing, right side has step up
* indicated as Row 11 (separately: this would be second row First Class)
* underseat electronics boxes (left to right):
 * under left seat: ??
 * under center: Boeing / Matsushita "Seat Electronics Box RD-AX4406"
 * under right seat: Astronics "AC In-Seat Power Supply P/N 3E2Y8/1191-8" , PGA Electronic P80437-M01 Rev A

### Matsushita SEB
* Two connectors at rear of box (left/right): coax plus five pins
* One connector at front of box, connected two two cables that head into the central armrest
* Interpretation: this looks like it receives an RF signal over coax, plus five other pins, and passes the same signal on to daisy chain to the next seat, while also passing a 24-pin output to this pair of seats. If the neighboring box (under right seat) is representative, the input goes into the left connector, and the right connector is the output to the next seat.
* I think this handles just the In Flight Entertainment (ie, audio only), not the 120V AC outlets. The diameter of the conductors seems too small for the power draw you might have on a power socket. Need to check the wiring to make sure.
* This *might* run the reading lights (I note that there *is* a light control on the IFE panel; does this control these reading lights, or a light placed in the cabin ceiling?), but if so, I suspect it's providing 5V to them, not anything more powerful.
* There are screen-printed labels between the two PC boards: (see photos)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x 1 2 3 4 x x x (1: L R) x x x x G? B5 5 8 G (AC: x x) (AC: x x)
(4: R L) (3: R L) (2: R L) (1: R L) GND INIT UP x (ATT CON: 1 2 3 4) +5V (4: L R) (1: L R) (2: L R) (3: L R) x x x x x x x x x
* There are screen-printed labels on the 24-pin outputs: (see photos)(CORY 71771 CB24R-3 R5SCB24R-3 9809)
(DATA: 1 2 3 4) (POWER: 1 2 3 4) (4: R L) (?: L R) (L R) (L R) (L R) GND
* The 1 2 3 4 likely refer to seats, not audio channels, since the largest number of seats in a row is hypotheticaly four (in a center section; that way, the same box could be used everywhere, and just wired up differently depending on the number of seats); the L and R then refer to left/right channel. (NOT left/right seat, which would then be specific to just a pair of seats)

* The output from this box is simpler, in terms of conductors in the receptacle. 
* I think the easiest thing will be to simply bypass this box; otherwise, I think I'd have to encode multiple audio streams into the RF input, and I'm not sure how to do that.
* There are just six pins that go in to each controller, though; I should be able to provide power and signal to those six pins for each side.

* NOTE: The controls that are on the IFE panel are: volume up; volume down; channel up; channel down; light toggle; attendant call; attendant call clear;

### Astronics power supply

* Labels on 2 rear connectors: no labels
* Left is 6 pin male, right is six pin female
* Interpreation: Same as PGA box? (daisy chained to next row of seats?)

### PGA box?

* Labels on 2 rear connectors:
* Left: "X1 INPUT 115V 400Hz", six pin male
* Right: "X3 OUTPUT next SEAT", six pin female
* Interpretation: power is daisy-chained from one row of seats to the next?

## Task list

* clean upholstery

* dust/clean upper/outer and inner/under

* re-glue center armrest top panel
(wait until I'm sure I don't need access to the center console)

* move upstairs -- I THINK I NEED TO DISASSEMBLE TO GET IT UP THE STAIRS

* build a frame so it won't tip forward when two are reclining?

* power supply to FRONT OUTLETS (INPUT: 115V400Hz into PGA box, OUTPUT: 110V60Hz out from PGA box to outlets on front of center console?)

* power supply to READING LIGHTS (5V from SEB?)

* power supply to MOTORS (INPUT: 115V400Hz into Astronics box?)

* In-flight entertainment:
ideas:
  * find a small FM radio with presets, and wire pre-sets in to the previous IFE bus?
  * Use R Pi to pull Internet radio streams based on which channel is selected on IFE seat arm panel?
  * Run separate source directly into 1/8in stereo jack (in which case pabel is non-functional)?
