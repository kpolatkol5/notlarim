# SQLİTE3 İLE VERİTABANI PROGRAMLAMA


<br>

- sqlite python 2.5 sürümünden itibaren python un bir parçasıdır. Bu sebeple direkt sqlite 3 ü projelerimizde kullanmak üzere import edebilriz.


```py
    import sqlite3 as vt 
    # "as db" ile takma ad vermiş olduk

     db = vt.connect("db_adi.sqlite")
```

- Yukarıdaki işlemde veri tabanı ile bağlantı kurduk. Veri tabanı ile bağlantı kurmak için ***.connect("db_name.sqlite")*** metodundan faydalanırız. Aynı dizin içerindeki veritabanı ile bağlantı kurmak için veritabanının ismini yazarız.Bu bağlantıyı sağlamak için tam yolu da girebilriz veya os modülünden de daydalanabilriz. 

<br><hr>

## ***VAROLAN VERİTABANI İLE BAĞLANTI KURMAK***

- ***connect metodu*** ile veritabanına bağlantı kurduğumuzu gördük. Eğer kökdizinde aynı isimde bir veritabanı varsa bağlantı kuracaktır. Ancak aynı isimde bir veritabanı yoksa yeni bir veritabanı oluşturacaktır.

<br><hr>


## ***İMLEÇ OLUTŞTURMA***

- imleç oluşturmak için ***.cursor()*** metodundan faydalanacağız.


```py 
    im = db.cursor()
```

- cursor metodu sayesinde im değişkeni bir nesnedir. Bu nesnenin ilgili metodlarını kullanarak SQL komutlarını işletebiliriz.

<br><hr>


## ***TABLO OLUŞTURMA***

```py   
    import sqlite3 as vt 
    
    db = vt.connect("db_adi.sqlite")
    im = db.cursor()

    im.execute(""" CREATE TABLE TOWNS (id , town_name) """)
    # ececute metodundan faydalanarak TOWN adında bir tablo oluşturduk ve bu tablolara 2 adet sütün başığı  ekledik.
```


- yukarıdaki örnekte tam bir bağlantı sağlayıp imleç oluşturarak sql kodlarımızı işletmiş olduk. ***.execute()*** metodu ile sql kodalrımız işletebileceğimizi öğrendik burada ***CREATE TABLE*** bir sql komutudur.

## ***ŞARTLI TABLO OLUŞTURMA***


- Yukarıdaki örnekte bşr tablo oluşturmuştuk. bu kodları bir daha çalıştıracak olursak hata verecektir. Bnun için şatrlı tablo oluşturmamız gerekiyor. 

```py 
    im.execute(""" CREATE TABLE IF NOT EXİSTS  TOWNS (id , town_name) """)
```

- Yukarıdaki örnekte olduğu gibi şart koymuş olduk bu şart TOWNS adında bir tablo yoksa oluştur denemktir. Kodlarımızı bu şekilde düzenledikten sonra tekrar çalıştıracak olursak hata almayacağız. 

<br><hr>


## ***TABLOYA VERİ GİRMEK*** 


- Tabloya veri girmek için tekrardan ***.execute()*** metodundan faydalanacağız.

```py 
    im.execute(""" INSERT INTO TOWNS VALUES () """)
```

- ***INSERT INTO table_name VALUES*** verileri içine yerleştir demektir. içine yerleştir (***INSERT INTO***) ,(***table_name***) tablo adını temsil eder. ***VALUES*** de zaten veri demektir.

<br><hr>


## ***VERİLERİN İŞLENMESİ***

<br>

- Verileri eklemek yeterli değil verileri kayıt edebilmek için ***.commit()*** metodunu kullanmamız gerekir.

- ancak verileri kayıt etmek için veri tabanını atadığımız değişkenin adını kullanmalıyız. Örnekle deha iyi anlaşılacaktır.


```py
    import sqlite3 as db

    db = db.connect("db.sqlite")
    # veritabanı bağlantısı kurduk
    im = db.corsor()
    # imleç oluşturduk
    im.execute(""" CREATE TABLE IF NOT EXISTS Town (town_name , city) """)
    # tablo oluşturma (tabiki tablo yoksa)
    im.execute(""" INSERT INTO town VALUES ('iskenderun' , 'hatay') """)
    # veri ekleme işlemi (verileri tırank içine aldık)
    db.commit()
    # Bağlantı kurduğumuz değişkede commit metodunu uyguladığımıza dikkat edin
```

- ***.commit()*** metodunu çalıştırmazsak verileri eklemeyecektir.

<br> <hr>



## ***VERİTABANININ KAPATILMASI***


<br>

- Veritabanı ile işimiz bittiğinde kapatmamız gerekir. Bunu yapmamızın sebebi bilgisayar veya sunucudu gereksiz alan işgal etmesini önlemektir. Bunu prensip olarak da benimseyebilirsiniz, işimiz bitince kapatırız. Veritabanını kapatmak için kullandığımz metod ***.close()*** metodudur. bu metodu da bağlantı kurduğumuz değişekene tanımlarız. aynı kayıt işleminde yaptığımız gibi.

```py
    db.close()
```


<br> <hr>


## ***VERİLERİN ÇEKİLMESİ***

<br>

- Verileri çekebilmek için farklı yollar vardır. Nasıl veritabanı oluşturup veritabanına veri eklemek içi ***.execute()*** metodunu kullandıysak aynı şekilde verileri çekebilmek için de bu metodu kullanacağız.Çünkü bu metod sayesinde  SQL komutlarını işleyebiliyoruz.

<br>

### Tüm verilerin çekebilmek için : ***im.execute("""SELECT * FROM table_name""")*** metodunu kullanırız (im => imleci oluşturduğumuz değişkenin adı). * ile ilgili tabloadan (table_name) tüm verileri seçeriz.

<br>

- ***fetchall() :***  veritabanından seçtiğimiz verileri almak için kullanırız. Bu method imlecin bir metodudur Tam bir örnekle açıklamak gerekirse ;


```py
    import sqlite3 as db
    vt = db.connect("database.sqlite")

    im = vt.cursor()

    im.execute(""" CREATE TABLE IF NOT EXISTS town (id , town_name , city) """)

    im.execute(""" INSERT INTO town VALUES ("5" , " Erzin" , "Hatay") """)

    # bu kısma kadar verileri eklemiş olduk 

    im.execute("SELECT * FROM Town")

    tum_veriler = im.fetchall()

    vt.commit()
    vt.close()

    print(tum_veriler)
    >>> [('5', ' Erzin', 'Hatay')]
```
<br>


seçilen Tablodaki istediğimiz sütunun verilerini seçmek istersek * yerine ***sütun_adı*** ' nı yazarız

```py
    db = db.connect("database.sqlite") 

    im = db.cursor()

    im.execute("SELECT city FROM town")

    tek_getir = im.fetchall()

    print(tek_getir)
    db.close()
    >>> [('Hatay',), ('Hatay',), ('Hatay',), ('Hatay',), ('Hatay',), ('Hatay',)]
```
<br>

### TABLOLAR HAKKINDA BİLGİ EDİNMEK

<br>

- Bütün Sqlite veritabanlarında, ilgili veritabanının şemasını gösteren ‘sqlite_master’ adlı bir tablo bulunur.Bu tabloyu sorgulayarak veritabanı hakkında bilgi edinebiliriz.

```py
    import sqlite3 as db
    db = db.connect("database.sqlite")

    im = db.cursor()
    im.execute("SELECT name FROM sqlite_master")

    tablo_adlari = im.fetchall()

    db.commit()
    db.close()

    print(tablo_adlari)
    >>> [('town',)]
```

<br>

- ***fetchone() :***  Seçtiğimiz verilerin tek tek alınabilmesini sağlar. Bu fonksiyonda önemli olan kısım kaç kez çalıştırırsan o kadar getirir ve bir sonraki veriyi getirir bir örnekle açıklayalım
 
```py
    import sqlie3 as db
    db = db.connect("database.sqlite") 

    im = db.cursor()

    im.execute("SELECT * FROM town")

    tek_getir = im.fetchone()
    print(tek_getir)

    tek_getir = im.fetchone()
    print(tek_getir)

    tek_getir = im.fetchone()
    print(tek_getir)

    tek_getir = im.fetchone()
    print(tek_getir)

    tek_getir = im.fetchone()
    print(tek_getir)

    tek_getir = im.fetchone()
    print(tek_getir)

    # bu kısımda artık veri kalmadı ve none değerini dönerdi eğer veri tabanına veri ekleme veya çıkartma işlemi yapmadığınız sürece bunu görebilirsiniz . Kısacası eğer getirecek veri kalmazsa None değerini döndürür

    tek_getir = im.fetchone()
    print(tek_getir)

    db.close()

    >>> ('5', ' Erzin', 'Hatay')
        ('6', 'Payas', 'Hatay')
        ('6', 'Payas', 'Hatay')
        ('6', 'Payas', 'Hatay')
        ('6', 'Payas', 'Hatay')
        ('6', 'Payas', 'Hatay')
        None

```
<br>

- ***fetchmany() :*** Veritabanından seçtiğiniz verileri istediğin kadarını alabilme imkanı verir.

<br>

```py
    db = db.connect("database.sqlite") 

    im = db.cursor()

    im.execute(""" SELECT *  FROM town""")

    istenen_kadar = im.fetchmany(3)

    print(istenen_kadar)

    db.close()
    >>>[('5', ' Erzin', 'Hatay'), ('6', 'Payas', 'Hatay'), ('6', 'Payas', 'Hatay')]

    # Eğer veritabanında istenenden az sayıda değer varsa olan tüm verileri getirecektir.mesela 5 tane var 7 tane istedik 5 tanesini getirir hata vermez.(Kendim deneyimledim isterseniz siz de deneyebilirsiniz.)

```

# Verileri Süzmek

SQL komutlarını çalıştırmak için ***.execute()*** metodundan faydalanıyorduk. Şimdiye kadar tüm verileri ***seçmek*** , veya istenen tablodaki istenen sütündaki tüm verileri seçmeyi gördük. Yine ***.execute()*** metodunu kullanarak sql komutlarını işleteceğiz bu sefer tüm verileri seçmek değilde ***where*** sql komutunu kullanarak verileri filitrelemeyi öğreneceğiz.

<br>

```py
    im.execute("SELECT * FROM town WHERE city = 'Hatay'")
```
<br>

- yukarıdaki kodun türkçesi şu şekildedir. town tablosundaki tüm verilerden city sütünu "Hatay" olan kayıtları seç . Seçtiğimiz verileri almak için de ***.fetchall()*** metodundan yararlanabilriz.



```py
    db = db.connect("database.sqlite")

    im = db.cursor()

    im.execute(""" SELECT * FROM town WHERE city = "Hatay" """)
    # im.execute(""" SELECT * FROM town WHERE id = "5" """) # ör:2

    hatay_verileri = im.fetchall() 

    print(hatay_verileri)
    db.close()

    >>> [('5', ' Erzin', 'Hatay'), ('6', 'Payas', 'Hatay'), ('6', 'Payas', 'Hatay'), ('6', 'Payas', 'Hatay'), ('6', 'Payas', 'Hatay'), ('6', 'Payas', 'Hatay')]

```


<br><hr>

