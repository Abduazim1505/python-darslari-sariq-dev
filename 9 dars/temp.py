# 09-dars. For tsikli
# Sana: 06/01/2022
# Muallif: Abduazim

# For tsikli
mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print("Salom", mehmon)
    
# For tsikli orqali range ni qo'llash
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
# For tsikli ustida amallar
raqamlar = list(range(11))
raqamlar_kvadrati = []
for raqam in raqamlar:
    raqamlar_kvadrati.append(raqam**2)

print(raqamlar)
print(raqamlar_kvadrati)

# For tsikli foydalanuvchi tomonidan malumoto'ldirish orqali shakllantirish
dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # range funksiyasi 0 dan boshlab 5 gacha son shakllantiradi
    # dostlar.append(input(f"{n+1} - do'stingiz ismini kiriting: "))

print(dostlar)