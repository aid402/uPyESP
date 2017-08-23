from machine import Pin

class RELAYConfig:
        
    def __init__(self, relaySet_id, pinButton, pinRelay, Pattern):
        self.state = 0
        self.relaySet_id = relaySet_id
        self.Pattern = Pattern
        self.Button = Pin(pinButton, Pin.IN, Pin.PULL_UP)
        for i in range(len(pinRelay)):
            self.relay[i] = Pin(pinRelay[i], Pin.OUT, value=0)
        
    def turn(self, pattern_num):
        p = self.Pattern[pattern_num]
        for n in range(len(self.relay)):
            self.relay[n].value(int(p[n]))
    
    def push(self):
        self.state += 1
        if self.state >= len(self.relay) :
            self.state = 0
