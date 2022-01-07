# 07-dars. List (ro'yxat)
# Sana: 15/12/2021
# Muallif: Abduazim

# mevalar ro'yxati
mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']

# narxlar ro'yxati
narhlar = [12000, 18000, 20000, 25000, 36000, -25, 63.2]

# son va so'zlar ro'yxati
sonlar = ['bir', 'ikki', 3, 4, 5]

# bo'sh ro'yxat
ismlar = []

# konsolda yoki shu yerda index yoziladi
print(mevalar[3])

# konsolda yoki shu yerda teskari index yoziladi
print(mevalar[-2])

# o'zgaruvchi indexlari orqali qo'shish
print(narhlar[0] + narhlar[1] + 12000)

# o'zgaruvchi qiymatini index berish orqali o'zgartirish
mevalar[0] = 'anor'
mevalar[-1] = 'uzum'

# append metodi orqali element qo'shish (bunda doim ro'yxat oxoriga qo'shilin qoladi)
mevalar.append('tarvuz')

# insert metodi orqali element qo'shish (bunda ro'yxat istalgan yeriga qo'sha olamiz)
mevalar.insert(0, 'banan')

# del metodi orqali ro'yxat ichidagi elementni o'chiramiz
del mevalar[0]

# agrda elementni nome bilan o'chirish kerak bo'lsa (index soni aniq bo'lmasa)
mevalar.remove('anjir')

# pop metodi orqali 1 ro'yxatdan 2 - ro'yxatga elementni oib o'tadi
sanjardagi_meva = mevalar.pop(1)