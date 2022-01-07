# 15-dars. Dictionary LUG'AT ELEMENTLARI Home Work
# Sana: 07/01/2022
# Muallif: Abduazim

# Python izohli lug'atini yarating
en_uz = {
    "Float" : "O'nlik son",
    "Boolean" : "Mantiqiy qiymat",
    "Integer" : "Butun son",
    "If" : "Shartlarni tekshirish operatori"
    }
# for sikli orqali alifbo ketma-ketligida chiroyli qilib konsolga chiqaring
for key, value in sorted(en_uz.items()):
    print(f"{key} - {value}")
    
# Davlatlar va ularning poytaxtlari lug'atini tuzing
davlatlar = {
    "O'zbekiston" : "Toshkent",
    "Aqsh" : "Washington D.C",
    "Qozog'iston" : "Nursulton",
    "Qirg'iziston" : "Bishkek",
    "Rossiya" : "Moskva",
    "Tojikiston" : "Dushanbe",
    "Italiya" : "Rim"
    }
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida
    # alifbo ketma-ketligida konsolga chiqaring
print("Dunyo davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(f"{davlat.upper()}")
print("Dunyo poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(f"{poytaxt.title()}")
    
# !!!! Foydalanuvchidan istalgan davlatni kiritishni so'rang
# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?: ').title()
# capital = davlatlar.get(country)
# shu davlatning poytaxtini konsolga chiqaring
# if capital==None:
    # print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
# else:
    # print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# !!!! Restoran menusi lug'atini tuzing    
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang
buyurtmalar = []
print("3 ta taom buyurtma bering.")
for n in range(3):
    buyurtmalar.append(input(f"{n+1} - taom: ").lower())
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")