student = {
    "name" : "samet",
    "surname" : "TAŞ",
    "age" : 22,
}

print(student["name"]) # samet
print(student["surname"]) # TAŞ
print(student["age"]) #22




plakalar = {
    'kocaeli' : 41 , 
    'İstanbul' : 34
}


print(plakalar['kocaeli']) #41
print(plakalar['İstanbul']) #34

plakalar['rize'] = 53

print(plakalar) # {'kocaeli': 41, 'İstanbul': 34, 'rize': 53}

plakalar['izmir'] = 35
print(plakalar) # {'kocaeli': 41, 'İstanbul': 34, 'rize': 53, 'izmir': 35}

ogrenciler = {100:"samet" , 101 : "Ada"}
print(ogrenciler[100]) # samet



ogrenciler2 = {

    100: {
        "ad" : "çınar",
        "aoyad" : "taş",
        "yas" : 4,
        "not": 56
    },


    102 : {
        "ad" : "ada",
        "soyad" : "bilgi",
        "yas" : 10,
        "not": 80

    },

    103 : {
        "ad" : "furkan",
        "soyad" : "erdenci",
        "age" :  25,
        "not": 32
    }

}

sonuc = ogrenciler2[100]["ad"]
sonuc2 = ogrenciler2[102]

print(sonuc) # samet
print(sonuc2["soyad"]) # bilgi
print(ogrenciler2[103]["age"]) #25



ortalama = ( ogrenciler2[100]["not"] +  ogrenciler2[102]["not"] + ogrenciler2[103]["not"] ) / 3
print(f"sınfın not ortalaması : {ortalama}") # sınfın not ortalaması : 56.0



