# 15-dars. Dictionary LUG'AT ELEMENTLARI BILAN ISHLASH
# Sana: 07/01/2022
# Muallif: Abduazim

# .items() METODI
# Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin. 
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }
print(talaba_0.items()) # bunda natijamiz biroz chunarsiz chiqadi
# for tsikli yordamida chaqirish uchun quydagicha yoziladi
for key, value in talaba_0.items():
    print(f"Kalit: {key}")
    print(f"Qiymat: {value} \n")
    
# yana bir misol
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    
# .keys() metodi - Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa
mahsulotlar = {     # Do'kondagi mahsulotlar
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
print(mahsulotlar.keys())
# for orqali ifodalash maqsadga muvofiq
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys(): # bu yerda keys yozmasaham bo'ladi
    print(mahsulot.title())
    
# sorted() metodi LUG'AT ELEMENTLARINI TARTIB BILAN CHIQADI
print("Do'konimizdagi mahsulotlar:")    
for mahsulot in sorted(mahsulotlar): # sorted qo'lanishi
    print(mahsulot.title())

# .values() METODI3
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in telefonlar.values(): # valueni qo'llash
    print(tel)
    
# SET bir hil qiymatlardan o'chirib tawlawda set() funktsiyasidan foydalanishimiz mumkin.
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
# quyidagi bir xil telefonlarni faqat bitadan korsatamiz
print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
for tel in set(telefonlar.values()):
    print(tel)
    
# Set ma'lumot turi bo'lib ham keladi
toys = {"ball", "car", "lamp", "ball"} # SET 
print(toys)