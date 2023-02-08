# Airplane seats

Pair of first class seats:
![pair of Sicma Aero Majesty 1606 seats](https://web.archive.org/web/20230204035608/https://cdn.shopify.com/s/files/1/0549/4924/9221/products/7ddae964-57fa-4efe-aad2-4c080b0e1153_590x.jpg?v=1659049286)

## Purchase information
SELLER: Whale Tail Sales
URL: https://whaletailsales.com/products/first-class-airline-seats [archived](https://web.archive.org/web/20221006153542/https://whaletailsales.com/products/first-class-airline-seats)

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

[History of 767-300s with El Al](https://www.israelairlinemuseum.org/el-al-fleet/el-al-fleet-historic/el-al-fleet-historic-boeing-767-300s/)

[Last 767-300 commercial flight in 2019](https://web.archive.org/web/20190209181344/https://worldairlinenews.com/2019/02/09/el-al-retires-the-last-boeing-767-300/)

First Class interior:

[Youtube: El Al 767-300 first class interior showing seat pods, Sicma Aerospace Majesty 1606](https://youtube.com/clip/Ugkx5eTNODJqJsnFVsUAPTpRQkua3Jl5rEdc)

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

## Other helpful online information

* [Someone trying to provide power to first class seats](https://www.reddit.com/r/arduino/comments/f3k6qs/first_class_airplane_seat_project_help/) (unsure of seat model, but may be similar electronics)
* [Wiring diagram, single seat](https://wingdesign.com/wp-content/uploads/2016/06/25-26-38-TESTO-PART-2-.pdf) for B767-300 (looks like a different seat model, but wiring principles may be similar?)

## Notes
* two seats
* left side looks like it was wall-facing, right side has step up
* indicated as Row 11 (separately: this would be second row First Class)
* Seats would normally be motorized to move in various ways
* Without power, the seat joints can be moved by hand if a particular joint is unlocked
* Lock/unlock panel is at lower front of seat, under foot section (which can be lifted clear if unlocked)
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

## Humor
Passenger items I've found in the seats so far:
* one pair black in-flight socks
* one unused toothpick in a paper wrapper
* one green string with split-ring ends
