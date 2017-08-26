from umqtt.simple import MQTTClient
import machine
from time import sleep
import network,json
import dht
import ubinascii

led = machine.Pin(2,machine.Pin.OUT)
#connect
led.off()
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect('ssid', 'password') #your wifi
    while not sta_if.isconnected():
        pass
    ip_node = sta_if.ifconfig()[0]
    print(ip_node)
led.on()

# Setup a GPIO Pin for DHT22
d = dht.DHT22(machine.Pin(14))

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
Topic1=b"esp1/sensor"
Topic2=b"esp1/switch"
state=b"off"

def sub_cb(topic, msg):
    global state
    state = msg

def main():
    client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
    client.set_callback(sub_cb)
    client.connect()
    client.subscribe(Topic2)
    while True:
      client.check_msg()
      if state == b"on":
        led.off()
        d.measure()
        msg = json.dumps({
          'IP':ip_node,
          'temperature':d.temperature(),
          'humidity':d.humidity()
          })
        client.publish(Topic1,msg)
        led.on()
      sleep(1)
    client.disconnect()

main()
