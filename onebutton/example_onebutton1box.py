from machine import Pin
from time import sleep_ms
import onebutton

#switch box @living room
boxID_1 = 'B1' 
pinList_1 = [14,12,13]
patList_1 = ['000','100','110','111','001']

#create onebutton object
Box_01 = onebutton.Config(boxID_1, pinList_1, patList_1)

#set pin 15 as button@living room
button1 = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    while not button1.value():
        pass
    Box_01.push()
    Box_01.turn()
    sleep_ms(300)
