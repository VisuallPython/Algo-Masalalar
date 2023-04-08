# # pip install num2words      
# from num2words import num2words

# number = int(input('Son kiriting: '))
# words = num2words(number)

# print(words)




raqam = int(input("Istalgan sonni kiriting: "))

if raqam < -999999999999 or raqam > 999999999999:
    print("Kiritilgan son juda katta/kichik!")
else:
    son_kichikligi = False
    if raqam < 0:
        son_kichikligi = True
        raqam = abs(raqam)
    elif raqam == 0:
        print("nol")
        if raqam > 999:
            print("Kiritilgan son juda katta!")
        else:
            yuzlik = raqam // 100
            raqam = raqam % 100
            onlik = raqam // 10
            birlik = raqam % 10
        if son_kichikligi:
            print("minus ", end="")
        if yuzlik:
            if yuzlik == 1:
                print("Bir yuz ", end="")
            if yuzlik == 2:
                print("Ikki yuz ", end="")
            if yuzlik == 3:
                print('Uch yuz ', end="")
            if yuzlik == 4:
                print('To\'rt yuz ', end="")
            if yuzlik == 5:
                print('Besh yuz ', end="")
            if yuzlik == 6:
                print('Olti yuz ', end="")  
            if yuzlik == 7:
                print('Yetti yuz ', end="")
            if yuzlik == 8:
                print('Sakkiz yuz ', end="")
            if yuzlik == 9:
                print('To\'qqiz yuz ', end="") 
            else:
                print("son 3 xonali emas!\n")
            
        if onlik:
            if onlik == 1:
                print("o'n ", end="")
            elif onlik == 2:
                print("yigirma ", end="")
            elif onlik == 3:
                print("o'ttiz ", end="")
            elif onlik == 4:
                print("qirq ", end="")
            elif onlik == 5:
                print("ellik ", end="")
            elif onlik == 6:
                print("oltmish ", end="")
            elif onlik == 7:
                print("yetmish ", end="")
            elif onlik == 8:
                print("sakson ", end="")
            elif onlik == 9:
                print("to'qson ", end="")
        if birlik:
            if birlik == 1:
                print("bir", end="")
            elif birlik == 2:
                print("ikki", end="")
            elif birlik == 3:
                print("uch", end="")
            elif birlik == 4:
                print("to'rt", end="")
            elif birlik == 5:
                print("besh", end="")
            elif birlik == 6:
                print("olti", end="")
            elif birlik == 7:
                print("yetti", end="")
            elif birlik == 8:
                print("sakkiz", end="")
            elif birlik == 9:
                print("to'qqiz", end="")
        print()
