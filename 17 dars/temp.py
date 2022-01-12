# 17-dars. INPUT() VA WHILE
# Sana: 11/01/2022
# Muallif: Abduazim

# input
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# while
son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end = ' ') # son ni konsolga chiqaramiz,
    son = son + 1 # songa 1 qo'shamiz.
print("Dastur tugadi")

# while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
    # qiymat = input(savol)
    # if qiymat != 'exit':
        # print(float(qiymat)**2)
# print('Dars tugadi')

# ishora - flag
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
    # qiymat = input(savol)
    # if qiymat == 'exit':
        # ishora = False
    # else:
        # print(float(qiymat)**2)
# print('Dastur tugadi')

# break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:
    # qiymat = input(savol)
    # if qiymat == 'exit':
        # break
    # else:
        # print(float(qiymat)**2)
# print('Dastur tugadi')

# for break
# sonlar = list(range(1, 11))
# for son in sonlar:
    # if son == 5:
        # break
    # else:
        # print(f"{son} ning kvadrati {son**2} gateng")
        
# for continue
sonlar = list(range(1, 11))
for son in sonlar:
    if son == 5:
        continue
    else:
        print(f"{son} ning kvadrati {son**2} gateng")
        
# Continue while toq yoki juft sonlarni chiqarish
son = 0
while son > 10:
    son += 1
    if son % 2 == 0: # son % 2 != 0:
        continue
    else:
        print(son)
        
