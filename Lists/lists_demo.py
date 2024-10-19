
modeller = ["Samsung S5" , "Samsung S6" , "Samsung S7" ,  "Samsung S8"]

print(len(modeller)) # 4

print(modeller[0] , modeller[-1]) # Samsung S5 Samsung S8

modeller[0] = "Samsung S9"
print(modeller) # ['Samsung S9', 'Samsung S6', 'Samsung S7', 'Samsung S8']

if "Samsung S6" in modeller:
    print("Samsung S6 bu listenin bir elemanıdır.") # Samsung S6 bu listenin bir elemanıdır.
else:
    print("Değildir.")

print(modeller[-3]) # Samsung S6

print(modeller[:2]) # ['Samsung S9', 'Samsung S6']

modeller[-2],modeller[-1] = "Samsung S9" , "Samsung S10"
print(modeller) #['Samsung S9', 'Samsung S6', 'Samsung S9', 'Samsung S10']

modeller = ["Iphone X" , "Iphone XR"] + modeller
print(modeller) # ['Iphone X', 'Iphone XR', 'Samsung S9', 'Samsung S6', 'Samsung S9', 'Samsung S10']

del modeller[-1]
print(modeller) # ['Iphone X', 'Iphone XR', 'Samsung S9', 'Samsung S6', 'Samsung S9']

print(modeller[::-1]) #['Samsung S10', 'Samsung S9', 'Samsung S6', 'Samsung S9', 'Iphone XR', 'Iphone X']


for i in modeller:
    print(i)



ogrenciA = ["Yiğit " ,"Bilgi",2010,[70,60,70]]
ogrenciB = ["sena" ,"Turan",1999,[80,80,70]]
ogrenciC = ["ahmet" ,"Turan",1998,[80,70,90]]

ogrenciler = [ogrenciA , ogrenciB , ogrenciC]

for ogrenci in ogrenciler:
    ad = ogrenci[0]
    soyad = ogrenci[1]
    yas = 2024 - ogrenci[2]
    ortalama = (ogrenci[3][0] + ogrenci[3][1] + ogrenci[3][2]) / 3
    print(f"ogrenci ad : {ad} - ogrenci soyad : {soyad} - ogrenci yas : {yas} - ogrenci ortalama : {ortalama}")


"""
ogrenci ad : Yiğit  - ogrenci soyad : Bilgi - ogrenci yas : 14 - ogrenci ortalama : 66.66666666666667
ogrenci ad : sena - ogrenci soyad : Turan - ogrenci yas : 25 - ogrenci ortalama : 76.66666666666667
ogrenci ad : ahmet - ogrenci soyad : Turan - ogrenci yas : 26 - ogrenci ortalama : 80.0
"""