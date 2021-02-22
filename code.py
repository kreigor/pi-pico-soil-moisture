import board
import digitalio
import simpleio
from analogio import AnalogIn
import time
import math

ledGreenPin = board.GP15
ledGreen = digitalio.DigitalInOut(ledGreenPin)
ledGreen.direction = digitalio.Direction.OUTPUT

ledYellowPin = board.GP14
ledYellow = digitalio.DigitalInOut(ledYellowPin)
ledYellow.direction = digitalio.Direction.OUTPUT

ledRedPin = board.GP13
ledRed = digitalio.DigitalInOut(ledRedPin)
ledRed.direction = digitalio.Direction.OUTPUT

analog_in = AnalogIn(board.GP26)

delay = 2.0
DRY_VALUE = 48832
WET_VALUE = 20096

print("Hello World!!!")

while True:
    moistureValue = analog_in.value
    print(moistureValue)

    moisturePercent = math.ceil(simpleio.map_range(moistureValue, DRY_VALUE, WET_VALUE, 0, 100))
    print(moisturePercent)

    if moisturePercent < 20:
        ledRed.value = True
        ledYellow.value = False
        ledGreen.value = False
    elif moisturePercent > 80 and moisturePercent <= 100:
        ledRed.value = True
        ledYellow.value = False
        ledGreen.value = False
    elif moisturePercent >= 20 and moisturePercent < 40:
        ledRed.value = False
        ledYellow.value = True
        ledGreen.value = False
    elif moisturePercent >= 40 and moisturePercent < 80:
        ledRed.value = False
        ledYellow.value = False
        ledGreen.value = True
    else:
        ledRed.value = True
        ledYellow.value = True
        ledGreen.value = True

    time.sleep(delay)