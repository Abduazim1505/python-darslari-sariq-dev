# 11-dars. Bir nechta shartlarni tekshirish
# Sana: 06/01/2022
# Muallif: Abduazim

# 2 tadan ortiq shartlar ustida amallar
yosh = int(input('Yoshingiz nechida?\n>>> '))
if yosh<=4:
    print('Sizga kirish bepul.')
elif yosh<=12:
    print('Sizga kirish 5000 so\'m')
elif yosh<=18:
    print('Sizga kirish 8000 so\'m')
else:
    print('Sizga kirish 10000 so\'m')
    
# print funksiyasini faqat bir marta ishlatish
yosh = int(input('Yoshingiz nechida?\n>>> '))
if yosh<=4:
    narh = 0
elif yosh<=12:
    narh = 5000
elif yosh<=18:
    narh = 8000
else:
    narh = 10000
print(f"Sizga kirish {narh} so'm")

# or(yoki) operatoridan foydalanish
kun =  input("Bugun nima kun?\n>>> ")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print(f"Bugun {kun} dam olish kuni")
else:
    print(f"Bugun {kun} ish kuni")
    
# and(va) operatoridan foydalanish
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<30:
    print("Uyda dam olamiz!")
    
# and / or operatorlarini aralashtirib ham yozish mumkin.
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
    print("Cho'milgani ketdik!")
elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
    print("Uyda dam olamiz!")
    
# BOOLEAN - malumot turi
narh = 15000 # mijoz 15000 so'mga taom oldi
choy = True # mijoz choy ham oldi
salat = False # mijoz salat olmadi

if choy and salat: # mijoz ham choy ham salat olgan bo'lsa
    narh = narh + 10000
elif choy or salat: # mijoz choy yoki salat olgan bo'lsa
    narh = narh + 5000

print(f"Jami {narh} so'm")

# SHARTLARNI KETMA-KET faqat IF orqali TEKSHIRISH
narh = 15000 # mijoz 15 so'mga ovqat oldi
choy = True
salat = False
non = True
kompot = True
assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
if choy:   # agar choy olsa
    print("Mijoz choy oldi.")
    narh = narh + 3000
if salat:  # agar salat olsa
    print("Mijoz salat oldi.")
    narh = narh + 5000
if non:    # agar non olsa
    print("Mijoz non oldi.")
    narh = narh + 2000
if kompot: # agar kompot olsa
    print("Mijoz kompot oldi.")
    narh = narh + 5000
if assorti: # agar assorti olsa
    print("Mijoz assorti oldi.")
    narh = narh + 15000
    
print(f"Jami {narh} so'm")

# ro'yhat ichida biz istagan element bor yoki yo'qligini bilich uchun in operatoridan foydlanamiz
menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?\n>>> ')
if ovqat.lower() in menu:
    print('Buyurtma qabul qilindi')
else:
    print("Afsuski bizda bunday ovqat yo'q")
    
# not in operatori
# 'sho'rva' not in menu < consoleda ....>

# IKKI RO'YXATNI SOLISHTIRISH
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar: # buyurtmalar ichidagi har bir taom uchun
    if taom in menu: # agar taom menuda bo'lsa
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")
        
# ro'yxat bo'sh bo'lganda birinchi uni tekshirib ko'ramiz
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = []

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")