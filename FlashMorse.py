
from time import sleep

from MorseCode import *

flashTime = 0.2

mes = "hello world"

signal = toSignal(encode(mes))

print(signal)

import kivy
from plyer import flash, vibrator

for char in signal:
    if char == "1":
        flash.on()
        vibrator.vibrate(time=flashTime)
    elif char == "0":
        flash.off()
        
    sleep(flashTime)

flash.off()