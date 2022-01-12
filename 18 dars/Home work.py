# 18-dars. While ro'yhatlar va lug'atlar Home work
# Sana: 11/01/2022
# Muallif: Abduazim

# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
savat =[]
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo\'shasizmi?(ha/yo\'q)")
    if javob != 'ha':
        break