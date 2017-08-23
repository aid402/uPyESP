from machine import Pin
from time import sleep
import onebutton

#switch box @living room
boxID_1 = 'B1' 
pinList_1 = [14,12,13]
patList_1 = ['000','100','110','111','001']

#switch box @terrace
boxID_2 = 'B2'
pinList_2 = [4,5]
patList_2 = ['00','10','01','11']

Box_01 = onebutton.Config(boxID_1, pinList_1, patList_1)
Box_02 = onebutton.Config(boxID_2, pinList_2, patList_2)

#set pin 15 as button@living room
button1 = Pin(15, Pin.IN, Pin.PULL_UP)

#set pin 2 as button@terrace
button2 = Pin(2, Pin.IN, Pin.PULL_UP)

while True:
    while not button1.value() or not button2.value():
        pass
    if not button1.value():
        Box_01.turn(Box_01.push())
    if not button2.value():
        Box_02.turn(Box_02.push())   
    time.sleep_ms(300)
