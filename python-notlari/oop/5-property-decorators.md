# ***Property Decorator***

<br>

Property benzeyicisinin yaptığı en temel iş bir metodu nitelik gibi kullanabilmemizi sağlamasıdır. Yazdığımız sınıflarda bazen mantıksal hatalarla karşılaşabiliriz. Mesela sınıfımızda örnek nitelikleri tanımladık. Daha sonradan bu örnek nitelikler üzerinden değişiklik yaptığımzıda tanımladığımız nitelikler düzgün çalışmayabilir. Bunun önüne geçmek için python da property değimi kullanılır. Örneklerle açıklayalım.

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil
        self.kullanim   =   f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 ,2022)

print(araba1.kullanim)

>>> Bu arac 3 yıldır kullanılıyor.
```

<br>

Yukarıdaki örnekte aracın kaç yıldır kullanıldığını gösteren bir örnek niteliği tanımladık. Varsayalım ki aracın modelini yanlış girdik ve daha sonradan değiştirmeye kara verdik.

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil
        self.kullanim   =   f"Bu arac {2022 - int(self.model)} yıldır kullanılıyor."



araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 , 2022)
print(araba1.kullanim)

araba1.model    =   2005

print(araba1.model)
print(araba1.kullanim)

>>> Bu arac 3 yıldır kullanılıyor.
>>> 2005
>>> Bu arac 3 yıldır kullanılıyor.
```

<br>

Örnekte de olduğu gibi aracın modelini daha sonradan güncelledik ancak aracın kaç yıl kullanıldığını söyleyen örnek niteliğinde hata ile karşılaştık. Eğer bunu örnek niteliği değil de örnek metodu olarak kullanamaya çalışsaydık.

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil


    def arac_kullanim(self):
        return f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 , 2022)
print(araba1.arac_kullanim())

araba1.model    =   2005

print(araba1.model)
print(araba1.arac_kullanim())

>>> Bu arac 3 yıldır kullanılıyor.
>>> 2005
>>> Bu arac 17 yıldır kullanılıyor.
```

<br>

Örnkete de olduğu gibi sorunu çözdük gibi görünüyor ancak biz örnek metodlarını çağırmadan işlem yapmaz. Örnek motodlar hafızada tutulmaz çağırıldığı zaman ilgili değerleri alır ve işlemi yaptıktan sonra verileri geriye döndürür. Örnek niteliklerinde de durum böyle değil. Örnek nitelikleri sınıf örneklendiğinde çalıştığı için sonradan değerleri değiştirmeye çalıştığımızda böyle hatalar alabiliriz. Bu durumda bizim yapmamız gereken işlem tanımladığımız örnek metodların örnek niteliği gibi çalışmasını sağlamak.Peki neden bunu yapıyoruz sebebi de biz bu örnek metodunu her kullandığımızda tetiklememiz gerekiyor. Bunun için örnek metodlarını örnek niteliğiymiş gibi kullanmalıyız. işte tam da burada ***@property***değimindenn faydalanıyoruz. Örnekle açıklayalım.

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model ,yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil

    @property
    def arac_kullanim(self):
        return f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."

araba1  =   Arabalar("bmw", "beyaz", "120000", 2019, 2022)

araba1.model    =   2005

print(araba1.arac_kullanim)

>>> Bu arac 17 yıldır kullanılıyor.
```

<br>

Örnekte de olduğu gibi property tanımlaması yaptık ve artık bu metod örnek niteliğiymiş gibi çalışıyor. Bu tanımladığımız property'de çağırdığımızda parantez kullanmadğımıza dikkat edin.


<br>

 ## ***Değer Atamak (Setter)***

<br>

Örnek metodlarını tanımlarken örnek niteliğiymiş gibi  davranmasını ***@property*** değimi ile sağladık ancak olası bir sorun daha var. Örnek niteliğiymiş gibi tanımladığımız örnek metodlar üzerinden tanımlama yapmaya çalışırsak hata alacağız. örnekle açıklayalım.

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil


    @property
    def arac_kullanim(self):
        return int(self.yil) - int(self.model)



araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 , 2022)
araba1.model    =   2005
print(araba1.arac_kullanim)

araba1.arac_kullanim    =   13

>>> 17
>>> AttributeError: can't set attribute
```

<br>


Örnekte de olduğu gibi property ile tanımladığımız metodu tekrardan tanımlamaya çalıştığımızda hata aldık. Burada hata almamız çok normal çünkü hangi veriyi değiştireceğini bilmiyor. Bu verileri de değiştirmek için setter tanımlamasını kullanmamız gerekiyor. Örneklerle açıklayalım

<br>

```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil


    @property
    def arac_kullanim(self):
        return int(self.yil) - int(self.model)


    @arac_kullanim.setter
    def arac_kullanim(self , yil):

        self.model  =  self.yil - yil

        print( f"aracın model bilgisi değiştirildi, güncel model : {self.model}")


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 , 2022)
araba1.model    =   2005
print(araba1.arac_kullanim)
print(araba1.model)

print("----------------------------------")
araba1.arac_kullanim    =   13
print(araba1.model)

>>> 17
>>> 2005
>>> ----------------------------------
>>> aracın model bilgisi değiştirildi, güncel model : 2009
>>> 2009
```

<br>

yukarıdaki örnekte ne yaptığımızı anlatalım. Setter parametresini kullanabilmemiz için @ işareti ile beraber ilgili fonksiyonun adını yazarız ve daha sonra setter parametresini ekleriz
```py
    @arac_kullanim.setter
    def arac_kullanim(self , yil):
```
daha sonra tekrardan ilgili fonksiyonun adı ile fonksiyon tanımlarız. Bu fonksiyonun fazladan 1 parametre aldığına dikkat edin. Bu parametre property ile tanımladığımız metodu tekrar yeni değer ile tanımlamaya çalıştığımızda değiştirilecek olan değeri temsil ediyor yani;

```py
araba1.arac_kullanim    =   13
```
yani burada gönderdiğimiz 13 değeri setter fonksiyonuma gönderdiğimiz argüman oluyor. Bu fonksiyonda argüman olarak göderdiğimiz değeri işleyerek ilgili örnek değişkenlerinin değerlerini güncelleyeceğiz. Biz bu tanımlama ile aracın 13 yıl kullanıldığını belirtiyoruz dolayıısyla aracın model bilgisinin de değişmesi gerekir. 


```py
 @arac_kullanim.setter
    def arac_kullanim(self , yil):

        self.model  =  self.yil - yil

        print( f"aracın model bilgisi değiştirildi, güncel model : {self.model}")
```

Şuanki yıldan aracın kaç yıl kullanıldığıbilgisini çıkartırsak model bilgisini bize verecektir. Daha sonra model bilgisini tekrar tanımlşayarak değerini değiştiriyoruz.

İlk örneğe tekrar bakarsanız aracın model bilgisinin de değiştiğini görebilirsiniz.


<br>


 ## ***Değer silmek (deleter)***

<br>

setter parameteresi ile neredeyse aynı kullanıma sahip direk örnek üzerinden anlatalım.

<br>


```py
class Arabalar():

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil


    @property
    def arac_kullanim(self):
        return int(self.yil) - int(self.model)


    @arac_kullanim.setter
    def arac_kullanim(self , yil):

        self.model  =  self.yil - yil

        print( f"aracın model bilgisi değiştirildi, güncel model : {self.model}")

    @arac_kullanim.deleter
    def arac_kullanim(self):

        self.model  =  None

        print( f"aracın model bilgisi değiştirildi, güncel model : {self.model}")


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 , 2022)
araba1.model    =   2005


print(araba1.arac_kullanim)
print(araba1.model)

del araba1.arac_kullanim

print(araba1.model)
```


<br>

deleter kulladığımızda değerleri sileceğimiz için parametre almasına gerek yok . Sadece dikkat etmemiz gereken kısım hangi metot da tanımlanmışsa nesne üzerinden o metodu çağırıyoruz ve ***del*** değimi ile beraber kullanmamız gerekiyor

```py
del araba1.arac_kullanim
```

Aracın model bilgisi ***None*** olarak güncellenecektir.