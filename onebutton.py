from machine import Pin

class Config:
        
    def __init__(self, box_id, pinSwitch, patternList):
        self.state = 0
        self.box_id = box_id
        self.pinSwitch = pinSwitch
        self.numSwitch = len(pinSwitch)
        self.patternList = patternList
        self.switch_0 = pinSwitch[0]
        if self.numSwitch > 1:
            self.switch_1 = Pin(pinSwitch[1], Pin.OUT, value=0)
        if self.numSwitch > 2:
            self.switch_2 = Pin(pinSwitch[2], Pin.OUT, value=0)
        if self.numSwitch > 3:
            self.switch_3 = Pin(pinSwitch[3], Pin.OUT, value=0)
        #...
        #...
        
    def turn(self, pattern_num):
        p = self.patternList[pattern_num]
        self.switch_0.value(int(p[0]))
        if self.numSwitch > 1:
            self.switch_1.value(int(p[1]))
        if self.numSwitch > 2:
            self.switch_2.value(int(p[2]))
        if self.numSwitch > 3:
            self.switch_3.value(int(p[3]))
        #...
        #...

    def push(self):
        self.state += 1
        if self.state >= len(self.relay) :
            self.state = 0
        return self.state
