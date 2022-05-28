# ***OS MODÜLÜ NEDİR NE İŞE YARAR***

<br>


Os modülü python da hazır olarak gelir. Dosya dizin işlemlerinde işlerimizi kolaylaştrır. Kısacası işletim sistemleri ile iletişim kurabilmemizi sağlar.

<br>


## ***İŞLETİM SİSTEMİNİN ADINI ÖĞRENMEK*** 

<br>



```py
    import os

    print(os.name)
```
<br>

Eğer işletim sitemi windows ise  ***"nt"*** ,  linux veya  MacOS ise "posix" olarak çıktı alırız.

<br>

## İŞLETİM SİSTEMİNİN DİZİN AYRACINI ÖĞRENMEK 

<br>

```py
    import os

    print(os.sep)
    >>> \
```
<br>

### NOT : 

sep niteliği programların farklı işletim sistemlerinde tutarlı çalışması için gereklidir.Bunu bir değişkene atayıp dizin işlemleri yaparken bu değişkenden faydalanırız. Sonuçta kullanıcıların işletim sistemlerinin ne olacağını bilemeyiz bu yüzden bu kısım önemlidir ve geçilmemelidir.


<br>

### ÖR:

```py
    import os

    os_imlec    =   os.sep

    meyveler    =   ["muz","kivi" , "karpuz"]

    liste       =   os_imlec.join(meyveler)

    print(liste)

    >>> muz\kivi\karpuz
```
<br><hr>

## ***os.getcwd() :***


<br>

Bu fonksiyon o an içinde bulunduğumuz dizin adını verir.

```py
    print(os.getcwd())
    
    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
```

<br><hr>

## ***os.chdir() :*** 


Bu fonksiyon ise diziler arasında gezinmemizi sağlar.Mesela;

<br>

```py
    gidilecek_konum     =   "C:/Users/Kadir/OneDrive/Masaüstü/projeler/frontend"

    konumum             =   os.getcwd()

    print(konumum)
    #şuanki bulunduğum konum

    os.chdir(gidilecek_konum)
    #istediğim konuma gittim

    print(os.getcwd())
    # istediğim konuma gittiğimin kanıtı 
```

<br>

### NOT: 

Dizin işlemleri yaparken ters taksim işeretinden kaçının çünkü ters taksim işareti kaçiş dizisi operatörlerinde kullanılır.( "\n , \t" )

<br><hr>

## ***os.listdir() :***

Bu fonksiyon ise bulunduğumuz dizin içerisindeki dosya ve klasörleri listeleme imkanı verir. Dosyalar liste olarak geriye döndürülür.
Eğer farklı bir dizindeki dosyaları listelemek istersen parantezler arasına dizin adını yazabiliriz.

<br>

```py
    print("Şuan içinde bulunuduğumuz dizin : " , os.getcwd())

    print(*os.listdir() , sep="\n")
    # yıldız sayesinde tüm elemanları tek tek aldık , eğer ilk defa görüyorsanız araştırmanızı tavsiye ederim.

    >>> Şuan içinde bulunuduğumuz dizin :  C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
    >>> dosya isimleri; 
    >>> os.md
    >>> os.py
    >>> os_notlar.py
```

<br><hr>

## ***os.curdir :***

<br>

İşletim sistemlerinin genelinde o an içinde bulunduğun dizini temsil eden karakter ***" . "*** dır. ***os.curdir*** niteliği de ilgili işletim sisteminin ***o an içinde bulunan dizini*** temsil eden karakter dizisini temsil eder.  

### Bir Örnek ; 

os.listdir() istediğimiz dizindeki klasör veya dosyaları listelememizi sağlıyordu.

<br>

```py

    print(os.listdir(os.getcwd()))

    print(os.listdir("."))

    print(os.listdir(os.curdir))

    >>> ['os.md', 'os.py', 'os_notlar.py']
    >>> ['os.md', 'os.py', 'os_notlar.py']
    >>> ['os.md', 'os.py', 'os_notlar.py']
```

Yukarıdaki örnekte 3 komutun da aynı işi yaptığını görüyoruz. Ancak os.getcwd() metodu ile karıştırmamak gerekiyor. Bir sonraki örnekte de bunları kıyaslayalım.

<br>


```py
    print(os.getcwd())

    print(os.curdir)

    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
    >>> .
```

<br><hr>

## ***os.pardir :***


<br>

***os.curdir*** niteliği o an içinde bulunduğumuz karakter dizisini temsil ediyorsa , os.pardir niteliği ise bir üst dizini temsil eden karakter dizisini temsil eder.Bu işletim sistmelerinde genelde ***" .. "*** ile temsil edilir.

<br>

```py
    print(os.pardir)
    >>> ..
```
<br><hr>


## ***os.startfile() :*** 

<br>

Bu metod ***sadece WİNDOWS İŞLETİM SİSTEMLERİNDE ÇALIŞIR.*** Bu fonksiyonun olayı ise bilgisayarda bulunan herhangi bir dosyayı açar.O an içinde bulunduğun dizinde bir dosyayı açmak istersen direkt dosya ismini yazabilrisn. Farklı bir dizindeki dosyayı açmak istersen dizin adıyla beraber yazmalısın.

<br>

```py
    print(os.listdir(os.getcwd()))
    # dizindeki dosyaları listeledik

    os.startfile("os-deneme.txt")
    # notepad ile açacaktır
```
<br><hr>


## ***os.mkdir() :*** 

<br>

Bu metod ise yeni dizinler (klasörler) oluşturmamızı sağlar. Eğer bulunduğun dizinde bir klasör oluşturmak istersen direkt dizin adını yaz. Ancak farklı bir dizinde oluşturmak istersen dizin adını komple yazman gerekir örnekle açıklayalım.

<br>

```py
    os.mkdir("yeni-dizin")
    # Bulunduğumuz dizinde oluşturacaktır.

    os.mkdir("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin")
    # ben masaüstü yolunu verdim siz de kendi bilgisayarınızda bunu yapabilrisiniz. ters taksime dikkt ediniz.
```

<br>

Eğer oluşturmak istediğin dizin varsa hata verecektir.Bu fonksiyon var olmayan tüm dizinleri oluşturmaz oluşturmak istediğimiz dizinden önceki dizinlerin tanımlanmış olması  gerekir. Bir örnekle açıklayalım.

<br>

```py
    os.mkdir("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")
    # son iki dosya şuan mevcut değil bu yüzden hata verecektir. alacağınız hata

    >>> Traceback (most recent call last):
    >>>   File "c:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.py", line 86, in <module>
    >>>      os.mkdir("yeni-dizin")
    >>> FileExistsError: [WinError 183] Halen varolan bir dosya oluşturulamaz: 'yeni-dizin'
```

<br>
 
Bu işlemi uygulamak istersen bir sonraki metodu kullanmamız gerekir.

<br>

## ***os.makedirs() :***

Bu metod ***.mkdir()*** metodu gibi dizin oluşturmamızı sağlar. Ancak bu metod ***.mkdir()*** metodundan farkı varolmayan iç içe dizinleri de oluşturmamızı sağlar.

<br>

```py
    os.makedirs("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")
    # son iki dosya şuan mevcut değil. Bu metod sayesinde iç içe dizinler oluşturabiliriz.
```
<br><hr>

## ***os.rename() :*** 

<br>


Bu fonksiyon sayesinde dizinlerin adlarını değiştirebiliriz.Eğer değiştireceğimiz dosyanın isminde bir dosya varsa hata vercektir

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

    os.chdir(konum)
    print(os.getcwd())

    os.rename("yenidizin1", "rename_ile_degistirildi")
    print(os.listdir())

    >>> C:\Users\Kadir\OneDrive\Masaüstü\yeni-dizin
    >>> ['rename_ile_degistirildi']
```

<br><hr>

## ***os.replace() :*** 

<br>

Bu fonskiyon da ***os.rename()*** fonksiyonu ile aynı işlemi yapar. Ancak aynı isimde bir dizin daha varsa onun üzerine yamaya çalışır.  


<br><hr>

## ***os.remove() :*** 

<br>

Bilgisayardan dosyları silmemizi sağlar. Dosyaları direkt silecektir soru sormadan bunun için dikkatli kullanmakta fayda var

<br>

```py
    konum   =   "D:/yeni-dizin"

    os.chdir(konum)
    print(os.getcwd())
    # konumda belirtiğimiz dizine gittik

    print(os.listdir())
    #konumdaki dosyalara bakalım

    os.chdir("rename_ile_degistirildi")
    print(os.getcwd())
    print(os.listdir())
    # alt dizine gittik ve bu alt dizindeki dizinleri listeledik


    os.remove("beni_sil")
    print(os.listdir())
```
<br><hr>

## ***os.rmdir() :***

<br>

Bu fonksiyon içi boş olan dizinleri silmemizi sağlar.Eğer silmek istediğin dizinlerde dosya veya dizin varsa hata verecektir.

<br>




```py
    konum   =   "D:/yeni-dizin"

    os.chdir(konum)
    print(os.getcwd())
    # konumda belirtiğimiz dizine gittik

    print(os.listdir())
    #konumdaki dosyalara bakalım

    os.chdir("rename_ile_degistirildi")
    print(os.getcwd())
    print(os.listdir())
    # alt dizine gittik ve bu alt dizindeki dizinleri listeledik


    os.rmdir("beni_sil")
    print(os.listdir())
```
<br> <hr>

## ***os.removedirs() :*** 

<br>

İçi boş olan tüm dizin yollarını siler. Aşağıdaki örnekte iç içe birkaç klasör oluşturdum ve komuut çalıştırdığımızda yenidizin dahil olmak üzere tüm klaörleri silecektir. 


<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/dizin-1/dizin-2/dizin-3"

    os.removedirs(konum)
```

<br><hr>

## ***os.stat() :***

<br>

Bu fonksiyon klasörler hakkında bilgi edinmemizi sağlar. Klasörün boyutunu oluşturulma tarihi gibi.Dosya hakında bilgi alırken bize bağzı nitelikleri geriye döndürecektir bunların ne anlama geldiğini listeleyelim ;

<br>

- ***st_atime*** : dosyaya en son erişilme tarihini temsil eder.

- ***st_ctime*** : dosyanın oluşturulma tarihini temsil eder.(win)

- ***st_mtime*** : dosyanın son değiştirilme tarihini temsil eder.

- ***st_size*** : dosyanın boyutunu temsil eder.


<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt"

    text_info   = os.stat(konum)

    print("dosyanın son erisilme tarihi : {}".format(text_info.st_atime))
    print("oluştrulma tarihi : {} ".format(text_info.st_ctime))
    print("dosyanın en sonki değiştirilme tarihi : {}" .format(text_info.st_mtime))
    print("dosyanın boyutu : {}".format(text_info.st_size))#byte
```

<br> <hr>

## ***os.system() :***

<br>

Sistem komutlarını veya programları çalıştırabilmemizi sağlar.

<br>

```py
    os.system("calc.exe")#hesap makinasınıu açar

    os.system("appwiz.cpl")#program ekle veya kaldır ekranını açar
```


<br> <hr>

## ***os.walk() :***

<br>

Bu fonksiyon ***os.listdir()*** fonksiyonu ile benzer işler yapar. ***os.listdir()*** fonksiyonunda parametre olarak verilen dizindeki dosyları listeliyordu. Bu fonksiyon ise belirttiğimiz dizinden itibaren içe doğru tüm dizinleri otomatik olarak taramamızı sağlar.

Direkt ekrana yazdırdığımız zaman ;

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/"
    print(os.walk(konum))
    >>> <generator object walk at 0x0000024DD98EE748>
```
<br>

Karşımıza bir obje geldi. İçindekileri görmek için for dögüsünü kullanmalıyız. Bir örnekle açıklayalım.

<br>

```py
    for i in os.walk(konum):
    print(i)

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/', ['arşiv'], ['os.txt', 'Sen Affetsen.mp3', 'Town.sql', 'WhatsApp Image 2022-05-09 at 09.10.27.jpeg'])

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv', ['dosyalar'], ['Uygulamalarla SQL Ogreniyorum Egitim Bilgi Formu.pdf', 'Yeni Microsoft Word Belgesi.docx'])
    
    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv\\dosyalar', ['text'], ['Yeni Bit eşlem resmi.bmp', 'Yeni Microsoft Access Database.accdb', 'Yeni WinRAR arşivi.rar'])

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv\\dosyalar\\text', [], ['Yeni Metin Belgesi.txt', 'Yeni Metin Belgesi.txt - Kısayol (2).lnk', 'Yeni Metin Belgesi.txt - Kısayol (3).lnk', 'Yeni Metin Belgesi.txt - Kısayol.lnk'])

```
<br> <hr>

## ***os.environ() :***

<br>

Kullanılan işletim sisteminin çevre değişkneleri hakkında bilgi edinmemizi sağlar.

<br>

```py
    sistem  =   os.environ
    # print(sistem)
    # bir sözlük geriye döndürür

    for i in sistem:
        print("{} \t : {}".format(i , sistem[i]))
        #işletim sisteminin hakkındaki bilgileri terminale yazdıracakıtr.
```

<br><hr>


## ***os.path :*** 

<br>

Bu nitelik kendi içinde birçok fonksiyon ve nitelik barındırır. Bunları inceleyelim;

<br>



### ***os.path.abspath() :*** 

<br>

Bu fonksiyon bir dosyanın tam yolunu bize söyler.

<br>

```py
    dosya_yolu  =   os.path.abspath("os.md")
    print(dosya_yolu)
    #bir dosyanın tam yolunun ne olduğunu söyler
    
    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python\os.md
```
<br><hr>



### ***os.path.dirname() :*** 

<br>

Dosya yolunun dizin kısmını verir

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    print(os.path.dirname(konum))

    >>> C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python
```
<br>

### ***NOT :***

***os.path.abspath()*** ile ***os.path.dirname()*** fonksiyonları birbirlerine çok benzer. Ancak örnkeldeki çıktılara bakarsanız ***taksim(/)*** işaretlerinin farklı olduğunu görürsünüz. Ayrıca ***os.path.dirname()*** fonksiyonu  sadece dizin (klasör) adlarını aldı.

<br><hr>


### ***os.path.exists() :***


<br>

Bu fonksiyon bir dosya veya dizinin var olup olmadığını kontrol eder. Geriye True veya False döndürür.

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    print(os.path.exists(konum))
    
    >>> True
```
<br><hr>

### ***os.path.expanduser() :*** 

<br>

Bu fonksiyon işletim sistemindeki Kullanıcıya ait olan ***dizin adresini*** geriye döndürür.

<br>

```py
    print(os.path.expanduser("~"))
    
    >>> C:\Users\Kadir
```
<br><hr>

### ***os.path.isdir() :***


Parametre olarak verilen öğenin dizin (klasör) olup olmadığını kontrol eder. Geriye True veya False döndürür.

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    konum2   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/"

    print(os.path.isdir(konum))
    print(os.path.isdir(konum2))

    >>> False
    >>> True
```

<br> <hr>


### ***os.path.isfile() :*** 


<br>

Parametre olarak verilen öğenin dosya olup olmadığını kontrol eder. Geriye True veya False döndürür.


<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    konum2   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/"

    print(os.path.isdir(konum))
    print(os.path.isdir(konum2))

    >>> True
    >>> False
```

<br><hr>


### ***os.path.join() :*** 

<br>

Bu fonksiyon kendisine verilen paremetrelerden işletim sistemine uygun yol adresleri oluşturur.

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

    yeni_konum   =  os.path.join(konum,"dizin1" , "dizin2")

    print(konum)
    print(yeni_konum)
    #eski konumla yeni konumu kıyaslayalım.

    >>> C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin
    >>> C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin\dizin1\dizin2
    # yeni dizinlerin oluşturulduğunu görebiliriz ancak bu sadece yol gerçek anlamda dizin oluşturmaz

    os.chdir(konum)
    print(os.listdir())
    # belirtilen konuma gidip dosyaları listeleyecek olursak dizinlerin oluşmadığını görürürz.

    >>> ['os.txt']
```

<br> <hr>

### ***os.path.split() :***

Bu fonksiyonu kullanarak dosya adları ile dizin adlarını ayırabilirsin veya son dizini baş kısımdan da ayırabilirsin kullanım alanlarına göre değişiklik gösterebilir.


<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

    result  =   os.path.split(konum) 

    print(konum)
    print(result)
    print(type(result))
```

<br>



### ***os.path.splitext() :***

<br>

Bu fonksiyon dosya adı ile uzantısını ayırır.Bir örnekle açıklayalım.

<br>

```py
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt"

    son_eleman  =   os.path.split(konum)   

    ayir    =    os.path.splitext(son_eleman[1])

    print(konum)
    print(son_eleman)
    print(ayir)
    print(type(ayir))

    >>> C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt
    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin', 'os.txt')
    >>> ('os', '.txt')
    >>> <class 'tuple'>
```

<br>

