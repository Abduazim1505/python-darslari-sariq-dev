# 12-dars. XATOLAR BILAN ISHLASH
# Sana: 07/01/2022
# Muallif: Abduazim

 
# SyntaxError - SINTEKS XATOLIK

# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?
print "Hello World!"  # qavs yo'q

# SyntaxError: EOL while scanning string literal
print("Hello World! 
# qo'shtirnoq yopilmay qolgan va buni python hato qayerda bo'lganligini ko'rsatib berolmaydi
      
# SyntaxError: unexpected EOF while parsing
print("Hello World!"
# qavs yopilmay qolgan va buni python hato qayerda bo'lganligini ko'rsatib berolmaydi

# IndentationError: unexpected error - JOY TASHLASHDA XATOLIK
 print("Hello World!")
 
# IndentationError: expected an indented block
print("O'ngacha sanaymiz")
for n in range(10):
print(n+1)
# for ishtirok etgan badani joy tashlash kerak


# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK

# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
son = input("Istalgan son kiriting: ")
print(f"{son} ning kvadrati {son**2} ga teng")
# Biz input (str) ni (int) ga o'girib olmadik

# NameError
# NameError: name 'prit' is not defined
prit("Hello World!")
# O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik.

# ValueError
son = int(input("Istalgan son kiriting: ")) # faqat butun son deyilgan (int)
if son>=0:
    print("Musbat son")
else:
    print("Manfiy son")
# inputga o'nlik son (float < 25.2 >) kirg'azilgandagi hatolik

# IndexError
# IndexError: list index out of range
mevalar = ['olma','anor','uzum']
print(mevalar[3]) # bizda 3-index yoq (0/1/2)

# ZeroDivisionError
# ZeroDivisionError: division by zero
x, y = 50, 50
z = 250/(x-y)
# Dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik


# MANTIQIY XATOLAR

# Aylana yuzi formulasidagi xatolik
radius = 5
pi = 4.14 # aslida 3.14
aylana_yuzi = pi*radius**2
print(aylana_yuzi)
# bunda natija chiqaveradi ammo bu hatoni o'zimiz aniqlashimiz kerak

# Yana bir misol ko'raylik:
son = float(input("Istalgan son kiriting: "))
ildiz = son**1/2 # bu yerda son**(1/2) ko'rinishda bo'lishi kerak edi
print(f"{son} ning ildizi {ildiz} ga teng")
# Javob chiqaveradi ammo biz kutgan javob emas buni ham o'zimiz qidirib
   # topishimiz kerak