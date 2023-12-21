
## Kayıt Ekleme 

```sql
INSERT INTO ecommerce.product (Name , Price , Categori ) VALUES ("iphone 11" , 11000, "telefon");
```


``ecoomerce.product :``  veritabanı ismi ve tablo ismidir. Daha sonrba parantez içerisine tablodaki sütun adladını yazıyoruz. ``Values()``  ile de bu tablodaki sütunları dolduruyoruz.


## Kayıt Güncelleme


```sql
update ecommerce.product SET NAME ="samsung note 11"
```

Kayıt güncelleme işlemi **update** ile yapılır daha sonra **veritabanıAdi + tabloAdi** gelir . ``SET`` ile artık hangi sütunu güncelleme işlemi yapacaksak seçilir . Burada Sütun adı NAME olan kayıtları seçtik. 


Bu şekilde çalıştırırsak Sütundaki tüm kayıtları günceller. Ancak belirli bir kayıdı güncelleştirmek istersek  ``where``  ile filitreleme işlemi yapmamız gerkir.

```sql
update ecommerce.product SET NAME ="samsung note 11" where Id =1
```

Yukarıdaki örnekte id si 1 olan kaydı güncelledik. 


```sql
update ecommerce.product SET NAME ="samsung note 11" where Price > 1400
```

Bu  örnekte ise fiyatı  1400 den büyük  olan kaydıtların name alanlarını güncelledik. 


Eğer Her kaydın fiyatına 1000 ekleyecek olursak ;

```sql
 update ecommerce.product SET Price = Price + 1000 
```

Bu tanımlama where ifadesini kullanmadığımız için güvenli güncelleme modu na geçer ve mysql de bu işlemi yapmaz. kullanıcıların yanlışlıkla bir WHERE deyimi olmadan bir tabloda birden çok satırı güncellemesini veya silmesini önleyen bir MySQL özelliğidir. Bu özellikten sıyrılmak için ister where kullan istersen aşağıdaki tanımlamayı kullan.


```sql
	SET SQL_SAFE_UPDATES = 0;
	update ecommerce.product SET Price = Price + 1000 
```

Bu şekilde Safe mode dan kurtulabilriz ancak kullanırken dikkatli olunması gerekir.

Şimdi de tüm kayıtlara %10 zam yapalım

```sql
	SET SQL_SAFE_UPDATE =0;
	UPDATE ecommerce.product SET Price  = Price *1.1
```


Mesle kayıtlar arasında imageUrl alanları var ve biz varsayılan bir resim atamak istiyoruz. Yani Sadece Null Alanlara sahip kayıtlara update sorgusu çalıştıracaz.


```sql
update ecommerce.product SET ImageUrl  = "default.png" where ImageUrl is not Null 
```

ImageUrl alanı Null olan tum kayıtların ImageUrl alanlarını günceller.


##  DELETE

```sql
DELETE from ecommerce.product where ID = 1
```

İd si 1 olan kaydı siler. Eğer filitreleme işlemi yapmazsan tüm kayıtları siler. Busebeple mutlaka filitreleme işlemi yapmalısın.






## Group By

Gruplama yapmak için kullanılır.Bu ifade, belirli bir sütundaki değerlere göre kayıtları gruplandırır ve sonuçları bu grupların bir araya getirilmesiyle hesaplar. Mesle işçiler tablomuz var bu tablodaki işçilerin departmanlarına göre gruplayıp maaş ortalamalarını almak istiyoruz.


Eğer bir tabloda kayıtlar birden fazla ise ve biz sadece farklı türdeki kayıtları istiyorsak ``distinc``  parametresini kullanırız. Mesela kategori sütununda birden fazla telefon ve bilgisayar kayıtları var. tekrarlayanları değil de farklı türdeki kayıtları hedefliyorsak bu parametreyi kullanabiliriz.


```sql
select distinct Categori from ecommerce.product 
```

Ayrıca, DISTINCT, GROUP BY ifadesi kullanmadan da bir sorgunun sonuçlarını gruplamak ve yalnızca benzersiz sonuçları döndürmek için kullanılabilir. Ancak, GROUP BY ifadesi daha güçlü bir gruplama aracıdır ve daha fazla işlevsellik sağlar özellikle de hesaplama işlemi yapacaksak.



```sql
   select Categori  from ecommerce.product group by Categori
```

Yukarıdaki ifade distinct ile aynı sonucu verir. Kategoriye göre bir gruplama işlemöi yapıyoruz. Eğer bu kayırlarda farklı kategori türlerinden kaçar adet olduğunu görmek istersek aşağıdaki gibi tanımlarız.

```sql
   select Categori , Count(categori) as Adet from ecommerce.product group by Categori
```

Bu tanımlama sayesinde kategorilerde mesela telefon ve bilgisayar kayıtları  var . Bu kayıt türlerini  yazar ve her bir kategori için kaç adet olduğunu da  ``Count(categori) as Adet`` tanımlaması ile başka bir sütunda bunu görebiliriz.
| Categori |Adet |
|:--------:|:--------:|
| Telefon | 8||
|Bilgisayar | 2|

gibi;

```sql
   select Categori , Sum(price) as Toplam from ecommerce.product group by Categori
```

Burada ise kayıtları categorilerine göre listeler ve kayıtların fiyatlarını toplar . 

| Categori |Price |
|:--------:|:--------:|
| Telefon | 139000||
|Bilgisayar | 12000|

Gruplanmış veriler üzerinde filtreleme yapmak için ``having`` değimi   kullanılır. Where değimi ile birbirine benzer ancak amaçları farklıdır. "WHERE" ifadesi, veritabanındaki tabloların satırlarına filtreleme yapar ve belirli bir koşulu sağlayan satırları seçer.

"HAVING" ifadesi, yalnızca "GROUP BY" ifadesi ile birlikte kullanılır ve gruplanmış veriler üzerinde filtreleme yapmak için kullanılır. "HAVING" ifadesi, gruplanmış verilerin toplamı, sayısı veya diğer toplama işlemleri gibi gruplama işlemleri üzerinde filtreleme yapar.

Özetle, "WHERE" ifadesi, tabloların satırlarına filtreleme yaparken, "HAVING" ifadesi gruplanmış veriler üzerinde filtreleme yapar. "HAVING" ifadesi, gruplama işlemleri üzerinde filtreleme yapmak için kullanılırken, "WHERE" ifadesi, herhangi bir sütun veya satır üzerinde filtreleme yapmak için kullanılır.

```sql
select categori ,  Count(*) as adet from ecommerce.product where price > 6000  group by categori having Count(*) > 1
```

Bu sorgu oncelikle kategorilere göre gruplama işlemi yapar ancak bunu yapmadan önce product tablosunda fiyatı 6000 den büyük kayıtları alır. İki sütun karşımıza çıkar kategori ve Adet. Sonra bu gurplanmış kayıtlar arasında sayısı 1 den büyük grubu alır. Yani yukarıda da bahsettiğimiz gibib having gruplama işleminde filitreleme yaparken where kayıtlar ile ilgili filitrelemeleri yapar.



