# 07-dars. List (ro'yxat) Home - work
# Sana: 15/12/2021
# Muallif: Abduazim

# ismlar ro'yxati yarating
name = ['Ahmad', 'Mahmud', 'Asror']

print(f'Salom {name[0]}, bugun choyxona bormi?')
print(f'{name[1]}, choyxonaga boramizmi?')

# sonlar degan ro'yxat yarating va usti turli mavzuga oid mashqlar bajaring
numbers = [5, 200, -1500, 45.5, 445, -480]
numbers.remove(5)
del numbers[2]
numbers.insert(0, 12345)
numbers.append(9876)

# tarixiy shahslar va zamonamizdagi shahslar ro'yxati
t_shaxslar = ['Imom Buhoriy', 'Alisher Navoiy']
z_shaxslar = ['Bill Gets', 'Ilon Mask']
print(f"Men tarixiy shaxslardan {t_shaxslar[0]} bilan,\nzamonaviy shahxslardan esa {z_shaxslar[0]} bilan \nsuhbat qilishni istar edim")

# friend nomli bo'sh ro'yxat tuzing va appendni qo'llab ko'ring
friend = []
friend.append('Sardor')
friend.append('Bexruz')
friend.append('Farhod')
friend.append('Akmal')
friend.append('Aziz')
friend.append("G'ayrat")

friend.remove('Sardor')
friend.remove('Akmal')

friend.insert(0, 'Sappi')
friend.insert(3, 'Nabi')
friend.append('Vali')
print(friend)

# mehmonlar degan bo'sh ro'yhat yarating
mehmonlar = []
mehmonlar.append(friend.pop(1))
mehmonlar.append(friend.pop(0))
mehmonlar.append(friend.pop(-1))
print(mehmonlar)