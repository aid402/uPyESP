from umqtt.simple import MQTTClient
from time import sleep_ms
import network
import machine,json,dht,ubinascii,onebutton

led = machine.Pin(2,machine.Pin.OUT,value=0)

#connect wifi
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('ssid', 'password')
    while not sta_if.isconnected():
        pass
    node_ip = sta_if.ifconfig()[0]
    led.value(1)
else:
    node_ip = sta_if.ifconfig()[0]
    led.value(1)

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
Topic = b"box1"

#switch box @living room
boxID = 'B1' 
pinList = [14,12,13]
patList = ['000','100','110','111','001']

#create onebutton object
box = onebutton.Config(boxID, pinList, patList)

#set pin 15 as button
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

def sub_cb(topic, msg):
    msg = json.loads(msg)
    if msg['pattern'] != box.pattern:
        led.off()
        print(msg + "(from dashboard)")
        box.pattern = msg['pattern']
        box.iturn()
        if box.pattern in box.patternList:
            box.state = box.patternList.index(box.pattern)
        led.on()
    else:
        print(msg + "(button pressed)")
#MQTT connect
client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
client.set_callback(sub_cb)
client.connect()
client.subscribe(Topic)
        
def main():
    msg = json.dumps({
        'IP':node_ip,
        'pattern':box.patternList[0],
        })
    client.publish(Topic,msg)
    while True:
        while not button.value():
            client.check_msg()
        if button.value():
            led.off()
            msg = json.dumps({
                'IP':node_ip,
                'pattern':box.patternList[box.push()],
                })
            client.publish(Topic,msg)
            box.turn()
            sleep_ms(300)
            led.on()

main()
