msg = "Python Kursumuza Hoş Geldiniz. Ben Sadık Turan"

msg = msg.upper() # PYTHON KURSUMUZA HOŞ GELDINIZ. BEN SADIK TURAN
print(msg)

msg = msg.lower() # python kursumuza hoş geldiniz. ben sadik turan
print(msg)


msg = msg.title() # Python Kursumuza Hoş Geldiniz. Ben Sadik Turan
print(msg)


msg = msg.capitalize() # Python kursumuza hoş geldiniz. ben sadik turan
print(msg)

msg = msg.islower() # False
print(msg)


sonuc = "   abc alfabenin il üç harfleridir."
print(sonuc)

sonuc = sonuc.strip() # başta ve sonraki boşluk karakterlerini alır
print(sonuc)

sonuc = sonuc.split() # her elemanı bir diziye koyar.
print(sonuc)

kelime = "merhaba. ben samet taş"

kelime = kelime.split(".") #noktaya göre ayırır.
print(kelime)

kelime = "-".join(kelime) # her elemanın arasına '-' koyar.
print(kelime)


index = kelime.index("ben") # string içerisinde bir arama işlemi yapmamıza yarar.
print(index)


kelime = kelime.startswith("m")
print(kelime)

sonuc2 = "merhabalar bu dersin hocası sadık turandır."
sonuc2 = sonuc2.replace("sadık","samet") # sadık ismini samet olarak değiştirir. yani verdiğin kelimeyi belirleidğin kelime yerine koyar.
print(sonuc2)

sonuc2 = sonuc2.replace("turan","Taş").replace("merhabalar","Selamlar") # Selamlar bu dersin hocası samet Taşdır.
print(sonuc2)
