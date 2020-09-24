from zeep import Client
from lxml import etree

# Define oil price server

client = Client('http://www.pttor.com/OilPrice.asmx?WSDL')

result = client.service.CurrentOilPrice("en")

root = etree.fromstring(result)

# define empty list

GasProduct = []
GasPrice = []

gas = {"Gasoline 95": 29.16, "Gasoline 91": 25.30, "Gasohol 91": 21.68,
       "Gasohol E20": 20.2, "Gasohol 95": 21.2, "Diesel": 21.1}


# traverse oil price list and print out

for r in root.xpath('FUEL'):
    product = r.xpath('PRODUCT/text()')[0]
    price = r.xpath('PRICE/text()') or [0]

    #    GasProduct.append([product, float(price[0])])
    #    GasPrice.append(price)

    #print(product, float(price[0]),' BAHT')
    if (float(price[0]) != 0):
        gas[product] = float(price[0])


a = 'Gasoline 95'
b = 'Gasoline 91'
c = 'Gasohol 91'
d = 'Gasohol E20'
e = 'Gasohol 95'
f = 'Diesel'


print('#' * 82)
print("#" + " " * 28, "Gasoline 95 : ",
      gas["Gasoline 95"], " BAHT" + " "*25 + "#")
print("#" + " " * 28, "Gasoline 91 : ",
      gas["Gasoline 91"], " BAHT" + " "*26 + "#")
print("#" + " " * 28, "Gasohol 91 : ",
      gas["Gasohol 91"], " BAHT" + " "*26 + "#")
print("#" + " " * 28, "Gasohol E20 : ", gas["Gasohol E20"], " "*30 + "#")
print("#" + " " * 28, "Gasohol 95 : ", gas["Gasohol 95"], " "*31 + "#")
print("#" + " " * 28, "Diesel : ", gas["Diesel"], "BAHT" + " "*31 + "#")
print('#' * 82)


# เลือกประเภทที่ต้องการ

g = input('เลือกเบอร์ 1 ใส่จำนวนเงิน เลือกเบอร์ 2 ใส่จำนวนลิตร : ')


# เงืือนไขสำหรับการคำนวนจากเงินแปลงเป็นลิตร
if g == '1':
    price_in = int(input("ใส่จำนวนเงิน :  "))
    oil_c = input("เลือกชนิดน้ำมัน : ")
    if oil_c == a:
        price = price_in / gas["Gasoline 95"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)

    elif oil_c == b:
        price = price_in / gas["Gasoline 91"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)

    elif oil_c == c:
        price = price_in / gas["Gasohol 91"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == d:
        price = price_in / gas["Gasohol E20"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == e:
        price = price_in / gas["Gasohol 95"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*20 + "#")
        print('#' * 82)
    elif oil_c == f:
        price = price_in / gas["Diesel"]
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
        price = price_in * gas["Gasoline 95"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*31 + "#")
        print('#' * 82)
    elif oil_c == b:
        price = price_in * gas["Gasoline 91"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*31 + "#")
        print('#' * 82)
    elif oil_c == c:
        price = price_in * gas["Gasohol 91"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*31 + "#")
        print('#' * 82)
    elif oil_c == d:
        price = price_in * gas["Gasohol E20"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*31 + "#")
        print('#' * 82)
    elif oil_c == e:
        price = price_in * gas["Gasohol 95"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*21 + "#")
        print('#' * 82)
    elif oil_c == f:
        price = price_in * gas["Diesel"]
        print('#' * 82)
        print("#" + " " * 28, "จำนวนลิตร :  ", str(price) + " "*31 + "#")
        print('#' * 82)

    else:
        print('#' * 82)
        print('#' + " " * 28, "error" + " "*46 + "#")
        print('#' * 82)

if(input("Enter continue or exit ") == "exit"):
    ll = False
