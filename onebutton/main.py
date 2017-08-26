from umqtt.simple import MQTTClient
from time import sleep_ms
import machine,json,dht,ubinascii,onebutton,wifi

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
Topic=b"box1/pattern"

#switch box @living room
boxID = 'B1' 
pinList = [14,12,13]
patList = ['000','100','110','111','001']

#create onebutton object
box = onebutton.Config(boxID, pinList, patList)

#set pin 15 as button
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

def sub_cb(topic, msg):
    if msg != box.pattern:
        led.off()
        box.pattern = msg
        box.iturn()
        led.on()
        
def main():
    ip_node = wifi.connect()
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
