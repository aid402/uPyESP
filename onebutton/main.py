from umqtt.simple import MQTTClient
import machine
from time import sleep_ms
import json
import dht
import ubinascii
import onebutton

led = machine.Pin(2,machine.Pin.OUT)
#connect
led.off()
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('LP_wireless', '1871157210')
    while not sta_if.isconnected():
        pass
    ip_node = sta_if.ifconfig()[0]
    print(ip_node)
led.on()

# Modify below section as required
CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "192.168.1.46",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     # unique identifier of the chip
     "CLIENT_ID": b"ESP8266" + ubinascii.hexlify(machine.unique_id())
}
Topic1=b"box1/pattern"

#switch box @living room
boxID_1 = 'B1' 
pinList_1 = [14,12,13]
patList_1 = ['000','100','110','111','001']

#create onebutton object
box = onebutton.Config(boxID_1, pinList_1, patList_1)

#set pin 15 as button
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

def sub_cb(topic, msg):
    if msg != box.patternList[box.state]:
        led.off()
        box.turn(msg)
        led.on()
        
def main():
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(Topic1)
    client.check_msg()
    msg = json.dumps({
        'IP':ip_node,
        'pattern':box.patternList[box.push()],
        })
    client.publish(Topic1,msg)
    while True:
        client.check_msg()
        if button.value():
            led.off()
            msg = json.dumps({
                'IP':ip_node,
                'pattern':box.patternList[box.push()],
                })
            client.publish(Topic1,msg)
            box.turn(box.patternList[box.state])
            sleep_ms(300)
            led.on()

main()
