# 19-dars. Funksiya - 2
# Sana: 11/01/2022
# Muallif: Abduazim 

def salom_ber(ism): # ism parametr
    """Fodyalanuvchi ismini qabul qilib, 
        unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}!")

salom_ber('hasan') # 'hasan' argument
salom_ber('olim') # 'olim' argument

# TO'G'RI TARTIBDA UZATISH
def yosh_hisobla(ism, tugilgan_yil):
    """Foydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

yosh_hisobla('olim', 1997)
# yosh_hisobla(1997, 'olim') # bu yerdagi ketma - ketlik hato

# ketma - ketlik hatosini oldini olish uchun
yosh_hisobla(tugilgan_yil = 1997, ism = 'olim') # parametr va argument juftligi

# standart qiymat berib ketish
def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
yosh_hisobla(1993)