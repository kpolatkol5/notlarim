# KALITIM (İNHERİTANCE)


<br>

Nesne tabanlı programlamaya ait bir kavram olan inheritance kavramı Temel sınıftan (base class) veya sınıflardan  istilenen özelliklerin , degerlerin metodların alt sınıflara aktarılmasıdır.  Bu sayede gereksiz ve tekrar eden kodlardan kurtulmuş olup daha okunabilir ve Don't Repeat Yourself felsefesine uyarak nesne tabanlı programlamayı kullanışlı ve faydalı bir programlama yaklaşımı haline getiren çok önemli bir kavramdır. Önceki derslerde kullandığımız örnekler üzerinden gidelim.

***Base class :***  Birkaç farklı sınıfta ortak olan nitelik ve metotları barındıran bir sınıf türüdür.

***Sub class  :*** Temel sınftan türeyen bütün sınıflara subclass (alt sınflar) denir. Alt sınıflar, kendilerinden türedikleri taban sınıfların metot ve niteliklerini miras yoluyla devralır.


<br>

```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani

    @classmethod
    def vergi_orani_guncelle(cls , yeni_oran):
        cls.vergi_orani = yeni_oran


    @classmethod
    def toplu_arac_ekle(cls ,data):
        eklenen_veriler = []

        for i in data:
           eklenen_veriler.append(cls(i["marka"], i["renk"], i["fiyat"], i["model"]))

        return eklenen_veriler

    @staticmethod
    def kok_al(deger):

        return deger ** 0.5
```

<br>

Örnekte de olduğu gibi bir araba sınıf tanımlamıştık. Bu sınıflarla aynı özellikte başka sınıflarda tanımlamamız gerektiğiniz varsayalım. Bu sınıf ortama 30 satırdan oluşuyor ve aynı özelliklerle 5 sınıf tanımlayacak olsak 150 satır kod yazmış olacağız. Fazla ve kendini tekrar eden kodlar yazmadan bu sınıftan alt sınıflar üretmek çok basittir bir örnkele açıklayalım.

<br>

```py
# Bir önceki örnekteki arabalar sınıfı referans alınmıştır.

class Sedan(Arabalar):
    pass



class SUV(Arabalar):
    pass


class Hatchback (Arabalar):
    pass

class Cabrio(Arabalar):
    pass
```

<br>

örnekte de olduğu gibi alt sınıflar tanımlamak bu kadar basit. parantezler arasına temel sınıfımızın adını yazıyoruz ve bir sonraki örnekte de alt sınıfalrımızı örnekleyelim ve şimdilik hiçbir şey tanımlamadık buna dikkat ederek aktarılan değişkenlere ve metodlara bakalım.

<br>

```py
print(dir(Sedan))

>>>  'kok_al', 'toplu_arac_ekle', 'vergi_orani', 'vergi_orani_guncelle', 'vergi_uygula', 'zam_orani', 'zam_uygula'
```


<br>

Oluşturduğumuz alt sınıfların hepsine dir() metodu ile bakabilirsiniz diğer oluşturduğumuz sınıflrada da bu metodların tanımlandığını görürsünüz. Bu metodların hepsi Temel sınıf olan Arabalar() sınıfından gelmektedir eğer bu sınıfa yeni metodlar ekleyip çıkartırsanız alt sınıflara da bu durum yanısyacaktır. Şimdi bu sınıfları birer kez örnekleyelim.

<br>

```py
sedan1  =   Sedan("mercedes", "beyaz", 120000, 2018)

suv1    =   Suv("kia", "siyah", 200000, 2020)

hatchback1  =   Hatchback("mazda", "mavi", 90000, 2019)

cabrio1 =   Cabrio("bmw", "turuncu", 190000, 2016)

print(dir(sedan1))


>>> 'fiyat', 'kok_al', 'marka', 'model', 'renk', 'toplu_arac_ekle', 'vergi_orani', 'vergi_orani_guncelle', 'vergi_uygula', 'zam_orani', 'zam_uygula'
```
 

<br>

Herhangi bir örneği dir metodu ile incelediğimizde de özelliklerin aynen aktarıldığını görebilirsiniz. Aynı durum diğer örnekler için de geçerlidir. Alt sınıflarda hiçbir şey tanımlamadık sadece hata almamak için pass değiminden faydalandık.

Sub classlar ile temel sınflardan nitelikleri ve metodlar koşulsuz şartsız devraldık . Ancak neden aldık aynı metodlar ve nitelikler olacaksa alt sınıfları oluşturmanın bir mantığı yok. Yani  miras alma mekanizmasının pek bir anlamı olmazdı.

Alt sınıflar tanımlarken temel sınıftaki ortak özellikleri alabilir ,  yeni özellikler ekleyebilir veya özellikleri yeniden tanımlayarak değiştirebiliriz. Eğer böyle bir durum söz konusu olmasaydı alt sınıfların hiçbir anlamı kalmayacaktı ve işlevsiz olacaktı. ALt sınıflarda tanımlanan yeni metodlar , değiştirilen metodlar **temel sınıfa yansımaz**. Bu değişiklikler sadece **ilgili alt sınıfta tanımlanmış olur**. Bir örnekle açıklayalım.

<br>

Temel sınıfımızı aynen yazdık
```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani

    @classmethod
    def vergi_orani_guncelle(cls , yeni_oran):
        cls.vergi_orani = yeni_oran


    @classmethod
    def toplu_arac_ekle(cls ,data):
        eklenen_veriler = []

        for i in data:
           eklenen_veriler.append(cls(i["marka"], i["renk"], i["fiyat"], i["model"]))

        return eklenen_veriler

    @staticmethod
    def kok_al(deger):

        return deger ** 0.5
```
<br>

Alt sınıf
```py


class Sedan(Arabalar):
    vergi_orani =   4.7

class Suv(Arabalar):
    vergi_orani =   4.2


class Hatchback (Arabalar):
    vergi_orani =   3.8

class Cabrio(Arabalar):
    pass


>>> 4.7
>>> 4.2
>>> 3.8
>>> 4.5
```


<br>

Örneklerde de olduğu gibi alt sınıflarda sınıf değişkenlerini değiştirdik. Bu değişiklikler temel sınıfa yansımadı ve Cabrio() sınıfında herhangi bir tanımlama yapmadığımız için ana sınıftan vergi oranı değerini aynen almış oldu. Peki işleyiş nasıl oluyor? 

Python yorumlayıcısı önce tanımladığımız alt sınıfın içerisine bakar. Eğer değerler değiştirilmemiş veya yeniden tanımlanmamış  ise temel sınıfa gider ve bu değerleri temel sınıftan alır. Buna işleyişe **method resolution order** (yöntem çözüm sırası) denir. Örnek üzerinden anlatacak olursak Sedan() sınıfımızın içerisinde **verigi_oranı** class niteliğini yeniden tanımladık.Bu sınıf niteliğinin aynısı temel sınıfta olduğu için temel sınıftaki değeri değiştirmek  istediğimizi algıladı ve tekrar bu değeri çağırmadı. Eğer farklı bir isimde bu vergi oranını tekrar tanımlayacak olsaydık hem tanımladığımız değer hem de temel sınıftaki değeri getirecekti. Bu durum alt sınıflarda  tanımlanan tüm metodlar ve nitelikler için geçerlidir. Özetleyecek olursak python yorumlayıcı ilk başta alt sınıfa bakar değerler değiştirilmemiş veya yeniden tanımlanmamış ise değerleri alt sınıfa aktarır. 

<br>


***KURAL :*** Eğer alt  sınıfa eklenen herhangi bir nitelik veya metod temel sınıfta da varsa alt sınıfta tanımlanan nitelik veya metodlar temel sınıftan gelecek olan nitelik veya metodların  yerine geçecektir.

<br> <br>



## ***Super() Fonksiyonuna Giriş***

<br>

Yukarıdaki kuralı referans alarak bir örnek daha yapalım. Bir temel sınıf bir de alt sınıfım var . Alt sınıfta herhangi bir tanımlama yapmadığım durumlarda veya alt sınıflarda temel sınıf ile aynı nitelik veya metotları tanımlamadığım durumlarda temel sınıftaki tüm özellikleri aynen alıabiliriyoruz. Tanımladığımız alt sınıflardan birinde , sınıfı her örneklediğimizde ayrıca aracın motor hacmi değerini alacağımızı da varsayalım. Bunun için tekrardan bir init fonksiyonu tanımlarsak temel sınıfta da aynı metod olduğu için alt sınıfta tanımladığımız init metodu daha baskın olacaktır. Bu durumda biz temel sınıfla aynı değerleri tekrardan almak zorunda kalıp kodlarımızı tekrar edeceğiz. Bu durum da nesne tabanlı programlamanın felsefesine aykırı bir durum. Önce bahsettiğimiz örneği verelim daha sonra da çözğmnü inceleyeceğiz.


<br>

***Temel Sınıf***
```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani

    @classmethod
    def vergi_orani_guncelle(cls , yeni_oran):
        cls.vergi_orani = yeni_oran


    @classmethod
    def toplu_arac_ekle(cls ,data):
        eklenen_veriler = []

        for i in data:
           eklenen_veriler.append(cls(i["marka"], i["renk"], i["fiyat"], i["model"]))

        return eklenen_veriler

    @staticmethod
    def kok_al(deger):

        return deger ** 0.5
```

<br>

***Alt Sınıf***

```py
class Sedan(Arabalar):
    vergi_orani =   4.7

    def __init__(self, marka, renk, fiyat, model , motor_hacmi):

        self.marka          =   marka
        self.renk           =   renk
        self.fiyat          =   fiyat
        self.model          =   model
        self.motor_hacmi    =   motor_hacmi


sedan1  =   Sedan("bmw", "beyaz", 120000, 2000, 1597)


print(sedan1.zam_uygula())
print(sedan1.marka)
print(sedan1.motor_hacmi)

>>> 180000.0
>>> bmw
>>> 1597
```

<br>

Örnekte de olduğu gibi alt sınfıta init fonksiyonunu tekrar tanımladık ve temel sınıftaki init fonksiyonunu ezdi. Ancak zam uygula metodunu tekrar tanımlamadık bu metodu aynen aldı ve bize zamlı fiyatını göstermiş oldu. Peki alt sınıfları her örneklediğimizde temel sınıftan farklı olarak yeri değerler eklemek istiyoruz ancak kendini tekrar eden kodlardan da kaçınmak istersek. super() fonksiyonunu kullanabiliriz. Önce super fonksiyonunun nasıl çalıştığını ve alternatif yolunu gösterelim daha sonra super fonksiyonunun kullanımını gösterelim. Temel sınıf aynı sadece alt sınıfı terkrar örnek vereceğim.


<br>


***Alt Sınıf***
```py
class Sedan(Arabalar):
    vergi_orani =   4.7

    def __init__(self, marka, renk, fiyat, model , motor_hacmi):
        Arabalar.__init__(self, marka, renk, fiyat, model)

        self.motor_hacmi    =   motor_hacmi

sedan1  =   Sedan("bmw", "beyaz", 120000, 2000, 1597)
sedan2  =   Sedan("mazda", "mavi", 140000, 2019, 1597)


print(sedan1.zam_uygula())
print(sedan1.marka)
print(sedan1.motor_hacmi)

print("sınfımızı ikinci kez örnekledik ")

print(sedan2.zam_uygula())
print(sedan2.marka)
print(sedan2.motor_hacmi)

>>> 180000.0
>>> bmw
>>> 1597
>>> sınfımızı ikinci kez örnekledik 
>>> 210000.0
>>> mazda
>>> 1597
```


<br>


Örnkete de olduğu gibi init fonksiyonunu alt sınıfta tekrar tanımladık ve temel sınıftaki init fonksiyonunu buraya tekrar çağırırsak (alt sınıftaki init fonksiyonunun içerisine) ***temel sınıftaki tanımlamaları tekrar yapmamıza gerek kalmadı***. Temel sınıfta *marka , renk , fiyat , model* gibi tanımlamaları ***alt sınıfta tekrar init fonksiyonu tanımlamamıza rağmen*** aldı ve ***temel sınıftan farklı olarak init fonksiyonuna yeni parametrelerimizi tanımlamış olduk***.


Yukarıdaki örneği şu şekilde de tanımlayabilirdik.

<br>

```py
class Sedan(Arabalar):
    vergi_orani =   4.7

    def __init__(self, marka, renk, fiyat, model , motor_hacmi):

        super().__init__(marka, renk, fiyat, model)
        self.motor_hacmi    =   motor_hacmi


sedan1  =   Sedan("bmw", "beyaz", 120000, 2000, 1597)
sedan2  =   Sedan("mazda", "mavi", 140000, 2019, 1597)


print(sedan1.zam_uygula())
print(sedan1.marka)
print(sedan1.motor_hacmi)

print("sınfımızı ikinci kez örnekledik ")

print(sedan2.zam_uygula())
print(sedan2.marka)
print(sedan2.motor_hacmi)

>>> 180000.0
>>> bmw
>>> 1597
>>> sınfımızı ikinci kez örnekledik 
>>> 210000.0
>>> mazda
>>> 1597
```
<br>

Örnekte sadece temel sınıfın adını sildik onun yerine super() yazdık ve init fonksiyonunun içeirisndeki self değimini sildik. İkisi de aynı işi yapar. Ancak ileri düzey sınıflar yazıldığında veyaçok boyutlu sınıflar yazıldığında super fonksiyonunu kullanamk daha doğru bir seçim olacaktır.

<br>

## ***Super fonksiyonu ne işe yarar?*** 


Bu fonksiyon ***miras alınan temel sınıfa*** atıfta bulunarak ***temel sınıftaki nitelik ve metodlar*** üzerinde değişiklik yaparken ***mevcut özellikleri de muhafaza edebilmemizi sağlar***. Örnekte de olduğu gibi temel sınıfımızdaki init fonksiyonunun özelliklerini alt sınıfa da aynen aktarmış olduk. Eğer yeni değerler eklemek istersek aynı kodları tekrar etmeden eklemek istediğimiz yeni değerleri ekleyebiliriz.


<br>


## ***Super fonksiyonun Sırası Önemlidir.*** 

<br>

Bunu direkt bir örnekle açıklayalım.

<br>

***Kısaltılmış Temel Sınıf***
```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

        print("temel sınıftaki init metodu çalıştı")
```

<br>

***Alt Sınıf***
```py
class Sedan(Arabalar):
    vergi_orani =   4.7

    def __init__(self, marka, renk, fiyat, model , motor_hacmi):

        super().__init__(marka, renk, fiyat, model)
        self.motor_hacmi    =   motor_hacmi
        print("alt sınıftaki init metodu çalıştı")

sedan1  =   Sedan("bmw", "beyaz", 120000, 2000, 1597)

>>> temel sınıftaki init metodu çalıştı
>>> alt sınıftaki init metodu çalıştı
```

<br>

Burada alt sınıfı örneklendirdik. Alt sınfıta init metodu çalıştı ve super fonksiyonu sayesinde temel sınıfa atladı ve oradaki init metodu çalıştı. Marka renk fiayt , model örnek nitelikleri tanımlandı ve tekrar temel sınıfımızdaki init fonksiyonumuzun içerisindeki print fonksiyonu çalıştı. Daha sonra kodlar okunmaya devam edildi alt sınıftaki örnek niteliği olan  motor hacmi tanımlandı daha sonra print fonksiyonu çalıştı. Peki biz aracın marka ismini ve fiyatını yazdıracak olsak ve bunu super fonksiyonundan önce tanımlasak nasıl bir sonuçla karşılaşırız. 

<br>

***Temel Sınıf***
```py

class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5

    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

        print(f"temel sınıftaki init metodu çalıştı : {self.marka} {self.fiyat}")
```


 
***Alt Sınıf***
```py
class Sedan(Arabalar):
    vergi_orani =   4.7

    def __init__(self, marka, renk, fiyat, model , motor_hacmi):
       
        print(f"alt sınıftaki init metodu çalıştı : {self.marka} {self.fiyat}")

        super().__init__(marka, renk, fiyat, model)
        self.motor_hacmi    =   motor_hacmi

sedan1  =   Sedan("bmw", "beyaz", 120000, 2000, 1597)

>>> AttributeError: 'Sedan' object has no attribute 'marka'
```

Örnekte de olduğu gibi hata aldık. Super fonksiyonu temel sınıfa atlar ve oradaki init fonksiyonunu çalıştırır ve bu şekilde biz alt sınıftan örnek niteliklerine ulaşabiliriz. super fonksiyonunun tanımlandığı sıraya dikkat edersek olası hataların önüne geçmiş oluruz. 

<br>



## ***Bilmeniz Gerekiyor***

<br>

***isinstance(nesne , sınıf) :*** Bu fonksiyon iki parametre alır. İlk parametre nesne ikinci parametre ise sınıfı temsil eder. Eğer ilk parametrede verilen nesne ikinci parametre ile verilen sınıftan üretilmişse geriye True değerini döndürür.

<br>

```py
print(isinstance(sedan1, Sedan))

>>> True
```

<br>


***issubclass(alt_sınıf , temel_sınıf) :*** Bu fonksiyon da iki parametre alır. İlk parametre alt sınıfları temsil eder ikinci parametre ise temel sınıfları. Eğer ilk parametre ile verilen sınıf ikinci parametre ile verilen sınıftan miras alınmışsa geriye True değerini döndürür.


<br>


```py
print(issubclass(Sedan, Arabalar))

>>> True
```
