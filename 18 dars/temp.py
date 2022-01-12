# 18-dars. While ro'yhatlar va lug'atlar - 1
# Sana: 11/01/2022
# Muallif: Abduazim

# while ro'yhat tuzish
print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
ismlar = []
n=1
while True:
    savol = f"{n} - do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input(f"Yana ism qo'shasizmi (ha / yo'q): ")
    n += 1
    if takrorlash == 'yo\'q':
        break
print("Do'stlaringiz ro'yhati")
for ism in ismlar:
    print(ism.title())