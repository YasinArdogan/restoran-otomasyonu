#Yasin Sunullah Ardoğan
def ekle():
    with open("restoran_kayıt.txt", "a") as kayitDefteri:
        masaKac = int(input("Musteriler kacıncı masaya geldi\n"))
        kacKisi = int(input("Kac kisi geldi\n"))
        kayitDefteri.write("{}. masa\n".format(masaKac))
        for i in range(1, kacKisi+1):
            kacSiparis = int(input("Musteri {} kac siparis verecek\n>>>".format(i)))
            kayitDefteri.write("\t\t{})Musteri  {}\n".format(masaKac, i))
            for j in range(kacSiparis):
                gidaAdi = input("Musteri {}'in almak istedigi gida\n>>>".format(i))
                gidaPorsiyon = input("Musteri {}'in almak istedigi gidanin porsiyonu\n>>>".format(i))
                porsiyonFiyat = input("Musteri {}'in almak istedigi gidanin porsiyon fiyati\n>>>".format(i))
                total = int(gidaPorsiyon)*int(porsiyonFiyat)
                siparis = { "yiyecek": gidaAdi, "porsiyon": gidaPorsiyon, "birim porsiyonunun fiyati": porsiyonFiyat, "tutar":total}
                for key, value in siparis.items():
                    kayitDefteri.write("\t\t\t{}){} > {}\n".format(masaKac, key, value))
                siparis.clear()

def guncelle():
    with open("21100011037.txt", "r+") as kayitDefteri:
        masalar = kayitDefteri.readlines()
        guncellenecekMasa = str(input("hangi masayı guncellemek istiyorsunuz"))
        kayitDefteri.seek(0)
        for masa in masalar:
            if guncellenecekMasa != masa[0]:
                if guncellenecekMasa != masa[2]:
                    if guncellenecekMasa != masa[3]:
                        kayitDefteri.write(masa)
        kayitDefteri.truncate()
        kacKisi = int(input("Kac kisi geldi\n"))
        kayitDefteri.write("{}. masa\n".format(guncellenecekMasa))
        for i in range(1, kacKisi + 1):
            kacSiparis = int(input("Musteri {} kac siparis verecek\n>>>".format(i)))
            kayitDefteri.write("\t\t{})Musteri  {}\n".format(guncellenecekMasa, i))
            for j in range(kacSiparis):
                gidaAdi = input("Musteri {}'in almak istedigi gida\n>>>".format(i))
                gidaPorsiyon = input("Musteri {}'in almak istedigi gidanin porsiyonu\n>>>".format(i))
                porsiyonFiyat = input("Musteri {}'in almak istedigi gidanin porsiyon fiyati\n>>>".format(i))
                total = int(gidaPorsiyon) * int(porsiyonFiyat)
                siparis = {"yiyecek": gidaAdi, "porsiyon": gidaPorsiyon, "birim porsiyonunun fiyati": porsiyonFiyat,
                           "tutar": total}
                for key, value in siparis.items():
                    kayitDefteri.write("\t\t\t{}){} > {}\n".format(guncellenecekMasa, key, value))
                siparis.clear()

def sil():
    with open("21100011037.txt", "r+") as kayitDefteri:
        masalar = kayitDefteri.readlines()
        silinecekMasa = str(input("hangi masayı silmek istiyorsunuz"))
        kayitDefteri.seek(0)
        for masa in masalar:
            if silinecekMasa != masa[0]:
                if silinecekMasa != masa[2]:
                    if silinecekMasa != masa[3]:
                        kayitDefteri.write(masa)
        kayitDefteri.truncate()
        kayitDefteri.close()

def goruntule():
    with open("21100011037.txt", "r") as defter:
        masalar = defter.readlines()
        masaKac = (input("Hangi masayi goruntulemek istiyorsunuz?\n >>> "))
        for masa in masalar:
            if masaKac == masa[0] or masaKac == masa[2] or masaKac == masa[3]:
                print(masa)

def faturaKes():
    with open("21100011037.txt", "r") as defter:
        masalar = defter.readlines()
        masaKac = (input("Hangi masanin fatursini goruntulemek istiyorsunuz?\n >>> "))
        toplam = 0
        for masa in masalar:
            if masaKac == masa[0] or masaKac == masa[2] or masaKac == masa[3]:
                if masa[5] == "t":
                    fatura = (masa.strip().split("tutar > ")[-1])
                    toplam = int(fatura) + toplam
        print(str(toplam) + " TL")

def doluverisk():

    with open("21100011037.txt", "r") as defter:
        masalar = defter.readlines()
        toplamMasa = int(input("Toplam kac masa var?\n >>>"))
        alan = int(input("Restoraniniz kac metrekare ? \n >>>"))
        def doluluk(masalar, toplamMasa):
            toplamMusteri = 0
            for masa in masalar:
                if masa[4] == "M":
                    toplamMusteri += 1
            print(str(toplamMusteri) + " kisi bulunmaktadır")
            # her masa 4 kisilik
            oran = float((toplamMusteri / (toplamMasa*4))*100)
            print("Doluluk orani %" + str(oran))
            return toplamMusteri
        musteriSayisi = doluluk(masalar, toplamMasa)
        def risk(musteriSayisi, alan):
            mesafeUygunluk= alan / musteriSayisi
            if mesafeUygunluk > 2:
                print("Sosyal mesafeye uygun orandasiniz. ")
            else:
                print("Sosyal mesafeye uygun oranda degilsiniz, dikkat ediniz.")
        risk(musteriSayisi, alan)

def hepsiniGoruntule():
    with open("21100011037.txt", "r") as defter:
        masalar = defter.readlines()
        for masa in masalar:
            print(masa)

donAnamenu = "1"
while donAnamenu == "1":
    anaMenu = int(input("\nYapmak istediginiz islem icin bir sayi degeri giriniz ||\n" +
                        "                                                     VVVV\n"+
                        "                                                      VV\n"+
                        "Masa siparişi oluşturmak için >>>>>>>>>>>>>>>>>>>>>>> 1\n" +
                        "Masa guncellemek icin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 2\n\n" +
                        "Masa silmek icin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 3\n\n" +
                        "Masa siparisini goruntulemek icin >>>>>>>>>>>>>>>>>>> 4\n\n" +
                        "Tum masalari goruntulemek icin >>>>>>>>>>>>>>>>>>>>>> 5\n\n" +
                        "Masa faturasi hesaplamak icin >>>>>>>>>>>>>>>>>>>>>>> 6\n\n" +
                        "Masaların doluluk oranını ve korana riski icin >>>>>> 7\n\n" +
                        "Cikmak icin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 8\n" +
                        "  >>>>>>>>>> "))

    if anaMenu == 1:
        ekle()
    elif anaMenu == 2:
        guncelle()
    elif anaMenu == 3:
        sil()
    elif anaMenu == 4:
        goruntule()
    elif anaMenu == 5:
        hepsiniGoruntule()
    elif anaMenu == 6:
        faturaKes()
    elif anaMenu == 7:
        doluverisk()
    elif anaMenu == 8:
        break
    else:
        print("\n**** Gecerli bir deger giriniz ****")
        anaMenu = ""
    donAnamenu = (input("---Anamenuye donmek icin 1, cıkmak icin herhangi bir deger giriniz"))
