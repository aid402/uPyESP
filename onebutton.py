from machine import Pin
import time

class RELAYConfig:
        button1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
light1 = machine.Pin(14, machine.Pin.OUT)
light2 = machine.Pin(12, machine.Pin.OUT)
light3 = machine.Pin(13, machine.Pin.OUT)
light4 = machine.Pin(15, machine.Pin.OUT)
light1.off()
light2.off()
light3.off()
light4.off()
stat=0
while True:
    if not button1.value():
        stat++
        if stat=4:
