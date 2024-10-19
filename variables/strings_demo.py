website = "http://www.sadikturan.com"
kursAdi = "python dersleri : sıfırdan ileri seviye python programlama"
hello = "Hello world"


print(len(kursAdi))

print(website[7:10])

print(website[-3:])

print(kursAdi[:16] , kursAdi[-15:])

print(kursAdi[::-1])

hello = hello[:6] + "W" + hello[-4:]
print(hello)

print("abc" * 3)


name , surname , age , job = "sadık", "turan", 37 , "öğretmen"

print(f"my name is {name} surname is  {surname}. ı am {age} years old. ı am a {job}")
