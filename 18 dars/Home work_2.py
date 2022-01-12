# 18-dars. While ro'yhatlar va lug'atlar Home work - 2
# Sana: 11/01/2022
# Muallif: Abduazim

#!!!! e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing
mahsulotlar = {}
while True:
    mahsulot = input("Mahsulot nomini kiriting: ")
    narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
    mahsulotlar[mahsulot] = narh
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != 'ha':
        break