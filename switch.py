from machine import Pin
import time
button1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
button2 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
button3 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
button4 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
light1 = machine.Pin(14, machine.Pin.OUT)
light2 = machine.Pin(12, machine.Pin.OUT)
light3 = machine.Pin(13, machine.Pin.OUT)
light4 = machine.Pin(15, machine.Pin.OUT)
light1.off()
light2.off()
light3.off()
light4.off()
while True:
    if not button1.value():
        light1.value(not light1.value())
    if not button2.value():
        light2.value(not light2.value())
    if not button3.value():
        light3.value(not light3.value())
    if not button4.value():
        light4.value(not light4.value())
    time.sleep_ms(300)
