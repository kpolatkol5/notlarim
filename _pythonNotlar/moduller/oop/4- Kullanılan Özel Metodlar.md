# ***Dunder & Magic Methods (Sihirli Metodlar)***

Dunder methotlar __ ile başlar ve biter. Sihirli metod olarak da bilinir. 

pythonthon da bir sınıf yazdığımızda bu sınıf varsayılan olarak pythonthonda tanımlanmış bir sınıftan miras alır. Eski yöndetm ile pythonthon da bir sınıf oluşturuken Object sınıfından miras alınması gerekiyordu.pythonthon3 'den itibaren artık oluştruduğumuz sınıflar yeni tip sınıflar olduğu için Object sınıfını belirtmemize gerek yok.

**Eski yöndem**
```python
Arabalar(objects)
```

Bir de kalıtım notlarında da bahsetmiştik. pythonthon da method resolution order kavramı vardı. Tanımladığımız nitelikler veya metodlar önce tanımladığımız sınıfa daha sonra miras alınan temel sınıfa bu ikisinde de yok ise pythonthonda tanımlanmış Sınıflara bakardı (builtins.object).
Yani bizim tanımladığımız her sınıf aslında pythonthonda tanımlanmış olan sınıfların üzerine tanımlanıyor. method resolution order 'da bunu gördük en son builtins.objects 'e bakıyor.

Bu da demek oluyor ki biz pythonthonda tanımlanan ve sürekli kullandığımız methodları keni sınıflarımızda da kullanabiliriz. Mesela toplama işlemi yapabilmek için ***\_\_add__(self, anotherObj)*** sihirli metodunu kullanabiliriz. Bu sürekli kulladnığımız ***+ operatörünün*** yaptığı işi yapar.

Sadece biz bu işlemleri sayılar üzerinden yapıyorduk veya string metodlarda yaptığımız farklı işlemler var. Biz kendi sınıfımızda da nesneleri toplama , çıkartma bölme gibi işlemleri hızlıca yapabileceğiz. Mesela iki adet objeyi toplamaya çalışsak hata alırız , ancak biz sınıfımızda add metodunu tekrar tanımlarsak bu hatayı almayız ve objeler ile işlem yaptığımzda istediğimiz sonucu daha kısa sürede alabilriz. Şimdilik kafanızda bir şeyler oturduysa birazdan bol örnekle ne demek istediğimi daha iyi anlayacaksınız.

Bir sınıf oluşturduğumuzda init fonksiyonunu kullanmıştık. Bu metod aslında bizim kullandığımız ilk dunder metod.

Şimdi bir nesne oluşturlım ve bu nesneyi konsolda yazdırmaya çalışalım.
## ***_\_str__()*** :


```python
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model


araba1  =   Arabalar("bmw", "beyaz", "120000", "2019") 
print(araba1)

>>> <__main__.Arabalar object at 0x0000029EFD179308>
```

Örnekte de olduğu gibi oluşturduğumuz nesneyi ekrana yazdırdığımızda hafızada depolandığı adresi geriye döndürdü. Bunu çıktı okunabilir değil ve biz dunder metodlarla bunları okunabilir yapabiliriz.

```python
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model


    def __str__(self):
        return self.marka


araba1  =   Arabalar("bmw", "beyaz", "120000", "2019") 
print(araba1)

>>> bmw
```

***\_\_str__()***  metodunu kullanarak oluşturduğumuz örneği daha okunabilir hale getirdik.



## ***_\_repr__()*** :

str fonksiyonu ile aslında benzer işleri yapıyorlar. Eğer str metodunu kullanmazsak pythonthon yedek olarak bu metodun içerisine bakacaktır. repr metodu daha çok örnkelerin sınflardan nasıl oluştuğunu aldığı argümanları bize açıklama olarak verebilmesi için tanımlarız. Mesela kodalrımzdan baya ilerledik ve örneklerin aldığı argümanlara bakmamız gerekiyor. Kısaca nesneleri nasıl oluşturduğumuzu geriye döndürmek için kullanıyoruz.

```python
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

    def __repr__(self):

        return f"Arabalar('{self.marka}', '{self.renk}', '{self.fiyat}', '{self.model}'))"


araba1  =   Arabalar("bmw", "beyaz", "120000", "2019") 

print(araba1)

>>> Arabalar('bmw', 'beyaz', '120000', '2019')
```

Örnkte de olduğu gibi artık nesneyi yazdırmaya çalıştığımızda bize o nesnenin nasıl oluştuğunu gösteriyor. repr metodu daha çok diğer geliştiriciler veya kendimiz için kullanırız. Str ise daha çok kullanıcının daha iyi okuması veya bizim daha okunabilir verilere ulaşmamız için kullanırız. Son kullanıcı için de denilebilir.

Repr metodunu str metodu ile kullandığımızda ilk başta str metoduna bakacaktır ve str metodundaki veriyi bize gösterecektir . Eğer repr metodundaki verilere de ulaşmak istersen help metodundan faydalanabilirsin. Oluşturduğumuz sınıfın en başına üç tırnak ile (""") yorum satırı ekleyebilir sınıf hakkında bilgiler verebilirsin. Ayrıca help metodu ile repr aracılığı ile ulaşmak istediğimiz verileri de orda görüntüleyebiliriz.

```python
class Arabalar():
    """
    Bu sınıf ile ilgili açıklamalarımızı buraya yazabiliriz
    sınıf hakkında bilgiler vererek hem help metodunu kullanarak bu
    açıklamlara ulaşabiliz hem de repr metodu ile örneklerin nasıl oluştuğunu
    görüntüleyebilriz 
    """
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model


    def __repr__(self):

        return f"Arabalar('{self.marka}', '{self.renk}', '{self.fiyat}', '{self.model}')"


araba1  =   Arabalar("bmw", "beyaz", "120000", "2019") 

print(help(araba1))


>>> Help on Arabalar in module __main__ object:
>>> 
>>> class Arabalar(builtins.object)
>>>  |  Arabalar(marka, renk, fiyat, model)
>>>  |
>>>  |  Bu s²n²f ile ilgili a²klamalar²m²z² buraya yazabiliriz
>>>  |  s²n²f hakk²nda bilgiler vererek hem help metodunu kullanarak bu
>>>  |  a²klamlara ula■abiliz hem de repr metodu ile ÷rneklerin nas²l >>> olu■tu­unu
>>>  |  g÷r³nt³leyebilriz
>>>  |
>>>  |  Methods defined here:
>>>  |
>>>  |  __init__(self, marka, renk, fiyat, model)
>>>  |      Initialize self.  See help(type(self)) for accurate signature.
>>>  |
>>>  |  __repr__(self)
>>>  |      Return repr(self).
>>>  |
>>>  |  ----------------------------------------------------------------------
>>>  |  Data descriptors defined here:
>>>  |
>>>  |  __dict__
>>>  |      dictionary for instance variables (if defined)
>>>  |
>>>  |  __weakref__
>>>  |      list of weak references to the object (if defined)
>>>  |
>>>  |  ----------------------------------------------------------------------
>>>  |  Data and other attributes defined here:
>>>  |  
>>>  |  vergi_orani = 4.5
>>>  |
>>>  |  zam_orani = 1.5
```

# ***Kullanılan Dİğer Metotların Bağzıları***


Tanımlamalar bu şekilde tüm metodlara dökümantasyondan araştırabilirsiniz. Aşağıda en çok kullanılan sihirli metodların listesini yazacağım inceleyip kendi sınıflarınıza ekleyebilirsiniz.
## ***_\_lt__(self, anotherObj) :*** 


***< operatörü için kullanılır.***


## ***_\_le__(self, anotherObj) :*** 


***<= operatörü için kullanılır***


## ***_\_eq__(self, anotherObj) :*** 


***== operatörü için kullanılır.***

## ***_\_ne__(self, anotherObj) :*** 


***!= operatörü için kullanılır.***


## ***_\_gt__(self, anotherObj) :*** 


***\> operatörü için kullanılır.***

## ***_\_ge__(self, anotherObj) :*** 


***\>= operatörü için kullanılır***

## ***_\_add__(self, anotherObj) :*** 


***+ operatörü için.***
## ***_\_sub__(self, anotherObj) :*** 


***için - nesne üzerinde işlem.***

## ***_\_mul__(self, anotherObj) :*** 


***nesne üzerinde * işlemi için.***
## ***_\_matmul__(self, anotherObj) :*** 


***@ operatörü için (sayısal matris çarpımı).***

## ***_\_truediv__(self, anotherObj) :*** 

***nesne üzerinde basit / bölme işlemi için.***

## ***_\_floordiv__(self, anotherObj) :*** 


***// nesne üzerinde kat bölme işlemi için.***

## ***_\_len__(self, anotherObj) :*** 


***len() fonksiyonu için.***

## ***_\_delitem__(self, key) :*** 


***del() işlev için . Dizindeki değeri silin key.***
## ***_\_abs__(self) :*** 

***abs() işlevi için destek olun. Mutlak değer döndür.***

## ***_\_int__(self, key) :*** 


***int(). Nesnenin tamsayı değerini döndürür.***

## ***_\_float__(self) :*** 


***float() Nesnenin kayan nokta eşdeğerini döndürür.***
