print('Gasoline 95')
print('Gasoline 91')
print('Gasohol 91')
print('Gasohol 91')
print('Gasohol 95')
print('Diesel')

g = input('เลือกเบอร์ 1 ใส่จำนวนเงิน เลือกเบอร์ 2 ใส่จำนวนลิตร : ')

a = 'Gasoline 95'
b = 'Gasoline 91'
c = 'Gasohol 91'
d = 'Gasohol E20'
e = 'Gasohol 95'
f = 'Diesel'

if g == '1':
    price_in = int(input("ใส่จำนวนเงิน :  "))
    oil_c = input("เลือกชนิดน้ำมัน : ")
    if oil_c == a:
        price = price_in / 29.16
        print("จำนวนลิตร :  ", price)

    elif oil_c == b:
        price = price_in / 25.30
        print("จำนวนลิตร : ", price)
    elif oil_c == c:
        price = price_in / 21.68
        print("จำนวนลิตร : ", price)
    elif oil_c == d:
        price = price_in / 20.2
        print("จำนวนลิตร : ", price)
    elif oil_c == e:
        price = price_in / 21.2
        print("จำนวนลิตร : ", price)
    elif oil_c == f:
        price = price_in / 21.1
        print("จำนวนลิตร : ", price)
    else:
        print("error")

if g == '2':
    price_in = int(input("ใส่จำนวนเงิน :  "))
    oil_c = (input("เลือกชนิดน้ำมัน : "))
    if oil_c == a:
        price = price_in / 29.16
        print("จำนวนลิตร :  ", price)
    elif oil_c == b:
        price = price_in / 25.30
        print("จำนวนลิตร : ", price)
    elif oil_c == c:
        price = price_in / 21.68
        print("จำนวนลิตร : ", price)
    elif oil_c == d:
        price = price_in / 20.2
        print("จำนวนลิตร : ", price)
    elif oil_c == e:
        price = price_in / 21.2
        print("จำนวนลิตร : ", price)
    elif oil_c == f:
        price = price_in / 21.1
        print("จำนวนลิตร : ", price)
    else:
        print("error")

