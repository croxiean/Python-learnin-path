opelObj = {
    "marka" : "opel",
    "model" : "corsa",
    "yıl" : 2020
}


sonuc = opelObj["marka"]
sonuc = opelObj.get("marka") # marka adlı objenin değerini verir.

for x in opelObj:
    print(x) # marka model yıl çıktısını verir.

for x in opelObj:
    print(opelObj[x]) # opel corsa 2020 çıktısnı verir
    pass


for x in opelObj.values():
    print(x) # opel corsa 2020 çıktısnı verir


for x in opelObj.keys():
    print(x) # marka model yıl çıktısını verir.

for x,y in opelObj.items():
    print(x,y) #key value bilgisi verir.


sonuc = "marka" in opelObj # herhangi bir key bilgisini sorgular.
print(sonuc) # varsa doğru bilgisini girer

sonuc = len(opelObj) #eleman sayısını gösterir.
print((sonuc)) # 3 çıktısını verir

opelObj["renk"] = "kırmızı" # verilen key ile value yi sözlüğe ekler.
print(opelObj)

opelObj.pop("renk") # renk adlı key ve ona ait value yi siler.
print(opelObj)

# opelObj.popitem() # en son olan key value değerini siler
# print(opelObj)


del opelObj["marka"] # marka adlı key ve value değerini siler
print(opelObj)

# del opelObj # opelobj adlı sözlüğü siler
# print(opelObj)

obj = opelObj # kopyalama işlemi yaptık referans oluyr yapacağın değişiklik ikisini etkiler
obj = opelObj.copy() # buda kopayalama işlemi yapar ancak bellekte bu sefer iki farklı obje olarak tutulur.


obj["marka"] = "mazda"


opelObj.update({ # marka adlı key in valuesını günceller.
    "marka":"BMW",
    "renk" : "kırmızı" # renk adında value yaratır ve değerini de sözlüğe ekler.
})

print(obj) 
print(opelObj)


#print(sonuc)
#print(opelObj)