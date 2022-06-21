# ***SINIF METODLARI***

Sınıf methodları nesne değişkenleri yani örnek niteliklerine bağımlı olmadan işlem yapan ancak anlam bakımından sınıfla ilişkili olduğu için sınıftan atamayacağımız fonksiyonlardır. Daha önceki örneklerde sınıf değişkenleri ile örnek değişkenleri arasındaki farkı anlatmıştık. Sınıf değişkenlerine örnekler üzerinden erişmenin tehlikeli olduğundan bahsettik. Hem yazdığımız kodun okunabilirliğini arttırmak hem de olası hataların önüne geçebilmek için sınıf niteliklerine sınıf adları üzerinden erişiyorduk. Ayrıca sınıf değişkenleri tüm örneklere aynen aktarıldığını ve değerlerin tüm nesnelerde aynı olduğunu da hatırlayalım. Eğer sınıf değişkenimiz değiştirilemeyecek veri tiplerinden ise (**integer , string , demet gibi**) bu değerleri değiştirmek için kendimiz oradaki değeri silip yeni değeri yazmamız gerekiyordu veya yeniden tanımlamak gerekiyordu. Eğer bu değerleri nesneler üzerinden değiştirmeye çalışsak bile sadece o nesneden değiştiğini geriye kalan nesneler ile daha sonradan eklenecek olan nesnelere yine eski değerin aktarıldığını hatırlayın ve hatta bir örnkele hatırlamaya çalışalım.

<br>

```py
class Arabalar():
    marka   =   "toyota"
    renk    =   "kırmızı"
    fiyat   =   100000


araba1  =   Arabalar()
araba2  =   Arabalar()


print(araba1.fiyat , araba1.marka , araba1.renk)
print(araba2.fiyat , araba2.marka , araba2.renk)

>>> 100000 toyota kırmızı
>>> 100000 toyota kırmızı
```

<br>

örnekte olduğu gibi sınıf değişkenleri oluşturduk ve bu iki nesnedeki değerler aynı şimdi nesne üzerinden herhangi bir değer değiştirelim.

<br>

```py
class Arabalar():
    marka   =   "toyota"
    renk    =   "kırmızı"
    fiyat   =   100000


araba1  =   Arabalar()
araba2  =   Arabalar()

araba1.renk =   "mavi"
# ilk nesnemizin rengini değiştirdik 

print(araba1.fiyat , araba1.marka , araba1.renk)
print(araba2.fiyat , araba2.marka , araba2.renk)


print("---------------------------------")
print("sınıfı örneklendirdik")

araba3  =   Arabalar()
#  yeni bir nesne ekledik 

print(araba1.fiyat , araba1.marka , araba1.renk)
print(araba2.fiyat , araba2.marka , araba2.renk)
print(araba3.fiyat , araba3.marka , araba3.renk)

>>> 100000 toyota mavi
>>> 100000 toyota kırmızı
>>> ---------------------------------
>>> sınıfı örneklendirdik
>>> 100000 toyota mavi
>>> 100000 toyota kırmızı
>>> 100000 toyota kırmızı
```

<br>

örnekte de olduğu gibi herhangi bir nesne üzerinden rengi değiştirdik ancak bu değişiklik diğer nesnelere de yeni oluşturulacak olan nesnelere de yansımadı. Eğer bu değişikliğin tüm nesnelere yansımasını istersek sınıf metodlarını kullanabilirz. Yapacağımız işlem kısaca sınıf değişkenlerini yeniden tanımlamak ve değerlerini değiştirmek olsun.


<br>

```py
class Arabalar():
    marka   =   "toyota"
    renk    =   "kırmızı"
    fiyat   =   100000

araba1  =   Arabalar()
araba2  =   Arabalar()

print(araba1.marka)
print(araba2.marka)

Arabalar.marka  =   "Ford"


print("yeni bir örnek oluşturalım")
araba3  =   Arabalar()

print(f"yeni oluşturduğumuz nesnenin markası : {araba3.marka}")

print("tüm örneklerdeki değerleri inceleyelim ")

print(araba1.marka)
print(araba2.marka)
print(araba3.marka)


>>> toyota
>>> toyota
>>> yeni bir örnek oluşturalım
>>> yeni oluşturduğumuz nesnenin markası : Ford
>>> tüm örneklerdeki değerleri inceleyelim
>>> Ford
>>> Ford
>>> Ford
```

<br>

## ***ÖNEMLİ!!***
Örnekte de olduğu gibi sınıf değişkenleri oluşturduk. Önceden oluşturduğumuz nesnelerin marka değerleri toyotaydı. Daha sonra Sınıf adı üzerinden sınıf değişkenine ulaşarak toyota değerini ford ile değiştirdik. Daha sonra yeni bir örnek oluşturduk ve bu yeni oluşturduğumuz nesnenin markası artık ford. Daha sonra önceden tanımladığımız nesnlerin de markasına baktığımız zaman onların da marka değerleri ford ile değiştirildiğini görebilirsiniz. Yani kısacası sınıf değişkenlerinin değerlerini değiştirebiliyoruz ve değiştirdiğimiz zaman sınıftan türetilen tüm nesneler için bu değer değişiyor. Peki bu değeri her değiştirmek istediğimzide tek tek gelip burda yeniden tanımlama yapmak yakışmazdı. Kod kirliliğine yol açacak ve daha sonradan okumaya kalktığımızda belki yazdığımız kodları okuayamayacağız bile. İşte tam burda classmethod devreye giriyor. Sınıf içerisinde tanımladığımız ve sınıfı ilgilendiren metodlardır bunlar. Örnek metodlarından tek farkı budur. Örnek metodları örnekler ile ilgilenirken sınıf metodları sınfıın genelini ilgilendirir.

<br>

```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani


araba1  =   Arabalar("toyota", "kırmızı", 100000)

print(f"aracın fiyatı             : {araba1.fiyat}")
print(f"aracın zamlı fiyatı       : {int(araba1.zam_uygula())}")
print(f"aracın vergi dahil fiyatı : {int(araba1.vergi_uygula())}")

>>> aracın fiyatı             : 100000
>>> aracın zamlı fiyatı       : 150000
>>> aracın vergi dahil fiyatı : 675000
```

<br>

yukarıdaki örnekte aracın zam ve vergi oranlarına göre yeni fayatlarının hesaplanması için örnek metodlar tanımladık. Bu örnek metodaların her nesne için ayrı ayrı oluşturulduğunu biliyoruz. yani yeni oluşturulacak olan nesnlerdeki araç fiyatları farklı olabilir ancak zam ve vergi oranları sabit. Söyle bir senaryo yazalım ekonomik krizden dolayı vergi fiyatları düşürüldü zam oranı sabit kaldı. Haliyle sınıf değişkeni olan verigi oranını bizim değiştirmemiz gerek bunun için de sınıf metodu tanımlamalıyız.bir sonraki örnektre sınıf metodu tanımlayalım.

<br>

```py
class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani

    @classmethod
    def vergi_orani_guncelle(cls , yeni_oran):
        cls.vergi_orani = yeni_oran



araba1  =   Arabalar("toyota", "kırmızı", 100000)

print(f"aracın fiyatı             : {araba1.fiyat}")
print(f"aracın zamlı fiyatı       : {int(araba1.zam_uygula())}")
print(f"aracın vergi dahil fiyatı : {int(araba1.vergi_uygula())}")

print("-------------------------------------------------")

print("vergi oranını değiştirelim")

Arabalar.vergi_orani_guncelle(4.0)

print(f"aracın fiyatı             : {araba1.fiyat}")
print(f"aracın zamlı fiyatı       : {int(araba1.zam_uygula())}")
print(f"aracın vergi dahil fiyatı : {int(araba1.vergi_uygula())}")


>>> aracın fiyatı             : 100000
>>> aracın zamlı fiyatı       : 150000
>>> aracın vergi dahil fiyatı : 675000
>>> -------------------------------------------------
>>> vergi oranını değiştirelim
>>> aracın fiyatı             : 100000
>>> aracın zamlı fiyatı       : 150000
>>> aracın vergi dahil fiyatı : 600000
```

<br>

Şimdi örnekte de olduğu gibi önceki iki örnek arasındaki tek fark classmethod tanımladığımız kısım. Bu yapıyı ayrıntılı inceleyelim.

***@classmethod*** *decorator* tanımlaması ile beraber hemen altına sınıf metodumuzu tanımlarız. Bu decoratör bir sonraki yazacağımız fonksiyonun bir sınıf metodu olduğunu makinaya bildirmemizi sağlıyor

***vergi_orani_guncelle()*** fonksiyonunu tanımladık ancak bu parantezler arasına ***ne gelecek neden cls yazdık*** bu kısım önemli.

Eğer parantezler arasına self koysaydık bu örnek metodu olacaktı. Biz sınıf metodu tanımlamak istiyoruz. Bunun için sınıfı işaret edecek bir tanımlama yazarız. direkt class yazarsak hata alırız çünkü bu tanımlama sınıf oluşturmak için kullandığımız bir tanımlama. Bir gelenek olarak class değiminin kısaltması olarak ***cls*** kullanırız. self ile cls arasındaki fark da bu ***self her bir örneği temsil ederken cls sınıfın kendisini temsil ediyor.***

Daha sonra ise fonskiyonda şu tanımlamayı kullanmışız.
```py
@classmethod
def vergi_orani_guncelle(cls , yeni_oran):
    cls.vergi_orani = yeni_oran
```
Burada ***vergi_orani  = yeni_oran*** şeklinde tanımlasaydık hata alırdık. Burada cls değimini kullanmamızdaki ***amaç makinaya sınıf değişkeninin yerini net bir şekilde belirtmemiz gerekiyor***. cls zaten sınıfı temsil ediyordu ***cls.vergi_orani*** tanımlaması ile sınıf değişkeninin yerini net bir şekilde belirtmiş olduk. Fonksiyonun ikinci parametresi kullanıcı tarafından veya bizim tarafımızdan gönderilecek olan yeni zam oranıdır. Sınıf değişkenindeki zam oranını bizim belirlemiş olduğumuz yeni zam oranı ile değiştirmiş olduk.


Daha sonra bu metodu çağırmamız gerekiyor bunun için sınıf adını kullanarak sınıf metodunu çağırmamız gerekiyor.

```py
Arabalar.vergi_orani_guncelle(4.0)
```
yukarıdaki gibi sınıf metodumuzu sınıf adı üzerinden çağırırız. İlk parametremiz cls ancak fonskiyon otomatik olarak bu kısmı aldı yani sınıf değişkenimizi aldı bizden ikinci bir değer olan yeni vergi oranını istiyor.


## ***ÖNEMLİ!!***


ikinci bir değeri girdiğimiz zaman yeni oran güncellenecektir. Bu oran sınıfta varolan tüm nesneler ve yeni üretilecek olan nesneler için güncellenecek , araçların vergili fiyatı hesaplanacak ve bu değer geriye döndürelecektir.

<br><br>



# ***ALTERNATİF İNŞACILAR (ALTERNATİVE CONSTRUCTOR)***

<br>

SInıf metodları ***yapılandırma metodu*** olarak da kullanılabilir. class methodlarını kullanarak bir sınftan nesne üretmenin farklı yolu olarak da kullanılabiliyorlar. Mesela elimizde bir veri var bu veriler json formatı da olabilir exel dosyası da olabilir herhangi bir string formatındaki değerler de olabilir. Bu verilkeri kulanarak sınıfı örneklendirmeyi amaçlıyoruz. Bir örnekle açıklayalım.

<br>

**Elimizde bunun gibi bir veri olduğunu varsayalım**
```py
data = [
    {
        "marka":"toyota",
        "renk":"beyaz",
        "fiyat":100000,
        "model":2002
    },
        {
        "marka":"mercedes",
        "renk":"beyaz",
        "fiyat":130000,
        "model":2008
    },
        {
        "marka":"bmw",
        "renk":"lacivert",
        "fiyat":180000,
        "model":2008
    },
        {
        "marka":"mazda",
        "renk":"kırmızı",
        "fiyat":150000,
        "model":2017
    },
        {
        "marka":"ford",
        "renk":"gri",
        "fiyat":300000,
        "model":2022
    },
        {
        "marka":"volkswagen ",
        "renk":"beyaz",
        "fiyat":280000,
        "model":2019
    },
]


```
<br>



Yukarıdaki verileri kullanarak Arabalar sınıfına bu verileri toplu bir şekilde yerleştirmek istiyoruz. Bunun için alternatif inşacıları kullanacağız. Yani oluştruduğumuz bir class metod sayesinde bu verileri örneklendireceğiz.

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


arabalar_data   =   Arabalar.toplu_arac_ekle(data)

print(arabalar_data)
print(arabalar_data[1].model)
print(arabalar_data[2].model)

>>> [
        <__main__.Arabalar object at 0x000002289B5EED48>,
        <__main__.Arabalar object at 0x000002289B5EED88>,
        <__main__.Arabalar object at 0x000002289B5EEDC8>, 
        <__main__.Arabalar object at 0x000002289B5EEE08>, 
        <__main__.Arabalar object at 0x000002289B5EEE48>,
        <__main__.Arabalar object at 0x000002289B5EEEC8>
    ]
>>> 2008
>>> 2008
```

<br>

Şimdi örneği inceleyecek olursak normal örnek metodları ve önceki derslerde anlattığımız vergi oranı güncelle sınıf metodu dışında ayrıca toplu arac ekle adında yeni bir sınıf metodu tanımladık.

<br>

```py
    @classmethod
    def toplu_arac_ekle(cls ,data):
        eklenen_veriler = []

        for i in data:
           eklenen_veriler.append(cls(i["marka"], i["renk"], i["fiyat"], i["model"]))

        return eklenen_veriler
```
<br>

Burada gerekli tanımlamaları yaptıktan sonra ilk parametre herzamanki gibi cls ikinci parametre ise bu fonksiyona göndereceğiz data parametresi. Bu parametreyi json dosyası olarak düşünelim.

ilk başta boş bir liste oluşturduk daha sonra data parametresinden gelem verileri döngü ile tek tek alarak sınfı örnekledik ve her bir örneği oluşturduğumuz boş listeye aktardık daha ve bu listeyü return ile geriye dönderdik

Ancak dikkat etmemiz nokta burada sınıf adını kullanmadık. Bunun yerine cls kullandık bunun da sebebi class methot tanımlarken cls nin sınıfı temsil ettiğini öğrenmiştik. cls nin sınıfı temsil ettiği için sınıf adı yerine cls değimini kullanmış olduk. aşağıdaki tanımlama ile aynı işi yapıyor.

```py
Arabalar(i["marka"], i["renk"], i["fiyat"], i["model"])
``` 
- bu iki tanımala da aynı amaca hizmet ediyor ancak biz sınıf metodu tanımladığımız için cls değimini kullanırız. cls sınıfı temsil ediyor. 


```py
cls(i["marka"], i["renk"], i["fiyat"], i["model"])
``` 

Döngü ile gelen her veri sözlük yapsısında olduğu için anahtar değerlerini ilgili sınıfı örneklemek için parametre olarak belirttik  ve toplu bir şekilde sınıfı örneklemiş olduk. 

<br>

# ***STATİK METODLAR***

<br>

Tanımladığımız fonksiyon içerisinde sınfımızı veya nesnelerin hehangi birisiyle **ilişkisi olmayan** ancak sınıf içerisinde **mantıksal olarak** bulunmasını istediğimiz metodlardır.

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


print(Arabalar.kok_al(144))

>>> 12.0
```

<br>

örnekte de olduğu gibi statik metodlar sınfla veya nesnelerele ilgili olmayan metodlar. Bu sınıf için kök alma metodu belki mantıksız olabilir fakat bazen bunun gibi metodları sınıf içerisinde ihtiyacımız oluyor ve kullanıyoruz.

