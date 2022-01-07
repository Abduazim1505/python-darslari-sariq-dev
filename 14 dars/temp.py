# 14-dars. Dictionary LUG'AT BILAN TANISHUV
# Sana: 07/01/2022
# Muallif: Abduazim

# Oddiy bir lug'at yaratamiz
car_0 = {'model':'ferrari','rang':'qizil'}
print(car_0['model'])
print(car_0['rang'])

# Murakkabroq bir misol
talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
print(f"{talaba_0['ism'].title()},\
 {talaba_0['t_yil']}-yilda tu'gilgan,\
 {talaba_0['yosh']} yoshda")
 
# Dictionaryga yangi kalit so'z va qiymat qo'shish
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatka'

# Lug'atga o'zgartirish kiritamiz
talaba_0['ism'] = 'Abdulloh'
print(talaba_0)

# Bo'sh lug'at yaratamiz
talaba_1 = {}
# Biz bu yerga malumo tqo'shamiz
talaba_1['kursi'] = 4
print(talaba_1)

# del operatori yordamida istalgan elemntni kalit so'zi orqali o'chirish
del talaba_0['yosh']
print(talaba_0)

# Agar lug'at uzun bo'lsa quyidagicha yozsaham bo'ladi
telefonlar = {
    'ali' : 'iphone x',
    'vali' : 'galaxy s9',
    'olim' : 'mi 10pro'
    }
print(telefonlar)

# get() METODI KeyError oldini oladi
phone = telefonlar.get('hasan','Bunday ism mavjud emas') # get metodiga kalit
                                       # so'z va qaytuvchi habar kitib o'tdik
                                    
# agar qaytuvchi malumot kiritmasak bizda NONE degan habar chiqadi
phone = telefonlar.get('hasan')
print(phone)