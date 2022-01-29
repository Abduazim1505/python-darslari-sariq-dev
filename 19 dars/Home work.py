# 19-dars. Funksiya Home work
# Sana: 11/01/2022
# Muallif: Abduazim

def yilini_hisobla(ism, yosh = 2022):
    """ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2022-yosh} - yilda tug'ilgan")

yilini_hisobla('azim', 21)

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing
def kvadrat_kubini_hisobla(number):
    """kvadrati va kubini konsolga chiqaruvchi funksiya"""
    print(f"{number} ning kvadrati {number**2} ga teng")
    print(f"{number} ning kubi {number**3} ga teng")
    
kvadrat_kubini_hisobla(5)

# Son juft yoki toqligini konsolga chiqaruvchi funksiya yozing
def toqmi_juftmi_hisobla(number):
    """son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if number % 2 == 0:
        print('Juft son')
    else:
        print('Toq son')
        
toqmi_juftmi_hisobla(12)

# kkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing
def kattasi_chiqsin(son_1, son_2):
    """2 ta sondan kattasini konsolga chiqaruvchi funksiya"""
    if son_1>son_2:
        print(son_1)
    elif son_1<son_2:
        print(son_2)
    else:
        print("Sonlar teng")
        
kattasi_chiqsin(8, 5)

# x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing
def daraja(x, y=2): # y uchun 2 standart qiymatini bering.
    """x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing"""
    print(f"{x} ning {y} - darajasi {x**y}")
daraja(8)

# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing
def qoldiqsiz_bol(x):
    y = 2
    while y <= 10:
        if x % y == 0:
            print(f"{x} ga {y} qoldiqsiz bo'linadi")
        y += 1
qoldiqsiz_bol(59)

# sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing
def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)