# Pytest Decorators
Decarotorler, test fonksiyonlarında belirli durumları sağlamak ve engellemek için kullanılan testlerin daha başarılı ve sağlıklı çalışmasında rol oynayan çok kullanışlı ve işlevli yapılardır.
# 
**• @pytest.fixture :** Test işlemlerinde testte tekrar edecek işlemleri tanımlamak için kullanılır. Birden çok testi tek bir test ile yapmayı sağlar. Fixture’e bağlı testler çalıştırıldığında birden çok kez çağrılır ve daha kolay bir test işlemi sağlar ve bu sırada testimiz tekrar tekrar çalıştırıldığının farkında olmaz . Veritabanı bağlantıları, test edilecek URL’ler ve inputlar ile değer gönderme işlemlerini tekrarlamadan değerleri teste döndürmeyi sağlar.  

**• @pytest.mark.parametrize :** Test işlemlerinde belirtilen testte birden fazla değer göndererek farklı değerler için tek bir test ile test etmeyi sağlar. Örnek olarak “www.saucedemo.com/” adresinde farklı username ve password değerleri ile test edilebilir. Test edilecek değerleri bir liste içerisinden tek tek çekerek test etmeyi sağlar.

**• @pytest.mark.xfail :** Bir testin herhangi bir nedenle başarısız olmasını beklediğimiz zamanlarda kullanılır. Henüz uygulanmayan bir özellik veya düzeltilmemiş bir hata olduğunda xfail ile bu durumu kontrollü şekilde başarısız olarak sonuçlandırırız. 

**• @pytest.mark.skip :** Bir testi test etmeden atlamayı sağlar. Tamamlanmamış veya hata kaynağı belirlenmemiş test işlemlerinde kullanılabilir. Bu sayede Pytest tarafından herhangi bir olumsuz dönüş almadan belirtilen testi test etmeden atlayarak diğer işlemlere geçilir.

**• @pytest.mark.timeout :** Test işlemlerinin yapılan teste türüne göre hızlı olmasını bekleriz. Çeşitli nedenlerden dolayı (kesintiler, server gecikmeleri vs) testleri askıda kalmasını önleyerek belirtilen bir süre içinde çalışmasını sağlamak çalışmıyorsa zaman aşımına uğratarak testi sonlandırır. 

**• @pytest.mark.filterwarning :** Belirli test öğelerine uyarı filtreleri ekleyerek hataların, uyarıların yakalanmasını sağlar. Yakalanan hatalar ve uyarılar sayesinde daha sağlıklı ve başarılı testler gerçekleştirilir.
# 
