# Pytnon Data Types (Python Veri Tipleri)

•	String : Metinsel ifadeler için kullanılan veri türüdür. Örnek olarak Ad, Soyad, Şehir, Ülke, Şirket isimleri vb. gibi metinsel ifadeleri tanımlamak üzerinde çalışmak için kullanılan veri türüdür.

•	Int : Sayısal ifadeleri tanımlamak için kullanılan veri türüdür. Ancak tam sayıları için kullanılır. Kesirli ve ondalıklı sayılar için kullanılmaz. Örnek olarak 3, 78, -191, yaşınız, bir şirketin çalışan sayısı gibi ifadeleri int ile tanımlanır.

•	Float: Kayan noktalı sayılar veya ondalıklı sayılar olarak adlandırılan ifadeler için kullanılan veri türüdür. Örnek olarak 10.32 , Pi sayısı (3,14), -21,43 vb. gibi ifadeleri tutan verin türüdür.

•	Bool : True (Doğru), False (Yanlış) gibi iki değeri döndürür. Örneğin x = 5 diyerek Int bir değer atadınız ve Python dilinde     “bool(x == 6)” diyerek bir sorgulama yaptığınızda False değerini döndürecektir. Bool veri tipi oldukça işlevsel biri veri tipidir. Kullanıcıdan alınan bilgilerin programdaki bilgilerle veya başka kaynaktaki verilerle tutarlılığını kontrol etmeye yarayan bir veri tipidir.

•	List : Liste veri tipi tıpkı günlük hayatta kullanılan liste/listeleme yöntemi çok benzerdir. İçerisinde String, Int, Float ve Liste gibi peçok veri tipi bulundurabilir. Örnek olarak                           “liste_1 = [15,28,”İstanbul”,17.2, -46.5, [1,2,3,4,5]]” şeklinde bir liste tanımlanabilir. Listeler üzerinde değişiklik yapmaya izin verirler yeni eleman ekleme, silme ve güncelleme gibi işlemler.

•	Tuples : Tuples veya Demetler yapı olarak listeye oldukça benzerdirler ancak en önemli farklarından birisi Tuple elemanları üzerinde değişiklik yapmaya izin vermez. Veri ekleme, silme ve güncelleme gibi işlemlere izin vermez.

•	Dictionary : Sözlük veri tipi günlük hayatta kullanılan sözlük mantığına benzer. Key (Anahtar) ve Value(Değer) olmak üzere iki bölümden oluşur ve Değerler Anahtarlar ile eşleşerek sözlük yapısını oluşturur. Key : Value şeklinde bir tanımlama ile örenklendirilebilir.

# Kodlama.io Sitesinde Değişken Olarak Kullanıldığını Düşündüğünüz Verileri, Veri Tipleriyle Birlikte Örneklendiriniz.

Kodlama.io üzerindeki metinsel ifadeler string tipiyle tanımlanmış veri tipleridir. Programlardaki ilerleme durumunu belirten sayısal ifadeler Int veri tipinde tanımlanmıştır. Kategori kısmındaki eğitimler bölümü içerisinde bulunan eğitim programları liste tipinde tanımlanmış olabilir. 

# Kodlama.io Sitesinde Şart blokları Kullanıldığını Düşündüğünüz Kısımları Örneklendiriniz ve Python Dilinde Bu Örnekleri Koda Dökünüz.

Verilen ödevlerin tamamlanmadan ve bir sonraki bölüme geçilmemesi bir şart bloğu örneğidir.

    durum = 0 
 
    for i in range(1,11):
     
      ilerleme = str(input())

      if ilerleme == 'Ok':
          durum += 1
          print('İlerleme durumunuz : 10/',durum)

      else:
          print('İlerleme durumunuz : 10/')
