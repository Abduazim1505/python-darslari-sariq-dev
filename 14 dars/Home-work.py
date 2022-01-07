# 14-dars. Dictionary LUG'AT BILAN TANISHUV Home - work
# Sana: 07/01/2022
# Muallif: Abduazim

# otam (onam, akam, ukam, va hokazo) degan lug'at yarating
otam = {'ismi' : 'Abduhamid',
        't_yili' : 1968,
        'shahri' : 'Toshkent',
        'manzili' : 'Yunusobod',
        }
onam = {'ismi' : 'Dilnoza',
        't_yili' : 1972,
        'shahri' : 'Toshkent',
        'manzili' : 'Yunusobod',
        }
opam = {'ismi' : 'Shahnoza',
        't_yili' : 1994,
        'shahri' : 'Toshkent',
        'manzili' : 'Yunusobod',
        }
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
print(f"Otamning ismi {otam['ismi']}, {otam['t_yili']} - yilda, {otam['shahri']} shahrida tug'ilgan")
print(f"Onamning ismi {onam['ismi']}, {onam['t_yili']} - yilda, {onam['shahri']} shahrida tug'ilgan")
print(f"Opamning ismi {opam['ismi']}, {opam['t_yili']} - yilda, {opam['shahri']} shahrida tug'ilgan")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing
taomlar = {
    'otam' : 'osh',
    'onam' : "sho'rva",
    'sh_opam' : 'norin',
    'z_opam' : 'pitsa',
    'men' : "lag'mon"
    }
# Kamida uch kishining sevimli taomini konsolga chiqaring
print(f"Otamning sevimli taomi {taomlar['otam']}")
print(f"Onamning sevimli taomi {taomlar['onam']}")
print(f"Opamning sevimli taomi {taomlar['sh_opam']}")

# Python izohli lu'gati tuzing
dictionary = {
    'integer' : 'butun son',
    'float' : 'kasr son',
    'string' : 'matn',
    'if' : 'agar',
    'else' : 'aks holda',
    'dictionary' : 'lug\'at'
    }
# Foydalanuvchidan biror so'z kiritishni so'rang
kalit = input("Biron bir kalit so'z kiriting: ").lower() # shunday qilsa bo'ladi
soz = dictionary.get(kalit, "Bunday so'z mavjud emas")
print(soz)

# Yuqoridagi vazifani if-else yordamida qiling
if kalit in dictionary:
    print(f"{kalit.title()} so'zi {dictionary[kalit].title()} deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")