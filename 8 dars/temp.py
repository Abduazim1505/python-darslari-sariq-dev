# 08-dars. List (ro'yxatlar bilan ishlash)
# Sana: 06/01/2022
# Muallif: Abduazim

# Sort metodi orqali elamtlarni tartiblash (butunlayga)
cars = ["Bmw", "mercedes benz", "volvo", "audi", "toyota"]
print(cars.sort())

# Sorted metodi elementlarni faqat shu yerdagisi print o'zgartiradi (butunlayga emas)
print(sorted(cars))

# Reverse metodidan foydalanish
print(cars.reverse())

# Reverse argument sort metodi bilan
print(cars.sort(reverse=True))

# Reverse argument sorted metodi bilan
print(sorted(cars, reverse=True))

# Len metodi ro'yxat ichidagi elementlari sonini ko'rsatib beradi
print(len(cars))

# Range funksiyasi 2 chegara sonlar orasidagi barcha sonlar ro'yxati
sonlar = list(range(1,10))
print(sonlar)

# Range funksiyasi orqali faqat toq yoki juft sonlar ro'yxati tuzish
toq_sonlar = list(range(1,20,2))
print(toq_sonlar)

juft_sonlar = list(range(0,20,2))
print(juft_sonlar)

# MAX(), MIN(), SUM(),
# Max funksiysi eng katta sonni chiqazib beradi
print(max(toq_sonlar))

# Min funksiysi eng kichik sonni chiqazib beradi
print(min(toq_sonlar))

# Sum funksiysi barcha ro'yxat elementi sonlarini yig'indisini chiqarib beradi
print(sum(toq_sonlar))

# Ro'yxatdagi istalgan elementni index berish orqali consolega chiqarish
print(cars[0])

# Ro'yxat ichidagi istalgan bir necha elementlarni consolega chiqarish
print(cars[2:5])

# Ro'yxat boshidage index bermasak 0 dan boshlab ko'rsatadi
print(cars[:5])

# Ro'yxat oxirgi index bermasak ohirgacha ko'rsatadi
print(cars[2:])

# Biron bir ro'yxatdan nusxa olish
my_cars = cars[:]

print(my_cars)

del my_cars[0]
print(my_cars)

# TUPLE - ro'yxatning elementlarini o'zgartirib bo'lmas bir turi
toys = ('bus', 'car', 'bear', 'snake')
print(toys)

# Tuple ni Listga o'girish orqali uni tahrirlash
toys = list(toys)
toys.append('lizard')
print(toys)

# List ko'rinishidagi ro'yxatni Tuple ga qaytarib qo'yamiz
toys = tuple(toys)
print(toys)