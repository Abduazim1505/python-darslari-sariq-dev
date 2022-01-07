# 07-dars. List (ro'yxat) Home - work
# Sana: 06/01/2022
# Muallif: Abduazim

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston", "Rossiya", "Qozog'iston", "Amerika", "Afrika", "Mexiko", "Xitoy"]

# Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)

davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200,2))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(sonlar)-min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblang
print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(sonlar[:20])
print(sonlar[-20:])
print(sonlar[260:280])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["osh", "norin", "somsa", "kabob", "lag'mon"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(nonushta)
print(taomlar)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non" # e'tibor bering tuple ga o'zgargandan so'ng unga o'zgartirish kirg'azib bo'lmaydi
# print(nonushta)