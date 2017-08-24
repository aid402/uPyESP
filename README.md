# micropython esp project
## onebutton.py
เป็น module ที่ใช้ควบคุม Pin.OUT หลายๆ pin พร้อมกัน ตามรูปแบบ(pattern) ที่กำหนดไว้ใน patternList
class onebutton.Config(Box_id, [pinList], [patternList])
    - Box_id : id ของกลุ่ม pin เช่น B01
    - [pinList] : รายการหมายเลข pin เช่น [12,13,14]
    - [partternList] : รายการรูปแบบ เช่น ['000','100','010','111']
    
onebutton.turn(pattern_num)
    กำหนด pin.value ตามรูปแบบ(pattern)
    pattern_num : ลำดับ pattern ใน [patternList]

onebutton.push()
    เพิ่มค่า state (state+1) ซึ่งระบุลำดับ pattern และคืนกลับค่า state
    ถ้า state มีค่าเท่ากับ จำนวน pattern ใน patternList จะคืนค่า state = 0
