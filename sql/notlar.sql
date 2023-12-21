
-- ** Kayıt Seçme ** 

-- select * from ecommerce.product
-- select Name from ecommerce.product

-- select Name , Price from ecommerce.product

-- ** Kayıt Filitreleme (where)
-- product tablosundan İd si olan kaydı getirir

-- select * from ecommerce.product where Id =1

 -- select * from ecommerce.product	where price =2000 -- produt tablosunda fiyatı 2000 olan kayıtları getirir(Birden fazla kayıt getirebilir)
 
 -- select Name , Price , Id from ecommerce.product where Price >= 2000 -- 2000 den büyük kaytları getirir. select ile from arasında yazdığımız ifadeler tablodaki sütün isimlerini ifade eder. where ise bir filitreleme işlemi yapar
 
--  select Name , Price from ecommerce.product where Price >= 1000 and Price <= 3500 -- aralık belirtmek için and kullanırız. ve and ve anlamındadır iki ifade arasında olan kayıtları getiri.
 
 -- select Name , Price from ecommerce.product where Price >=2000 or Price <= 3000 -- 2000 den büyük tüm kayıtları ve 3000 den küçük tüm kayıtları getirir.
 
 
 
 -- select * from ecommerce.product where Name ="iphone 5" -- name i iphone 5 olan kayıtları getirir.
 
-- select * from ecommerce.product where Name !="iphone 5" -- name i iphone 5 olmayan kayıtları getirir.
-- select * from ecommerce.product where Not Name ="iphone 5" -- name i iphone 5 olmayan kayıtları getirir.
 
 
 -- select * from ecommerce.product where Name ="iphone 6" and (Price = 1500 or Price = 2000) -- parantez işlem önceliği gibi düşün burda iki koşul var 
 
 
 -- ** Kayıt Filitreleme de kullanılan operatörler (between in Like)
 
 
 -- select * from ecommerce.product where price Between 2000 and 9000 -- between arasında demektir fiyatı 2000 ile 3000 arasındaki kayıtları getirir.
 
 -- select * from ecommerce.product where Categori In ("telefon" or "bilgisayar") -- Profuct tablosundaki categori sütununda telefon ve bilgisayar kategori kaydına sahip kayıtları getirir
  -- select * from ecommerce.product where Categori Not  In ("telefon") -- Profuct tablosundaki categori sütununda telefon kategori kaydına sahip olmayan kayıtları getirir
 
 -- select * from ecommerce.product where Name Like '%iphone%'
 -- produt tablosunda isim sütünu için bir arama yapıyoruz ancak burada içerisinde iphone geçen kayıtları istiyoruz. 
 -- %aranacak_Deger% ler arasında yazdığımız ifade aramak istediğimiz ifade ve % ile başında ve sonunda ne olduğu önemli değil diyoruz.
 -- herhangi bir kelimeyi herhangi bir kolan içerisnde aramak istersek kullanabilirir.
  
 -- select * from ecommerce.product where Name Like '%iph%' -- 'iph' ifadesi geçen tüm kayıtlar gelir
 
-- select * from ecommerce.product where Name Like 'i%' -- 'i' ile başlayan tüm kayıtlar gelir

-- select * from ecommerce.product where Categori Like '%r' -- Categori sütununda 'r'  ile biten tüm kayıtlar gelir
 
 -- select * from ecommerce.product where Categori Like '%a_' -- Categori sütununda sondan ikinci harfi 'a'  ile biten tüm kayıtlar gelir. _ nin olayı ise en son karakter önemli değil yani alt çizgi bir karakter için geçerli 
 
 -- % ile _  arasındaki fark % birden fazla karater olabiliyorken _ için tek bir karater
 
 -- select * from ecommerce.product where Categori Like '__l%' -- ilk iki karakterin ne olduğu önemli değil 3. karakter l ve 4. karakter ve geriye kalanı önemli değil
					 
					  -- ** Kayıt Sıralama **
					  
-- select * from ecommerce.product order by Price -- fiyat bilgisine göre küçüten büyüğe doğru sıralar
-- select * from ecommerce.product order by Price ASC  --  fiyat bilgisine göre küçüten büyüğe doğru sıralar
-- select * from ecommerce.product order by Price DESC --  fiyat bilgisine göre büyükten  küçüğe doğru sıralar
-- select * from ecommerce.product order by categori , Price 	--  İlk başta kategori bilgisine göre sıralanır daha sonra  kendi aralarında da fiyat bilgisine göre sıralanır.
--  select * from ecommerce.product order by categori DESC , Price 	ASC --  İlk başta kategori bilgisine göre büyükten küçüğe sıralanır daha sonra  kendi aralarında da fiyat bilgisine küçükten büyüğe göre sıralanır.
   
   
					-- ** Sql Hesaplama fonksiyonları  **
  
--  select min(Price) as "minimum fiyat" from ecommerce.product -- Tabloda fiyatı en düşük kaydı getirir.
-- select max(Price) as "max fiyat" from ecommerce.product -- Tabloda fiyatı en yüksek kaydı getirir.

		-- ** alternatif olarak ** --
        
-- select name , Price from ecommerce.product order by price Desc limit 1 -- ürün tablasunda name ve fiyat bilgisini aldık ve bu tabloda fiyat bilgisine göre büyükten küçüğe doğru sıralama yaptık. limit 1 tanımlaması ile ilk kaydı aldık.
-- select count(*) from  ecommerce.product -- hangi kolonu verirsen ver satırları sayacaktır. yani kayıt sayısını geriye döndürür.
-- select count(Id) from  ecommerce.product -- fark etmez aynı sayıyı verir
-- count()  metodu null alanları saymaz kullanırken dikkatli olmalısın.
-- select avg(price) as ortalama from  ecommerce.product  -- tablodaki kayıtların fiyat bilgilerinin ortalamsını alır
-- select sum(price) as toplam from  ecommerce.product --  tablodaki kayıtların fiyat bilgilerinin toplamını alır

   
					-- ** Sql String  fonksiyonları  **
   
-- select length("kadir polatkol") as "karakter sayisi" -- lenght fonsiyonu içerisine yazdığım elemanın uzunlugunu verdi.    
-- select name , length(name) as "karakter sayisi" from ecommerce.product -- ürünler tablosunda name alanın için kayıtların karakter uzunlugunu verdi uzunlugunu verdi.
-- select name , concat(left(name , 3) , "...") as "karakter uzunlugu" from ecommerce.product -- concat iki string ifadeyi birleştirmek için kullanılabilir. left() fonksiyonu ise belirttiğimiz karakter sayısı kadar ilgili kayıtları alır.
-- select left("kadir" , 3 ) as soldan_getir
-- select right("kadir" , 3) as sagdan_getir
-- select lower("KADİR") as "kucuk yap" -- büyük harfleri küçük harfe dönüştürür.
-- select upper("kadir") as "buyuk yap" -- kucuk  harfleri buyuk harfe dönüştürür.
-- select name  , upper(name) as buyuk_yap  from ecommerce.product -- kayıtların name alanlarına göre büyük harf yapar
-- select name  , lower(name) as kucukYap from ecommerce.product -- kayıtların name alanlarına göre küçük harf yapar
-- select name , replace(name , " ","-" ) as degitstir from ecommerce.product -- bosluk karakterlerini "-" ile değiştirir.
-- select trim("     kadir         " )  -- sağdan ve soldan boşlukları temizler
   
   
   
   
   
   
   -- select * from ecommerce.product
   
--   INSERT INTO ecommerce.product (name , price, ImageUrl , categori ) VALUES ("iphone 11" , 110000 , "8.jpg" ,"telefon")  ;
  
-- update ecommerce.product SET NAME ="samsung note 11"

-- Bu şekilde kullanırsan tüm kayıtların name alanlarını günceller. Filitrelerme işlemi yapmak için where kullanılması gerekir

-- update ecommerce.product SET name  ="samsung note 11" where Id =1 -- id si 1 olan kaydın name alanını günceller

   
  -- SET SQL_SAFE_UPDATES =0;
   -- update ecommerce.product SET Price = Price + 1000 
   
   
   -- ** GROUP BY ** --
   
-- select Categori from ecommerce.product
-- select distinct Categori from ecommerce.product
   
   -- select Categori , avg(price) as ortalama from ecommerce.product where price > 400 group by Categori 
	-- select categori ,  Count(*) as adet from ecommerce.product where count(*) > 1  group by categori
	-- select categori ,  Count(*) as adet from ecommerce.product  group by Categori having count(*) > 1
 	-- select categori ,  Count(*) as adet from ecommerce.product where price > 10000  group by categori
    -- select categori ,  Count(*) as adet from ecommerce.product where price > 6000  group by categori having Count(*) > 1
    
    
   -- Update ecommerce.product Set 
     
     select * from ecommerce.product where ImageUrl is Null
     