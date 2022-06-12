# ***FONKSİYONLAR***
<br>

Karmaşık işlemleri tek adımda yapmamızı sağlayan kod parçalarıdır. Sürekli tekrar edilen , verilen  görevleri yerine getirirler.Programlama dillerinde kod tekrarının yapılmaması için önemli bir yeri vardır. 

<br> <hr>

## ***FONKSİYONLAR NASIL TANIMLANIR ?***

<br>

Bir örnek üzerinden açıklayalım.

<br>

```py
    def us_al(num):
        
        print(num**2)

    us_al(5)
```
<br>

Bir fonksiyon tanımlamak için ***def*** ifadesinden yararlanıyoruz. def değiminden sonraki ***us_al*** ifadesi tanımladığımız fonksiyonun adıdır.Daha sonra parantez içerisinde belirttiğimiz kısım , tanımladığımız fonksiyonun paramterleridir. Bu parametreleri fonksiyonun içinde kullanırız.Burda dikkat etmemiz gereken şey fonksiyonları çağırmadan kullanamıyor olmamız. Aşağı tarafta fonksiyonu çağırdık ve parametreyi verdik ve verdiğimiz paramterenin üssünü aldı ve ekrana yazdırdı.Fonksiyonu tanımladıktan sonra işlemi yaptığımız alanda girinti bırakmayı unutmayın yoksa hata alırsınız.

<br><hr>

## ***PARAMETRE TANIMLAMAK***

<br>


Önceki örnkete tanımladığımız fonksiyonda parantez içerisine prametreler tanımladığımızı öğrendik. Bu parametreleri kullanarak fonksiyon içerisinde işlemler yapabiliryoruz. Ancak parametre tanımlarken uymamız gereken bağzı kurallar var bunları açıklayalım ;

<br>

- Parametrelere ne isim verdiğimizin bir önemi yok ancak kodun okunaklılığını arttırmak için o parametre ne işi yapacaksa onunla ilgili anlamlı parametreler tanımlamakta fayda var.
- Değişken adlarını tanımlarken uymamız gereken kuralların hepsi parametre tanımlarken de geçerlidir.
- Fonksiyonları çağırıken eksik parametre girmemeliyiz. Eğer eksik girilmesini istersen varsayılan parametre kullanmamız gerekir.
  

<br>

```py
    def kullanici_ekle(isim, soyisim , yas ):
        
        bilgiler    =   """
        {} isimli kullanıcının bilgileri;

        Kullanıcının adı            :   {} , 
        Kullanıcının soyadı         :   {} , 
        Kullanıcının yaşı           :   {} ,
        Kullanıcının doğum tarihi   :   {}, 
        """
        print(bilgiler.format(isim,isim,soyisim,yas,2022-yas))


    kullanici_ekle("kadir", "polatkol", 22)
```

<br>

Yukarıdaki örnekte kullanıcıların bilgilerini ekleyebileceğimiz bir fonksiyon tanımladık. Fonksiyon tanımlarken istenilen tüm parametreleri verdik. Eğer bu fonksiyonu çağırıken parametrenin birini eksik girersek;

```py
    def kullanici_ekle(isim, soyisim , yas ):

        bilgiler    =   """
        {} isimli kullanıcının bilgileri;

        Kullanıcının adı            :   {} , 
        Kullanıcının soyadı         :   {} , 
        Kullanıcının yaşı           :   {} ,
        Kullanıcının doğum tarihi   :   {}, 
        """
        print(bilgiler.format(isim,isim,soyisim,yas,2022-yas))


    kullanici_ekle("kadir", "polatkol")
    
    # alacağımız hata
    >>> Traceback (most recent call last):
    >>> File "c:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/fonksiyonlar/fonksiyonlar.py", line 26, in <module>
    >>>     kullanici_ekle("kadir", "polatkol")
    >>> TypeError: kullanici_ekle() missing 1 required positional argument: 'yas'
```


<br><hr>



## ***VARSAYILAN PARAMETRE TANIMLAMAK***
<br>

Yukarıdaki örnekte de olduğu gibi tanımladığımız parametreleri eksik girdik ve hata aldık. Varsayalım ki fonksiyonda bir parametre tanımladık ve bu parametreye bir değer gitmediği durumlarda yine bizim  tanımladığımız varsayılan parametre ile işlem yapsın. Bununla ilgili bir örnek verelim.

<br>


```py
    def kullanici_ekle(isim = "bilinmiyor", soyisim ="bilinmiyor" , yas = "bilinmiyor" ):

        bilgiler    =   """
        {} isimli kullanıcının bilgileri;

        Kullanıcının adı            :   {} , 
        Kullanıcının soyadı         :   {} , 
        Kullanıcının yaşı           :   {} ,
        Kullanıcının doğum tarihi   :   {}, 
        """
        print(bilgiler.format(isim,isim,soyisim,yas, yas  if yas == "bilinmiyor" else 2022-yas ))

        # Burada hata almamak için doğum tarihi hesaplamasında farklı bir if kullanıldı. Eğer yas paramteresinin değeri "bilinmiyor ise direkt yazdırılacaktır yani if bloğunun sol tarafı çalışır eğer bilinmiyor değil ise if blogunun sağ tarafı çalışır ve işlem yapar"

    kullanici_ekle("kadir", "polatkol",22)

    >>> kadir isimli kullanıcının bilgileri;

    >>> Kullanıcının adı            :   kadir ,
    >>> Kullanıcının soyadı         :   polatkol ,
    >>> Kullanıcının yaşı           :   19 ,
    >>> Kullanıcının doğum tarihi   :   2003,
```

<br>

Yukarıdaki örnekte varsayılan değer tanımladık eğer hiçbir değer girmezseninz ilgili alanlara ***bilinmiyor*** yazdıracaktır.

<br> <hr>

## ***İSİMLİ PARAMETRE TANIMLAMAK***

Fonksiyonları çağırdığımız zaman parametrelerin sırası çok önemlidir. Eğer paramtereleri sırasını yanlış girersek ilgili parametre ile yanlış değerlerin gitmesi demektir. Dolayısıyla yazdığımız program çökebilir.
Yazdığımız fonksiyonda sıranın önemsiz olmasını istersen paramterelerin adlarına göre tanımlamam yapmamız gerekir. Bunu bir örnekle açıklayalım.

<br>

```py
    def kullanici_ekle(isim = "bilinmiyor", soyisim ="bilinmiyor" , yas = "bilinmiyor" ):

        bilgiler    =   """
        {} isimli kullanıcının bilgileri;

        Kullanıcının adı            :   {} , 
        Kullanıcının soyadı         :   {} , 
        Kullanıcının yaşı           :   {} ,
        Kullanıcının doğum tarihi   :   {}, 
        """
        print(bilgiler.format(isim,isim,soyisim,yas, yas  if yas == "bilinmiyor" else 2022-yas ))

    kullanici_ekle(yas=20, soyisim="polatkol", isim="kadir")

    >>> kadir isimli kullanıcının bilgileri;

    >>> Kullanıcının adı            :   kadir ,
    >>> Kullanıcının soyadı         :   polatkol ,
    >>> Kullanıcının yaşı           :   19 ,
    >>> Kullanıcının doğum tarihi   :   2003,
```

<br>

Fonksiyonu çağırıdğımız kısma iyi bakın , fonksiyonda tanımladığımız parametreleri , vereceğimiz değerlerle eşitledik ve sırasını farklı yazdık. Bu şekilde yaptığımız sürece parametrelerin sırası pek de önemli değil.

<br> <hr>

## ***RASTGELE ve SINIRSIZ SAYIDA İSİMSİZ PARAMETRE BELİRTMEK (\*ARGS)***

<br>

Bazen yazdığımız fonksiyonlarda ne kadar parametre geleceğini tahmin edemeyiz. Bunun için sınırsız sayıda isimsiz paramerte belirleyebildiğimiz fonksiyonlar yazarız. Bir örnek verip bu örneği açıklayalım;

<br>

```py
    def getir(*args):

        return args
        # return ilerleyen kısımlarada anlatılacak

    # getir("kadir" ,"polatkol" , "20 " ,20000)

    result  =   getir("kadir" ,"polatkol" , "20 " ,20000)
    print(result)
    print(type(result))
   
    >>> ('kadir', 'polatkol', '20 ', 20000)
    >>> <class 'tuple'>
```

<br>

Yukarıdaki örnekte olduğu gibi fonksiyonumuza args (args yerine başka bir şey de tanımlayabilirsin) ile sınırsız parametre alabilme özelliği kazandırdık. Burada özellikle göstermek istediğim kısım args ile aldığımız değerlerin veri türü ***tuple*** dir. Biz tuple veri türleri ile yapabileceğimiz tüm işlemleri artık burda da yapabiliriz.

<br> <hr>



## ***RASTGELE VE SINIRSIZ SAYIDA İSİMLİ PARAMETRE BELİRTMEK (\*\*KWARGS)***


<br>

Yukarıdaki *args tanımımızda isimsiz parametreleri nasıl tanımlıyorsak bu sefer parametreleri isimlerndirerek tanımlayacaz. args da bize tuple verirken burda bize sözlük verecektir.Örnekle daha iyi anlaşılacaktır.
<br>

```py
    def getir(**kwargs):

        return kwargs
        
    # getir("kadir" ,"polatkol" , "20 " ,20000)

    result  =   getir(isim="kadir" ,soyisim="polatkol" ,yas= "20 " ,dt= 2000)
    print(result)
    print(type(result))

    >>> {'isim': 'kadir', 'soyisim': 'polatkol', 'yas': '20 ', 'dt': 2000}
    >>> <class 'dict'>      
```
<br>

Yukarıdaki örnekte tanımladığımız fonksiyonu çağırırken parametre isimlerini kendimiz belirledik ve belirlediğimiz parametre isimlerine değerler atadık ve artık bu parametrelere göre yapacağınız işlemler size kalmış. Sözlük metodlarınıda burda istediğiniz gibi kullanabilirsiniz.

<br>

```py
#   ÖR-1:

    def getir(**kwargs):

        for par1 , par2 in kwargs.items():
            print(f"{par1}\t:  {par2}")

    getir(isim="kadir" ,soyisim="polatkol" ,yas= "20 " ,dt= 2000)

    # items() fonksiyonu sözlüklerde anahtar ve değer öğelerini verir for döngüsündeki par1 sözlükteki anahtar değerini temsil ederkn , par2 değeri de anahtarın değerini temsil eder.
```
<br>

```py
    #   ÖR-2:
    def bul(*args, **kwargs):
        for par1 in args:
            if par1 in kwargs:
                print(f"{par1} : {kwargs[par1]}")

    sözlük = {"ad"      : "kadir",
            "soyad" : "polatkol",
            "yas": "21"}

    bul("ad", "soyad", "yas", "dt", **sözlük)
```
<br>

Bu örnekte ise elimizde bir sözlük var ve bu sözlükteki anahtar değerlerini sırasız liste ile verdiğimiz değerlerle(*args) kıyaslıyoruz. Eğer sözlükte varsa parametre ile sözlükteki değeri eşleştirip ekrana yazdırıyoruz.

<br> <hr>



## ***RETURN :***

<br>

Return değimi fonksiyonlarda eğer çıktıyı başka bir yerde kullanmak istersek bize fonksiyondaki değeri döndürür. Anlaması biraz zor olabilir örnekle açıklayalım.

<br>

```py

    def isim_ne():
        result  =   input("isminiz nedir?")
        print(f"{result} ")

    result  =   isim_ne()

    print(result)

    print(f"merhaba {result} nasıl gidiyor.")

    >>> isminiz nedir?kadir
    >>> kadir 
    >>> None
    >>> merhaba None nasıl gidiyor.
```

<br>

Yukarıdaki örneğin tek görevi ekrana bir şeyler yazdırmak. ben bu fonksiyondaki değeri başka bir değişkene atamak istersem return kullanmam gerekir. İyi anlaşılabilmesi için daha basit bir örnek verelim.

<br>

```py
    def isim_ne():
        result  =   input("isiminiz nedir?   ")

    print(isim_ne())
    >>> isiminiz nedir?   kadir
    >>> None
```

<br>

Gördüğünüz gibi çıktı None . Bir de aynı örneği return ile yapalım.

<br>

```py
    def isim_ne():
        result  =   input("isiminiz nedir?   ")
        return result
        
    print(isim_ne())

    >>> isiminiz nedir?   kadir
    >>> kadir
```

<br>

Artık fonksiyondan çıkan değeri bir değişkende kullanabiliyoruz. Bu örnek geriye bir liste de döndürebilirdi eğer dönen bir listede for döngüsü kullanmamız gerekiyorsa kesilikle burda return kullanmamız gerekir.

<br>

```py
    def deger_gir():
        liste   =   []

        while True:
            result  =   input("deger gir?   ")
        
            if result == "q":
                break
            else:
                liste.append(result)
        return liste

    result  =   deger_gir()
    print(*result , sep="\n")

    >>> deger gir(çıkmak için q ya basın) :   kadir
    >>> deger gir(çıkmak için q ya basın) :   polatkol
    >>> deger gir(çıkmak için q ya basın) :   hatay
    >>> deger gir(çıkmak için q ya basın) :   20
    >>> deger gir(çıkmak için q ya basın) :   q
    >>> kadir
    >>> polatkol
    >>> hatay
    >>> 20
```

<br><hr>

## ***GLOBAL KAVRAMI*** 

<br>


Kodlarımızı normal akışta tanımladığımız alan bizim için global alanlardır. Fonksiyon içerisinde tanımladığımız değişkenler veya değerler de ***local alanlardır*** ve fonksiyon içinde tanımlıdırş. Global alandaki herhangi bir değerle karışmaz .Aynı zamanda  global alanda tanımlanmış bir değişken de fonksiyonun local alanında tanımlanan bir değişkenle de  karışmaz. Bir örnek verelim

<br>

```py
    result  =   "Bu alan global alandır ve local alandaki değişkenden farklıdır"

    def local_alan():
        result  =   "bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır."

        return result

    print(result)
    print(local_alan())

    >>> Bu alan global alandır ve local alandaki değişkenden farklıdır
    >>> bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.
```

<br>

Yukarıdaki örnekte de olduğu gibi değişken isimleri aynı olduğu halde değerler birbirinden farklı çıktı. Kısacası şu fonksiyonun içerisinde tanımladığımız alanlar o fonksiyona özeldir ve global alandan etkilenmez.

<br>


***ANCAK ;*** 

Fonksiyonun local alanında ilgili değişken tanımlı değilse global alana taşabilir. Bir örnekle açıklayalım.


<br>


### ***ÖR-1***
```py
result  =   []

    def local_alan():
        return result.append("bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.")
        # result global alanda tanımlı local alanda tanımlı değil
    print(result)
    local_alan()
    print(result)

    >>> []
    >>> ['bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.']
```

<br>

### ***ÖR-2***

```py
    result  =   []
    
    def local_alan():
        result  = []

        result.append("bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.")
        return result 
        # result local alanda tanımlı global alanda tanımlı olan listeye değer aktarılamadı.

    print(result)
    print(local_alan())
    print(result)

    >>> []
    >>> ['bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.']
    >>> []
```


<br>

Birinci örnekte global alandaki result listesine veriler eklendi bunun nedeni local alanda result değişkenini aradı ve bulamadı. Bulamadığı için global alanda  yukarıya doğru tarama yaparak bulduğu ilk result listesine veriyi ekledi. 

İkinci örnekte ise global alanda değişken tanımlanmış ve aynı değişken local alanda da tanımlanmış. Python ilk başta local alanı taradı ve bulduğu listeye veriyi ekledi.

Eğer nesneler değiştirilebilir bir nesne ise local alandan o nesnenin değerini değiştirebilirsin. karakter dizileri değiştirilemez yeniden tanımlanır o yüzden fonksiyonun local alanından karakter dizikerini değiştirmeye çalışırsanız hata alırsınız. Global alandaki bir listeyi local alanda yeniden tanımlanamaz ancak yeni veriler eklenebilir . Nasıl veri eklendiğine dair örnek vermiştik bir de nasıl değiştirilemezle ilgili örnek verelim.

<br>

```py
    result  =   []

    def global_liste_degis():
        result += ["kadir", "polatkol"]
        return result
        
        #burada listeye veri eklemedik listeyi yeniden tanımladık , aynı durum karakter dizileri için de geçerlidir.

    print(result)
    global_liste_degis()
    print(result)

    >>> Traceback (most recent call last):
    >>> File "c:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/fonksiyonlar/fonksiyonlar.py", line 265, in <module>
    >>>     global_liste_degis()
    >>> File "c:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/fonksiyonlar/fonksiyonlar.py", line 260, in global_liste_degis
    >>>     result += ["kadir", "polatkol"]
    >>> UnboundLocalError: local variable 'result' referenced before assignment
```


<br>

Yukarıdaki örnekte yaptığımız işlemi yapmak  istiyorsunuz yani amacınız global alandaki bir veriyi değiştirmek olsun. Bunu yapabilmek için ***global*** değiminden faydalanacağız. Bu değimin amacı global alandaki bir değişkeni veya değeri fonksiyonda tanımlı olan local alana çağırmak. Bu durum global alandaki değişkende değerin değişmesine yol açacaktır. Bu yüzden bu aracı kullanırken dikkatli olmakta fayda var. Çünkü global alanın kirlenmesi , hata yapmamıza sebep olabilir, programın hatalı çalışması kötü sonuçlar ortaya çıkartabilir. Bir örnekle açıklayalım 


<br>

```py
    text    =   "kadir"

    def degistir():
        global text
        
        text    +=  " polatkol" 
        return text

    print(text)
    degistir()
    print(text)

    >>> kadir
    >>> kadir polatkol
```

Global alandaki değişkenin de değiştiğini görebilirsiniz.

<br><hr>




