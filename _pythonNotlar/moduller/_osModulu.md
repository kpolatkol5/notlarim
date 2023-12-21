# ***OS MODÜLÜ NEDİR NE İŞE YARAR***

Os modülü python da hazır olarak gelir. Dosya dizin işlemlerinde işlerimizi kolaylaştrır. Kısacası işletim sistemleri ile iletişim kurabilmemizi sağlar.

## ***İŞLETİM SİSTEMİNİN ADINI ÖĞRENMEK*** 


```python
    import os

    print(os.name)
```

Eğer işletim sitemi windows ise  ***"nt"*** ,  linux veya  MacOS ise "posix" olarak çıktı alırız.

## İŞLETİM SİSTEMİNİN DİZİN AYRACINI ÖĞRENMEK 


```python
    import os

    print(os.sep)
    >>> \
```
### NOT : 

sep niteliği programların farklı işletim sistemlerinde tutarlı çalışması için gereklidir.Bunu bir değişkene atayıp dizin işlemleri yaparken bu değişkenden faydalanırız. Sonuçta kullanıcıların işletim sistemlerinin ne olacağını bilemeyiz bu yüzden bu kısım önemlidir ve geçilmemelidir.

### ÖR:

```python
    import os

    os_imlec    =   os.sep

    meyveler    =   ["muz","kivi" , "karpuz"]

    liste       =   os_imlec.join(meyveler)

    print(liste)

    >>> muz\kivi\karpuz
```
## ***os.getcwd() :***

Bu fonksiyon o an içinde bulunduğumuz dizin adını verir.

```python
    print(os.getcwd())
    
    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
```

## ***os.chdir() :*** 

Bu fonksiyon ise diziler arasında gezinmemizi sağlar.Mesela;

```python
    gidilecek_konum     =   "C:/Users/Kadir/OneDrive/Masaüstü/projeler/frontend"

    konumum             =   os.getcwd()

    print(konumum)
    #şuanki bulunduğum konum

    os.chdir(gidilecek_konum)
    #istediğim konuma gittim

    print(os.getcwd())
    # istediğim konuma gittiğimin kanıtı 
```
### NOT: 

Dizin işlemleri yaparken ters taksim işeretinden kaçının çünkü ters taksim işareti kaçiş dizisi operatörlerinde kullanılır.( "\n , \t" )

## ***os.listdir() :***

Bu fonksiyon ise bulunduğumuz dizin içerisindeki dosya ve klasörleri listeleme imkanı verir. Dosyalar liste olarak geriye döndürülür.
Eğer farklı bir dizindeki dosyaları listelemek istersen parantezler arasına dizin adını yazabiliriz.

```python
    print("Şuan içinde bulunuduğumuz dizin : " , os.getcwd())

    print(*os.listdir() , sep="\n")
    # yıldız sayesinde tüm elemanları tek tek aldık , eğer ilk defa görüyorsanız araştırmanızı tavsiye ederim.

    >>> Şuan içinde bulunuduğumuz dizin :  C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
    >>> dosya isimleri; 
    >>> os.md
    >>> os.python
    >>> os_notlar.python
```

## ***os.curdir :***

İşletim sistemlerinin genelinde o an içinde bulunduğun dizini temsil eden karakter ***" . "*** dır. ***os.curdir*** niteliği de ilgili işletim sisteminin ***o an içinde bulunan dizini*** temsil eden karakter dizisini temsil eder.  

### Bir Örnek ; 

os.listdir() istediğimiz dizindeki klasör veya dosyaları listelememizi sağlıyordu.

```python

    print(os.listdir(os.getcwd()))

    print(os.listdir("."))

    print(os.listdir(os.curdir))

    >>> ['os.md', 'os.python', 'os_notlar.python']
    >>> ['os.md', 'os.python', 'os_notlar.python']
    >>> ['os.md', 'os.python', 'os_notlar.python']
```

Yukarıdaki örnekte 3 komutun da aynı işi yaptığını görüyoruz. Ancak os.getcwd() metodu ile karıştırmamak gerekiyor. Bir sonraki örnekte de bunları kıyaslayalım.

```python
    print(os.getcwd())

    print(os.curdir)

    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python
    >>> .
```
## ***os.pardir :***

***os.curdir*** niteliği o an içinde bulunduğumuz karakter dizisini temsil ediyorsa , os.pardir niteliği ise bir üst dizini temsil eden karakter dizisini temsil eder.Bu işletim sistmelerinde genelde ***" .. "*** ile temsil edilir.


```python
    print(os.pardir)
    >>> ..
```
 
## ***os.startfile() :*** 

Bu metod ***sadece WİNDOWS İŞLETİM SİSTEMLERİNDE ÇALIŞIR.*** Bu fonksiyonun olayı ise bilgisayarda bulunan herhangi bir dosyayı açar.O an içinde bulunduğun dizinde bir dosyayı açmak istersen direkt dosya ismini yazabilrisn. Farklı bir dizindeki dosyayı açmak istersen dizin adıyla beraber yazmalısın.


```python
    print(os.listdir(os.getcwd()))
    # dizindeki dosyaları listeledik

    os.startfile("os-deneme.txt")
    # notepad ile açacaktır
```
## ***os.mkdir() :*** 

Bu metod ise yeni dizinler (klasörler) oluşturmamızı sağlar. Eğer bulunduğun dizinde bir klasör oluşturmak istersen direkt dizin adını yaz. Ancak farklı bir dizinde oluşturmak istersen dizin adını komple yazman gerekir örnekle açıklayalım.

```python
    os.mkdir("yeni-dizin")
    # Bulunduğumuz dizinde oluşturacaktır.

    os.mkdir("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin")
    # ben masaüstü yolunu verdim siz de kendi bilgisayarınızda bunu yapabilrisiniz. ters taksime dikkt ediniz.
```

Eğer oluşturmak istediğin dizin varsa hata verecektir.Bu fonksiyon var olmayan tüm dizinleri oluşturmaz oluşturmak istediğimiz dizinden önceki dizinlerin tanımlanmış olması  gerekir. Bir örnekle açıklayalım.

```python
    os.mkdir("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")
    # son iki dosya şuan mevcut değil bu yüzden hata verecektir. alacağınız hata

    >>> Traceback (most recent call last):
    >>>   File "c:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.python", line 86, in <module>
    >>>      os.mkdir("yeni-dizin")
    >>> FileExistsError: [WinError 183] Halen varolan bir dosya oluşturulamaz: 'yeni-dizin'
```
 
Bu işlemi uygulamak istersen bir sonraki metodu kullanmamız gerekir.

## ***os.makedirs() :***

Bu metod ***.mkdir()*** metodu gibi dizin oluşturmamızı sağlar. Ancak bu metod ***.mkdir()*** metodundan farkı varolmayan iç içe dizinleri de oluşturmamızı sağlar.

```python
    os.makedirs("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")
    # son iki dosya şuan mevcut değil. Bu metod sayesinde iç içe dizinler oluşturabiliriz.
```
## ***os.rename() :*** 

Bu fonksiyon sayesinde dizinlerin adlarını değiştirebiliriz.Eğer değiştireceğimiz dosyanın isminde bir dosya varsa hata vercektir

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

    os.chdir(konum)
    print(os.getcwd())

    os.rename("yenidizin1", "rename_ile_degistirildi")
    print(os.listdir())

    >>> C:\Users\Kadir\OneDrive\Masaüstü\yeni-dizin
    >>> ['rename_ile_degistirildi']
```
## ***os.replace() :*** 

Bu fonskiyon da ***os.rename()*** fonksiyonu ile aynı işlemi yapar. Ancak aynı isimde bir dizin daha varsa onun üzerine yamaya çalışır.  
## ***os.remove() :*** 

Bilgisayardan dosyları silmemizi sağlar. Dosyaları direkt silecektir soru sormadan bunun için dikkatli kullanmakta fayda var

```python
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
## ***os.rmdir() :***

Bu fonksiyon içi boş olan dizinleri silmemizi sağlar.Eğer silmek istediğin dizinlerde dosya veya dizin varsa hata verecektir.

```python
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
## ***os.removedirs() :*** 

İçi boş olan tüm dizin yollarını siler. Aşağıdaki örnekte iç içe birkaç klasör oluşturdum ve komuut çalıştırdığımızda yenidizin dahil olmak üzere tüm klaörleri silecektir. 

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/dizin-1/dizin-2/dizin-3"

    os.removedirs(konum)
```
## ***os.stat() :***

Bu fonksiyon klasörler hakkında bilgi edinmemizi sağlar. Klasörün boyutunu oluşturulma tarihi gibi.Dosya hakında bilgi alırken bize bağzı nitelikleri geriye döndürecektir bunların ne anlama geldiğini listeleyelim ;

- ***st_atime*** : dosyaya en son erişilme tarihini temsil eder.

- ***st_ctime*** : dosyanın oluşturulma tarihini temsil eder.(win)

- ***st_mtime*** : dosyanın son değiştirilme tarihini temsil eder.

- ***st_size*** : dosyanın boyutunu temsil eder.

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt"

    text_info   = os.stat(konum)

    print("dosyanın son erisilme tarihi : {}".format(text_info.st_atime))
    print("oluştrulma tarihi : {} ".format(text_info.st_ctime))
    print("dosyanın en sonki değiştirilme tarihi : {}" .format(text_info.st_mtime))
    print("dosyanın boyutu : {}".format(text_info.st_size))#byte
```

## ***os.system() :***

Sistem komutlarını veya programları çalıştırabilmemizi sağlar.

```python
    os.system("calc.exe")#hesap makinasınıu açar

    os.system("appwiz.cpl")#program ekle veya kaldır ekranını açar
```
## ***os.walk() :***

Bu fonksiyon ***os.listdir()*** fonksiyonu ile benzer işler yapar. ***os.listdir()*** fonksiyonunda parametre olarak verilen dizindeki dosyları listeliyordu. Bu fonksiyon ise belirttiğimiz dizinden itibaren içe doğru tüm dizinleri otomatik olarak taramamızı sağlar.

Direkt ekrana yazdırdığımız zaman ;

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/"
    print(os.walk(konum))
    >>> <generator object walk at 0x0000024DD98EE748>
```

Karşımıza bir obje geldi. İçindekileri görmek için for dögüsünü kullanmalıyız. Bir örnekle açıklayalım.

```python
    for i in os.walk(konum):
    print(i)

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/', ['arşiv'], ['os.txt', 'Sen Affetsen.mp3', 'Town.sql', 'WhatsApp Image 2022-05-09 at 09.10.27.jpeg'])

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv', ['dosyalar'], ['Uygulamalarla SQL Ogreniyorum Egitim Bilgi Formu.pdf', 'Yeni Microsoft Word Belgesi.docx'])
    
    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv\\dosyalar', ['text'], ['Yeni Bit eşlem resmi.bmp', 'Yeni Microsoft Access Database.accdb', 'Yeni WinRAR arşivi.rar'])

    >>> ('C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/arşiv\\dosyalar\\text', [], ['Yeni Metin Belgesi.txt', 'Yeni Metin Belgesi.txt - Kısayol (2).lnk', 'Yeni Metin Belgesi.txt - Kısayol (3).lnk', 'Yeni Metin Belgesi.txt - Kısayol.lnk'])

```
## ***os.environ() :***

Kullanılan işletim sisteminin çevre değişkneleri hakkında bilgi edinmemizi sağlar.

```python
    sistem  =   os.environ
    # print(sistem)
    # bir sözlük geriye döndürür

    for i in sistem:
        print("{} \t : {}".format(i , sistem[i]))
        #işletim sisteminin hakkındaki bilgileri terminale yazdıracakıtr.
```
## ***os.path :*** 

Bu nitelik kendi içinde birçok fonksiyon ve nitelik barındırır. Bunları inceleyelim;
### ***os.path.abspath() :*** 

Bu fonksiyon bir dosyanın tam yolunu bize söyler.

```python
    dosya_yolu  =   os.path.abspath("os.md")
    print(dosya_yolu)
    #bir dosyanın tam yolunun ne olduğunu söyler
    
    >>> C:\Users\Kadir\OneDrive\Masaüstü\düzenlenecek-notlar\OS-modulu-python\os.md
```
### ***os.path.dirname() :*** 

Dosya yolunun dizin kısmını verir

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    print(os.path.dirname(konum))

    >>> C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python
```
### ***NOT :***

***os.path.abspath()*** ile ***os.path.dirname()*** fonksiyonları birbirlerine çok benzer. Ancak örnkeldeki çıktılara bakarsanız ***taksim(/)*** işaretlerinin farklı olduğunu görürsünüz. Ayrıca ***os.path.dirname()*** fonksiyonu  sadece dizin (klasör) adlarını aldı.
### ***os.path.exists() :***

Bu fonksiyon bir dosya veya dizinin var olup olmadığını kontrol eder. Geriye True veya False döndürür.

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    print(os.path.exists(konum))
    
    >>> True
```
### ***os.path.expanduser() :*** 

Bu fonksiyon işletim sistemindeki Kullanıcıya ait olan ***dizin adresini*** geriye döndürür.

```python
    print(os.path.expanduser("~"))
    
    >>> C:\Users\Kadir
```
### ***os.path.isdir() :***

Parametre olarak verilen öğenin dizin (klasör) olup olmadığını kontrol eder. Geriye True veya False döndürür.

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    konum2   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/"

    print(os.path.isdir(konum))
    print(os.path.isdir(konum2))

    >>> False
    >>> True
```
### ***os.path.isfile() :*** 

Parametre olarak verilen öğenin dosya olup olmadığını kontrol eder. Geriye True veya False döndürür.

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
    konum2   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/"

    print(os.path.isdir(konum))
    print(os.path.isdir(konum2))

    >>> True
    >>> False
```
### ***os.path.join() :*** 

Bu fonksiyon kendisine verilen paremetrelerden işletim sistemine uygun yol adresleri oluşturur.

```python
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

### ***os.path.split() :***

Bu fonksiyonu kullanarak dosya adları ile dizin adlarını ayırabilirsin veya son dizini baş kısımdan da ayırabilirsin kullanım alanlarına göre değişiklik gösterebilir.

```python
    konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

    result  =   os.path.split(konum) 

    print(konum)
    print(result)
    print(type(result))
```
### ***os.path.splitext() :***

Bu fonksiyon dosya adı ile uzantısını ayırır.Bir örnekle açıklayalım.

```python
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
