postgresql e komut satırı ile ulaşmak isterden aşağıdaki komutu kullan postgres burada kullanıcı adıdır. Eğer eklemediysen dosya konumuna gidip bin klasörünü path e ekle.


```bash
psql -U postgres
```

# SQL TEMELLERİ



## Kayıt Seçme


```sql
select * from tablo;
```

Yıldız kullanırsak tablodaki tüm sütünları alır. Eğer sütün veya sütünları almak için aşağıdaki gibi kullanabilirsin.

```sql
select sutun_adı from tablo;
```

```sql
select sutun_adı1 , sutun_adı2 from tablo;
```





## Kayıt Filitreleme

```sql
SELECT first_name , last_name 
FROM actor
WHERE actor_id < 10;
```

Kayıtları filitrelemek için **WHERE**  anahtar elimesini kullanırız. WHERE den sonra tablodaki hangi sütünda işlem yapacaksak ismini ve koşulu yazarız. Bu sorguda aktör tablosundan id si 10 dan küçük kayıtları getirirz ve gelen kayıtlardan sadece isim ve soy isim bilgilerini alırız.


### String bir koşul test etmek için tek tırnak ('') kullanılır.

```sql
SELECT * FROM actor
Where first_name = 'Penelope';
```

### NOT:
Karşılaştırma Operetörleri çoğu dil ile aynı farklı olarak <> operatörü var o da eşit değil demektir != i de kullanabilirsin.


## Mantıksal Operatörler 

3 mantıksal Operatör var. Bunlar ***AND , OR , NOT*** operatörleridir. Örnekle açıklayalım.

```sql
SELECT * FROM actor
WHERE first_name = 'Penelope' AND last_name = 'Guiness';
```
- İsmi Penelope olan ve soyadı Guiness olan kayıtlar gelir

```sql
SELECT * FROM actor
WHERE first_name = 'Penelope' OR last_name = 'Guiness';
```
- İsmi Penelope olan veya soy adı Guiness olan kayıtlar gelir

```sql
SELECT * FROM actor
WHERE first_name = 'Penelope' AND NOT last_name = 'Guiness';
```
- İsmi Penelope olan ve soy adı Guiness olmayan kayıtlar gelir


### PARANTEZ (İŞLEM ÖNCELİĞİ)

```sql
SELECT * FROM actor
WHERE first_name = 'Penelope' AND NOT (last_name = 'Guiness' OR last_name ='Pinkett');
```

- Parantez işlem önceliği gibi düşün burda iki koşul var. ***AND*** için kendinden önceki ve sonraki sorgunun True değer döndürmesi gerek ***OR*** da ise sanki filitreleme yeniden başlıyor gibi düşün.


## BETWEEN & IN 

BETWEEN sorgular arasında belirli değer aralığındaki  soruguları almak için kullanılıyor. Yani arasında anlamında.

```sql
SELECT title , length FROM film
WHERE length BETWEEN 90 AND 120;
```
- Bu sorguda film uzunluğu 90 ile 120 arasındaki sorguları alır.

```sql
SELECT title , length FROM film
WHERE length NOT BETWEEN 90 AND 120;
```
 - Bu sorguda ise film uzunlugu 90 ' dan küçük 120 ' den büyük sorguları getirir.

```sql
SELECT rental_rate , replacement_cost FROM film
WHERE (rental_rate  BETWEEN 2 AND 4) AND (replacement_cost BETWEEN 15 AND 20 );
```
- İki parantez ve iki koşul var .

IN ' ise aramak istediğimiz değerler birden fazla ise arka arkaya OR yazmak yerine in kullanabilirsin. Mesela;

```sql
SELECT * FROM film
WHERE length IN (40 , 50 ,60);
```

- Kayıtlardan film uzunlugu 40 , 50 , 60 olan kayıtları getirecektir.

```sql
SELECT * FROM film
WHERE length = 50 OR length = 60 OR length = 40;
```

- Kayıtlardan film uzunlugu 40 , 50 , 60 olan kayıtları getirecektir. Yukarıdaki örnekle ⤴️ ayı anlama gelir.

## LIKE & ILIKE

Bazen yer tutuculara ihtiyacımız olur mesle basit bir örnek ismi Ka ile başlayan kayıtlara ihtiyacımız var. Bunun için LIKE değiminden faydalanıyoruz.Büyük Kuçuk harf duyarlıdır.Eğer Büyük- Kucuk harf duyarlı olmasını istemiyorsan ILIKE Anahtar kelimesini kullanabilirsin.


```sql
SELECT * FROM actor 
WHERE first_name  LIKE 'P%'; 
```

Mesela bu sorguda **' % '** işareti kullanılmış. Yukarıda bahsettiğim yer tututcudur. İlk harfi 'P' ile başlayan kayıtları getirir.Daha karmaşık sorgular da yazılabilir.

```sql
SELECT * FROM actor 
WHERE first_name  LIKE 'Mi%e';
```

- Mi ile başlayıp e ile biten kayıtları getirir.

Burada % işaretinin konumlarına dikkatli bakalım. % işareti oldugu zaman ' ya rastgele bir karakter olacak ya da hiç karakter olmayacak'
şeklinde çalışıyor.



```sql
SELECT * FROM actor 
WHERE first_name  ILIKE 'mi%e';
```
- Büyük- küçük harf duyarlı değil.

### NOT:

% işareti birden fazla karakter için yer tutu görevi görür. Eğer sadece bir karakter için yer tutucu kullanmak istersen   ''` __ ` " kullanabilirsin.

```sql
SELECT * FROM actor 
WHERE first_name  ILIKE 'm_n%';
```

|"first_name"|
|----|
|"Mena"|
|"Minnie"|
|"Minnie"|
|"Mena"|

## DISTINCT


Eğer bir sütunda olan  farklı kayıtları almak istersen **DISTINCT** anahtar kelimesi kullanılır.

```sql
 SELECT DISTINCT first_name
 FROM actor;
```

aktor tablosundan isimleri farklı olan kayıtları getirir.

Birden fazla sütunda bu işlemi yapmak istersek ;

```sql
SELECT DISTINCT city , country FROM Customers;
```
Burada iki sütünu bir arada düşün. Yani Berlin - Germany &  Aachen- Germany gibi kayıtlar gelebilir burada sorgudan gelen ikili veriler birbirinden farklıdır .



## Count()

Bu bir fonksiyondur. ister tablodaki tüm verileri saydır istersen sadece sütuna göre sayım yap.

```sql
SELECT COUNT(*) FROM actor;
```

- aktör tablosundaki tüm kayıtların sayısını verir.

```sql
SELECT count(DISTINCT first_name) FROM actor;
```
- Aktör tablosunda isimleri birbirinden farklı kayıtların sayısını verir.

```sql
SELECT count(*) FROM actor 
WHERE first_name LIKE 'A%';
```

- Aktör tablosunda ism A ile başlayan kayıtların sayısını verir.




## PSQL TERMİNAL KULLANIMI

- Aşağıdaki iki komut veritabanlarını gösterir.

```bash
\l
```

```bash
\list
```

- Veritabanına bağlanmak için aşağıdaki komutu kullan.

```bash
\connect db_name
```

- var olan tabloları görmek için aşağıdaki komutu kullan;
```bash
\dt
```

- tablo hakkında özet bir bilgi istersen ;
```bash
\d tablo_adi
```

- veritabanına bu aşamada bağlıyız eğer bağlı değilsen bağlantı kurup direkt sql sorguları yazabilirsin;

```bash
dvdrental=# SELECT * FROM actor WHERE first_name LIKE 'P%' ;
 actor_id | first_name | last_name |      last_update
----------+------------+-----------+------------------------
        1 | Penelope   | Guiness   | 2013-05-26 14:47:57.62
       46 | Parker     | Goldberg  | 2013-05-26 14:47:57.62
       54 | Penelope   | Pinkett   | 2013-05-26 14:47:57.62
      104 | Penelope   | Cronyn    | 2013-05-26 14:47:57.62
      120 | Penelope   | Monroe    | 2013-05-26 14:47:57.62
(5 rows)
```


- Bir sorguyu tek satırda yazmak zorunda değilsin ``' ; '``  kullanmadığın sürece alt alta yazabilirsin.

```bash
dvdrental=# SELECT COUNT(*) FROM actor
dvdrental-# WHERE first_name LIKE 'P%';
 count
-------
     5
(1 row)
```

```bash
 \d+ tablo_adi
```

- Tablonun detaylarını gösterir



## ORDER BY

ORDER BY anahtar kelimesi sayesinde sorguları herhangi bir tablodaki değerlere göre artan veya azalan şekilde sıralayabilriz. Order By koşullardan sonra kullanılır.

```sql
SELECT * FROM film  ORDER BY length;
```

- Direkt sütun adı verirsen küçükten büyüğe doğru sıralar.


```sql
SELECT * FROM film  ORDER BY length ASC;
```

- ASC ' de küçükten büyüğe doğru sıralar.


```sql
SELECT * FROM film  ORDER BY length DESC;
```

- DESC büyükten küçüğe doğru sıralama yapar.



## LIMIT

Limit anahtar kelimesi seçilen kayıtlardan istediğin kadarımnı getirir.
Sorgu yazarken mantık akışı aşağıdaki şekildedir.

- Hangi tablodan hangi sütunları seçeceğimizi ``SELECT sutun_adi FROM tablo_adi``
- Eğer koşul varsa ``WHERE`` anahtar kelimesi.
- Koşula göre seçtiğimiz kayıtları sıralamak istersen ``ORDER BY`` 
- Koşula göre sıraladığımız kayıtlardan istediğin kadarını seçmek istersen de ``LIMIT`` 

anahtar kelimeleri kullanılır.


Basit bir örnek;
```sql
SELECT * FROM actor
LIMIT 20;
```

```sql
SELECT first_name FROM actor
WHERE first_name LIKE 'M%'
ORDER BY first_name DESC
LIMIT 5;
```

- Actor tablosundaki fist_name sütunundaki verileri seçtik Where ile M ile başlayanları aldık Order By ile sıralamayı tersine çevirdik tüm bu kayıtlardan 5 tanesi aldık.


## OFFSET

Eğer verileri atlamak istersen ``OFFSET`` kullanabilirsin. ORDER BY dan sonra kullanılır.

```sql
SELECT first_name FROM actor
WHERE first_name LIKE 'M%'
ORDER BY first_name DESC
OFFSET 2
LIMIT 2;
```


## Aggregate Fonksiyonlar;

Bu fonksiyonlar tek bir sonuç döndürür. Group By konusunda işlenecek.


### AVG()

Ortalama alır.

```sql
SELECT AVG(length) FROM film;
```

- Film tablosundaki uzunluk sütunundaki verilerin ortalamasını alır.

```sql
SELECT AVG(length) , AVG(replacement_cost) FROM film;
```

Birden fazla sütun için de **' , '** kullanabilirsin.

### SUM()

Toplama işlemi yapar.

```sql
SELECT AVG(length) , SUM(replacement_cost) FROM film;
```

### MAX()

Sütuna göre en yüksek değeri getirir.

```sql
SELECT MAX(length) FROM film;
```

### MIN()

Sütuna göre en düşük değeri getirir.

```sql
SELECT MIN(length) FROM film;
```


### ROUND()

Yuvarlama işlemi yapar. Ondalıklı sayılarda , den sonraki kaç basamağı almak istersen 2. parametre olarak verilir.
```sql
SELECT AVG(length) FROM film;
```

```sql
SELECT ROUND(AVG(length) , 2) FROM film;
```



## GROUP BY


SQL’de GROUP BY ifadesi, aynı değerlere sahip satırları özet satırlara gruplandırır. Bu sayede, gruplara göre toplama, ortalama, maksimum, minimum gibi hesaplamalar yapabilirsiniz. Örneğin, bir tabloda her şehirden kaç tane müşteri olduğunu bulmak için şehir sütununa göre gruplayabilir ve her gruptaki müşteri sayısını sayabilirsiniz.

***SIRALAMA AŞAĞIDAKİ ŞEKİLDEDİR ;***

```sql
SELECT _column_name(s)_  
FROM _table_name_  
WHERE _condition_  
GROUP BY _column_name(s)_  
ORDER BY _column_name(s);_
```

### NOT :

GROUP BY da verdiğimiz sütun adından farklı bir sütun adı kullanamayız. ( aggregate fonksiyonları ile ayı hizada)

**Yanlış Kullanım **❗
```sql
SELECT length , COUNT(*) as rating_count FROM film
GROUP BY rating;
```


```sql
SELECT rating , COUNT(*) as rating_count FROM film
GROUP BY rating;
```

- Bu sorguda film tablosundaki rating sütununu grupladık ve her farklı rating değerinin sayısını da yazdırdık.

| rating | rating_count |
| ------ |:------------:|
| R      |     195      |
| NC-17  |     210      |
| G      |     178      |
| PG     |     194      |
| PG-13  |     223      |


```sql
SELECT replacement_cost , MIN (length) FROM film
GROUP BY replacement_cost
LIMIT 5;
```

- Burada da **replacement_cost**  değerine göre grupladığımız ve uzunlugu en kısa olan 5 filmi sıraladık.

 | "replacement_cost" | "min" |
 | ------------------ | ----- |
 | 19.99              | 47    |
 | 25.99              | 46    |
 | 13,99              | 49    |
 | 10,99              | 46    |
 | 23,99              | 49    |


### Birden Fazla Sütun Gruplamak Istersek :


GROUP BY ifadesinde birden fazla sütun adı belirtmek, sorgu sonucunu o sütunların birleşik değerlerine göre gruplandırmak anlamına gelir. Yani, aynı ülke ve kullanıcı id değerlerine sahip satırlar bir grup oluşturur ve bu gruptaki sipariş sayılarının en büyüğü seçilir. Bu şekilde, her ülkeden her kullanıcı için en fazla sipariş verdiği kaydı bulunur.

```sql
SELECT replacement_cost , rental_rate FROM film 
GROUP BY replacement_cost , rental_rate
ORDER BY replacement_cost ASC;
```



## HAVING

Gruplanmış veriler ile koşul işlemi yapılıyor. Where ile arasında fark var. Mesela

```sql
SELECT rental_rate , COUNT(*) as film_sayisi  FROM film 
GROUP BY rental_rate
```

- Burada gruplanmış verilerin yani **rental_rate**' in benzersiz her değeri için film sayısını hesaplıyoruz 

 |  rental_rate | film_sayisi |
| ----------- | ----------- |
| 2.99        | 323         |
| 4.99        | 336         |
| 0.99        | 341         |



```sql
SELECT customer_id , SUM(amount) FROM payment
GROUP BY customer_id 
HAVING SUM(amount) > 100;
```

- toplam satısı 100' den büyük olan müşterileri alırız.

```sql
SELECT rental_rate , COUNT(*) as film_sayisi  FROM film 
GROUP BY rental_rate
HAVING COUNT(*) > 325;
```

- Burada ise her bir rental_rate için koşul sağlıyoruz 325 den büyük değerleri aldık

| "rental_rate" | "film_sayisi" |
| ------------- | ------------- |
| 4.99          | 366           |
| 0.99          | 341           |

Örnekte de oldugu gibi 2.99 değerini almadı. Bunu Where ile almak isteseydik 2.99 değerlerini alma gibi bir koşul koymamız gerekecekti. Peki bunun gibi 100 tane veri olsaydı ?


```sql
SELECT rental_rate , COUNT(*) as film_sayisi  FROM film 
WHERE rental_rate != 2.99
GROUP BY rental_rate;
```

Satır bazlı koşul koyduğumuzda WHERE , GROUP bazlı koşul koyduğumuzda HAVING anahtar kelimesini kullanırız.
AYNI İŞLEM DEĞİL  ❗ ***`` HAVING ``***  ❗ KULLAN..


## ALIAS

Sorgu içerisinde daha anlamlı isimler vermek için kullanılır . `` AS `` anahtar kelimesi ile kullanılır  yukarıdaki örneklerde de kullandım.

Birleştirme işelmini sütunlar arasında da kullanabilirsin. Bunun için CONCAT() fonksiyonundan faydalanacaz. Concat fonksiyonna parametre olarak sütun isimlerini yazarız ve sütundaki değerleribirleştirir. 

```sql
SELECT CONCAT(first_name , ' ' , last_name) AS full_name FROM customer;
```


| "Jared Ely"        |     | 
| ------------------ | --- |
| "Mary Smith"       |     |
| "Patricia Johnson" |     |
| "Linda Williams"   |     |
| "Barbara Jones"    |     |



# TABLO OLUŞTURMAK  & SİLMEK

## Tablo Oluşturmak - CREATE

Tablo oluşturmanın genel söz dizimi aşağıdaki şekildedir.


```sql
CREATE TABLE author(
	author_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL ,
	email VARCHAR(100) ,
	birthday DATE
	-- oluşturulacak sütun kadar eklenir.
);
```




## Veri Eklemek 

Oluşturduğumuz tabloya veri ekleyelim.Tablodaki sıra ile uyuşmasına gerek yok ancak önemli olan kısım sütun adlarına karşılık gelecek olan değerler aynı olması gerek mesela ilk sütun adını 'first_name' olarak girdiysen değer girerken de ilk başta isim girmemiz gerek.

```sql
INSERT INTO author (author_id , first_name , last_name , email , birthday) 
VALUES(1 , 'kadir' , 'polatkol' , 'polatkolkadir1@gmail.com' , '2000-11-17');
```

Burada author_id Primary Key ve Serial kısıtlamaları oldugu için bir değer girmemize gerek yok yani aşapıdaki gibi olmalıdır.

```sql
INSERT INTO author (first_name , last_name , email , birthday)
VALUES ('kadir' , 'polatkol' , 'polatkolkadir1@gmail.com' , '2000-11-17');
```

## Şablon Tablo

### Şablon

Bir tablodaki sütunları , veri türlerini ksıtlarlamaları bir şablon olarak alıp yeni bir tablo oluşturabiliriz.

```sql
CREATE TABLE author2 (LIKE author)
```

### Klon 

Bir toblodaki kayıtları başka bir tabloya klonlamak.

```sql
INSERT INTO author2 SELECT * FROM author;
```

Bu şekilde tüm kayıtları alabiliriz. Hatta koşul oluşturup içinde seçebilirir.

### Koşul ile Klonla

```sql
INSERT INTO author2 SELECT * FROM author WHERE first_name = 'kadir';
```

- Adı kadir olan yazarları ekler.Ancak kopyaladığımız tablodaki yazarın id si ne ise aynen onu ekler❗

### VERİ İLE KLONLAMAK

AS anahtar kelimesini kullanırız.

```sql
CREATE TABLE author3 AS SELECT * FROM author;
```

- Bu şekilde tüm verilerle beraber author3 tablosu oluşur.


## Tablo Silmek - DROP

```sql
DROP TABLE author;
```

Bu sorgu 'yazar' tablosunu silecektir ancak tablo yoksa hata verecektir. Bu hata kodunu almak istemiyorsak aşağıdaki gibi kullanabilirsin. 

```sql
DROP TABLE IF EXISTS author;
```


## VERİ GÜNCELLEMEK VE SİLMEK

Öncelikle örnek data oluşturmak için [mockaroo](https://www.mockaroo.com/) sitesini kullanıyoruz. burada rastgele oluşturulan verileri sql kodu olarak alıp tablomuza rastgele kayıtlar ekleyebiliriz.




### VERİ GUNCELLEMEK - UPDATE


UPDATE anahtar kelimesi ile veriler güncellenebilir.

```sql
UPDATE author SET first_name ='kadirrrr' , last_name ='polatkol' ;	
```

- Bu şekilde kullanırsan tablodaki tüm kayıtşara bu işlemi uygulayacaktır.

```sql
UPDATE author SET first_name ='kadirrrr' , last_name ='polatkol' WHERE author_id = 13 ;	
```

- Bu şekilde WHERE anahtar kelimesi kullanırsan istediğin kaydı veya kayıtları seçip güncelleme işlemi yapılabilir.

```sql
UPDATE author SET first_name ='kadirrrr' , last_name ='polatkol' WHERE author_id = 12 RETURNING *;	
```

- Eğer `` RETURNING `` anahtar kelimesini kullanırsan güncellenen kaydı geriye döndürür. Istersen  **' * '** ile tüm sütunları değil de istediğin sütun adını yazarak da kayıtları alabilirsin.

 ```sql
UPDATE author SET first_name ='RETURNING' , last_name ='polatkol'
WHERE first_name ILIKE 'Kad%'
RETURNING CONCAT(first_name ,' ', last_name) AS full_name ;	
```

- Bu şekilde CONCAT() fonksiyonu ile sütunalrı birleştirererk de güncellenen kayıtları alabilirsin.

### VERİ SİLMEK - DELETE

DELETE anahtar kelimesi ile veriler silinir. Veriler silinince diğer verilerin **' id '** değerleri değişmez❗.

```sql
DELETE FROM author 
WHERE first_name ILIKE 'RO%';
```

- ***ro*** ile başlayan kayıtları siler.  

## En Çok Kullanılan Kısıtlamalar Ve Veri Türleri

### Constraints (Kısıtlamalar)

Diğer veri türleri için  [website](https://www.tutorialspoint.com/postgresql/postgresql_constraints.htm)

1. **NOT NULL** : Bir sütunun boş olmayacağı anlamına gelir.
2. **UNIQUE** : Bir sütun da benbzersiz değerlerin bulunabileceği anlamına gelir
3. **PRIMARY KEY:** Bir tablodaki benzersiz bir sütunu tanımlar ve tablonun satırlarını tanımlamak için kullanılır.
4. **SERİAL** : Bir sütuna bir otomatik artımlı numara atar. Bu numara, sütuna yeni bir satır eklendiğinde otomatik olarak artar. Serial kısıtlama, sütunun benzersiz ve sıralı olmasını sağlar. Ayrıca, sütunun boş olmamasını sağlar.
5. **FOREIGN KEY:** Bu kısıtlama, bir tablodaki bir sütunun, başka bir tablodaki bir sütunun değerine bağlı olduğunu tanımlar.
6. **CHECK:** Bu kısıtlama, bir sütunda belirli değerlerin bulunabileceği anlamına gelir.
7. **DEFAULT:** Bu kısıtlama, bir sütuna varsayılan bir değer atar.
8. **ENABLE/DISABLE:** Bu kısıtlama, bir kısıtlamayı etkinleştirir veya devre dışı bırakır.
9. **CASCADE:** Bu kısıtlama, bir satırın silinmesi durumunda, bağlı olan satırların da silinmesi gerektiğini belirtir.
10. **RESTRICT:** Bu kısıtlama, bir satırın silinmesi durumunda, bağlı olan satırların silinmesine izin verilmediğini belirtir.


### DATA TYPES

Diğer veri türleri için  [website](https://www.postgresql.org/docs/current/datatype.html)

1. **INT:** Tamsayılar için kullanılır.
2. **SMALLINT:** Küçük tamsayılar için kullanılır.
3. **BIGINT:** Büyük tamsayılar için kullanılır.
4. **DECIMAL:** Ondalık sayılar için kullanılır.
5.  **NUMERIC:** Ondalık sayılar için kullanılır.
6. **FLOAT:** Ondalık sayılar için kullanılır.
7. **REAL:** Ondalık sayılar için kullanılır.
8. **CHAR:** Sabit uzunluklu metinler için kullanılır.
9. **VARCHAR:** Değişken uzunluklu metinler için kullanılır.
10. **DATE:** Tarihler için kullanılır.
11. **DATETIME:** Tarih ve saatler için kullanılır.
12. **TIMESTAMP:** Tarih ve saatler için kullanılır.
13. **TIME:** Saatler için kullanılır.
14. **BOOLEAN:** Mantıksal değerler için kullanılır.
15. **XML:** XML verileri için kullanılır.
16. **JSON:** JSON verileri için kullanılır.


### PRIMARY KEY 

Bir tablodaki benzersiz bir sütunu tanımlar ve tablonun satırlarını tanımlamak için kullanılır. Bir tabloda sadece bir tane olur.


### FOREGIN KEY 

Başka bir tablonun satırına referans vermek(Genellikle PK) için kullanılır.

```sql
CREATE TABLE book (
	id SERIAL PRIMARY KEY,
	title VARCHAR(50) NOT NULL ,
	page_number INTEGER NOT NULL,
	author_id INTEGER REFERENCES author(author_id)
)
```


Burada yeni bir tablo oluşturduk ve en sona eklediğimiz ifade FOREGIN KEY . author tablosundaki primary key sütununu referens gösterdik. Primary Key sütunu integer veri türünde oldugu için burda da veri türünü INTEGER olarak belirliyoruz.

Eğer book tablosuna author_id girerken author tablosunda olmayan bir yazarı refarans gösterirsen hata alırsın. Referans göstermeden önce author tablosunda ilgiliş yazarın kaydının olup olmadığını kontrol et.


```sql
insert into book (title, page_number, author_id) values ('Muffin Mix - Blueberry', 235, 7);
```

- Veri eklerken yukarıdaki gibi 
- Bir yazarın birden fazla kitabı olabilir.



### NOT NULL & ALTER

**NULL** bilinmeyen veri anlamındadır. Boş string veya 0 verilerinden farklıdır. Şu şekilde bir senaryo düşünelim bir kullanıcının email hesabı yoksa buradaki veriyi boş string şeklinde düşünebiliriz. Acak eğer kullanıcının maili var ancak ne olduğunu bilmiyorsak bu durumda o veri NULL (bilinmeyen) olarak tanımlanabilir. NOT NULL da kayıt oluşturulurken ilgili alanın boş null olarak kalmamasını sağlıyor. Yani o alana veri türüne göre bir şey yazmak zorunda bırakıyoruz

``' ALTER '`` ise varolan bir tabloda değişiklik yapmak istersek kullanırız.



```sql
CREATE TABLE IF NOT EXISTS users2(
	user_id SERIAL PRIMARY KEY , 
	username VARCHAR(50),
	email VARCHAR(100),
	age INTEGER,
	lastname VARCHAR(50)
)
```



BU şekilde bir user tablomuz oldugunu varsayalım. Bu tabloyu oluştururken username alanı için NOT NULL kullanmadık ve birkaç kayıt ekledik. Eğer sonradan bu sütunu **' NOT NULL'**  olarak değiştirmek istersen aşağıdaki gibi kullanabilirsin.


```sql
ALTER TABLE users
ALTER COLUMN username
SET NOT NULL;
```

Ancak kayıtlarda username alanı NULL olan kayıtlar varsa hata verecektir. İster sil istersen varsayılan değerler ata.

Ben silmeyi tercih ettim. Nasıl yapıldıgını öğrenene kadar aşağıdaki gibi yazdım bir türlü olmadı. 

```sql
SELECT * FROM users WHERE username= '';
SELECT * FROM users WHERE username= 'null';
SELECT * FROM users WHERE username= NULL;
```


NULL değerleri seçmek için ***' IS '*** kullanılıyormuş.

```sql 
SELECT * FROM  users WHERE username IS NULL;
```

Daha sonra ALTER komutlarını kullanarak sütunu  **' NOT NULL'** olarak değiştirdim ve veri eklemek istedğimde.

```sql
INSERT INTO users (username , email , age) VALUES ('arda' , 'arda@demo.com' , 20);
INSERT INTO users (email , age) VALUES ( 'arda@demo.com' , 20);
```

```bash
ERROR: Failing row contains (7, null, arda@demo.com, 20).null value in column "username" of relation "users" violates not-null constraint ERROR: null value in column "username" of relation "users" violates not-null constraint SQL state: 23502
```

#### ALTER

Alter kullanırken çok dikkatli olmalısın. Kısıtlama eklerken eğer kayıtlarda kısıtlamayla eşleşmeyen değerler varsa hata verecektir. Veri türünü değiştiriken kayıtlardaki değerlerin veri türüne dikkat etmen gerek vs..
 
1. **SÜTUN EKLEMEK İSTERSEN**

``' ALTER TABLE ' `` bir  tabloya sütun eklemek silemeke güncellemek için de kullanılabilir.

```sql
ALTER TABLE user2
ADD first_name VARCHAR(50);
```

2. **SÜTUN SİLMEK  İSTERSEN**

```sql
ALTER TABLE user2
DROP COLUMN username;
```

3. **SÜTUN ADINI DEĞİŞTİRMEK  İSTERSEN**

```sql
ALTER TABLE user2
RENAME  COLUMN user_id to id;
```

4. **SÜTUNUN VERİ TÜRÜNÜ DEĞİŞTİRMEK**

Tablodaki bir sütunun veri türünü değiştirmek için aşağıdaki sözdizimini kullanın:

```sql
ALTER TABLE user2
ALTER COLUMN age TYPE bigint;
```


5. Genel olarak, bir tabloya kısıtlama eklemek için ALTER TABLE ADD CONSTRAINT ifadesini kullanırsınız:


```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name constraint_definition;
```

- `table_name`: Kısıtlama eklemek istediğiniz tablonun adı.
- `constraint_name`: Yeni kısıtlamaya vermek istediğiniz ad. Bu adı, daha sonra kısıtlamayı yönetmek veya silmek için kullanabilirsiniz.
- `constraint_definition`: Yeni kısıtlamayı tanımlayan ifade.

MESELA UNIQUE KISITLAMASI

```sql
ALTER TABLE table_name
ADD CONSTRAINT unique_constraint_name UNIQUE (column_name);
```



### UNIQUE

Tablo oluşturuken bu kısıtlamayı ekleyebilirsin ya da ALTER ile ekleyebilirsin. UNIQUE kısıtlaması sütundaki kayıtların benzersiz olmasını sağlar. Eğer tablo oluştururken Unique eklemediysen ALTER ile daha sonradan  eklemek istiyosan tablodaki kayıtlara dikkat et eğer birbirinin aynısı kayıtlar varsa silmen gerekir.

**ALTER İLE EKLEMEK İSTERSEN**

```sql
ALTER TABLE user2
ADD UNIQUE(email);
```


### CHECK

**CHECK** kısıtlaması ile uyguladığımız sütundaki verilere belirli koşullar verebiliriz. Örneğin age (yaş) olarak belirlediğimiz bir sütuna negatif değerler verebiliriz veya web portaline üye olan kullanıcıların yaşlarının 18 yaşından büyük olması gibi kendi senaryolarımıza uygun başka kıstlamalar da vermek isteyebiliriz.

CHECK kısıtlamasını da tablo oluştururken veya ALTER komutu ile beraber tablo oluştuktan sonra kullanabiliriz.

### CHECK Kullanımı

Employees şeklinde bir tablomuzu oluşturalım. Tablodaki age sütununda bulunan verilerin 18'e eşit veya büyük olmasını istiyoruz.

```sql
ALTER TABLE table_name 
ADD CHECK expression;
```


# JOIN YAPILARI

Birbiri ile ilişkili olan tablardaki verileri farklı JOIN yapıları kullanarak sanal olarak birleştirip daha anlamlı veriler haline getirebiliriz.

## INNER JOIN 

INNER JOIN yapısı sayesinde birbiriyle ilişkili olan tabloların birbiriyle eşleşen (kesişen) verilerini sıralayabiliriz.


```sql
SELECT title , first_name , last_name FROM book 
INNER JOIN author ON book.author_id = author.author_id ;
```

- `INNER JOIN`: SQL'e iç birleştirme yapmak istediğinizi belirten anahtar kelimedir.
- `author`: Birleştirmek istediğiniz ikinci tablo.
- `ON`: İki tabloyu birbirine bağlayan koşulu belirtir. İki tablo arasındaki ilişkiyi, hangi sütunların eşleşen değerlere sahip olması gerektiğini tanımlar.

`INNER JOIN`, `book` tablosundaki `author_id` sütununu, `author` tablosundaki `author_id` sütunu ile eşleştirir ve koşulu sağlayan satırları birleştirir. Sonuç, ilgili kitap başlıgını (title)  yazarın adı ve soyadını içerir.


Aşağıdaki şekilde **tablolara göre** sütundaki veriler de alınabilir.

```sql
SELECT book.title , author.first_name , author.last_name FROM book 
INNER JOIN author ON book.author_id = author.author_id ;
```


## LEFT JOIN 

LEFT JOIN, sol tablodaki tüm satırları ve sol tablodaki eşleşen satırları sağ tablodaki eşleşenlerle birleştirir. Eşleşmeyen sağ tablo satırları için NULL değerler kullanılır.

```sql
SELECT customer.first_name, customer.last_name, rental.rental_date
FROM customer
LEFT JOIN rental ON customer.customer_id = rental.customer_id;
```


Yani customer tablosundaki tüm kayıtları alır ve customer tablosunda rental tablosu ile eşleşen kayıtları da alır . rental de olmayaıp custumer de olan kayıtları (yani sipariş vermemiş kullanııcları) da haliyle getireceği için kiraladığı ürün bilgileri vs 'NULL' olarak gelir.


![Güzel Bir Manzara](sql/assets/LeftJoin.png)


## RIGHT JOIN 


RIGHT JOIN, sağ tablodaki tüm satırları ve sağ tablodaki eşleşen satırları sol tablodaki eşleşenlerle birleştirir. Eşleşmeyen sol tablo satırları için NULL değerler kullanılır.


```sql
SELECT rental.rental_date, inventory.film_id, film.title
FROM rental
RIGHT JOIN inventory ON rental.inventory_id = inventory.inventory_id
LEFT JOIN film ON inventory.film_id = film.film_id;
```


![rightjoin](../assets/RightJoin.png)


## FULL JOIN 

FULL JOIN (Tam Birleştirme): FULL JOIN, hem sol hem de sağ tablodaki tüm satırları ve eşleşen satırları birleştirir. Eşleşmeyen satırlar için NULL değerler kullanılır.

```sql
SELECT customer.first_name, customer.last_name, rental.rental_date, film.title
FROM customer
FULL JOIN rental ON customer.customer_id = rental.customer_id
LEFT JOIN inventory ON rental.inventory_id = inventory.inventory_id
LEFT JOIN film ON inventory.film_id = film.film_id;
```


![fulljoin](../assets/fullJoin.png)



## UNION


**UNION** operatörü sayesinde farklı SELECT sorgularıyla oluşan sonuçları tek bir sonuç kümesi haline getiririz.

```sql
(SELECT * FROM book WHERE page_number > 60) UNION (SELECT * FROM book WHERE title LIKE '_u%');
```

Bazen her iki select sorgusunda da aynı kayıt olabilir ve bu kaydı sandece 1 kez gözterir.Eğer 1 kez değil kaç kez tekrar etmiş görmek istersen;


```sql
(SELECT * FROM book WHERE page_number > 60) UNION ALL (SELECT * FROM book WHERE title LIKE '_u%');
```


Aynı tablo olmak zorunda değil farklı tabloda olabilir ancak burada sürun sayısı ve sütunun veri türü aynı olması gerek.

YANLIŞ❗

```sql
(SELECT title , page_number FROM book WHERE page_number > 60) UNION (SELECT *  FROM author);
```

YANLIŞ❗
```sql
(SELECT title , page_number FROM book WHERE page_number > 60) UNION (SELECT first_name , author_id  FROM author);
```


## INTERSECT


Unıon un aksine iki sorgunun birleşimini değil kesişimini bulur.


```sql
(SELECT id , title FROM book WHERE page_number > 60 ) INTERSECT (SELECT id , title FROM book WHERE title LIKE '_a%');
```


## EXCEPT

EXCEPT anahtar kelimesi sayesinde ilk sorguda olup ancak ikinci sorguda olmayan verileri gösterir.

```sql
( SELECT * FROM book ORDER BY title LIMIT 5)  EXCEPT ( SELECT * FROM book ORDER BY page_number DESC LIMIT 5 );
```

ilk sorguda olup ikinici sorguda olmayan kayıtları getirir.




# SUBQUERIES (ALT SORGULAR)

"subquery" (alt sorgu), bir ana sorgunun içinde yer alan başka bir sorgudur. Bir ana sorgu içinde kullanılan alt sorgu, genellikle bir alt küme veya filtreleme için kullanılır.

```sql
SELECT * FROM film WHERE  film_id =  (SELECT film_id FROM film WHERE title = 'Zorro Ark')
```

- Saçma bir örnek olabilir ancak anlaşılması için basit olması gerek . Burada olay şu ki  ilk sorguda bazen film_id değeri statik bir değer değildir ve başka bir sorguya ihtiyaç duyarız. Burada parantez içerisinde belirttiğimiz sorgu bir alt sorgudur ve önce alt sorgu işleme alınır. 

- Fark ettiysen alt sorgudan dönen değer sadece bir tane ve ihtiyacımız olan sadece film_id değeri oldugu için alt sorguda sadece film_id sütun adını aldık (``SELECT film_id FROM film ....)`` . 

```sql
SELECT * FROM film WHERE  film_id >  (SELECT film_id FROM film WHERE title = 'Ali Forever')
```

- Burada ise title değeri **'Ali Forever'** olan kaydın id değerinden büyük olan kayıtları alıyoruz.

```sql
SELECT title , release_year , (SELECT MAX(length)FROM film  )  AS "en uzun film"  , (SELECT MAX(length) FROM film) - length AS "Diff" FROM film; 
```

- Bu şekilde sütunlarda da işlem yapabiliriz
  
  
## ANY & ALL  

Any ve All operatörleri alt sorugularda sıklıkla kullanılır ve tek bir sütunda bulunan bir değerle bir değer dizisinin karşılaştırılmasını sağlar.


```sql
SELECT first_name , last_name FROM author
WHERE author_id = 
(
	SELECT author_id FROM book WHERE title = 'Sugar - Invert' 
)	
```

- bu bir alt sorgu örneği . Eğer OR operaötür kullanarak bir title bilgisi daha eklersek hata alırız.

- Hatalı kullanım ❗
```sql
SELECT first_name , last_name FROM author
WHERE author_id = 
(
	SELECT author_id FROM book WHERE title = 'Sugar - Invert' OR title = 'Barramundi'
)
```


- Hata almak istemiyorsan ANY operatörünü kullan.

### ANY

"ANY" operatörü, bir alt sorgudan dönen herhangi bir değerle karşılaştırma yapar ve en az bir durum doğru olduğunda bir sonuç döndürür.(or operatörüne benziyor)


```sql
SELECT first_name , last_name FROM author
WHERE author_id = ANY
(
	SELECT author_id FROM book WHERE title = 'Sugar - Invert' OR title = 'Barramundi'
)
```

#### DİKKAT ⚠️

- Burada  koşulu sağlayan iki farklı id değeri gidiyor. Normalde author_id =(SELECT author_id FROM book WHERE title = 'Sugar - Invert') sorgusunda bir tane author_id değeri gidiyordu.

-----


**FARKLI BİR ÖRNEK**
```sql
SELECT product_name FROM products
WHERE product_price > ANY (SELECT product_price FROM products WHERE product_category = 'Electronics');
```


- Bu sorgu, elektronik kategorisindeki ürünlerden daha yüksek fiyatlı ürünleri döndürür.

### ALL


"ALL" operatörü, bir alt sorgudan dönen tüm değerlerle karşılaştırma yapar ve mantıksal ifadenin tüm durumları doğru olduğunda bir sonuç döndürür. (and operatörüne benziyor)

```sql
SELECT product_name 
FROM products 
WHERE product_price > ALL (SELECT product_price FROM products WHERE product_category = 'Electronics');
```

- Bu sorgu, "products" tablosundan ürünlerin fiyatını, elektronik kategorisindeki tüm ürünlerin fiyatlarından daha büyük olanları seçer.

Özetle, "ALL" operatörü, alt sorgudan dönen tüm değerlerin mantıksal ifadenin tüm durumlarını doğrulaması durumunda sonuç döndürürken, "ANY" operatörü, alt sorgudan dönen en az bir değerin mantıksal ifadenin doğrulaması durumunda sonuç döndürür.

## Alt Sorgular ve JOIN Kullanımı

```sql
SELECT book.title ,book.page_number , (SELECT AVG(page_number) FROM book) AS "ORTALAMA SAYFA SAYISI", author.first_name ,author.last_name  FROM book 
INNER JOIN author ON book.author_id = author.author_id
WHERE page_number > (SELECT AVG(page_number) FROM book );
```

	