#Fonksiyonlar
def ogrenci_ekle():
    ekleme_sayisi = int(input("\nKac Ogrenci Ekleyeceksiniz? : "))
    sayac = 0
        
    ogrenci_liste_coklu_ekleme = []
    while sayac < ekleme_sayisi:
        ad_soyad = str(input("Eklenecek {deger}.ogrencinin adinini ve soyadinini giriniz :".format(deger = sayac+1))) 
        ogrenci_liste_coklu_ekleme.append(ad_soyad)
        sayac += 1
    ogrenci_liste.extend(ogrenci_liste_coklu_ekleme)
    print("{eklenen_sayisi} yeni ogrenci listeye basariyla eklenmistir.".format(eklenen_sayisi = ekleme_sayisi))
    print("\nGuncel liste\n",ogrenci_liste)

#-----------------------------------------------------------------------------------------------------------------------------

def ogrenci_sil():
    silme_sayisi = int(input("Kac adet ogrenci sileceksiniz? "))
    sayac = 0 

    while sayac < silme_sayisi:
        ad_soyad = str(input("Silinecek {deger} .Ogrencinin adini ve soyadini giriniz :".format(deger = sayac+1)))
        ogrenci_liste.remove(ad_soyad)
        sayac += 1
    print("{silinen_sayisi} ogrenci basariyle silinmiştir.".format(silinen_sayisi = silme_sayisi))
    print("Guncel liste\n",ogrenci_liste)
#-----------------------------------------------------------------------------------------------------------------------------

def ogrenci_goruntule():
    print("Ogrenciler :\n")
    for i in ogrenci_liste:
        print(i)
#-----------------------------------------------------------------------------------------------------------------------------

def ogrenci_numara_goruntuleme():
    j = 0
    for i in ogrenci_liste:
        j+= 1
        print(j," Numarali Ogrenci ",i)

#Ana program

dongu_durum = True
ogrenci_liste = ["Umut Yalcin","Murat Yucel","Zeynep Gundogdu"]
print("\nOgrenci Kayit Sistemine Hosgeldiniz.")
print("\nListe -->",ogrenci_liste)

while dongu_durum:
    
    print("\n1- Ogrenci Ekle\n2- Ogrenci Sil\n3- Ogrencileri Goruntule\n4- Ogrenci Numaralari Goruntule\n5- Programdan Cikma\n\n")
    secim = int(input("Seciminiz : "))

    if secim == 1:
        ogrenci_ekle()
    
    elif secim == 2:
        ogrenci_sil()
    
    elif secim == 3:
        ogrenci_goruntule()

    elif secim == 4:
        ogrenci_numara_goruntuleme()

    elif secim == 5:
        print("Programdan Cikiliyor...")
        dongu_durum = False
    else:
        print("Hatali Tuslama Yaptiniz.")            





