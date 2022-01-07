# 10-dars. IF - ELSE (Tarmoqlanish)
# Sana: 06/01/2022
# Muallif: Abduazim

# avtomabil royhati tuzing va ularni katta harflarda chiqring
avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw': # avto bmw ga tengmi
        print(avto.upper())
    else:
        print(avto.title())
        
# biz valini kutmoqdamiz
ism = input("Ismingiz nima:\n>>> ")
if ism.lower() != 'vali':
    print(f"Uzur, {ism.title()} biz Valini kutyapmiz.")
else:
    print("Hush kelibsan Vali")
    
# Else yozmasdan tarmoqlash
javob = float(input("12*6 nechiga teng\n>>> ")) # bu yerda float yoki int farqi yo'q
if javob!=72:
    print("Javob xato!")

# Katta yoki teng tarmoqlanish    
yosh = int(input("Yoshingiz nechida?\n>>> "))
if yosh>=18: # yosh 18 dan katta yoki teng
    print('Xush kelibsiz!')
else:
    print("Kirish mumkin emas!")
    
# Login uzunligini tekshirish
login = input("Yangi login kiriting:\n>>> ")
if len(login)<=5:
    print("Login 5 harfdan ko'proq bo'lishi shart!")

# foydalanuvchini yoshini hisoblash    
yil = int(input("Tug'ilgan yilingizni kiriting:\n>>> "))
if 2022-yil<18:
    print(f"Yoshingiz {2022-yil}da ekan")
    print("Sizga kirish mumkin emas")
else:
    print("Xush kelibsiz!")
    
# If qatoridan print funksiyasini yonma yon yozish
yosh = int(input("Yoshingiz nechida?\n>>> "))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# if va else bog'lamasini bir qatorda yozish
x, y = 25, 50 # x=25 y=50
print("x>y") if x>y else print("x<y")