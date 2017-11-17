from umqtt import MQTTClient
from time import sleep
import machine,network,json,dht

# Setup a GPIO Pin for DHT22
d = dht.DHT22(machine.Pin(14))

# Relay is on GPIO3
relay = machine.Pin(12,machine.Pin.OUT,value=1)

# Modify below section as required
CONFIG = {
     # Configuration details of the MQTT broker
     "MQTT_BROKER": "192.168.0.107",
     "USER": "",
     "PASSWORD": "",
     "PORT": 1883,
     # unique identifier of the chip
     "CLIENT_ID": b"esp8266_2"
}
ssid = 'xxxxxxx'
password = 'yyyyyyy'
Topic1 = b"esp2/sensor"
Topic2 = b"esp2/relay"

def sub_cb(topic, msg):
  global r
  r = int(msg)

def connect_wifi():
  sta_if = network.WLAN(network.STA_IF)
  if not sta_if.isconnected():
    sta_if.active(True)
    sta_if.connect(ssid, password) 
    while not sta_if.isconnected():
      pass
  global client
  client = MQTTClient(CONFIG['CLIENT_ID'], CONFIG['MQTT_BROKER'], user=CONFIG['USER'], password=CONFIG['PASSWORD'], port=CONFIG['PORT'])
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(Topic2)

while True:
  try:
    client.check_msg()
    d.measure()
    msg = json.dumps({
      'ID':CONFIG['CLIENT_ID'],
      'temperature':d.temperature(),
      'humidity':d.humidity()
      })
    client.publish(Topic1,msg)
  except:
    connect_wifi()
    continue
  if relay.value() != r:
    relay.value(r)
  sleep(1)
