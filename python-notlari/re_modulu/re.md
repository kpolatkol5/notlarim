# ***DÜZENLİ İFADELER | REGULAR EXPRESSİON (re)***


<br>


Düzenli ifadeleri kullanarak metin veya karakterler üzerinde saatler sürecek işlemleri çok kısa sürede yapabiliriz. Ancak düzenli ifaderlerin okunması zordur ve karakter dizilerine kıyasla daha yavaş çalışırlar o yüzden olabildiğince karakter dizilerini kullanmakta fayda var. İhtiyacınız olmadan kullanmak kodların okunabilirliğini azaltacaktır. Karakter dizilerini kullanarak uzun kodlar yazmaktan da kaçınmalıyız. Sonuç olarak ikisinin de ortrasını bulmak size kalmış.

<br>


# ***DÜZENLİ İFADELERİN METODLARI***


<br>

Düzenli ifadelerde modül içeriğindeki metod ve nitelikleri öğrenmek için ***dir()*** donksiyonundan faydalanabiliriz.

<br>

```py
    import re

    print(dir(re))
```

<br>

## ***match() :***

<br>


Bir karakter dizisi içerisinde aramak isterdiğiniz karakteri , karakter dizisinin başında arar , daha doğrusu eşleştirme işlemi yapar zaten match ingilizcede eşleşme demektir. Bu metod geriye bir obje döndürür bir örnkele açıklayalım.

<br>

```py
    import re
    
    text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

    result  =   re.match("Lorem", text)

    print(result)  # geriye bir obje döndürdüğünü görebilirsiniz.
    >>> <re.Match object; span=(0, 5), match='Lorem'>
    
    print(dir(result))
    # bu objedeki metodları görüntülemek istersek.
    >>> ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
```


<br>

Eğer string ifadede arayacağımız değer değişkende var ancak başta değilse None değerini döndürecektir.

<br>

```py
    text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

    result  =   re.match("simply", text)

    print(result)
    >>> None
```

<br>

### ***match() eşleşme nesnesinin metodları :***

<br>

- ***span()  :*** Aradığımız ifadenin sorgu dizisindeki yerini gösterir.
- ***group() :*** Aradığımız ifadeyi gösterir. Bu ifade macth objesinde görünsede işlemlerimizde kullanabilmemiz için bu metotdan fayfalanırız.

<br>

```py
    text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

    result  =   re.match("Lorem", text)

    print(result)
    print(result.span())    #ifadenin sorgu dizisindeki yeri
    print(result.group())   #aradığımız ifade
```

<br><hr>

## ***search() :***

<br>

Aramak istediğimiz karakter dizisinin genelinde bir arama yapmak istersek bu metodu kullanabiliriz.Bir örnekle açıklayalım.

<br>

```py
    text    =   "Lorem Ipsum is simply dummy Lorem text of the printing and typesetting industry."
    text2    =   "Ipsum is simply dummy Lorem text of the printing and typesetting industry."

    result  =   re.search("Lorem", text)
    result2  =   re.search("Lorem", text2)

    print(f" text1 :  {result.group()} , {result.span()} " )
    print(f" text2 :  {result2.group()} , {result2.span()} " )
    
    >>>  text1 :  Lorem , (0, 5) 
    >>>  text2 :  Lorem , (22, 27) 
```

<br>

Yukarıdaki örnekte iki tane değişkenimiz var ilk değişkende aramak istediğimiz değerden 2 tane var ancak ***search()*** metodu bize 1 tane değer getirdi ortadaki değere hiç bakmadı. Sonuç olarak bu fonksiyon aradığımız değeri string değişkende bulur ve ilk bulduğu değeri bir obje olarak geriye döndürür. Eğer geçen bütün kelimeleri bulmak istersek bir sonraki metoda bakalım.***findall()***

<br><hr>


## ***findall() :*** 

<br>

String bir değişkende aradğımız değeri almak istersek kullanabiliriz.***search()*** metodu ile benze işleri yapar farkı ise search metodu bulduğu ilk değeri geriye döndürürdü. Bu metod ise string değişkeni arar ve string değişkende geçen tüm değerleri bir liste veri türünde geriye döndürür.


<br>

```py
    text    =   "Lorem Ipsum is simply dummy Lorem text of the printing and typesetting industry."

    result  =   re.findall("Lorem", text)

    print(result)
```
<br>


# ***META KARAKTERLER***

<br>

Meta karakterler programlama dillerinde özel bir anlam ifade eden sembollerdir mesela ***" \t "*** python'da bir sekme boşluk bırakır veya ***" \n "*** bir alt satıra geçer gibi.

## ***Meta karakterler :***

- ***[ ]*** : Köşeli parantez
- ***.*** : Nokta
- ***" * "*** : Yıldız
- ***+*** : artı
- ***?*** : soru işareti
- ***{ }*** : Küme parantezi
- ***^*** : şapka
- ***$*** : dolar
- ***" \ "*** (ters taksim)
- ***|*** : düz çizgi
- ***( )*** : parantez

<br>

## ***[ ] (KÖŞELi PARANTEZ)***

<br>

Bu meta karakter aradığın string değişkendenki değerde istisna karakterler oluşturmamızı sağlar. Bir örnekle açıklayalım. 


<br>


```py
    text    =   "Lorem kadir Ipsum kader is simply dummy Lorem text kadar of the printing and typesetting industry."

    for i in text.split(" "):
        result  =   re.search("kad[iea]r", i)

        if result:
            print(result.group())
```

<br>

Yukarıdaki örnekte aramak istediğimiz string değişkendeki değerlerde sadece 1 harf farklı. Eğer biz bu harfleri istisna olarak belirmek istersek köşeli parntezler arasında yazarız. Aramak istediğimiz değerler ;

- kadir
- kader
- kadar
  
Kodu açıklayacak olursak elimizde bir string değişken var ve biz ilk  başta string değişkendeki tüm karakterler ***.split()*** metodu ile ayırdık ve bir liste olmasını sağladık. Bu listeyi de for döngüsüne aldık ve gelen her karakterede ***.search()*** metodunu kullanarak aradığımız kelimeyi ve istisna karakterleri belirttik. Daha sonra koşul belirterek result değişkeninin True değer içermesi durumunda o andaki değeri ***.group()*** metodu ile ekrana yazdırdık.

Bu örnekte bir karakter için istisnalar belirttik , eğer birden fazla istisna belirtmek istersek köşeli parantezi o kadar kullanmamız gerekiyor. Bir örnkle açıklayalım


<br>

```py
    text    =   "Lorem kadirden Ipsum kaderdir is simply dummy Lorem text kadardır of the printing and typesetting industry."

    for i in text.split(" "):
        result  =   re.search("kad[iea]rd[eiı][nr]", i)

        if result:
            print(result.group())
    >>> kadirden
    >>> kaderdir
    >>> kadardır
```


<br>

### ***Not :*** Eğer aradığımız karakterlerden eşleşen varsa olan karakterleri getirir, aradığımız değerdeki diğer karakterleri getirnmez buna da bir örnek verelim  

<br>

```py
    text    =   "Lorem kadirden Ipsum kaderdir is simply dummy Lorem text kadardır of the printing and typesetting industry."

    for i in text.split(" "):
        result  =   re.search("kad[iea]rd[eiı]", i)

        if result:
            print(result.group())
    >>> kadirde
    >>> kaderdi
    >>> kadardı
```
<br>

- ***[0-9] :*** Ayıklanacak istisna karakterin 0 ile 9 arasındaki herhangi bir rakam olmasını kapsar.
- ***[A-Z] :*** Ayıklanacak istisna karakterlerin A dan Z he bütün ***BÜYÜK HARFLERİ*** kapsar.
- ***[a-z] :*** Ayıklanacak istisna karakterlerin a dan z ye bütük ***KÜÇÜK HARFLERİ*** kapsar.



<br><hr>


## ***. (Nokta)*** 

<br>

Bu meta karakter ise bütün karakterleri temsil eder yeni satır karakteri hariç. Bu metakarakter de sadece 1 tane karakterin yerini tutar.Bir örnekle açıklayalım ;

<br>


```py
    text    =   "Lorem kadiri Ipsum kader2 is simply dummy Lorem text kadarA of the printing and typesetting industry."

    for i in text.split(" "):
        result  =   re.match("kad[iea]r.", i)

        if result:
            print(result.group())

    >>> kadiri
    >>> kader2
    >>> kadarA
```

<br>

Yukarıdaki örnekte birden fazla meta karakter kullandık. Köşeli parantez içerisinde istisna karakterleri belirttik ve en sonra ise ***" . "*** meta karakteri kullandık ve tüm karaktereleri kapsadığını gördük.


<br> <hr>

## * (YILDIZ)

<br>

Bu metakarakter kendisindeki önce gelen karakteri ifade eder ve bu sıfır veya daha fazla sayıda eşleştirir.Yani aranacak string değişkende kendisinden önce gelen karakter kaç  geçerse geçsin ayıklamaya dahil eder. Bir örnekle açıklayalım.


<br>

```py
    liste = ["st", "sat", "saat", "saaat","saaaaaaaaaaaaaaaaaaaat" ,"kat"]

    for i in liste:
        if re.match("sa*t",i):
            print(i)

    >>> st
    >>> sat
    >>> saat
    >>> saaat
    >>> saaaaaaaaaaaaaaaaaaaat
```

<br>

Yukarıdaki örnekte yıldız meta karakteri kendisinden önce gelen karakter kaç kez tekrarlanırsa tekrarlansın değerleri ayıkladı.Ancak bu metakarakterde bir farklılık olduğunu siz de fark etmişsinizdir. Diğer meta karakterler sadece 1 karakterin yerinin tutatken bu metakarakter birden fazla karakterin yerinin tutabiliyor. Başka bir örnek;

<br>

```py
    liste = ["12ASst", "q21wesat", "saVwsdaat","kaaat"]

    for i in liste:
        if re.match(".*at",i):
            print(i)
            
    >>> q21wesat
    >>> saVwsdaat
    >>> kaaat
```
<br>


Bu örnekte ise rastgele karakterler var ve bu değerlerin karkater sayıları eşit değil.Bu aramada ise sonu ***" at "*** ile biten karakterleri getir demiş olduk ve diğer karakterlerin yerini ***" . "*** meta karakteri ve ***" * "*** meta karakterleri ile yerlerini durdurmuş olduk.


<br> <hr>

## ***+ (ARTI)***

<br>

Bu meta karakter yıldız meta karakterine berzer iş yapar tek farkı ***\* (yıldız)*** metakarakteri aranan değerdeki karakterin 0 kez tekrar etmesi veya bir-birden fazla kez tekrar etmesi gerekirken ,  ***+ (artı)*** metakarkterinde aranan değerdeki karakterin en az bir veya daha fazla kez tekrar etmesi gerekir. Bir örnkle açıklayalım ;

<br>

```py
    liste = ["aaahmet", "messssshmet", "met", "ahtapot"]

    for i in liste:
        if re.match(".+met",i):
            print(i)

    >>> aaahmet
    >>> messssshmet
```


<br>

Yukarıdaki örnekte ***" . "*** meta karakterini kullandık. Bu meta karkater tüm karkterlerin yerini alıp ayıklamamızı sağlıyordu . ***" . "*** ve ***" + "*** meta karkterlerinin kombinasyonlarını kullanarak sonu met ile biten değerleri almış olduk. Yani ***" . "*** meta karakterini tekrarlamış olduk . Benzer örneği ***" * "*** meta karakteri ile de yapmıştık ancak bu meta karakter ile yapmış olsaydık met değişkenini de alacaktık.Çünkü ***" * "*** meta karketerinde 0 kez tekrarlanan değerleri de istisna olarak kabul ediyordu. ***" + "*** meta karakteri ise en az bir kez tekrar etmesi gerekir. ***" + "*** ile ***" * "*** meta karakterinin fakları da bu şekilde.

<br> <hr>



## ***? (SORU İŞARETİ)***

<br>

Bu meta karakter ise eşleşme sayısının 0 ya da 1 olmasını kapsar.

<br>

```py
    text    =   "st sat saat saaat kadir"

    for i in text.split(" "):
        if re.match("sa?t", i):
            print(i)
    >>> st
    >>> sat
```

<br>

Yukaridaki örnekte a karakterşnin hiç olmadığı veya 1 kez olduğu karakterleri ayıklamış olduk.

<br> <hr>


## ***{ } (KÜME PARANTEZİ)***

<br>


Bu meta karkater ile kendisinden önce gelen karakterin kaç kez tekrarlanacağını belirtebiliriz. Bir örnekle açıklayalım

<br>

```py
    text    =   "st sat saat saaat kadir"

    for i in text.split(" "):
        if re.match("sa{2}t", i):
            print(i)
    
    >>> saat
```


<br>

Yukarıdaki örnkete ilk karakteri s olan , a nın 2 kez tekrarlandığı ve t ile biten karakterleri getirecektir (saat) . Eğer istersen alt limit ve üst limit de belirleyebiliriz bunun için bir sonraki örneğe bakalım.

<br>


```py
    text    =   "st sat saat saaat kadir"

    for i in text.split(" "):
        if re.match("sa{1,2}t", i):
            print(i)

    >>> sat
    >>> saat
```

<br><hr>

## ***^ (ŞAPKA)***

<br>



Bu meta karkaterin iki işlvi vardır;

1. match() metodu ile aynı işlevi yapar yani karakter dizisindeki ilk veriyi sorgular.
2. ***[ ] köşeli parantez*** içerisinde kullanıldığı zaman ***hariç anlamı*** taşır. Mesela [^A-Z] büyük harfler hariç gibi , bunlar ayıklama işlemine dahil edilnmez.

<br>

### ***1. İşlevi***

<br>

```py
    text        =   "st sat saat saaat kadir"

    result      =   re.search("^s.", text)
    result2     =   re.search("^k.*", text)

    print(result)
    print(result2)
    
    >>> <re.Match object; span=(0, 2), match='st'>
    >>> None
```

<br>

Yukarıdaki örnekte herhangi bir string değişkende ***search()*** metodunu kullanarak arama yaptık. Normalde search() metodu string değişkenin genelinde bir arama yapardı. Şapka meta karakterini kullanarak sadece string değişkenin başında arama yaptığını aynı ***match()*** metodu gibi davrandığını görebiliriz.

Ancak search metodunda çıkan değeri tanımladığımız kadarını getirir ve gerisini kırpar. Bunun tanımını yapmak biraz zor bir örnekle açıklayalım.

<br>

```py
    text      =   "kadir st sat kadir saat saaat"


    for i in text.split():
        result  =   re.search("^k.", i)
        if result:
            print(result.group())

    >>> ka
    >>> ka
```
<br>

Yukarıdaki örnekte string değişkeni split metodu ile parçaladık liste veri türüne çevirdik. For döngüsü ile gelen her string karakterin ***" k "*** ile başlaması durumunu ele aldık. Ancak örnekte de olduğu gibi bizim tanımladığımız meta karakterler kadarını getirdi. String ifadede kadir var ancak biz k ile başlayan ve ***" . "*** meta karakterini kullanarak değerleri aldık. ***" . "*** meta karakteri herhangi bir karakterin yerini tutuyordu. Sonuç olarak da bize belirttiğimiz kısmla eşleşen karkaterleri getirdi ve geriye kalan karakterleri kırptı.


Eğer karakterleri kırmadan geriye kalan kısmı da almak istersek ***" . "*** ve ***" * "*** meta karatkelerinin kombinasyonlarını kullanabiliriz.

<br>

```py
    text      =   "kadir st sat saat kadir saaat"


    for i in text.split():
        result  =   re.search("^k.*", i)
        if result:
            print(result.group())

    >>> kadir
    >>> kadir
```
<br>

### ***2. İşlevi***

<br>

Bu meta karakterin 2. işlevi ancak köşeli parnatez içerisinde kullanılıdğında tanımlıdır. Köşeli parantez içerisinde kullanıldığı durumlarda o ifadeleri ayıklama işlemine dahil etmez hariç anlamını taşır. Bir örnek ile açıklayalım.


<br>

```py
    text      =   "kAdir st sat saat ka2dir  kadir kaDir2 saaat"

    for i in text.split():
        result  =   re.search("k[^A-Z][^0-9].*", i)
        if result:
            print(result.group())

    >>> kadir
    >>> kaDir2
```
<br>

Yukarıdaki kanser örneği anlamak biraz zor olabilir o yüzden tek tek açıklayacağım;

String ifadeyi split() metodu ile parçaladık ve for döngüsü ile tüm karakterleri tek tek aldı.

- ***search()*** metodu ile ilk karakterin k ile başlayacağını belirttik.
- 2 karakterin ***BÜYÜK HARFLER OLMAYACAĞINI BELİRTTİK*** *kAdir* karakteri elendi ve geriye *ka2dir* *kadir* *kaDir2* 
- 3 karakterin sayı olmayacağını belirttik ve *ka2dir* de elendi geriye *kadir* ve *kaDir2* kaldı
- Bir sonraki meta karakter de ***" . "*** bu meta karakter herhangi bir karakteri temsil ediyordu ***" * "*** meta karakteri ile beraber kullanınca geriye kalan kısmı kırpmadan almamızı sağladı. 


<br> <hr>

## ***$ (DOLAR)***

<br>
Bu metakarakter dizilerin nasıl biteceğini belirliyor.

<br>

```py
    text    =   "kadir3  asda kadar5 turşu falan3 34 python3"

    for i in text.split(" "):
        result  =   re.search(".*[0-9]$", i)
        if result:
            print(result.group())

    >>> kadir3
    >>> kadar5
    >>> falan3
    >>> 34
    >>> python3
```
<br>

Yukarıdaki örnekte son karakteri sayı ile biten tüm değerleri aldık ***" . "*** ve ***" * "*** meta karakterlerini de kullanarak kırpma işlemi yapmasının önüne geçmiş olduk. Eğer bunları kullanmasadık değerlerdeki son karakteri yani sadece sayıları getirecekti geriye kalan kısmı kırpacaktı.

<br><hr>


### ***\ (TERS TAKSİM)***

<br>

Bu bildiğimiz kaçış karakteri. Eğer strin değişkende ayıklayacağımız karakterler meta karakterlerden biri ise (^ , + gibi) bu kaçış dizisini kullanırız. Bir örnek verelim.

<br>


```py
    text    =   "10+ google+ parol+ kadir topla+"

    for i in text.split():
        result  =   re.search(".*\+$", i)
        if result:
            print(result.group())

    >>> 10+
    >>> google+
    >>> parol+
    >>> topla+
```
<br>

Yukarıdaki örnekte sonu + ile biten tüm karakterkeri almak istediğimizi varsayalım. ***" + "*** normalde meta karakter eğer biz kaçış karakterini kullanmazsak istediğimiz sonucu alamayız. Bu yüzen + karakterinin önüne \ kullandık ve bunun metakarakter olmadığını belirttik. bu şekilde sonu + ile biten tüm karakterleri almış olduk.


<br> <hr>

### ***| (DİK ÇİZGİ)***

<br>

Birden fazla metakarakter kalıbını kullanamızı sağlar . or karakteri gibi çalışıyor iki durumdan bir dahi eşeşlemi sağlarsa ayıklamaya dahil eder. Bir örnekle açıklayalım.

<br>

```py
    text    =   "10+ google+ parol+ Kadir kadir+ topla+"

    for i in text.split():
        result  =   re.search("[a-z].*\+$|[A-Z].*", i)
        if result:
            print(result.group())

    >>> google+
    >>> parol+
    >>> Kadir
    >>> kadir+
    >>> topla+   
```

<br>

Bunu daha basit bir şekilde de yapabilirdik ancak örnek olması için ve bu ifadeyi kullanabilmek için böyle bir örnek yaptık.

<br>

- Birinci ifade kalıbında sadece küçük harfle başlayan ve sonu + ile biten karakterleri ayıkladık.
- İkinci ifadede ise Büyük harfle başlayan karakterleri ayıkladık.

<br><hr>

## ***( ) PARANTEZ*** 

<br>

Yazdığın kalıpları guruplamak için kullanılıyor. Matematikteki gibi öncelik belirlerken kullanmak gibi dişünebilirsin. Bir örnekle açıklayalım.


<br>

```py

    text    =   "10+  google+ parol+ Kadir Kadirsdfgs+ kadir+ topla+"

    for i in text.split():
        result  =   re.search("([K-k]adir)\+$", i)
        if result:
            print(result.group())

    >>> kadir+
```

<br>

### ***ÖR-2 ;***

<br>

```py
    text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"


    for i in text.split(" "):
        result  =   re.search("(Lorem Ipsum)|(is)|(simply)|(dummy text)|(of)|(the printing and)|(typesetting)|(industry)", i)
        if result:
            print(f"sonuç:   {result.group()}")
        else:
            print("sonuç:   yok")

    >>> sonuç:   yok
    >>> sonuç:   yok
    >>> sonuç:   is
    >>> sonuç:   simply
    >>> sonuç:   yok
    >>> sonuç:   yok
    >>> sonuç:   of
    >>> sonuç:   yok
    >>> sonuç:   yok
    >>> sonuç:   yok
    >>> sonuç:   typesetting
    >>> sonuç:   industry
    
```

<br>

Yukarıdaki örnekte aramak istediğimiz karakterleri parantezler ile guruplara ayırdık. Ayrıca | meta karakterini de kullandığımıza dikat edin. Bu sayede parantez içerisindeki karakterlerden herhangi birisinin eşlenmesi durumunda , eşleşen sonucu yazdırıyoruz.


<br><br>


# ***EŞLEŞME NESNESİNİN METODLARI***

<br>


## ***group() :***

<br>

Bu metod sayesinde bir eşleşme nesnesinin , eşleşen karakter dizisini temsil ediyordu. Bu  metodu ***" ( ) "*** meta karakteri ile guruplandırarak daha verimli sonuçlar alabiliriz. Bir örnekle açıklayalım ;

<br>

```py
    text     =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

    result2  =   re.search("(Lorem) (Ipsum) (is) (simply) (dummy) (text) (of) (the) (printing) (and) (typesetting) (industry)", text)


    print(result2)
    print(result2.group())
    print(result2.group(0))
    print(result2.group(1))
    print(result2.group(2))
    print(result2.group(3))
    print(result2.group(4))

    >>> <re.Match object; span=(0, 73), match='Lorem Ipsum is simply dummy text of the printing >
    >>> Lorem Ipsum is simply dummy text of the printing and typesetting industry
    >>> Lorem Ipsum is simply dummy text of the printing and typesetting industry
    >>> Lorem
    >>> Ipsum
    >>> is
    >>> simply
```

<br>

Yukarıdaki örnekte de olduğu gibi parantez içerisine yazdığımız değerler () meta karakteri ile ayırdığımız gurupları tek tek veriyor.

<br><hr>

## ***groups() :***

<br>


Bu metod ise kullanabileceğimiz tüm gurupları demet veri türünde geriye döndürür.



<br>

```py
    text     =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

    result  =   re.search("(Lorem) (Ipsum) (is) (simply) (dummy) (text) (of) (the) (printing) (and) (typesetting) (industry)", text)

    print(result.groups())

    >>> ('Lorem', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting', 'industry')
```

<br>


# ***ÖZEL DİZİNLER :***

<br>


1. ***\s özel dizisi :*** boşluk karakterlerini ayıklar.
2. ***\d özel dizisi :*** ondalık sayıları ayıklar. ***[0-9]***
3. ***\w özel dizisi :*** alfanümerik karakterleri ve “_” karakterini ayıklar.***[A-Za-z0-9_]***


<br>

## ***Ters işlem yapan özel dizinler;***

<br>

1. ***\S özel dizisi :*** boşluk olmayan karakterlerini ayıklar.
2. ***\D özel dizisi :*** sayı olmayanları ayıklar. ***[^0-9]***
3. ***\W özel dizisi :*** alfanümerik olmayan  ve “\_” olmayan karakterleri ayıklar. ***[^A-Za-z0-9_]***


<br>

# ***DÜZENLİ İFADELERİN DERLENMESİ***

Düzenli ifadeler karakter dizilerine göre daha yavaş çalıştığını öğrendik. Düzenli ifadelerin daha hızlı çalışması için derleme metodu olan ***compile()*** metodundan faydalanacağız. Düzenli ifade kalıplarını (meta karakterleri) compile() metodu ile önce derlememiz gerekiyor. Büyük projlerde çok önemlidir!!!

<br>

```py
    text     =   "Lorem Ipsum is simply 2Dummy text of 5the printing and typesetting industry"


    derle   =   re.compile("\d[A-Z].*")

    for i in text.split(" "):
        result  =   derle.search(i)
        if result:
            print(result.group())

    >>> 2Dummy
```



<br>

## ***DERLEME SEÇENEKLERİ*** 

<br>

### ***re.IGNORECASE*** veya ***re.I***


<br>

Bu seçenek büyük harf küçük harf duyarlılığını kaldırır.Bir örnekle açıklayalım.

<br>

```py
    text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"


    derle   =   re.compile("(lorem)" , re.IGNORECASE)

    for i in text.split(" "):
        result  =   derle.search(i)
        if result:
            print(result.group())

    >>> Lorem
    >>> lorem
    >>> loRem
```

<br>


### ***re.DOTALL*** veya ***re.S***

<br>

***" . "*** meta karakteri yeni satır karakterinin ***( \n )*** yerini tutmuyordu. Eğer yeni satır karakterleri varsa ve biz bu karakterlerin de okunmasını istersek bu seçeneği kullanabiliriz. Bir örnekle açıklayalım.

<br>

```py
    text     =   "Lorem Ipsum is simply dummy text of\n lorem the printing and typesetting loRem industry"

    derle   =   re.compile("(lorem).*" , re.IGNORECASE)

    print(derle.search(text).group())

    >>> Lorem Ipsum is simply dummy text of
```

<br>

Yukarıdaki örnekte of dan sonrasını okumadı ***" . "*** meta karakteri \n yerini alamıyor.(ben büyük harf küçük harf duyarlı olsun diye compile() metodu ile birlikte kullandım ) . Eğer geriye kalan kısmı da amak istersek ***re.DOTTAL*** parametresi ile birlikte kullanmamız gerekiyor.  



<br>

```py
    text     =   "Lorem Ipsum is simply dummy text of\n lorem the printing and typesetting loRem industry"

    derle   =   re.compile("(lorem).*" , re.DOTALL)

    print(derle.search(text).group())

    >>> lorem the printing and typesetting loRem industry
```

<br>

Yukarıdaki örnekte de olduğu gibi \n (yeni sekme) karkaterlini atlamasını sağladık.


<br>



# METİN VEYA KARAKTER DİZİSİ DEĞİŞTİRME İŞİLEMLERİ


<br>

## ***sub() :***

<br>

Bu metod karakter dizilerinde değiştirme işlemi yapar. ***replace()*** metoduna benzer. Bir örnekle açıklayalım

```py
    text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"

    derle   =   re.compile("lorem" , re.IGNORECASE)

    liste=[]

    for i in text.split(" "):
        result  =   derle.search(i)

        if result:
            result  =   derle.sub("Kadir", i)
            liste.append(result)
            # EŞLEŞME VARSA EŞLEŞEN KELİMEYİ DEĞİŞTİRİP LİSTEYE EKLEYECEKTİR
        else:
            liste.append(i)
            # EĞER EŞLEŞME YOKSA DEĞİŞTİRECEĞİMİZ BİR KARAKTER DE YOKTUR O YÜZDEN DİREKT EKLEDİK.
            
    print(liste)
    ['Kadir', 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'Kadir', 'the', 'printing', 'and', 'typesetting', 'Kadir', 'industry']
```

<br><hr>

## ***subn() :***

<br>

Bu metod ise ***sub()*** metoduna  benzer iş yapar. Farkı ise metin içinde yapılan değişiklik sayısını göstermesidir.




```py
    text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"

    derle   =   re.compile("lorem" , re.IGNORECASE)

    liste=[]

    for i in text.split(" "):
        result  =   derle.search(i)

        if result:
            result  =   derle.subn("Kadir", i)
            liste.append(result[0])
            # EŞLEŞME VARSA EŞLEŞEN KELİMEYİ DEĞİŞTİRİP LİSTEYE EKLEYECEKTİR

        else:
            liste.append(i)
            # EĞER EŞLEŞME YOKSA DEĞİŞTİRECEĞİMİZ BİR KARAKTER DE YOKTUR O YÜZDEN DİREKT EKLEDİK.
            
    print(liste)
    [('Kadir', 1), 'Ipsum', 'is', 'simply', 'dummy', 'text', 'of', ('Kadir', 1), 'the', 'printing', 'and', 'typesetting', ('Kadir', 1), 'industry']
```

<br>

Ayrıca bu metod geriye bir tuple döndürür. bu tuple nin 1. index i değiştirilen karakter , 2. index i ise kaç kez değiştirildiğidir.