# 16-dars. NESTING Lug'at ichida ro'yxat, ro'yxat ichida lug'at? Home - Work
# Sana: 10/01/2022
# Muallif: Abduazim


# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang
shaxs_0 = {
    'ismi' : 'Abu Abdulloh',
    'familiyasi' : 'Muhammad ibn Ismoil',
    't_yili' : 810,
    't_shaxri' : 'Buxoro',
    'yashagan_yili' : 60,
    'asarlari' : ["Al-jome' as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]
    }
shaxs_1 = {
    'ismi' : 'Abdulla',
    'familiyasi' : 'Qodiriy',
    't_yili' : 1984,
    't_shaxri' : 'Toshkent',
    'yashagan_yili' : 44,
    'asarlari' : ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"]
    }
shaxs_2 = {
    'ismi' : 'Erkin',
    'familiyasi' : 'Vohidov',
    't_yili' : 1936,
    't_shaxri' : 'Farg\'ona',
    'yashagan_yili' : 80,
    'asarlari' : ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"]
    }
shaxs_3 = {
    'ismi' : 'Alisher',
    'familiyasi' : 'Navoiy',
    't_yili' : 1441,
    't_shaxri' : 'Xirotda',
    'yashagan_yili' : 60,
    'asarlari' : ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"]
    }
t_shaxslar = [shaxs_0, shaxs_1, shaxs_2, shaxs_3]
for shaxs in t_shaxslar:
    print(f"{shaxs['ismi']} {shaxs['familiyasi']} {shaxs['t_yili']}-yilda",
          f"{shaxs['t_shaxri']}da tavallud topgan. {shaxs['yashagan_yili']}",
          f"yil umr ko'rgan")
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
for shaxs in t_shaxslar:
    print(f"\n{shaxs['ismi']}ning mashxur asarlari:")
    for asar in shaxs['asarlari']:
        print(f"{asar}")

# yuqoridagi for siklni qisqartirilgan versiyasi
for shaxs in t_shaxslar:
    ism = shaxs['ismi']
    asarlar = shaxs['asarlari']
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)
        
#  3 ta sevimli kino-seriali haqida so'rang
kinolar = {
    'Ali' : ['Terminator', 'Rambo', 'Titanic'],
    'Vali' : ['Tenet', 'Inception', 'Intersteller'],
    'Hasan' : ['Abdullajon', 'Bomba', 'Shaytanat'],
    'Husan' : ['Mahallada duv-duv gap', 'John Wick']
    }
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang
for ism, filmlar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for film in filmlar:
        print(film)
        
# Davlatlar degan lug'at yarating
davlatlar = {
    "o'zbekiston" : { 'poytaxti' : 'toshkent',
                       'Hududi' : 448978,
                       'aholi' : 33_000_000,
                       'pul birligi' : "so'm"
                      },
    'rossiya' : { 'poytaxti' : 'moskva',
                  'Hududi' : 17098246,
                  'aholi' : 144_000_000,
                  'pul birligi' : "rubl"
                 },
    'aqsh' : { 'poytaxti' : 'vashington',
               'Hududi' : 9_631_418,
               'aholi' : 327_000_000,
               'pul birligi' : "dollar"
              },
    'malayziya' : { 'poytaxti' : 'kuala-lumpur',
                    'Hududi' : 329750,
                    'aholi' : 25_000_000,
                    'pul birligi' : "rinngit"
                   }
    }
for davlat, info in davlatlar.items():
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxti'].capitalize()}:"
          f"\nHududi: {info['Hududi']}"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
    
search = input("Davlat nomi kiriting: ").lower()
if search in davlatlar:   
    info = davlatlar[search]
    print(f"\n{search.capitalize()}ning poytaxti {info['poytaxti'].capitalize()}:"
          f"\nHududi: {info['Hududi']}"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")