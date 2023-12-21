
# Serializer Kavramı 


Karmaşık veri yapılarını , model örnkelerini  json xml gibi veri yapılarını python verilerine dönüştürmek ve  diğer sistemlerle iletişim kuracak şekilde veri oluşturmak için kullanırız. Mesela elimizde ürün bilgilerinin bulunduğu bir json verileri ve bir e-ticaret uygulaması olsun. Serileştiriciler ile kolaylıkla json verilerini alıp python verilerine dönüştürerek veritabanına ekleme işlemi yapabilriz. Veya bu durumun tam tersi de olabilir. Elimizde ürünlerin bir datası varsa ve biz bu datayı ilgili kişilerle paylaşmak istersek bunu serializer ile json veri türüne dönüştürüp paylaşabiliriz.  


# Manuel Serializer Tanımlaması



Oluşturduğumuz app in içersine api dizini tanımlayalım. Projedeki dosyaların daha düzneli olması ve kullanılabilirliği arttırmak için yapıyoruz. A slında öyle bir dizin oluşturulmak zorunda değiliz.  Model dosyasında tanımladığımız sınıfı ve serializer dosyasını import edelim.

blog/models

```python
from django.db import models

class Blog(models.Model):
    yazar = models.CharField(max_length=50 , verbose_name="yazar")
    baslik = models.CharField(max_length=50 , verbose_name="baslik")
    aciklama = models.CharField(max_length=100)
    metin = models.CharField(max_length=150)
    yayimlanma_tarihi = models.DateField(auto_now=True)
    yaratilma_tahrihi = models.DateField(auto_now_add=True)
```



blog/api/serializer.py
```python
from rest_framework import serializers
from blog.models import Blog


class Blog_Serializer(serializers.Serializer):

    id=serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama=serializers.CharField()
    metin = serializers.CharField()
    yayimlanma_tarihi = serializers.DateField(read_only=True)
    yaratilma_tarihi = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Blog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.yazar = validated_data.get("yazar" , instance.yazar)
        instance.baslik = validated_data.get("baslik" , instance.baslik)
        instance.aciklama = validated_data.get("aciklama" , instance.aciklama)
        instance.metin = validated_data.get("metin" , instance.metin)
        instance.save()
        return instance
```

Serializer tanımlarken dikkat edilmesi gerekenler;

- Modelde tanımlanan alan isimleri ile serializer da tanımlanan alan isimleri aynı olması gerekiyor.
- Modelde tanımlanan alanların parametrelerini tekrar tanımlaya gerek yok zaten oluşturulan serileri modelde kaydetmeye çalıştığımızda o tanımlamalar modelde olacağı için tekrar tanımlamamıza gerek yok. **ör max_length = 100** gibi  
- Eğer değişiklik yapılmayacak alanlar tanımlamak istersek paranterler içerisinde ```read_only=True``` paramteresini tanımlamamız gerekiyor. Bu alanlar okuanbilir ancak değiştirilemez.


Örnekteki serializer sınıfında tanımladığımız create() ve update() metodları eğer post metodu ile veya put metodu ile bir veri gelirse bu veriyi işlemek ve kaydetmek için kullanılır. Create() metodundaki ```validated_data``` paramtresi doğrulanmış verileri ifade eder (validated_data bir dictionary | sözlük veri türündedir). Drf gelen json verilerini doğrular eğer hatalı bir işlem varsa bu metodlar çalışmaz. Gelen verilerin doğrulanmis olup olmadığını ```is_valid()``` metodu ile öğrenebiliriz (ilerleyen örnklerde kullanacağız).Kayıt etmek istediğimiz sınıfı çağırarak create metoduna ```**validated_data``` paramteresi ile alanları ekler ve kayıt ederiz. Aynı şekilde update metodunda da ```validated_data``` ve ```instance```   parametreleri var . Buradaki instance parametresi ise ```güncellemek istediğimiz nesneyi``` (instance) ı temsil eder. Peki update fonksiyonunda tanımladığımız ifadeler ne demek onu da açıklayalım.

```python
instance.yazar = validated_data.get("yazar",instance.yazar)
```

Bu tanımlamada yapılması hedeflenen şey gelen doğrulanmış data ile kayıtlı olan data arasındaki farktır. Eğer iki data arasında farklılıklar varsa ```get()``` metodu sayesinde doğrulanmış veriler alınır eğer gelen veri farklı değilse instance da kayıtlı olan veri tekrar tanımlanır. Tüm alanlar için bu tanımlama yapıldıktan sonra instance save() fonksiyonu ile kayıt edilip return ile geri döndürülür.



## Serializer Sınıfını Shell De Kullanımı (Örnekleri)


Yukarıda oluşturduğumuz serializer sınıfını kullanarak shell de örnek yapalım. Bu projede django_extensions daki shell_plus ı kullanacağım .

Serialization İşlemi
```python
from blog.api.serializers import Blog_Serializer
from blog.models import Blog
from rest_framework.renderers import JSONRenderer

blog = Blog.objects.first()

serializer = Blog_Serializer(blog)
serializer.data

#{'id': 2, 'yazar': 'kadirtest', 'baslik': 'test33333', 'aciklama': '12test', 'metin': 'test', 'yayimlanma_tarihi': '2022-11-22'}

print(type(serializer.data))
#<class 'rest_framework.utils.serializer_helpers.ReturnDict'>


data = JSONRenderer().render(serializer.data)

print(data)

# b'{"id":2,"yazar":"kadirtest","baslik":"test33333","aciklama":"12test","metin":"test","yayimlanma_tarihi":"2022-11-22"}'


print(type(data))
# bytes
```



Yukarıdaki örnekte serialization işlemi nasıl olur. Arka planda json a dönüştürme işlemi nasıl yapılır örnek verdik. Örneği açıklayacak olursak ilk başta import işlemlerimizi yaptık. İlgili modelimizi ve serileştirici sınıfını import ettik.İlk başta elimizde bir instance olması gerekiyor. Amacımız bu instance daki verileri alıp json veri yapsısına dönüştürmek. İnstance ı seçtikten sonra ilgili serializer sınıfına instance ı vererek json yapsına benzer bir serializer objesi oluşturuyoruz. Eğer oluşturduğumuz serideki datayı almak istersek ```.data``` metodunu kullanmamız gerekiyor. örnekte de olduğu gibi bize json a benzer bir yapı verdi , datayı type() metodu ile kullandığımda da serializer objesi olduğunu gördük. Eğer ben bu serializer objesini byte a yani json a dönüştürmek istersen rest framework dan JSONRederer ı import etmem gerekiyor. Burdan da ```render()``` metodunu kullanarak serializerdaki datayı json a dönüştürebiliriz. Peki elimizde bir json verisi varsa bunu nasıl python veri yapsına dönüştürecez aşağıdaki örneği inceleyin.



Deserialization İşlemi
```python
from rest_framework.parsers import JSONParser
import io

data = b'{"id":2,"yazar":"kadirtest","baslik":"test33333","aciklama":"12test","metin":"test","yayimlanma_tarihi":"2022-11-22"}'


stream_str = io.BytesIO(data)
stream_str
#  <_io.BytesIO at 0x7f718f9dd080>

data = JSONParser().parse(stream_str)

data

"""
{'id': 2,
'yazar': 'kadirtest',
'baslik': 'test33333',
'aciklama': '12test',
'metin': 'test',
'yayimlanma_tarihi': '2022-11-22'} 
"""

type(data)
# dic

serializer = Blog_Serializer(data=data)
serializer

""" 
Blog_Serializer(data={'id': 2, 'yazar': 'kadirtest', 'baslik': 'test33333', 'aciklama': '12test', 'metin': 'test', 'yayimlanma_tarihi': '2022-11-22'}):
id = IntegerField(read_only=True)
yazar = CharField()
baslik = CharField()
aciklama = CharField()
metin = CharField()
yayimlanma_tarihi = DateField(read_only=True)
yaratilma_tarihi = DateField(read_only=True)
"""

serializer.is_valid()
# True



serializer.validated_data
""" 
OrderedDict([('yazar', 'kadirtest'),
             ('baslik', 'test33333'),
             ('aciklama', '12test'),
             ('metin', 'test')])
"""

Blog.objects.count()
# 2

serializer.save()
# <Blog: Blog object (5)>

Blog.objects.count()

# 3

```



Parse işlemi için çalışma alanına JSONParser ve io modillerini import ettik.IO modülü sınıfların ve işlevlerin, Unicode verilerine yazmayı etkinleştirmek için işlevselliği genişletmemize izin verir.Byte IO işlemlerini kullandığımızda veriler bir bellek içi arabellekte bayt olarak tutulabilir.Daha sonra oluturduğumuz byte ı JSONParser a veriyoruz. 

Bu oluşturduğumuz byte verisini python sözlüğüne dönüştürür.Artık elimizde python sözlüğü olduğu için gerisi basit.Oluşturduğumuz datayı serializer sınıfına ```data parateresi ile birlikte gönderiyoruz```. Artık elimizde bir seri var bu serinin doğrulanmış olup olmadığını is_valid() metodu ile kontrol ederiz. Eğer doğrulanmış ise veritabanına kayıt işlemini yapacağız. Eğer oluşturulan doğrulanmış datayı almak istersek ```.validated_data``` yı kullanabiliriz.

Örnekte kayıt işlemini yapmadan önce objelerin sayısını ekrana yazdırdım daha sonra kayıt işlemini yaptım ve tekrar sayı yazdırdım. Örnekte de olduğu gibi serializer işlemi başarılı ve instance sayısının arttığını görebilirsiniz.