# 09-dars. For tsikli Home - work
# Sana: 06/01/2022
# Muallif: Abduazim

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing
ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Ahad']

# ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
for ism in ismlar:
    print(f"Salom {ism}")
    
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring
print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing
sonlar = list(range(11,100,2))

# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
for n in sonlar:
    print(f"{n**3}")
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang
kinolar = []
print("5 ta eng sevimli kinolaringiz qaysilar?")

# Kinolar degan ro'yxatga saqlab oling
for k in range(5):
    kinolar.append(input(f"{k+1}-kino: "))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang
n_people = int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
ismlar = []

# Har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)