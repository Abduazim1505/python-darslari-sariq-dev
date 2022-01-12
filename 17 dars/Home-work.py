# 17-dars. INPUT() VA WHILE Home work
# Sana: 11/01/2022
# Muallif: Abduazim

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang
# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "
# while True:
    # kitob = input(savol)
    # if kitob == 'exit':
        # break
# print('Rahmat!')

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
# savol = "Yoshingizni kiriting: "
# while True:
    # qiymat = input(savol)
    # if qiymat == 'exit' or qiymat == 'quit':
        # break
    # yosh = int(qiymat)
    # if yosh<7:
        # narh = 2000
    # elif 7<=yosh<18:
        # narh = 3000
    # elif 18<=yosh<65:
        # narh = 10000
    # else: narh = 0
    # if narh==0:
        # print("Sizga chipta bepul")
    # else:
        # print(f"Chipta {narh} so'm")
        
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")