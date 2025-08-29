

print('---------------------')
print('ตรวจสภาพรถ')
print('---------------------')
car_owner = input('ป้อนชื่อเจ้าของรถ :')
car_number = input('ป้อนทะเบียนรถ : ')
car_carbon = float(input('ป้อนปริมาณก๊าซคาร์บอนไดซออกไซน์ :'))
print('---------------------')
if car_carbon > 678.55 :
    print(f'ทะเบียนรถ {car_number} ของคุณ {car_owner} ไม่ผ่านเกณฑ์ ')
    print('ทะเบียนรถ {} ของคุณ {} ไม่ผ่านเกณฑ์ '.format(car_number,car_owner))
else :
    print(f'ทะเบียนรถ {car_number} ของคุณ {car_owner} ผ่านเกณฑ์ ')
    print('ทะเบียนรถ {} ของคุณ {} ผ่านเกณฑ์'.format(car_number,car_owner))     
print('---------------------')
print('ขอบคุณที่ใช้บริการ')