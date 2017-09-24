# micropython esp project
## onebutton.py
onebutton เป็น module ที่ใช้กำหนดค่า `Pin.value` หลายๆ pin พร้อมกัน ตามรูปแบบ(pattern) ที่กำหนดไว้

### *class* onebutton.Config(Box_id, [pinList], [patternList]) \:
สร้าง object onebutton

- `Box_id` : id ของกลุ่ม pin เช่น 'B01'
- `[pinList]` : รายการหมายเลข pin เช่น [12,13,14]   
- `[patternList]` : รายการรูปแบบ(pattern) เช่น ['000','100','010','111']

### onebutton.iturn(pattern) \:
กำหนดค่า Pin.value ตาม `pattern`
- `pattern` : รูปแบบ(pattern) เช่น '010'

### onebutton.turn() \:
กำหนดค่า Pin.value ตามรูปแบบ(pattern) ใน `[patternList]` ซึ่งระบุ index โดย onebutton.state
    
### onebutton.push() \:
เพิ่มค่า onebutton.state (onebutton.state+1) ซึ่งระบุ index ของ onebutton.patternList และคืนกลับค่า onebutton.state    
ถ้า onebutton.state มีค่าเท่ากับ len(onebutton.patternList) จะคืนค่า onebutton.state = 0
