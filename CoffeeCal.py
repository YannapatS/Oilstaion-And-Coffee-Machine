print(" The Coffee machine has : ")

w = 400
m = 540
c = 120
d = 9
mo = 550

while True:
    print('#' * 93)
    print('#' + " " * 91 + "#")
    print('#'+" " * 91 + "#")
    print("#" + " " * 28, 'The Coffee machine has' + " "*40 + "#")
    print('#'+" " * 91 + "#")
    print('#'+" " * 91 + "#")
    print("#" + " " * 28, w, 'of water'+" "*50+"#")
    print("#" + " " * 28, m, 'of milk'+" "*51+"#")
    print("#" + " " * 28, c, 'of coffee beans'+" "*43+"#")
    print("#" + " " * 28, d, 'of disposable cups'+" "*42+"#")
    print("#" + " " * 28, mo, 'of moneys'+" "*49+"#")
    print('#'+" " * 91 + "#")
    print('#'+" " * 91 + "#")
    print('#'+" " * 91 + "#")
    print('#'+" " * 91 + "#")
    print('#'*93)

    # เลือกประเภทที่ต้องการทำรายการ(buy,fill,take)
    i = input('write action ( buy, fill , take ) : ')

    # เงื่อนไขของชนิดกาแฟ
    if (i == 'buy'):
        i2 = int(input("1- espresso, 2- latte, 3- cappuccino :"))
        # เงื่อนไขสำหรับการซื้อกาแฟ Espresso
        if (i2 == 1):
            c -= 16
            d -= 1
            mo += 4
            print('#'*93)
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, 'The Coffee machine has'+" "*40+"#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, w, 'of water'+" "*50+"#")
            print("#" + " " * 28, m, 'of milk'+" "*51+"#")
            print("#" + " " * 28, c, 'of coffee beans'+" "*43+"#")
            print("#" + " " * 28, d, 'of disposable cups'+" "*42+"#")
            print("#" + " " * 28, mo, 'of moneys'+" "*49+"#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'*93)
        # เงื่อนไขในการซื้อกาแฟ Latte
        if (i2 == 2):
            w -= 350
            m -= 75
            c -= 20
            d -= 1
            mo += 7
            print('#'*93)
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, 'The Coffee machine has'+" "*40+"#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, w, 'of water'+" "*51+"#")
            print("#" + " " * 28, m, 'of milk'+" "*51+"#")
            print("#" + " " * 28, c, 'of coffee beans'+" "*43+"#")
            print("#" + " " * 28, d, 'of disposable cups'+" "*42+"#")
            print("#" + " " * 28, mo, 'of moneys'+" "*49+"#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'*93)
        # เงื่อนไขในการซื้อกาแฟ Cappuccino
        if (i2 == 3):
            w -= 200
            m -= 100
            c -= 12
            d -= 1
            mo += 6
            print('#'*93)
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, 'The Coffee machine has'+" "*40+"#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print("#" + " " * 28, w, 'of water'+" "*50+"#")
            print("#" + " " * 28, m, 'of milk'+" "*51+"#")
            print("#" + " " * 28, c, 'of coffee beans'+" "*43+"#")
            print("#" + " " * 28, d, 'of disposable cups'+" "*42+"#")
            print("#" + " " * 28, mo, 'of moneys'+" "*49+"#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'+" " * 91 + "#")
            print('#'*93)

    # เงื่อนไขในการเติมวัตถุดิบของเครื่องชงกาแฟ(fill)
    elif i == 'fill':
        i3 = int(input("Write How many ml of water do you want to add :"))
        i4 = int(input("Write How many ml of milk do you want to add :"))
        i5 = int(input("Write How many grams of coffee beans" +
                    " do you want to add :"))
        i6 = int(input("Write How many disposable cups of " +
                    "coffee do you want to add :"))
        print('#'*93)
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print("#" + " " * 28, 'The Coffee machine has'+" "*40+"#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print("#" + " " * 28, i3+w, 'of water'+" "*50+"#")
        print("#" + " " * 28, i4+m, 'of milk'+" "*51+"#")
        print("#" + " " * 28, i5+c, 'of coffee beans'+" "*43+"#")
        print("#" + " " * 28, i6+d, 'of disposable cups'+" "*42+"#")
        print("#" + " " * 28, mo, 'of moneys'+" "*49+"#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'*93)
        
    # เงื่อนในการเอาเงินออกจากเครื่อง(take)
    elif i == 'take':
        print("I gave you", mo)
        mo = 0

        print('#'*93)
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print("#" + " " * 28, 'The Coffee machine has'+" "*40+"#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print("#" + " " * 28, w, 'of water'+" "*50+"#")
        print("#" + " " * 28, m, 'of milk'+" "*51+"#")
        print("#" + " " * 28, c, 'of coffee beans'+" "*43+"#")
        print("#" + " " * 28, d, 'of disposable cups'+" "*42+"#")
        print("#" + " " * 28, mo, 'of moneys'+" "*51+"#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'+" " * 91 + "#")
        print('#'*93)
    print("1 - exit, 2- back  the menu. ")
    e = input()
    if(e == "1"):
        break