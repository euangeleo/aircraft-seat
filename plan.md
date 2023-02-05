# Current plan

* In-flight entertainment: ideas:
  * find a small FM radio with presets, and wire pre-sets in to the previous IFE bus?
  * Use Raspberry Pi to pull Internet radio streams based on which channel is selected on IFE seat arm panel?
  * Run separate source directly into 1/8in stereo jack (in which case pabel is non-functional)?

## Plan Number 1 (NOW DEPRECATED)
*Summary* Provide all inputs just as they would be on the aircraft. This includes inflight entertainment (audio only) encoded over RF coax input, and input AC power (at 115V400Hz) to all power boxes.
*Difficulties*
* Providing 115V400Hz power via a frequency adapter is economically infeasible. I paid US$400 for the pair of seats, and I'm not paying [US$1400](https://www.powerstream.com/1-phase-frequency-converter-60Hz-to-400hz-500w.htm) to convert wall power (110V60Hz) to proper input for the seats; best budget would be US$150 or less. (Maybe find a salvage frequency converter? Build one from parts?)
* Providing multiple audio signals encoded over RF (by some protocol that I don't currently know) exceeds what I'm able to do on my own.

## Plan Number 2 (CURRENTLY WORKING)
*Summary* Determine the power or signals that would be *output* from each electronics box, and provide those through some other means
Outstanding questions:
* Does the Astronics power box simply convert 115V400Hz to 28 VDC for the motors and controllers? Converters (110V60Hz to 24VDC or 28 VDC can be found in the ideal budget range; just need to know the current draw/wattage.)
* Does the PGA Electronic box just convert 115V400Hz to 110V60Hz for front-side EmPower outlet? If so, mains power can be wired to these without modification.
* Does the Matsushita SEB provide DC power to the reading lights? Specs for this power?
* Does the Matsushita SEB provide line-level stereo audio signal to the armrest? Does the armrest control panel adjust volume, or does it just send volume up / down signals to the SEB to control volume in the signal?
* What signals does the armrest control panel send to the SEB for audio channel up / down?
* What signals does the SEB send to the armrest control panel to determine channel number as shown on the 7-segent display?
* What signal is sent for the attendant call / attendant clear buttons?

## Task list
* clean upholstery
* dust/clean upper/outer and inner/under
* re-glue center armrest top panel (this must wait until I'm sure I don't need access to the center console for any wiring/rewiring work)
* move upstairs -- I THINK I NEED TO DISASSEMBLE TO GET IT IN THE DOOR AND UP THE STAIRS
* build a frame so it won't tip forward when both seats are reclining? CHECK CENTER OF MASS RELATIVE TO FRONT/REAR FEET WITH TWO PAX
* power supply to FRONT OUTLETS (INPUT: 115V400Hz into PGA box, OUTPUT: 110V60Hz out from PGA box to outlets on front of center console?)
* power supply to READING LIGHTS (5V from SEB?)
* power supply to MOTORS (INPUT: 115V400Hz into Astronics box?)
