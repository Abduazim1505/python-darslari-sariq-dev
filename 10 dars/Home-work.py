# 10-dars. IF - ELSE (Tarmoqlanish) Home - work
# Sana: 06/01/2022
# Muallif: Abduazim

# Yangi cars degan ro'yxat tuzing
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring
# GM uchun ikkala harfni katta qiling
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())
        
# Foydalanuvchi login ismini so'rang
login = input("Login ismingizni kiriting: ")
if login.lower() == "admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {login.title()}")

# Foydalanuvchidan 2 ta son kiritishni so'rang.
# sonlar bir-biriga teng yoki yo'qligini tekshirish    
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y: print(f"Sonlar teng: {x}={y}")

# sonni manfiy yoki musbatligini aniqlang
son = float(input("Istalgan son kiriting: "))
if son >= 0:
    print(f"{son} musbat son")
else:
    print(f"{son} manfiy son")

# ildizini hisoblab konsolga chiqaring
son = float(input("Istalgan son kiriting: "))
if son >= 0:
    print(f"{son} - ning ildizi {son**(1/2)} ga teng")
else:
    print("Musbat son kiriting")