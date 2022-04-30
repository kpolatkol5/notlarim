# DJANGO KURULUMU

- django-admin startproject proje_adi
- python manage.py runserver : ilk kurulum ve sql dosyasinin oluşturulmasi için
- python manage.py migrate :veritabani kurulumu için gereklidir
- python manage.py createsuperuser

- python manage.py startapp uygulamaadi

- eklediğin uygulamayi root projede settings dosyasina ekle virgükl koymayi unutma

# HTTP TALEPLERİ

- **reguest** : talep istek anlaminda 
<br>
<br><br>

## EKLEDİĞİN UYGULAMA İÇİNDE URL YAPISI OLUŞTUR

- **path()** i ve views dosyasını import edelim 

<br>

```python
    from django.urls import path
    from . import views 
```
<br>

- ekldeiğimiz urls dosyasina urls listesine **path** tanimladik şimdi burdaki path in içindeki "" içine yazdiğimiz deger arama motorundaki **uzanti adi** oluyor peki bu uzantiyi nerden nasil alacak? onu da yanda belirttiğimiz views dosyasindan çekecez views dosyasina da bir fonksiyon tanimladik **views.fonksiyon_adi** ile hangi fonksiyonu görüntülemek istersek onun adini yanda belirtiyoruz yukarıda tanımladığımız import işlemlerinde views dosyasını da import etmiş olduk **from . import views**  bu şekilde urls.py dosyasina views dosyasini import ediyoruz bu kod views dosyasindaki tüm foksiyonlari import edecektir


<br>

```python
    urlpatterns = [
        path("" ,views.ana_sayfa , name=" ana_sayfa"),
        path("sozluk" ,views.sozluk , name=" sozluk"),
    ]
```
<br>


- peki views dosyasina nasil  fonksiyon tanimlanir?
<br>


```python 
    def index(request):
        return HttpResponse("home page")
         # buradaki fonksiyon adlari ile urls dosyasindan birer path oluşturuyoruz şimdilik HttpResponse gönderelim daha sonra render methodu ile template göndereceğiz
```

<br>

-  şimdi biz buraya kadar eklediğimiz uygulamadaki url yapisi ve gereken fonksiyonlari tanimladik şimdi biz kurduğumuz uygulama içerisinde tanımladığımız urls dosyasını  root projeye eklememiz gerekiyor bunun için root projedeki **urls.py** dosyasina gidiyoruz.

<br>


### SIRASIYLA
<br>

1. ilk başta include import etmemiz gerekiyor path in yanina hemen , koyup import yaziyoruz bu import bize farkli uygulamada oluşturdugumuz url yapilarini ana root projeye tanimlamamizi sağlar.

<br>

```python
    from django.contrib import admin
    from django.urls import path,include
```
<br>

2. sonraki adimda ise urlpatterns listesine , koyup yeni bir path tanimliyoruz


<br>

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("genelsayfalar.urls")),
]
```
<br>


### NOT :
- eğer root projedeki urls yapisindaki path e bir değer girersen uygulamada oluşturduğun uzantilar girdiğin degerin alt uznatilari olacaktir mesela


```python
# eklediğimiz uygulamadaki urls
urlpatterns = [
    path("" ,views.ana_sayfa , name=" ana_sayfa"),
    path("sozluk" ,views.sozluk , name=" sozluk"),
]


```


```python
# root projedeki urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("genel", include("genelsayfalar.urls")),
]
# include ile genel sayfalar uygulamasından url dosyasını çekmiştik path in içerisine de genel ifadesini tanımladık  uygulama içindeki urls dosyasında sözlük ve içi boş olan ana sayfa fonksiyonuna url den ulaşmak için başına genel eklemek gerekiyor

#  genel/sözlük ==> sözlük template ine gider
# genel/ ==> yazdğımızda da anasayfa template ine gider

#  ör: 

# http://127.0.0.1:8000/genel/sozluk ==> sozluk 
# http://127.0.0.1:8000/genel/ ==> ana sayfa

```


<br>
<br>


 # TEMPLATES İŞLEMLERİ(APP)

- eklediğin uygulamanin içine **templates** adinda bir klasör olustur bu dosya özel bir klasör adıdır. root projedeki settings dosyasindaki tamplates listesine  bakarsan orda eklediğin tüm uygulamalarda bu dosya adini aradiğini göreceksin. bunu eklediğimiz uygulama içerisinde yapıyoruz

- views dosyasinda yazdiğimiz fonksiyonlarda özel bir metod kullandik **render metodu**.  render metodu araciliği ile bir kaynağı kullanıcıya  gönderebiliriz. render in ilk parametresi **request** ( yani gelen istek) sonra ilgili uygulama içerisinde templates dosyasinda dosya adi arar bu dosya adi **index.html** olsun


<br>


```python
    def index(request):
        return render(request, "index.html")
```
<br>

- ancak bu metod tüm uygulamalarin içerisindeki templates klasörünün içindeki index.html i arar . **eğer başka bir uygulamada da index.html varsa kodlar çakisacaktir**. bunun önüne geçmek için **tamplates klasörünün altina ilgili uygulamanin adinda bir klasör daha ekleyelim** ve şablon dosyalarimiz bunun içinde dursun bunu views dosyasinda render metodu ile çağirdiğimizda ise şöyle yazmamiz gerkir

<br>

```python
    def index(request):
        return render(request, "uygulama_adi/index.html")
```

<br><br>


# STATİCK FİLES (APP)

- static dsyaları ile çalışırken uygulama içinde  bir **static** dosyası oluşturman gerekiyor. css js ve img dosyalarını burda barındıracaksın bu dosyaları eklerken  de {% static '' %} içerisine tırnaklar arasına static dosyalarının adını yazıyosun ancak bunun çalışması için her şablonun üstüne {% load static %} yazman gerek bu static dosyalarını çalıştırğın ortama aktarmaya yarar

<br>



```django
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
```

<br>

- **projelerimizde birden fazla uygulama olacaktır** bunun için uygulamaya özel olan css ,js veya img dosyalarını  static **klasörünün içine çalıştığın uygulama adında bir klasör oluşturup bu uygulamaya özel olan dosyaları klasöre atarız** bu şekilde başka bir uygulamada da aynı isimde başka **bir dosya varsa karışmayacaktır.**



# BASE TEMPLATES & BASE STATİC

- html iskeleti ve ortak olan kod parcalarini ve içeriklerini tek bir yerden yönetebiliriz. bunun için root dosya izinine tamplates diye bir dosya ekliyoruz ancak django bu templates dosyasini taramaz taranan templates dosyalari uygulamalarin içindeki templates dosyalariydi. bu klasöründe taranmasi için  root projedeki settings dosyasina gideriz ve DIRS:[] listesinin içine BASEDIR / "templates" yazmamiz gerekiyor

<br>


```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates" # sadece buraya tanımlama  yaptık
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
<br>

- root projedeki templates klasöründeki base.html sayfasina tüm sayfalarda ortak olan kodlari yaziyoruz mesala html iskeleti ve menü kısmı falan

- uygulama içersidneki belirttiğimiz index.html kısmı gibi yerlere de block tanımlaması yapıyoruz. block tanımlaması söyle normlade görünen kısım base.html ama url kısmından index.html e ulaştığımda yine her  sayfada ortak olan base.html kısmı gelecek ancak index.html de yazdığımız farklılıklar da orda görünecektir . başka bir safa olan blog sayfasi mesela orda da ortak olan base.html kısmı görünecek ancak yine blog sayfasindaki farkliliklar block etiketi arasında yazdiğimiz farklılıklar görünecektir

- block tanimalamasi yaparken; 

```django
    {% block block_name %}{% endblock block_name %}
```
<br>

- bu base.html kısmında görünen kısım block etiketine bir isim verdik bu isime sahip olan index.html deki block kısmındaki farklılıklar dikkate alınarak görüntülenecektir

- şimdi biz block kısmıda gereken tanımlamalar yaptık ancak bu index.html ile base.html i birbirine bağlamamız gerekir. bunun için ise index.html in en üstüne  aşağıdaki kodu yazarız
<br>

```django
   {% extends 'base.html' %} 
```
<br>

- extends tanımlaması ile base.html e göndermiş oluyoruz bunu ara sayfalara yapıyoruz mesela hakkımızda sayfası gibi base html de açtığımız alanlar(block alanlar) hakkımızda sayfasındaki tanımladığımız **aynı isimdeki block** alanları orayı dolduracaktır bu sayede hangi sayfada çalışırsak çalışalım base html deki boş block alanarını  doldurarak sayfaları daha dinamik hale getiriyoruz 



- peki biz root projedeki templates dosyasina uygulamadaki index.html i nasıl extends ediyoruz ?

### ŞÖYLEKİ ;

- biz root projede settings dosyasinda root projedeki templates yolunu belirmiştik şimdi biz extends ettiğimizde django genel olarak **templates klasörü altında base.html** i arar biz bu settings dosyasindaki tanımlamamız ile bunun görünmesini sağlamış olduk  eger biz farklı bir uygulama oluştursaydık bile root projedeki **base.html** deki kodlar görünecekti 

<br>
<br>


## BASE STATİC


- şimdiye kadarki kısım uygulamaların içerisindeki static dosyalarıydı . uygulamaya özel yazdığımız css js ve img dosyalarını burada static klasörü  altında eklemiştik birden fazla uygulama olduğuna karışmaması için  çalıştığımız uygulama adında bir klaör oluşturup dosyalarımızı içine attık çünkü varsayılan olarak static dosyası tüm uygulamalrda aranır eğer biz tüm uygulamalarda da geçerli olan css js veya img dosyaları varsa root dizinde bir static dosyası oluşturuyoruz ve bunu root projedeki settings dosyasında en alta yolunu  eklememiz gerekiyor  


```python  
    STATICFILES_DIRS=[
        BASE_DIR / "static"
    ]
```

- şeklinde tanımlama yaparak root projeye static dosyalarını eklemis olduk . burada kafan karışabilir şimdi biz uygulama düzeyinde de static belirledik root projede de static bunlar karışmayacak mı?


-  1.  django genel olarak static dosyalarını arar şimdi biz uygulama düzeyinde static klasörü açtık ve bu uygulama ile aynı isimde bir klasör daha açtık ve içine style dosyalarını attık bunu çağırırken  **uygulama_adi/css/style.css** olarak çağırıyoruz ama bir de root projede tüm uygulamalarda ortak olan css dosyaları var bunda da dosyalrı direkt css js img diye oluşturuyoruz şablonda çağırırken de bir uygulama adındaki dosyanın altından çağırmayacağımız için sorun olmayacaktır direkt çağırırken css/style.css şeklinde çağıracaz burdaki amaç uygulama düzeyinde bakımı kolaylaştırmaktır. uygulamayı geliştirirken daha az kodla ilgileneceğiz

- uygulamaya özel bir css yazdığımızı varsayalım ve base.html den ayrı olarak index.html yazdık ve base.html e extend ettik burda index.html e özel olarak yazdığımız css in çalışabilmesi için base.html de **{% block css_files %}{% endblock content %}** şeklidne bir alan açmamız gerekiyor (head etiketleri altına normal css dosyalarını çağırdığımız yere ) ve index.html de de bu alanı dolduracak 

<br>


```django
    {% block css_files %} 
        <link rel="stylesheet" href="{% static 'blog/css/style.css' %}">
    {% endblock content %} 
```

<br>

- şimdi biz bunu index.html de doldurduğumuzda base.html deki **{% block css_files %}**  bölümüne gelecek eğer başka bir sayfa olsun mesela hakkimizda.html buraya da  aşağıdaki gibi tanımlarsak base.html de alanı doldurmuş oluyoruz

<br>


```django
    {% block css_files %} 
        <link rel="stylesheet" href="{% static 'blog/css/hakkimda.css' %}">
    {% endblock content %} 
```

<br>

# BOOTSTRAP DOSYASINI PROJEYE EKLEME

- ilk başta bootstrap js ve css dosyalarını root projedeki static dosyasına ekleriz çünkü bootstrap **bize her sayfada lazım olacaktır**

- base static de birer tane custom css ve js dosyalarını ekleyip base.html de çağırıyoruz bu tüm sayfalarda ortak olacak olan dosyalar
uygulamaya özel css dosyalarını çağırırken mesela index.html için ayrı bir css yazdın önce base.html de head etiketlerine bunu block etiketleri altında çağırıyoruz yukarıda anlatılan gibi js dosyaları da buna dahil ancak bunu biz en altta çağırırız js dosyaları altta çağırılır çünkü

<br>


# KISMİ ŞABLONLAR (PARTİALS)

- tasarımı tek bir sayfada oluşturmak yerine **parcalara ayırarak oluşturmaya** çalışıyoruz 

- mesela navbar tüm uygulamaların ieçrisinde olması gereken bir parça bunu **base template içerisinde** (tüm sayfalara ortak olan template klasörü) **partial** diye bir klasör oluşturup **_navbar.html** şeklinde ekleriz.

- sonra bu parcayı base.html içerisinde çağırmamız gerekiyor 

<br>

```django
    {% include 'partials/_navbar.html' %} 
```
<br>

# KISMİ ŞABLONLAR (APPS)

- eger uygulama içerisinde partials oluşturacaksan oluşturduğun tamplates dosyasından itibaren kaç dosyanın kökdizinindeyse hepsini belirtmen gerekiyor mesela uygulamanın templates dosyasından itibaren ;

<br>


```django 
{% include 'genelsayfalar/ana_sayfa/partials/_manset.html' %}
```
<br>

- yukarıdaki gibi belirmemiz gerekiyor genel sayfaların bir üst klasörü templates klasörüdür




# LİNK EKLEME

- yaptığımız uygulamanın içine urls.py dosyası açmıştık path de belirlediğimiz url yapısına biz **isim** veriyoruz  (name) bu isime göre de dinamik olarak link ekliyoruz link ekleyeceğimiz kod ise  {% url 'link_adi' %} olacak şekilde ekleyebiliyoruz
<br>

```django
    {% url 'link_adi' %}
```

<br>

# DİNAMİK VERİ İLE ÇALIŞMAK

- gelecek


# MODEL OLUŞTURMAK

- model  database de oluşturulan  bir tabloya denk geliyor. uygulama tarafında verilerimizi taşımak için  bir sınıf oluşturacaz be bu sınıfı models den türetiyor olmamız gerekiyor **ör :**
```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    #input text gibi oluşturur    Ture parametresi herhangi bir kayıt göndereden de oluşturlması için
    image = models.ImageField(upload_to="blog")
    description = RichTextField()
    is_active= models.BooleanField(default = False)
    is_home= models.BooleanField(default = False) # kolonlara varsayılan olark false değeri gider

```

<br>

- yukarıdaki örnekte blog uygulamasının içindeki model.py dosyasına sınıf tanımladık . burda paylaşacağımız blogların açıklama bilgisi başlık bilgisi resim bilgisi aktif veya pasif bilgisini tutan veriler ekledik bu verilerde her değişiklik yaptığımızda migrate işlemi yapmalıyız burda eklediğimiz özellikler admin panelde görünecektir   

<br>


# YAZAR BLOG İLİŞKİSİü

<br>

- yazılan makale veya postların kime ait olduğunu belirtmek için models.py dosyasında oluşturduğumuz sınıfa yazar alanı ekleyeceğiz

-  her makalenin bir yazarı olacak ve her yazar birden fazla makale veya blog ekleyebilecek

- bunun için bire bir ilişki tipini kullanacağız

<br>

```python
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = RichTextField()
        image = models.ImageField(upload_to="genelsayfalar")
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        yayimlanma_tarihi = models.DateTimeField()
        yazar = models.ForeignKey('auth.User')
```
<br>

- **models.ForeginKey('auth.User')** ile  kullanıcı modelini referans gösterdik artık yazar alanında  kullanıcılar görünecektir

- **models.ForeginKey('auth.User' , verbose_name="yazarlar")** : verbose_name parametresi admin panede görüntülenecek olan ismi temsil eder

```python 
    yazar = models.ForeignKey('auth.User' ,default=1, on_delete = models.SET_DEFAULT )
```
- yukarıdaki tanımlamada models.set default tanımlaması ile eğer yazar silinirse yazdığı bloglar silinmesin diye varsayılan olarak 1 id sini sahip kullanıcıya aktarılacaktır




<br>



# DJANGO MİGRATİONS

- models.py de yazdığın sınıflarla ilgili  veritabanında tabloları oluşturacak kodları yazar migrations klasorundeki _initial.py diye bir dosya gelecektir 

-  oluşturduğumuz migrationu uygulamak ve veritabanında görüntülemek için  migrate komutunu yazarız bu şekilde bekleyen migrateleri uygular

```python
>>> python manage.py makemigrations 
>>> python manage.py migrate
```
<br>


# KAYIT EKLEMEK


- ilk başta shell üzerinden birkaç kayıt eklememiz gerekiyor daha sonra bu kayıtları kullanarak admin uygulamasını düzenleyeceğiz

- sehell e girmek için terminale aşağıdaki komutu yazarız

```python 
>>> python manage.py shell
```

<br>

- ilk başta models.py dosyasında oluşturuduğumuz ilgili sınıfı import etmek gerekiyor


```python 
>>> from genelsayfalar.models import Blog
```
<br>

- shell e blog sınıfını ekledik artık bu sınıftan obje üreteceğiz bu obje veritabanında kayıt olacaktır

- obje oluşturuken ;

```python 

>>> b1 = Blog(title="python eğitimi" , description="kjlasdasdas", is_active=True , is_home = True ) 

>>> b2 = Blog(title="php  eğitimi" , description="kjlasdasdas", is_active=True , is_home = True )   
```
 
- models dosyasında oluşturduğumuz tüm alanları dolduruyoruz

- bunların veritabanında kayıt edilebilmesi için ise aşağıdaki gibi tanımlama yapmamız gerekiyor


```python 

>>> b1.save()
>>> b2.save()
```

- eğer veritabanında kayıt olan title bilgisinin içeriğini görmek istersen 

- models.py dosyasında tanımladığımız Sınıf a aşağıdaki tanımlamayı yapmalıyız 

<br>


```python 
    def __str__(self):
        return self.title
```
<br>

- kayıt alma işleminde bir tane kayıt almak istersenn

```python 
   >>> Blog.objects.get(id=1).title
```

- yukarıdaki işlemin açıklaması Blog sınıfından türetilen objelerden id si 1 olan objenin title bilgisini getir demektir



- eğer Blog sınıfından türetilen objelerin hepsini almak istersen aşağıdaki tanımlamayı kullanırsın burdan gelen değer listedir indek numarasına göre elemanları alabilirsin ve içerisindeki bilgilere olaşabilirsin  

```python 
>>> Blog.objects.all()
>>> Blog.objects.all().[1].title # 1. numaralı indexteki objenin title bilgisini verir 
```

<br>

- shell  den çıkış yapmak için terminal e  **exit()** yazılır. 


# KAYITLARI LİSTELEME


- kayıtları yukarıda olduğu gibi birkaç tanesini custom olarak ayarladık şimdi ise bu kayıtlari uygulamamızın içerisidneki views dosyasında çağırmamız gerekiyor çalıştığımız uygulamanın views dosyasına gidelim ve uygulamamızdaki models.py dosyasından ilgili sınııf import edelim

<br>


 ``` python 
    from calistiğin_uygulama_adi.models import Blog , Catagories
 ```

<br>

- hangi fonksiyonda işlem yapacaksan mesela ana sayfa olsun bu fonskiyonun içerisine sözlük yapısı oluşturuyoruz ve en son  render fonksiyonu ile bu sözlüğü sayfaya göndereceğiz


<br>

``` python 
    def ana_sayfa(request):
        context={
            "blogs":Blog.objects.filter(is_active=True,is_home=True)
        }
        return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)
```

<br>

- blogs takma isimdir var olan objeleri tutar var olan objeler liste türündedir.

- sonraki adımda ise sayfada objeden gelecek olan veriler mesela title alanı description alanı gibi alanları sayfada  doldurmamız gerekiyor ve her eklenen obje için bir html alanı tekrarlanır bu alanı döngüye almamız gerekiyor döngüye aldığımız bu alanın içerisidne de objelerden gelen title ve description verileri ile dolduracağız 

<br>


### DJANGO HTML

```django
    {% for genel_bloglar in blogs  %}
        {% include 'genelsayfalar/ana_sayfa/partials/_genel_bloglar.html' %}   
    {% endfor %}   
```
<br>

- for döngüsü ile tekrarlanacak olan alan aşağıdaki gibidir 

<br>


### DJANGO HTML

```django
    
<div class="row mb-4 blog_container p-1 w-100">
    <div class="col-sm-4 col-12">
        <div class="blog_img-container p-2 me-2">
            <img class="img-fluid" src="{% static 'genelsayfalar/img/'|add:genel_bloglar.image %}" alt="">
        </div>
    </div>
    <div class=" col-sm-8 col-12  p-1">
        <div class="blog-content-container">
            <div class="blog_info">
                <div class="blog_info_kategori">
                    <a class="" href="#">bilim</a>
                </div>
                <div>
                    <span>ŞUBAT/10/2020</span>
                </div>
            </div>

            <div class="blog-header mt-3">
                <h1 class="display-2">{{genel_bloglar.title}}</h1>
            </div>

            <div class="blog_text ps-2">
                <span>
                    {{genel_bloglar.description}}
                </span>
            </div>
            <div class="okuma_zamanı mt-2">
                <span class="ms-2">Tahmini okuma süresi : <b>1.5dk</b> </span>
            </div>
            <div class="row d-flex justify-content-md-start align-items-center justify-content-around ">
                <div class=" col-md-4 col-12  ">
                    <div class=" blog_like_container  pt-2">
                        <div class="  blog_like  me-3">
                            <a href="#">
                                <i class="fa-solid fa-angle-up"></i>
                            </a>
                            <span class="ms-2">32</span>
                        </div>
                        <div class="blog_dislike">
                            <a href="#">
                                <i class="fa-solid fa-angle-down"></i>
                            </a>
                            <span class="ms-2">32</span>
                        </div>
                    </div>
                </div>
                <div class=" col-md-8 me-auto col-12 author_container  p-2 pe-4">
                    <div class="author_image_container mt-2">
                        <img src=" {% static 'genelsayfalar/img/1.jpg' %} " alt="">
                    </div>
                    <div class="author_content-container mt-sm-3 ms-3">
                        <span>KAĞAN CEM KAYACI</span>
                        <span class="text-muted ms-1"> YÖNECİTİ/YAZAR</span>
                    </div>

                </div>
            </div>

        </div>
    </div>
</div>   
```
<br>


- for döngüsündeki  **{% for genel_bloglar in blogs  %}** genel_bloglar kısmı takma addır yani index sayfasına gelen blogs yapısının içerisindeki her bir objenin yerini alır

- döngüde tekrar eden kısımda resmi çağırıken bir filitre kullandık

<br>


```django
    <img class="img-fluid" src="{% static 'genelsayfalar/img/'|add:genel_bloglar.image %}" alt="">
```
<br>

- bu filitre string birleştirmede kullanılır **|add:genel_bloglar.image** burda resim yolunu belirtirken veritabından gelen resim ismini yola eklemiş olduk kısacası resimlerin varsayılan olarak tutulduğu dosyadan veritabanındaki gelen resim ismine göre resimler yerleşecektir

- veritabanından gelen diğer bilgiler mesela title veya description alanlarını ilgili yerlerde çağırıken **{{ }}** içerisinde belirtiriz for döngüsünde verdiğimiz takma ad burda genel_bloglar kısmı



<br>


```django
    <div class="blog_text ps-2">
        <span>
            {{genel_bloglar.description}}
        </span>
    </div>
```
<br>

## VİEWS DOSYASINDA KULLANDIĞIMIZ FİLİTRELER

<br>


``` python 
    def ana_sayfa(request):
        context={
            "blogs":Blog.objects.filter(is_active=True,is_home=True)
        }
        return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)
```
<br>


- **Blog.objects.filter()**  buradaki Blog bizim çalıştığımız sınıfın adıdır burdaki objeleri filitrelemek istersek objects.filter(is_active=True , is_home=True) ile aktif olarak seçilen ve anasayfada göstermek istediklerini filitreleyip öyle göndeiriz
 
- **Sınıf_adı.objects.all()** ile var olan tüm kayıtları getirir.

- **Sınıf_adı.objects.get()** ile sadece istenen bir kayıt gelir. bunu yaparken id ile çağırabilirsin


<br>


# ADMİN PANEL UYGULAMASI

<br>

- çalıştığımız  uygulamanın içerisindeki admin.py dosyasına gideriz ve yine aynı uygulama içerisindeki models dosyasınında tanımladığımız sınıfları çağırmamız gerekiyor

<br>


```python
    from .models import Blog,Catagories
```

<br>
 
- **" . "** kullanmamızın sebebi admin.py ile models.py dosyası aynı kökdizinde olmasıdır


- daha sonraki adımda ise bu sınıfları admin panele eklemeliyiz
  

<br>


```python
    admin.site.register(Blog)
    admin.site.register(Catagories)
```

<br>
 
- admin panele eklediğin ve veritabanından gelen değerler uygulama_adi-object olarak görünür bunu düzeltmek için models.py dosyasına gideriz ve ilgili sinifa fonksiyon tanımlarız
<br>


```python
    def __str__(self):
      return self.title
    #(title yerine artık üretilen nesneden ne çağırmak istiyorsan onu yazarsın description gibi)
```

<br>

- eklediğin uygulama üzerinde  admin panelde çalışırken kontrol panelini özelleştirebilirsin  örneğin çalıştığın sınıftan "title" bilgisinin yanıda birkaç bilgi saha eklemek istiyosun mesela is_active veya is_home değerlerinin bilgilerini **bunun için admin.py dosyasında yeni bir sınıf oluştururuz** 

<br>

```python
    class Blog_Admin(admin.ModelAdmin):
        list_display = ("id" , "title", "is_active" , "is_home")
```

<br>


- sinifi yazdiktan sonra reqister ile parametre olarak göndermemiz gerekiyor

<br>

```python
    admin.site.register(Blog, Blog_Admin)
    admin.site.register(Catagory)
```

<br>


## ADMİN PANELİ ÖZELLEŞTİRİRKEN KULLANDIĞIMIZ BAĞZI ÖZELLİKLER
<br>


- yukarıdaki örnekte admin.py dosyasında  bir sınıf oluşturmuştuk bu sınıfta kullanılan bağzı filitreler

<br>

- **list_display=("id" , "title" , "is_active")** : gibi veritabanından gelen objelerin isimlerini ve değerlerini admin panelde listeleyebilriz

- **list_editable=("id" , "title" , "is_active")** : ise veritabanından gelen objeleri üzerine tıklamadan  düzenleyebiliyoruz.

- **search_fields = ("title", "description")**  : kontrol paneline arama kutusu eklemek istersen kullanabilirsin

- **readonly_fields = ("description",)** : sadece okunabilir olan ve düzenlenemez olan alanları eklemek istersen yine admin.py dosyasına eklediğin sınıfa eklersin

- **list_display_links =("title , "description")** : kontrol panelinde üzerine tıklayıp da düzenleme alanına gideceğin kısımları belirlersin


<br>

## ADMİN AKSİYON EKLEME VE ÖZELLEŞTİRME
<br>

- admin panelde varsayılan olarak silme eylemi gelmektedir 
- görünen text aksiyonun kısa adı olarak geçer (short description)
- işaretlediğimiz her veri querydir ve queryset olarak gitmektedir
- bu işlemelri ilgili uygulamaın admin.py dosyasında oluşturduumuz ilgili modelin adminclassına  yazarız. 

- ilgili sınıfa bir eylem fonksiyonumuzu yazarız mesela bu fonksiyon seçilen queryleri **is_active=True** olarak değiştirsin

<br>

```py
    def yayinla(self, request,queryset):
        count=queryset.update(is_active=True)
        self.message_user(request, "{} adet yazı yayına alındı".format(count))
            #format kısmında hata olabilir hatırlayamadım
```
<br>

- fonksiyonumuzu yazdıktan sonra sınıfta bunu çağırmamız gerekiyor

<br>

```py
    class Blog_Admin(admin.ModelAdmin):
        list_display = ("title" , "is_active" , "is_home" ,"yayimlanma_tarihi", "selected_categories")
        readonly_fields=("slug",)
        ordering=("-yayimlanma_tarihi",)    
        list_per_page=15
        actions=("yayinla",)
```

<br>

- eğer aksiyonun short name ine müdahale edip adını değiştirmek istersen de

```py
    yayinla.short_description="işaretlenen yazıları yayına al"
```
<br>

- **date_hierarchy** kavramı hangi zamana göre hiyerarşi uygulamak istersen onu paremetre olarak vermemiz gerekiyor

- ay ve gün verilerine göre bir yapı oluşturur


```py
    date_hierarchy=("yayimlanma_tarihi",)
```

<hr><br>



## FORM FİELDSLERİ ÖZELLEŞTİRME VE FİELDS KÜMELERİ

<br>

- fieldslerin sıralamasını değiştirebilirsin

```py
    fields=("başlık" , "slug" , "içerik" , "aktif" )
```
- yukarıdaki her bir eleman bir satırı temsil eder eğer birtakım öğreleri yan yana almak istersen onları bir tuple a almalısın mesela;

```py
    fields=( ("başlık" , "slug" ), "içerik" , "aktif" )
```
- başlık ve slug fieldsleri yan yana gelecektir

<br>

### **FİELDS KÜMELERİ (fieldsets)**

<br>
 
- tuple içinde tuple olacak şekilde yer alır 

```py

    fieldsets=(
        ("başlık",{
            "fields":("baslık", "slug" , "aktif")
            "descriptions":"yazı için genel ayaralr"
        })
    )
```
### NOT:
- fieldsets tanımlamasını kullanacaksan  fields tanımlamasını kullanamazsın

<br>

### raw_id_fields
- Varsayılan olarak, Django'nun yöneticisi, şu alanlar için bir seçim kutusu arabirimi (select box) kullanır ForeignKey. Bazen, açılır menüde görüntülenecek tüm ilgili örnekleri seçmek zorunda kalmanın ek yüküne maruz kalmak istemezsiniz.


```py
    raw_id_fields = ("newspaper",)
```


# SLUG FİELD 

- uygulamada herhangi bir blog detayına gitmek için slug bilgisine göre gitmemiz gerekiyor blog bilgisinin title bilgisine göre url ye ve seoya uygun bir formatta  otamatik olarak oluşturulur

-  models.py dosyasına çalıştıgın uygulamanın ilgili Class ın altına  tanımlamamızı yaparız

<br>


``` python 
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = models.CharField(max_length=300)
        image = models.CharField(max_length=50)
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        slug = models.SlugField()
        
        def __str__(self):
            return self.title
```
<br>


- slugField varsayılan olarak **null=False** ile gelir yani bu  doldurulması zorunlu alan demektir eğer biz bu alanı eklemeden önce veritabanında kayıtlı olan objeler varsa o objelere yeni bir sütün eklenecektir ve bu alanlara ne gelecek bunu belirtmemiz gerekiyor. bunu yaparken ilk başta bu alanı **null=True** değerini yapalım yani var olan objeler için boş değer kabul etsin biz var olan objeleri doldurduktan sonra tekrardan bu alanı **null=False** olrak değiştireceğiz 

<br>


``` python 
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = models.CharField(max_length=300)
        image = models.CharField(max_length=50)
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        slug = models.SlugField(null=True)
        
        def __str__(self):
            return self.title
```
<br>

### Null dışında alabileceği bağzı paremetreler var

- unique="True" : bu parametre her bir değer için farklı bir slug alanı olup olmadığını kontrol eder.benzersiz kimlik sağlar

-  db_index = True : database açısından verilerin daha etkin şekilde ulaşmak için oluştrduğumuz kolonun indexlenmesini sağlar 


<br>


``` python 
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = models.CharField(max_length=300)
        image = models.CharField(max_length=50)
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        slug = models.SlugField(null=True , unique=True , db_index=True )
        
        def __str__(self):
            return self.title
```
<br>

- yukarıda null=False değeri için varsayılan değer girebiliriz 

```python
    slug = models.SlugField( null=False , default="slug_name" , db_index=True )
```

### Ancak

- **unique=True** : değeri için bu çakışacaktır unique tüm slug ifadelerin benzersiz olmasını sağlar ancak biz default ile varsayılan değer atadığımız için tüm değerlerde aynı ifade olacaktır

### SONUÇ OLARAK 


- tanımlamamız aşağıdaki gibi olacak ve daha sonra migrate işlemi yapacağız veritabanında bir sütun oluşturmak için



```python 
    slug= models.SlugField(null=True,unique=True, db_index="True")   
```

<br>

- **models.py** dosyasına gidip oraya bir fonksiyon tanımlamamız gerekiyor fonksiyon veritabanındaki title bilgisine göre otomatik slug bilgisi oluşturacak ve bu oluşturulan bilgiyi kayıt edecek 

- djangoda tanımlı olan models.Model sınıfının içinde tanımlı olan **save()** fonksiyonunu burda ezip yeni bir fonksiyon tanımlayacağız

- models.py dosyasına slugify bilgisini import edelim

```python
    from django.utils.text import slugify
```

- buraki save() fonksiyonunu ezip yeni bir fonksiyon tanımlayacağız 

- tanımladığımız **self.slug** bilgisini import ettiğimiz **slugify** fonksiyonuna **self.title** bilgisini gönderdik ve kayıt etmesi için super()fonksiyonu ile base.py dosyasından save() fonksiyonunu çağırdık gelen değerleri ona gönderdik bu şekilde biz title bilgisine göre otomatik slug bilgisi oluşturmuş olduk

```python
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
```

- admin panele gidip kontrol ettiğimizde **slug alanı boş içerik kabul etmiyor** bunun için models.py dosyasıana tanımladığımız  ilgili sınıfının slug alanına ek paremetre olarak  blank="True" eklememiz gerekiyor.Bu şekilde imput alanı boş değer kabul edecektir. Biz zaten otomatik oluşturması için ayarladık bu yüzden böyle bir tanımlama yapmamız gerkir


```python 
    slug= models.SlugField(null=True, blank=True ,unique=True, db_index="True")   
```
- tüm bu  işlemleri yaptıktan sonra yukaraıdaki slug alanındaki **null ="False"** yapmamız gerekiyor  çünkü buraların doldurulması zorunlu olan alanlar olması gerekiyor
-  ancak veritabanında bütün alanların doldurulduğundan emin ol yokas migrate ettiğinde hata alırsın

- makemigrations migrate dedikten sonra kayıt işlemi yapılır 

```python
    slug= models.SlugField( null=True ,blank=True , unique=True, db_index=True ,editable=False )
```
- **editable=False** ekledik bu slug alalnındaki imput alalnını kaldırır ve admin panelinden bu düzenlenemez ancak yine de sadece görmek istersen admin.py dosyasına gidip bunu ekleyebilirsin veya sadece o alanda görünmesini ancak sadaece okunabilmesini istersen aşağıdaki gibi tanımlama yapabilirsin


```python
    class Blog_Admin(admin.ModelAdmin):
        list_display = ("id" , "title", "is_active" , "is_home" , "slug")
```
<br>


- tüm bu işlemleri yaptıktan sonra admin panele gidip tüm blogları birer kez kaydedersek otomatik olarak slug alanı oluşacaktır


# KATAGORİLER İÇİN SLUG OLUŞTURMA


- yukarıdaki işlemle aynsı işlemi yapacağız ancak ancak katagorilerin title bilgisi yok name bilgisi var ona dikkat et

<br>
<br>



# SLUG BİLGİSNE GÖRE BLOG DETAY SAYFASI

- çalıştığın uygulama içerisindeki urls.py dosyasına gidip önce bir urls yapsı oluşturalım

``` python
    path("" ,views.ana_sayfa , name="anasayfa"),
    path("sozluk" ,views.sozluk , name=" sozluk"),
    path("<slug:slug>" , views.blog_detay , name="detay")
```

- slug yazan yerlere oluşturduğumuz blog objelerinin slug alanları gelecektir

- daha sonra ise ilgili uygulamadaki views dosyasında yukaıdaki örnkte **views.blog_detay** isminde bir fonksiyon oluşturalım 
    
```python 
    def blog_detay(request , slug):

        blog =Blog.objects.get(slug=slug)

        return render(request, "genelsayfalar/blog_detay/blog_detay.html" ,{"blog":blog})
```

- slug paremetresi ile ilgili objenin slug bilgisi gelecek ve aşağıdaki **blog=Blog.objects.get(slug=slug)** tanımlaması ile Blog sınıfından üretilen ve request den gelen slug paremetre ile aynı slug bilgisine sahip olan objeyi getirdik ve bunu blog diye bir sözlük yapısı oluşturup oraya atadık **.get()** tek bir tane obje getirirdi burda da zaten bir tane blog objesi gerekiyordu daha sonra da render fonksiyonu ile bu objeyi blog detay sayfasına göndermiş olduk artık aynı blogu blog detay sayfasında bilgileri kullanıyor olacağız

- bloglar ana sayfada ise bloglara tıklandığında urls yapısı ile ilgili bloga gitmesi gerekiyor url yapısını oluşturmak için ise;

```python


<div class="blog-header mt-3">
    <a class="class="display-2"" href=" {% url 'detay' genel_bloglar.slug %} ">
        {{genel_bloglar.title}}
    </a>
</div>

```

### NOT :

- burdaki genel_bloglar.slug alanı for döngüsü ile aldığımız takma isimdir biz for döngüsü ile ilgili blog objelerini alıyoduk tüm objelere de slug alanları tanımladığımız için **genel_bloglar.slug** tanımlamsı yaptık

- url in de içinde yazan **detay** uygulamada belirlediğimiz urls.py dosyasında gidilecek ismi temsil eder biz her bir sayfa için **name** tanımlaması yapmıştık bu da o name i temsil ediyor

<br>
<br>


# İMAGE FİELD

- kullanıcı admin panelden resmi upload edecek . bizim uygulama içerisinde belirtmiş olduğumuz bir klasöre resim kayıt edilecek 

- çalıştığın uygulama içerisinde models.py dosyasında oluşturduğun ilgili sınıfın içerisine  image alanı için aşağıdaki gibi tanımlama yapmıştık

```python
     image =models.CharField(max_length=200)
```

- artık aşağıdaki gibi bir tanımlama yapacağız 

```python
    image =models.models.ImageField(upload_to="")
```
- bu tanımlama sadece resim dosyaları yüklemek için kullanılır ancak resim dışında başka dosyalar da yüklemek istersen onun için de ;

```python
    image =models.models.FileField(upload_to="")
```
- upload_to="" parametresi içerisine ise ana dizin içerisine tanımlayacak olduğumuz klasör içerinde nereye kayıt edeceksen onun adını yazıyoruz ana dizinde her yerden erişilebileceği için biz blog uygulaması için ImageField tanımladıysak upload_to() parametresi içinde çalıştığın uygulama adını **upload_to("uygulama_adi")** yazmamız gerek

- sonraki adımda root dizine uploads adında bir klasör oluşturuyoruz ve bunu root projedeki settings.py dosyasında tanımlamamız gerekiyor

```python
    MEDIA_ROOT = BASE_DIR / "uploads"
        MEDIA_URL = "/images/"
```
-  MEDIA_ROOT : ile biz root dizinde uploads adında bir klasör oluşturduk ve bunun tanımlamasını yaptık

-  MEDIA_URL : ise bu dosyamızın gizli kalması için takma isim verdik url kısmında artık images altındaymış gibi görünecektir

- ImageField için python -m pip install Pillow ile Pillow kütüphanesini kurman gerekiyor

- model üzerinde değişiklik yaptıgın için migration olşturman gerekiyor

- admin panelde yüklü olan resmi görüntülemek istesen hata alırsın bunun için ek bir ayar yapmamız gerekiyor
- ilk başta root proje  içindeki urls.py dosyasına gideriz burda urlspatterns e köşeli karantez sonrasına + koyarak birkaç tanımlama yapacağız

- amaç şu ilgili upload dosyasının içerisindeki resimleri dışarı açmak bunun için ise static kullanımını açmamız gerek static metodunu urls.py dosyasına import edelim

```python 
    from django.conf.urls.static import static
```

-  static dosyasına eriştikten sonra eklediğimiz upgrade dosyasına erişmek için root projedeki settings dosyasına erişmeliyiz hatırlarsan orda MEDIA_ROOT ve MEDIA_URL tanımlamalarımız vardı amaç bunlara erişmek

```python 
   from django.conf import settings
```
-  urls.py dosyasında urlspatterns da köşeli karantez sonrasına + koymuştuk bundan sonra


```python 

    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

```

- ilk başta url e eriştik yani takma ad a  daha sonra ise  MEDIA_ROOT ile uploads dosyasına eriştik  amaç uploads dosyasındaki değerlere ulaşabilmek

- artık admin panelde resim eklerken şuanki resmi görüntülemek istersen hata almayacaksın

- dosyaları sayfada göstermek için ise ;

```django

    {{blog.image.url}}

```

- blog çalıştığın uygulama adı olacak önceden static metodu ile çağırıyorduk artık resimerimizi bu şekilde veritabanından çağıracağız

<br>
<br>



# HTML (CK) EDİTÖR

- eğer wordpresdeki gibi yazdığın blog içeriğinin düzgün görüntülenmesi ve içeriğin oromatik olarak html taglarına dönüşmesi için eklenti kullanacağz eklentinin adı **ckeditor**

- komut satırına  **pip3 freeze** dersen yüklü olan kütüphaneleri görüntülersin

- ck editor kurulumu için terminal e aşağıdakş kodu yaz

```python 
    >>> pip install django-ckeditor
```
- kurulumu yaptıktan sonra root projedeki settings dosyasına  install app e en alta ckeditor yazmalısın

- daha sonra çalıştığın uygulamada models.py dosyasına ckeditor u import etmen gerek

```python
    from ckeditor.fields import RichTextField
```

- artık models.py de nerde kullanmak istersen mesela description alalnında  TextField ataması vardı ve bu bize textarea oluşturuyordu

<br>


```python
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = models.CharField(max_length=300)
        image = models.ImageField(upload_to="genelsayfalar")
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        slug  = models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
```
<br>

- description alanına ckeditör'ü çağırmamız gerek

<br>


```python
    class Blog(models.Model):
        title= models.CharField(max_length=200)
        description = RichTextField()
        image = models.ImageField(upload_to="genelsayfalar")
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        slug  = models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
```
<br>

- artık burda RichTextField kullanabilriz modelde değişiklik yaptığın için migration oluşturman gerekiyor

- admin panelde ckeditor görünecektir ancak sayfalara yorumlanmis şekiled gelmez yorumlanmış şekilde gelmesi için sayfalarında **{{blog.description}}** yerine **{{blog.description|safe}}** safe yazman yeterli artık descriptondan gelen veriler yorumlanıp da gelecektir 

- eger gelen değerlerin belirli birkaç satırını almak istersen 

- **{{blog.description|slice:"0:100"}}** 0dan baslar ve ilk 100 karekteri alır

- etiketler de değer olarak sayılır bunları temizlemek için ek olarak **|striptags** yazmalısın


<br><hr>
<br>


# DJANGO ORM (query set)

<br>


## *Sorgu Kümeleri döndüren yöntemler*

<br><hr>

### ***fileter()*** 

- verilen paremetrelerle eşleşen objeleri döndürür

```py 
    b1= Blog.objects.fiter(is_active=True)
```
- blog sınıfı içerisindeki objelerden is_active=Ture olan objeleri b1 değişeknine atamış olduk

<br><hr><br>

### ***exclude()*** 

- verilen paremetrelerde eşleşmeyen objeleri döndürür

```py 
    b1= Blog.objects.exclude(is_active=True)
```
- blog sınıfı içerisindeki objelerden is_active=False  olan objeleri b1 değişeknine atamış olduk

<br><hr><br>


### ***annotate()*** 

- veri tabanında genelde sayısal işlem yapmakta kullanırız mesela ülkeler veya şehirlerde yaşayan insanların sayısı yaş ortalaması veya diğer istatiskel şeyleri hesaplamak için kullanırız bunu daha iyi anlamak için bir video buldum : **[VİDEO URL](https://www.youtube.com/watch?v=KbwmdKl-QbI)**


<br><hr><br>

### ***alias()*** 

- annotate ile aynı işemi yapar ancak açıklama eklemek yerine ifadeyi daha sonra başka QuerySet yöntemlerle yeniden kullanmak üzere kaydeder  filtreleme, sıralama veya karmaşık bir ifadenin parçası olarak kullanıldığı durumlarda kullanışlıdır 

- özetle tüm verileri almak yerine  verileri filitreleyerek daha iyi performansla sonuçlanması sağlarız

- bunu daha iyi anlamak için bir video buldum : **[VİDEO URL](https://www.youtube.com/watch?v=KbwmdKl-QbI)**


<br><hr><br>

### ***order_by()*** 

- query set ile gelen objeleri sıralamak için kullanılır id ye göre sıralayabilirsin eklenme , güncelleme tarihine göre sıralayabilirsin veya bunları tam tersine de çevirebilirsin . son eklenen blogu ilk başta göndermek gibi

```py
    b1=Blog.objects.all().order_by("-date")
```

- **" - "** ifadesi terse çevrimek anlamındadır yani son eklenen blog ilk gösterilecektir parametre içerisinde belittiğind eğere göre sıralama yapabilirisin



<br><hr><br>

### ***values()*** 

- Yinelenebilir olarak kullanıldığında model örnekleri yerine sözlükler döndüren bir QuerySet döndürür

- Bu sözlüklerin her biri, anahtarlar model nesnelerinin nitelik adlarına karşılık gelen bir nesneyi temsil eder.

- shell de bir örnek yapalım : 


```py
    from genelsayfalar.models import Blog  
    
    k1=Blog.objects.values("title", "id")
    
    >>> <QuerySet [{'title': 'Paris Sendromu: Paris Seyahatinize Yönelik Abartılı Beklentileriniz, Yaşadığınız Hayal Kırıklığı Sonucu Psikolojik Sorunlara Dönüşebilir mi?', 'id': 1}, {'title': 'Sifonu Çekmeden Klozet Kapağını Kapatın!', 'id': 3}, {'title': 'VSEPR Teorisinin Gücü: Elektronlar Üzerinden Moleküllerin Şeklini Açıklayabilmek', 'id': 4}, {'title': 'Rusya\'nın Ukrayna İşgali ve Sonrasında Gelen Yaptırımlar, Avrupa Uzay Ajansı\'nın "Rosalind Frankin" Mars Rover Projesi\'ni Erteleyecek!', 'id': 5}, {'title': 'sdfdsfsdfsadfqawfdasfdsgqa', 'id': 6}, {'title': '"Post-Coğrafya": Coğrafyaya Bakış Açımızı Değiştirerek, Dünyaya Bakış Açımızı Nasıl Genişletiriz?', 'id': 7}, {'title': 'Paleoklimatoloji Nedir? Kendi Gözlerimizle Asla Göremeyeceğimiz Geçmiş İklim Koşullarını Nasıl Anlayabiliriz?', 'id': 8}, {'title': 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro, quia! Quos, sint explicabo. Iste accusamus, ipsa obcaecati culpa veniam adipisci.', 'id': 9}, {'title': 'Organizmalar Nasıl Vekil Olarak Kullanılır', 'id': 10}, {'title': 's when you are querying across model relati', 'id': 11}]>     

    for i in k1:
        print("blogun id si = {} , blogun basligi = {} ".format(i["id"], i["title"]))


        
    """
    blogun id si = 1 , blogun basligi = Paris Sendromu: Paris Seyahatinize Yönelik Abartılı Beklentileriniz, Yaşadığınız Hayal Kırıklığı Sonucu Psikolojik Sorunlara Dönüşebilir mi?
    blogun id si = 3 , blogun basligi = Sifonu Çekmeden Klozet Kapağını Kapatın!
    blogun id si = 4 , blogun basligi = VSEPR Teorisinin Gücü: Elektronlar Üzerinden Moleküllerin Şeklini Açıklayabilmek
    blogun id si = 5 , blogun basligi = Rusya'nın Ukrayna İşgali ve Sonrasında Gelen Yaptırımlar, Avrupa Uzay Ajansı'nın "Rosalind Frankin" Mars Rover Projesi'ni Erteleyecek!
    blogun id si = 6 , blogun basligi = sdfdsfsdfsadfqawfdasfdsgqa
    blogun id si = 7 , blogun basligi = "Post-Coğrafya": Coğrafyaya Bakış Açımızı Değiştirerek, Dünyaya Bakış Açımızı Nasıl Genişletiriz?
    blogun id si = 8 , blogun basligi = Paleoklimatoloji Nedir? Kendi Gözlerimizle Asla Göremeyeceğimiz Geçmiş İklim Koşullarını Nasıl Anlayabiliriz?
    blogun id si = 9 , blogun basligi = Lorem ipsum dolor, sit amet consectetur adipisicing elit. Porro, quia! Quos, sint explicabo. Iste accusamus, ipsa obcaecati culpa veniam adipisci.
    blogun id si = 10 , blogun basligi = Organizmalar Nasıl Vekil Olarak Kullanılır
    blogun id si = 11 , blogun basligi = s when you are querying across model relati
    """
```

- **" - "** ifadesi terse çevrimek anlamındadır yani son eklenen blog ilk gösterilecektir parametre içerisinde belittiğind eğere göre sıralama yapabilirisin



<br><hr><br>








# DİNAMİK KATAGORİ MENÜSÜ


-  biz views sayfasına Blog sınıfını models.py dosyasından eklemiştik artık aynı yerden catagory sinifini da çağırmamız gerekiyor

```python
    from blog.models import Blog,Catagory
```

- bunu yaptıktan sonra daha önceden nasıl blog sınıfını index metonuna ve blog metoduna gönderdiysek aynı şekilde göndereceğizdirekt context listesinin altına sözlük şeklinde tanımlamam yaparız ve 
```python
    "catagories":Catagory.objects.all()
```
- bu şekilde tanımlama yaparsak veritabanında catagory tablosunda kaç tane değer varsa hepsini index metodu ile sayfalara göndeririz aynı şeyi blog metoduna da yapabilirsin


- daha sonra sayfa üzerinde  bu değeri almak için for döngüsünden yararlanırız catagory sayfasına git ve tekrarlanmasını sitediğin ani verilerin gelecek alan yerlerini döngü içine al

``` django
    {% for catagory in catagories  %}
        <a href="#" class="list-group-item list-group-item-action">
            {{catagory.name}} 
        </a>
    {% endfor %}
```

- catagories den gelen değerleri catagory değerine at ve aşağıda {{catagory.name}} tanımlaması ile sinif üzerinden gelen name değerini aldık
- veritabanından gelen değerlerin hepsi küçük harfle gelir bunu düznelemk istersen filitreleri kullanabilirsin **|title** filtresini kullanırsan sadece baş harfleri büyük olur

- catagory için lik tanımlaması yapmak istersen **urls.py** dosyasına gidip **path** oluşturman gerekiyor


``` python
    path("category/<slug:slug>" , views.blog_by_category , name="blog_by_category"),
```
- url kısmında category/ slug bilgi neyse o gelecek ve vievs içersinde bir metod tanımlayacaz metod adı  **blog_by_category** bunun adına da yine blog_by_category dedik işlemlerimizi yaparken bu isim üzerinden çağıracağız

```python
    def blog_by_category(request,slug):
        pass
```

- slug bilsini paremetre olarak göndermemiz gerekiyor

- daha sonra katagoriler nerden gelecekse href kısmına url tanımlaması yapacağız

```django
    {% url 'blog_by_category' catagory.slug %}
```

-  blog_by_category metodunan gelecek değer ve bir boşluk bırakıp category.slug yazıyoruz slug bilgisi veritabanından geliyor ve bu bir objedir

# DİNAMİK KATAGORİ MENÜSÜ BİRE BİR İLİŞKİ TİPİ (MANY TO ONE)

- birden fazla katagori olduğunu düşünelim ve bloglarımız var burda olay şu bir blog anck bir tane katagoriye ait olabilir ancak bir katagorinin de birden fazla bloğu olabilir mesela web programlama  katagorisinde  angular kursu , javascrip kursu olabilir ancak angular kursu aynı zamanda web programlama ve frontend katagorisinde olamaz 

- ilişkilendirme id bilgisine göre yapılır 

- ilk başta **models.py** dosyasına gidip Blog sınıfına catagory tanımlaması yapalım

```python
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
```

- parantez içerisine ilk paremetre olarak kullanılacak olan katagori sınıfının adı (Category ) ikinci paremetre ise


### NOT 

- **on_delete = models.CASCADE** bu paremetre eğer katagori silinirse onunla ilişkili olan bloglar da veritabanından  silinecektir

- **on_delete = models.SET_NULL** bu paremetre eğer katagori silinirse onunla ilişkili olan bloglar da veritabanından  silinemz ancak onun yerine boş değer tanımlanır ancak bunun için spesifik olarak nul=True tanımlaması yapmamız gerekiyor yani boş değerleri de kabul etmesini istiyoruz 

```python
    category = models.ForeignKey(Category ,null=True, on_delete = models.SET_NULL ) 
```

- **on_delete = models.SET_DEFAULT**  bu paremetre eğer katagori silinirse onunla ilişkili olan bloglar varasyılan olarak belitttiğimiz katagoriye aktarılır ancak bunun için default bir değer tanımlamamız gerekiyor

```python
   category = models.ForeignKey(Category ,default=1, on_delete = models.SET_DEFAULT ) 
```

-  bizim şuan veritabanıda kayıtlarımız var ve  var olan kayıtlar için hangi değer ataması yapmamız gerekiyor nasıl bir yol izlememiz gerekiyor


- nul=True değerini verip migarte ederek sonra bu değeri False çevirerek tekrar migrate ederiz bu birinci yol

- veya varsayılan bir değer veririz sonra bunu kaldırarak null =False yaparız bu şekilde bize hata vermeyecektir

<br>
<br>


# KATAGORİYE GÖRE BLOG FİLİTRELEME

- admin panele filtireleeme yapmak için admin.py dosyasına gidip oluşturduğun blog sınıfı içine 

```python
    list_filter = ("category", "is_active" , "is_home" ,) 
```

- böyle bir tanımlama yaptıktan sonra admin panelde sağda catagory is_active ve is_home bilgisine göre filitreleme işlemi yapabilrsin

- kategoriye göre filitreleme işlemini sayfa üzerinde nasıl yapacağız?


- urldeki slug bilgisini alarak bir responsu ona göre filitreleyip geriye göndermemiz gerekiyor bunun için views dosyasına gidip bir method tanımlayacağız

```python
def blog_by_category(request,slug):

    context = {
        "blogs": Blog.objects.filter(is_active=True , category__slug = slug),
        "catagories":Category.objects.all()
    }
    return render(request,"blog/blog.html",context)
``` 

- blog sınıfıyla  ilişkilendirilmiş bir catagory metodumuz var  burda amaç şu her bir bloğun katagori bilgisine ulaşacağız ancak katagori bilgisininde slug alanına ulaşağız ilk başta yukarıdaki tanımlamada catagory metoduna ulaştık 
 
```python
 "blogs": Blog.objects.filter(is_active=True , category
```

- buraya kadar catagory metoduna ulaştık daha doğrusu Blog sınıfında üretilen her objenin katagori bilgisine ancak  biz katagori bilgisinde slug alanına ulaşmmaız gerekiyor bu bilgiye ulaşmak için  başka bir sınıf olan Catagory sınıfının slug metoduna ulaşmalıyız


- bu  metoda ulaşmak için catagoryden sonra __sınıfınSlugMetoduAdı yani ;

```python
    "blogs": Blog.objects.filter(is_active=True , category__slug = slug),
```

- burdan gelen slug bilgisini paremetre ile gelen slug bilgisine eşitlememiz atmamız  gerekiyor

- eğer blog yoksa ve bunu sayfada görüntülemek istersen


```django
{% if blogs|length > 0  %}
    {% for blog in blogs  %}
        {% include 'blog/partials/_blog.html' %}
    {% endfor %}

{% else %}
        <div class="alert alert-warning" > blog yok</div>
{% endif %}
```


# MANY TO MANY İLİŞKİ TİPİ (ÇOKA ÇOK)

-  many to one ilişki tipinde bir blog sadece bir tane kategoriye ait olabiliyordu bunda ise bir blog birden fazla katagoriye ait olabilir

- iki model arasında çoka çok ilişki tipi 

- models.py dosyasına geliyoruz katagori ya da blog açısından bakarak kaydı nerden almak istiyosan yani katagoriye ait olan blog bilgileriyle mi daha çok ilgileniyosun ya da blog modelinden bakıp elde etmiş olduğun bir blog üzerinden o bloga ait olan katagori bilgilerini almayı mı tercih ediyosun ve buna göre hangisini almayı tercih edersen  o tablo içerisine bir manytomanyField eklemen gerekiyor

- mesela Blog tablosuna gittin ve aldığın her blog bilgisinin de hangi katagoriye ait olduyunu alma ihtiyacı duyalım  bu durumda blog sınıfına manytomanyField ekleyelim

- bir bloga ait olan  catagories lerele ilgileniyoruz

```python
    catagories = models.manToManyField(Catagory)
```

-  bu şekilde bir tanımlama yaptık ve parantez içersine hangi sınıfı referans alacaksa o sınıfın adını yazdık

-  

```python
    list_filter = ("category",)
```

- eğer admin.py dosyasına bçyle bir tanımlama yaptıysan hata verecektie şimdilik bu filitreyi kaldır

- models dosyasında bir değişiklik yaptıgımız için migrate etmemiz gerekiyor

# MANY TO MANY İLİŞKİ TİPİNDE MODEL SORGULAMA


- ilgili blogun hangi katagoriye ait olduğunu admin panelde görüntülemek için admin.py dosyasına gidip ilgili sınıf a  list_display tanımlaması oluşturmuştuk ve bu bloglarda hangi katagorilerde ait olduğunu görüntülemek için bir fonksiyon oluşturacağız ve  oluşturacağımız fonkisyon isimini list_display içerisinde belirtiyor olmamız gerekiyor.

- mesela şöyle bir fonksiyon tanımlayalım.

```python
    def selected_categories(self, obj):
            html=obj.title
            return html
```

- seçili olan tablodaki veriler obj içinde tanımlanır obj içinde o anki bloğun title bilgisini yazdırmak istersen bu şekilde yazarsı ancak bizim amacımız blogun hangi kategorilerde olduğunu oraya yazdırmak bunun için obj nin altındaki title bilgisi değil de catagories bilgisine ulaşmamız gerekiyor 



```python
    def selected_categories(self, obj):
        html="<ul>"

        for category in obj.categories.all():
            html += "<li> " +category.name + "</li> "
        
        html += "</ul>"
        return mark_safe(html) 
```

-  yukarıdaki fonksiyonda  for döngüsü içinde yapılan işlem obj altındaki categories e erişmek ve bu nesnenin içindeki name bilgisine ulaşmak ul ve li etiketlerinin içine alarak listeler halinde gelmesini sağladık ve en sonra mark_safe () fonksiyonunu import ettik 

```python
    from django.utils.safestring import mark_safe
```

-  bu şekilde admin panele gönderdiğimiz  ul ve li etiketleri yorumlanacaktır 

- **mark_safe:**   html etiketlerinin yorumlanmasını sağlar fonksiyonda admin panelde ul ve li etiketlerini kullandığımız için yorumlanmasını da isteriz bunun için makrk_safe import ettik ve kullandık



- eğre bu kategorileri filitrelremk istersen admin panlde sağ tarafta bunun için admin.py dosyasında tanımladığımız BlogAdmin sınıfında list_filter e models.py Blog sınıfnda en son tanımladığımız çok a çok ilişkisini kurduğumuz metodun adını yazmalısın biz ordakine categories demiştik bu yüzden list_filter e categories yazarız


<br>
<br>


# MANY TO MANY İLİŞKİ TİPİ (SAYFA ÜZERİNDE SORGULAMA)


```python
    def blog_by_category(request,slug):
        context = {
            "blogs": Blog.objects.filter(is_active=True , category__slug = slug),
            "catagories":Category.objects.all()
        }
        return render(request,"blog/blog.html",context)
```

- burda blog üzerinden bir filitreleme yapmıştık ve bu filitrelemeye de category ve is_active alanlarını atamıştık ve  blog açısından baktığımızda  her almış olduğumuz blogun kategori bilgisine gidiyoruz  böyle değilde biz ilk başta kategoriyi almış olsak ve kategori üzerinden de  o kategoriye ait olan blog bilgilerini almış olsak çok daha güzel  olur 


- **"blogs": Category.objects.get(slug=slug)** context e böyle bir tanımlama yaptık biz burda Category sınıfında ulaştık ve budan .objects diyerrek nesneleri aldın ve tekrar .all diyerek bütün nesneleri aldık bu işlem nasıl çalışıyor örneğin 

- mesela katagorilerimizden birinin adı web programlama  web porgramlama ile ilişkili olan tablo models.py dosyasında tanımladığımız Blog sınıfındaki bloglara erişmek için özel bir isimlerndirme var onu kullanıyopruz

- hangi tabloya geçiş yapacaksak (burda blog modeline ) adını yazarız ve _set deyerek ulaşmış oluyoruz  

```python
    "blogs": Category.objects.get(slug=slug).blog_set.all() 
```

-   blog_set özel bir tanımlamadır o anki ulaşmış olduğumuz katagorilerin altındaki tüm blogları almış oluyoruz ancak hepsini almak bir seçim istersen _set.filter () diyip filitre uygulayabilriiz

```python
    "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True) 
```
-  bu şekilde ilişkili olan katagöride  aktif olan blogları alırız 

- eğer bir blogun kategorierlini kalfırmak istersen kategorisi olmayan bir blog oluşturmak istersen hata alırsın bunun için models.py dosyasında Blog sınıfına tanımladığımız categories metoduna şöyle bir tanımlama yapmıştık;


```python
    categories = models.ManyToManyField(Category)
```


- bu tanımlamaya ek olarak parentez içerisine blank=True tanımlaması yapmamız gerekiyor bu boş değer alsın demek 


# KULLANICI MODELİ OLUŞTURMA VE YAZAR BLOG İLİŞKİSİ

<br>

- ilgili uyguladaki models.py dosyasında yeni bir sınıf oluşturuyoruz ve bu sınıfı "auth.User" ile ilişkilendiriyoruz ancak ilişkilendirme işlemi yaparken **OneToOneField** ilişki tipini kullanıyoz aslında bu ilişki tipi **models.ForeignKey** ile aynı işi yapıyor ancak bunda sadece aynı isimden sadece bir tane kullanıcı oluştururuz foregin key i blog sınıfında kullandık nedeni ise bir kullanıcı birden fazla blog yazabilsin diye



<br>


```python
    class Blog(models.Model):
        blogun_yazari=models.ForeignKey(Yazar, on_delete=models.CASCADE)
        title= models.CharField(max_length=200)
        description = RichTextField()
        image = models.ImageField(upload_to="genelsayfalar")
        is_active=models.BooleanField(default=False)
        is_home = models.BooleanField(default=False)
        yayimlanma_tarihi = models.DateTimeField()
        slug  = models.SlugField(null=False ,blank=True,unique=True, db_index=True,editable=False )
        kaynakca=RichTextField()
        

        
        def save(self , *args , **kwargs):
            self.slug=slugify(self.title)
            super().save(*args,**kwargs)
        
        def __str__(self):
            return self.title
```

<br>


<br>


```python
    class Yazar(models.Model): 

        yazar_adi=models.OneToOneField("auth.User", verbose_name="yazar adi", on_delete=models.CASCADE)
        isim=models.CharField(max_length=500 ,verbose_name="yazar adı ve soyadı" , default="kadir")
        instagram_adresi=models.CharField(max_length=500 , null=True , blank=True)
        facebook_adresi=models.CharField(max_length=500 , null=True , blank=True)
        youtube_adresi=models.CharField(max_length=500 , null=True , blank=True)
        twitter_adresi=models.CharField(max_length=500 , null=True , blank=True)
        web_site=models.CharField(max_length=500 , null=True , blank=True)
        yazar_acıklama=RichTextField(blank=True)
        yazar_resim = models.ImageField(upload_to="genelsayfalar" )

        def __str__(self):
            return self.isim  
```

<br>

- biz Blog  sınıfını ilgili alana zaten göndermiştik

<br>

```python
    #uygulamadaki views dosyası

    def ana_sayfa(request):
            context={
                "blogs":Blog.objects.filter(is_active=True,is_home=True),
            }
            return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)
```
<br>

- blog sınıfında **blogun_yazari**  alanı var biz bu alanı kullanarak oluşturduğumuz modele ulaşabiliriz **(YAZAR)**


<br>

```django
    <span>
        {{genel_bloglar.blogun_yazari.yazar_adi.get_full_name|title}}
     </span>
```
<br>

- genel_bloglar for döngüsünde kullandığımız takma addı bu döngüde sözlük yapısı ile sayfaya gönderdiğimiz Blog objelerine ulaşıyoduk 

- her bir blogun bir yazarı var ve bu yazar adı ile yazara kendi tanımladığımız yazar bilgilerini tutan sınıfa ulaşacağız

- blogun_yazari ile tanımlanan kısım bizim oluşturduğumuz yazar bilgilerini ve kullanıcıları tutan sınıfa gideriz

- ve bu sınıfta da **" auth.User "** sınıfı ile **birebir ilişki kurduğumuz alan var** burdaki alan ile kullancıların kısa adına e posta adresine veya ad soyad bilgilerine ulaşabileceğiz


<br>

```django
    <span>
        {{genel_bloglar.blogun_yazari.instagram_adresi}}
     </span>
```
<br>
<br>



# SAYFALAMA (PAGİNATİON)

<br>


- web sayfasında veritabanından gelen tüm blogları sayfada toplayamayız bu durm hem sayfanın çok kalabalık görünmesi  hem de tüm blogları yüklemeye çalışacağı için istemciye yüklenecektir bunun önüne geçmek için sayfalarımızda fazla olan postları sayfalandırarak bu durumu düzeltmiş olacağız 


- ilgili uygulamanın views dosyasına pagination metodunu import edelim 

<br>

```python
    from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
```
<br>


- ilk başta sayfada gösterilecek olan blog nesnelerinin bir değişkene atarız


- daha sonra Paginator fonksiyonunu çağırırız birinci paremetrede objeleri tuttuğumuz değişken ikinci paremetrede ise sayfada kaç tane görüntüleneceğini belirtiriz

<br>

```python

    def ana_sayfa(request):
        
        blog_list = Blog.objects.filter(is_active=True, is_home=True)

        paginator = Paginator(blog_list,5) 

        page = request.GET.get('page')

        try:
            blogs=paginator.page(page)
        
        except PageNotAnInteger:
            blogs=paginator.page(1)
        
        except EmptyPage:
            blogs=paginator.page(paginator.num_pages)

        context={
            "blogs":blogs,
            "kategori":Catagories.objects.filter(is_active=True),
            "nav_blogs":Blog.objects.filter(is_active=True),
            "manset":Blog.objects.get(manset=True),
            "youtube":Youtube.objects.filter(is_active=True)
        }
        return render(request , "genelsayfalar/ana_sayfa/anasayfa.html" ,context)
```
<br>

-   **page = request.GET.get('page')** ile get metodunu kullanarak sayfadaki blogların bilgisini aldık try except ile olası karşılaşılacak hatalar için bağzı hata kodalrı döndürdük en sonuda da sayfaya göndermek için context sözlüğüne gönderdik 


- kullancıların bloglar arasında gezinmesi yani ileri geri çubuklarının eklenmesi için arayüz sağlamamız lazım


```Django
    {% for genel_bloglar in blogs  %}
        {% include 'genelsayfalar/ana_sayfa/partials/_genel_bloglar.html' %}
    {% endfor %}
    <div class="pagination">
        <span class="step-links">
            {% if blogs.has_previous %}
                <a href="?page=1">&laquo; İLERLE</a>
                <a href="?page={{ blogs.previous_page_number }}">ÖNCEKİ</a>
            {% endif %}

            <span class="current">
                SAYFA {{ blogs.number }} KALAN {{ blogs.paginator.num_pages }}.
            </span>

            {% if blogs.has_next %}
                <a href="?page={{ blogs.next_page_number }}">SONRAKİ</a>
                <a href="?page={{ blogs.paginator.num_pages }}">SON SAYFA &raquo;</a>
            {% endif %}
        </span>
    </div>
```


- blogs yazan kısma views dosyasında sayfaya gönderdiğin sözlük yapsındaki anahtar değeri gelecek ve bu tanımlamayı for döngüsünden hemen sonra kullanmalısın



<br>


# SAYFADA ARAMA YAPMAK
<br>




<br>

# AUTH NEDİR 

- kullanıcılar için hesap oluşturma yetkilendirme işlemidir işlemidir.

- uygulamaya giriş yaptıktan sonra kullanıcılar uygulamaya belirli bir süre giriş yapabilir kullanıcıların tarayıcılarında bir sessionid oluşturulur bu sessionid tarayıcıda bir cookie bilgisine karşılık gelir ve bu id olduğu silinmediği sürece uygulanmaya giriş yapabilir 


- taryıcıda login işlemi yapan bir kullanıcı için sessionid oluşturulur  ve buna bir anahtar  bilgisi verilir bu anahtar bilgisine verilen value değeri  şifrelenmiş bir şekilde veritabanında  saklanır

- şimdilik nav menü kısmında 3 tane daha menü kısmı ekleyelim girş yap kayıt ol ve çıkış yap kısımları olsun 


- griris yap kayıt ol ve çıkış yap linkelerini ma,enü kısmına ekledik kullancı eğer giriş yapmışsa yani bir sessionid varsa çıkış yap linki gösterelim eğer bir sessionid yoksa da giriş yap ve kayıt ol linkleri göseterilmesi gerekiyor bunun için nav menüde bir if blogu oluşturalım

```django
    {% if user.is_authenticated %}
        <li class="nav-item">
            <a class="nav-link" href="">Çıkış yap</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="">Giris Yap</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="">Kayıt Ol</a>
        </li>
    {% endif %}
```

- user.is_authenticated metodu sayfaya biz request gnderiyoruz bu objenin içerisinde de   user.is_authenticated metodu var bu sitede bir sessionid varmı kontrol eder eğer sessionid varsa çıkış yap butonu gösterilir yoksa da giriş yap ve kayıt ol butonaları gösterilir

<br>
<br>




# ACCOUNT UYGULAMASI



- Kullanıcı yetkilendirme ve oturum açma işlemlerini modüler hale getirmek ve daha fazklı uygulamalarda da kullanabilmek için yeni bir uygulama ekleyeceğiz 

- Eklediğimiz uygulamayı root projeye bağlıyoruz , **urls.py** ekleyip  dosyamızda linklerimizi oluşturuyoruz , **views.py** dosyasında gerekli fonksiyonlarımızı yazıyoruz , templates dosyası oluşturup kullanacağımız şablonları ekliyoruz. tüm bu işlemler bittikten sonra **root projedeki urls.py** dosyasına uygulamada tanımladığız urls.py dosaydını include ediyoruz

- views.py dosyadına redirect ve render fonkisyonlarının eklendiğinden emin olmalıyız.
<br>

```python
    path("account/" , include("account.urls")),
```
<br>

```python
    from django.shortcuts import redirect, render
```
<br>

- Biz bu uygulamamızda Giriş yap , Kayıt ol , Çıkış yap ve Profil linkleri oluşturacağız ve bu linkleri sitemizde navbar da göstereceğiz . Bunun için kullanıcının giriş yapıp yapmadığını kontrol etmemiz gerekiyor. Eğer giriş yapmışsa **Profil** ve **Çıkış** yap linkleri görünecek , kullanııc giriş yapmamışsa **Giriş yap** ve **Kayıt  ol** linleri görünecektir
<br>

```py
    {% if user.is_authenticated %}
        <a href="#">Profil</a>
        <a href="#">Çıkış Yap</a>
    {% else %}
        <a href="#">Giris Yap</a>
        <a href="#">Kayıt Ol</a>
    {% endif %}
```





# LOGİN SAYFASI 

- Login sayfasına  formlarımızı oluşturalım

- Kullanıcıların inputlara girdiği verileri  action parametresi ile işleyeceği bir alana göndermemeiz gerekiyor.Biz bu örnekte yine aynı fonksiyon olan **giris_yap** fonksiyonuna gönderdiğimizi varsayalım. Bunun için action kısmına o fonksiyonun çalıştığı urls yapısına tekrar göndermemiz gerekiyor.Bu da **urls.py** dosyasında tanımladığımız link in **name** bilgisini yazmalıyız

<br>


```py
from django.urls import path
from . import views 

urlpatterns = [
    path("giris_yap/" , views.giris_yap , name="giris_yap"),#buradaki name bilgisini actionda kullanacağız veri giris_yap fonksiyonunda işlenecek
    path("cikis_yap/" , views.cikis_yap , name="cikis_yap"),
    path("kayit_ol/" , views.kayit_ol , name="kayit_ol"), 
    path("profil/" , views.profil , name="profil"),
]
```
<br>

- Yukarıda tanımladığımız fonksiyonlarda verileri GET metodu ile sayfalarda çağırırız. POST metodu ile sayfalardan veya formlardan verileri güvenli bir biçimde işlenmesi için  gönderirirz. POST metodu GET metoduna göre daha güvenlidir bu yüzden biz bu işlemi yaparız. 

- Sayfagı GET requesti ile çağırıyorduk bunun için bir fonksiyon tanımlamıştık zaten eğer POST requesti için farklı bir fonksiyon yapıp verileri o fonksiyonda işlemek isteyebilirsin .Burda sadece hangi fonskiyonda işlem yapacaksan **urls.py** dosyasında yeni bir path tanımlayıp yeni bir fonksiyon oluşturmaktır. 

- Ancak biz bu örnkete farklı bir fonksiyon kullanmadan aynı fonksiyon üzerinden işlemlerimize devam edeceğiz.

<br>

```django
    <form action="{% url 'giris_yap' %} method="POST">
        <div class="mb-3">
            <label for="usrnm" class="form-label">Kullanıcı Adı</label>
            <input type="text" class="form-control" id="usrnm" name="username">
        </div>
        <div class="mb-3">
            <label for="psw" class="form-label">Şifre</label>
            <input type="password" class="form-control" id="psw" name="password">
            <a style="text-decoration: none;" class="mt-3 form-text" href="#">Şifreni mi unuttun?</a>
        </div>
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-dark p-2">GİRİŞ YAP</button>
        </div>
    </form>
```
- Sıradaki işlem tanımladığımız fonksiyonda verileri işlemek.Sayfamıza authenticate ve login methodlarımız import ediyoruz. 

- Formdan POST metodu ile gelen verileri (username ve password) bir değişkene atıyoruz. Bunun için ilk başta gelen methodun GET mi POST mu onu öğrenmeliyiz. Bu değerler request in içindeki POST objesinde saklanır. POST objesindeki işleyeceğimiz veriler de sayfadaki formda tanımladığımız **name bilgileridir** yani ;

<br>

```html
    <input type="text" class="form-control" id="usrnm" name="username">
    <input type="password" class="form-control" id="psw" name="password">
```

<br>

- Gelen verileri bir değişkene atarız

```py
if request.method =="POST":
            username= request.POST["username"]
            password= request.POST["password"]
```

- Daha sonra ise authenticate metodu ile bu değerleri karşılayan bir kullanıcımız var mı onu test ederiz. authenticate methodunun ilk paremetresi **request** dir diğer parametreler ise oluşturduğumuz değişkenler (username ve password) .Yine bu değerleri bir değişkene atarız kullanıcının olup olmadığını sınamak için .


<br>

```py
    if user is not None:
        login(request, user)
        return redirect("anasayfa")
    else:
        return render(request, "Account/giris_yap/giris_yap.html" , {  "error" : "kullancı adı veya şifre yanlış"})


```

<br>

- Eğer bu değerleri karşılayan tanımlanmış bir kullanıcı varsa login fonksiyonunu çağırırız . Login fonksiyonun ilk paremetresi request ikinci parametresi ise authenticate metodu ile oluşturduğumuz değişkendir

- Eğer bu değişkenin değeri varsa login işlemi gerçekleştirilir ve redirect methodu ile anasayfaya yönlendiririz. 

### NOT:
- *Redirect metoduna parametre olarak urls.py dosyasındaki tanımladığımız pathlerdeki **name değerlerini** yazarız.*
<hr>

- Eğer kullanıcı yanlış bilgi girmiş ise else blogu çalışır ve buda kullanıcıya bir mesaj gönderebiliriz.

<br>

```py
    else:
        return render(request, "Account/giris_yap/giris_yap.html" , {  "error" : "kullancı adı veya şifre yanlış"})
```

```django

    {%comment%} Hata Mesajı {%endcomment%}

    {% if error %}
        <div class="alert alert-danger">{{error}}</div>
    {% endif %}
```

<br>
<br>


```py
# " TAM KOD " giris_yap fonksiyonu bu şekilde olmalıdır.

    from django.contrib.auth import authenticate , login

    def giris_yap(request):
        if request.method =="POST":
            username= request.POST["username"]
            password= request.POST["password"]

            user = authenticate(request , username = username , password=password)

            if user is not None:
                login(request, user)
                return redirect("anasayfa")
            else:
                return render(request, "Account/giris_yap/giris_yap.html" , {  "error" : "kullancı adı veya şifre yanlış"})

        context={
            "site_ayar":Site_gorunum.objects.get(is_active=True),
            "footer_kontrol":Footer_kontrol.objects.get(is_active=True),
            "kategori":Categories.objects.filter(is_active=True),
        }

        return render(request, "Account/giris_yap/giris_yap.html",context)
```
<br>
<br>

# KAYIT OL (register) Sayfası