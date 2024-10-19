sayilar = [1,5,8,9,3,45]
harfler = ['a','b','e','s','a','z','y']

sonuc = min(sayilar)
sonuc2 = max(sayilar)

sonuc3 = max(harfler)

print(sonuc) # 1
print(sonuc2) #45
print(sonuc3) # z


sayilar.append(39)
print(sayilar) # [1, 5, 8, 9, 3, 45, 39]

sayilar.insert(3,5) # 3 numaralı indexe 5 sayısını ekler.
print(sayilar) # [1, 5, 8, 5, 9, 3, 45, 39]

sayilar.pop()
print(sayilar) # [1, 5, 8, 5, 9, 3, 45]

sayilar.pop(0)
print(sayilar) # [5, 8, 5, 9, 3, 45]

sayilar.remove(45)
print(sayilar) # [5, 8, 5, 9, 3]

harfler.remove("z")
print(harfler) # ['a', 'b', 'e', 's', 'a', 'y']


print(sayilar.count(1)) # 0

print(sayilar.index(8)) # 1 ->  verilen sayının index numarasını alır.






