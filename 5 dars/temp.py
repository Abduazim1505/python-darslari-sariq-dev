# 05-dars. String va string metod
# Sana: 02/12/2021
# Muallif: Abduazim

# Unicode-table sayti orqali olingan smilek
matn = "meing kayfitam 😂 shunday"
print(matn)

ism = 'Ahmad'
print("Mening ismim " + ism)

# Print funksiyasida "+" va "," farqlari
ism = "Ahad"
familya = "Qayum"
print(ism + ' ' + familya)
print(ism, familya)

# f-string
ism = "Ahad"
print(f"Mening ismim {ism}")

# \t so'zlar orasida keng joy qoldiradi
print("Hello \tWorld")

# \n yangi qatorga o'tadi
print("Hello \nWorld")

#############################

# String metodlari <matn.metod()>
ism = 'jAmes'
familiya = 'bOnd'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

# upper - barcha harflarni katta qilib beradi
print(ism_sharif.upper())

# lower - barcha harflarni kichik qilib beradi
print(ism_sharif.lower())

# title - barcha bosh harflarni kata qilib beradi
print(ism_sharif.title())

# capitalize - faqat birinchi harf kata qilib beradi
print(ism_sharif.capitalize())

# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham
    # qo'llash mumkin (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning)
        # manzili xolos)
print('james bond'.upper())

#######################################

meva = "   olma   "
print("Men " + meva + " yaxshi ko'raman")

# lstrip - olma so'zining chap bo'sh qismini yo'qotadi
print("Men " + meva.lstrip() + " yaxshi ko'raman")

# rstrip - olma so'zining o'ng bo'sh qismini yo'qotadi
print("Men " + meva.rstrip() + " yaxshi ko'raman")

# strip - olma so'zining chap va o'ng bo'sh qismini yo'qotadi
print("Men " + meva.strip() + " yaxshi ko'raman")

#####################

# INPUT

ism = input("Ismingiz nima?\n>>>")
print("Assalom alaykum, " + ism.title())