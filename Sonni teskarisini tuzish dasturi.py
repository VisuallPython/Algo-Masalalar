# Sonning teskarisini tuzish
son = int(input("Sonni kiriting: "))
teskari_son = 0
while son > 0:
    son1 = son % 10
    teskari_son = (teskari_son * 10) + son1
    son = son // 10
print("Kiritilgan sonning teskarisi:", teskari_son)
