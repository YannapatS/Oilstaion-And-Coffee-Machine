print('#' * 82)
print("#" + " " * 28, 'Gasoline 95 = 29.16/ลิตร' + " "*28 + "#")
print("#" + " " * 28, 'Gasoline 91 = 25.30/ลิตร' + " "*28 + "#")
print("#" + " " * 28, 'Gasohol 91 = 21.68/ลิตร' + " "*29 + "#")
print("#" + " " * 28, 'Gasohol E20 = 20.2/ลิตร' + " "*29 + "#")
print("#" + " " * 28, 'Gasohol 95 = 21.2/ลิตร' + " "*30 + "#")
print("#" + " " * 28, 'Diesel = 21.2/ลิตร' + " "*34 + "#")
print('#' * 82)


# เลือกประเภทที่ต้องการ

g = input('เลือกเบอร์ 1 ใส่จำนวนเงิน เลือกเบอร์ 2 ใส่จำนวนลิตร : ')

a = 'Gasoline 95'
b = 'Gasoline 91'
c = 'Gasohol 91'
d = 'Gasohol E20'
e = 'Gasohol 95'
f = 'Diesel'

# เงืือนไขสำหรับการคำนวนจากเงินแปลงเป็นลิตร
if g == '1':
    price_in = int(input("ใส่จำนวนเงิน :  "))
    oil_c = input("เลือกชนิดน้ำมัน : ")
    if oil_c == a:
        price = price_in / 29.16
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)

    elif oil_c == b:
        price = price_in / 25.30
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)

    elif oil_c == c:
        price = price_in / 21.68
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == d:
        price = price_in / 20.2
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == e:
        price = price_in / 21.2
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == f:
        price = price_in / 21.1
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)

    else:
        print('#' * 82)
        print('#' + " " * 28, "error" + " "*46 + "#")
        print('#' * 82)


# เงืือนไขสำหรับการคำนวนจากลิตรแปลงเป็นเงิน
if g == '2':
    price_in = int(input("ใส่จำนวนเงิน :  "))
    oil_c = (input("เลือกชนิดน้ำมัน : "))
    if oil_c == a:
        price = price_in * 29.16
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == b:
        price = price_in * 25.30
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == c:
        price = price_in * 21.68
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == d:
        price = price_in * 20.2
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == e:
        price = price_in * 21.2
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == f:
        price = price_in * 21.1
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)

    else:
        print('#' * 82)
        print('#' + " " * 28, "error" + " "*46 + "#")
        print('#' * 82)

if(input("Enter continue or exit ") == "exit"):
    ll = False
