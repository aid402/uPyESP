from machine import Pin

class Config:
        
    def __init__(self, box_id, pinList, patternList):
        self.state = 0
        self.box_id = box_id
        self.pinList = pinList
        self.numSwitch = len(pinList)
        self.patternList = patternList
        self.numPattern = len(patternList)
        self.switch_0 = Pin(pinList[0], Pin.OUT, value=0)
        if self.numSwitch > 1:
            self.switch_1 = Pin(pinList[1], Pin.OUT, value=0)
        if self.numSwitch > 2:
            self.switch_2 = Pin(pinList[2], Pin.OUT, value=0)
        if self.numSwitch > 3:
            self.switch_3 = Pin(pinList[3], Pin.OUT, value=0)
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
        if self.state >= self.numPattern:
            self.state = 0
        return self.state
