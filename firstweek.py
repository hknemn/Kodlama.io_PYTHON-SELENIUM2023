#odev1

#String: metin veri tipleridir. Harf, kelime veya cumle olabilir. Asagidakilerin hepsi string tipindedir.
harf = "a"
kelime = "Hakan"
cumle = "kodlamaio selamlar"

#Integer: tam sayi tutar.
sayi1 = 15

#Float: ondalikli sayi tutar.
sayi2 = 3.14

#Complex: karmasik sayilarda kullanilir.
sayi3 = 1j

#List: icerisinde degerler bulunduran listelerdir. Asagidaki ornekte str(String) tipinde bir liste. mutable*
list1 = ["ankara","istanbul"]

#Tuple: icerisinde degerler bulundururlar. immutable*
tuple1 = ("ankara","istanbul")

#Boolean: true ya da false olan mantiksal degerlerdir.
boolean1 = True

#Dictionary: anahtar ve deger mantigiyla calisan sozluklerdir.
sozluk1 = {"il":"istanbul","plaka":34}

#kodlamaio sitesi veri tipleri ornek
sayi4 = 0 #int
isim = "engin demirog" #str
kurslar = ["pyhton","java"]
bildirimler = False #bildirim gelme istegi acik veya kapali

#kodlamaio sitesi sart bloklari
database1 = "xxx@x.com" #kayitli bilgiler
database2 = "xxxx"

email = "xxx@x.com" #kullanici giris bilgileri
password = "xxxx"

if (email == database1 and password == database2):
        print("sisteme girildi")
else:
        print("sifre veya mail hatali")


button1 = True

if(button1):
        print("bitir ve devam et butonuna basildi. ilerleme islensin")
else:
        print("butona basilmadi. ilerleme yok")