# 11-dars. Bir nechta shartlarni tekshirish Home - work
# Sana: 06/01/2022
# Muallif: Abduazim

# Foydalanuvchidan juft son kiritishni so'rang
son = float(input("Juft son kiriting: "))
if son%2:
    print('Bu son juft emas.')
else:
    print("Rahmat!")
    
# Foydalanuvchi yoshini so'rang
yosh = int(input("Yoshingizni kiriting: "))
# muzeyga kirish uchun chipta narhini quyidagicha chiqaring
if yosh < 4 or yosh > 60:
    print("Sizga chipta bepul")
elif yosh < 18:
    print("Siga chipta 10000 so'm")
else:
    print("Sizga chipta 20000 so'm")
    
# Foydalanuvchidan ikita son kiritishni so'rang
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
# sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
if a == b:
    print(f"{a}={b}")
elif a > b:
    print(f"{a}>{b}")
else:
    print(f"{a}<{b}")
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting
mahsulotlar = ["sabzi", 'olma', 'kartoshka', 'uzum', 'anjir', 'piyoz', 'bexi', 'karom', "go'sht", 'tuxum']
# Yangi, savat degan bo'sh ro'yxat yarating
savat = []
# foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
for n in range(5):
    savat.append(input(f"{n+1} - mahsulot nomini kiriting: "))
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor")
    else:
        print(f"Do'konimizda {mahsulot} yo'q")
        
# !!!!!!! foydalanuvchidan 5 ta mahsulot kiritishni so'rang
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"{n+1} - mahsulot nomini kiriting: "))
bor_mahsulot = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulot.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q: ")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
# foydalanuvchilar degan ro'yxat tuzing
foydalanuvchilar = ['ali', 'vali', 'hasan', 'husan', 'ahad']
#  Foydalanuvchidan yangi login tanlashni so'rang
login = input("Yangi login kiriting: ")
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")
    
# !!!!!! Foydalanuvchidan biror butun son kiritishni so'rang
son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")