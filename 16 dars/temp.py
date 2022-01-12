# 16-dars. NESTING Lug'at ichida ro'yxat, ro'yxat ichida lug'at?
# Sana: 10/01/2022
# Muallif: Abduazim

# Kelin quyidagi misolni ko'ramiz, bazamizda bir nechta mashinalar bor. Har bir mashina alohida lug'at shaklida. 
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }
car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }
car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
# consolega quyidagicha print qilib chiqishimiz biroz murakkab yo'li
# car = car0
# print(f"{car['model'].title()}, "     # f string boshqacha ko'rinishi
      # f"{car['rang']} rang, "
      # f"{car['yil']}-yil, {car['narh']}$")

# endi buning onson yo'li bunda for tsiklidan foydalanamiz
cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")
    
# listdagi lug'atlardan birining mashina modelini chiqarish (ichma - ich)
print(cars[0]['model'])

# for tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin:
malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz   
# birinchi 3 ta mashinaga qizil rang beramiz:
for malibu in malibus[:3]:
    malibu['rang']='qizil'
# Keyingi 3 tasiga esa qora:
for malibu in malibus[3:6]:
    malibu['rang']='qora'
# Keling endi, mashinalarning korobkasidan chiqqan holda narh belgilaymiz:
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000

# LUG'AT ICHIDA RO'YXAT
# dasturchilar lug'atini tuzamiz va har bir dasturchi haqidagi ma'umotni konsolga chiqaramiz:
dasturchilar = {
    'ali' : ['python', 'c++'],
    'vali' : ['html', 'css', 'js'],
    'hasan' : ['php', 'sql'],
    'husan' : ['python', 'php'],
    'maryam' : ['c++', 'c#']
    }
for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f'{til.upper}', end='') # end vazifasi for sikli tasirida qatorma - 
                  # qator tushgan elementlarni consolega bir chiziqda chiqarish

