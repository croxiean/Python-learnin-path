# - 3  ürün bilgisini (id,ad,fiyat) kullanıcdıan aldığınız bilgiler ile dictionary de saklayınız
# - ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

"""
urunler = {}


ürünId = input("ürün ID si giriniz : ")
ürünAd = input("ürün Adını giriniz :")
ürünFiyat = input("ürün fiyatını giriniz : ")


urunler[id] = {
    "ad" : ürünAd,
    "fiyat" : ürünFiyat
}

ürünId = input("ürün ID si giriniz : ")
ürünAd = input("ürün Adını giriniz :")
ürünFiyat = input("ürün fiyatını giriniz : ")


urunler[id] = {
    "ad" : ürünAd,
    "fiyat" : ürünFiyat
}


ürünId = input("ürün ID si giriniz : ")
ürünAd = input("ürün Adını giriniz :")
ürünFiyat = input("ürün fiyatını giriniz : ")


urunler[id] = {
    "ad" : ürünAd,
    "fiyat" : ürünFiyat
}

print(urunler)


id =input("aramak istediğiniz ürün ID sii nedir ? ")
urun = urunler[id]

print("girmiş olduğunuz id ye sahip ürün : {}".format(urun))

"""



urunler = {
    '100' : {'ad' : 'ıphone 8' , 'fiyat' : '5000'},
    '200'  :{'ad' : 'iphone x' , 'fiyat' : '5000'},
    '300'  :{'ad' : 'iphone xr' , 'fiyat' : '6000'}
}

id = input("lütfen bir ürün id giriniz :")
urun = urunler[id]

print(f"girmiş olduğunuz urun id : {urun['ad']} - urun ismi : {urun['fiyat']}")
