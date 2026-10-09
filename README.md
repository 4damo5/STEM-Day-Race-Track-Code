# STEM-Day-Race-Track-Code

Timing system for a toy-car race track built for Kenney Center STEM Day. A Raspberry Pi starts the clock and records video when the starting gate opens, then stops when an ultrasonic sensor sees the car at the finish and prints race time and speed.

## Hardware
- Raspberry Pi with Pi Camera
- Foil contact on the starting gate (GPIO 4) — opening the gate breaks the circuit and starts the timer
- Ultrasonic distance sensor at the finish (trigger GPIO 5, echo GPIO 17)

`python3 racecar.py` — video is saved to `~/Desktop/video.h264`.
