from machine import Pin
import time

class RELAYConfig:
        
    def __init__(relay_id, pinButton, pinRelay, patturn):
        button = Pin(pinButton, Pin.IN, Pin.PULL_UP)
        for i in range(len(pinRelay)):
            relay[i] = Pin(pinRalay[i], Pin.OUT, value=0)

stat=0
while True:
    if not button1.value():
        stat++
        if stat=4:
