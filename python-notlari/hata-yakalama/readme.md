# ***Hata Yakalama***

<br>

Hata yakalama işlemi kullanıcıların veya yazılımcıların programın işleyişi sorunsuz şekilkde devam etmesi ve olası hataların düzeltilmesi için ilgil hatayı kullanıcıya göstermek için kullanıyoruz. Mesela çok basit bir hesap makinası yaptık ve kullanıcı yanlışlıkla sayısal bir değer girmedi. Bu durumda program çalışmayı durdurur ve kullanıcıların anlayamayacığı hata mesajları geriye döndürür. Ancak biz bu olası hataları önceden öngörüp yakalayabilir ve bunlarla alakalı hata mesajları geriye döndürebilriiz. 
Mesela yukarıda verdiğm toplama işlemini düşünün. Kullanıcı bu hatayı aldığında konsolda ***ValueError*** yazısını görecek belkide hiçbir şey anlamayacak. Kısacası bu tür hataları öceden tahmin edip ilgili hataların giderilmesi için hata mesajları iletirirz. Toplama işelemi çok basit bir örnek oldu ancak daha gelişmiş kodalr yazdığınızda hata yakalamanın önemini daha iyi anlayacksınız.  

<br>


Önce bir hata görelim daha sonra Hata yakalama nasıl yapılır örnekle açıklayalım
```py

sayi1   =   int(input("İlk sayıyı girirniz  : "))
sayi2   =   int(input("İlk sayıyı girirniz  : "))

toplam  =   sayi1 + sayi2

print(toplam)


>>> Traceback (most recent call last):
>>>   File "c:/Users/Kadir/OneDrive/Masaüstü/notlarim/python-notlari/hata-yakalama/deneme.py", line 15, in <module>
>>>     sayi2   =   int(input("İlk sayıyı girirniz  : "))
>>> ValueError: invalid literal for int() with base 10: 'a'
```

<br>

Yukarıdaki örnekte kullanıcıya gösterilecek hata mesajı bu şekildedir. Dikkat ederseniz ***ValueError*** yazısı bir hata türüdür ve bir sonraki örnekte bu hatayı yakalayarak kullanıcıya istediğimiz mesajı ileteceğiz


<br>

```py
try:
    sayi1   =   int(input("İlk sayıyı girirniz  : "))
    sayi2   =   int(input("İlk sayıyı girirniz  : "))

    toplam  =   sayi1 + sayi2

    print(toplam)
    
except ValueError:
    print("lütfen sayı giriniz")


>>> İlk sayıyı girirniz  : 21
>>> İlk sayıyı girirniz  : a
>>> lütfen sayı giriniz
```

<br>

Kodu açıklayacak olursak kullandığımız iki yapı var. try kod blogu arasına hata alacağını tahmin ettiğimiz kodları yazarız. except de ise olası  hata türünü yazarız eğer bu hata ile karşılaşılırsa except altındaki kod blogu çalışır ve ekrana lütfen sayı giriniz yazdırılacaktır. 

except kısmını istediğimiz kadar tanımlayabiliriz. Mesela herhangi bir sayı sıfır a bölünmesi durumunda alacağımız hata türü  ***ZeroDivisionError*** . bir sayıyı sıfır a bölünmesi durumunda bu hata ile karşılaşıyoruz bir de bu hatayı yakalayalım

<br>


```py
try:
    sayi1   =   int(input("İlk sayıyı girirniz  : "))
    sayi2   =   int(input("İlk sayıyı girirniz  : "))

    bölüm  =   sayi1 / sayi2

    print(bölüm)
    
except ValueError:
    print("lütfen sayı giriniz")

except ZeroDivisionError:
    print("bir sayı 0 a bölünemez")

>>> İlk sayıyı girirniz  : 2
>>> İlk sayıyı girirniz  : 0
>>> bir sayı 0 a bölünemez
```


<br>


Eğer isterseniz hata türlerini guruplayıp bir hata mesajı da üretebiliriz

<br>

```py
try:
    sayi1   =   int(input("İlk sayıyı girirniz  : "))
    sayi2   =   int(input("İlk sayıyı girirniz  : "))

    bölüm  =   sayi1 / sayi2

    print(bölüm)
    
except (ValueError , ZeroDivisionError):
    print("hatalı işlem yaptınız")


>>> İlk sayıyı girirniz  : 2
>>> İlk sayıyı girirniz  : 0
>>> Hatalı işlem yaptınız
```
<br>

## ***Finally değimi***

<br>

finally bir hata ile karşılaşılsa da karşılaşılmasada çalışacaktır. Mesela ödeme sistemleri üzerinde çalışıyoruz ve bir hata ile karşılaşıldı. Ödeme işlemini sonlandırmak ödeme gerçekleşse de gerçekleşmese de yapılması gereken bir işlemdir.Eğer hata ile karşılaşılırsa bu hatayı kullanıcıya göstermek ve ödemeyi sonlandırmamız gerekiyor işte tam da burada bu yapıyı kullanabilirsiniz. Basit bir örnekle nasıl kullanıldığını anlatalım.

<br>

Hatalı örnek
```py
try:
    sayi1   =   int(input("İlk sayıyı girirniz  : "))
    sayi2   =   int(input("İlk sayıyı girirniz  : "))

    bölüm  =   sayi1 / sayi2

    print(bölüm)
    
except ValueError:
    print("Lütfen sayı giriniz")

except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez")
    
finally:
    print("hata ile karşılaşsak da karşılaşmasak da bu kod blogu çalışacaktır")

>>> İlk sayıyı girirniz  : 2
>>> İlk sayıyı girirniz  : 0
>>> bir sayı sıfıra bölünemez
>>> hata ile karşılaşsak da karşılaşmasak da bu kod blogu çalışacaktır
```
<br>

Hata olmayan örnek
```py
try:
    sayi1   =   int(input("İlk sayıyı girirniz  : "))
    sayi2   =   int(input("İlk sayıyı girirniz  : "))

    bölüm  =   sayi1 / sayi2

    print(bölüm)
    
except ValueError:
    print("Lütfen sayı giriniz")

except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez")
    
finally:
    print("hata ile karşılaşsak da karşılaşmasak da bu kod blogu çalışacaktır")

>>> İlk sayıyı girirniz  : 2
>>> İlk sayıyı girirniz  : 2
>>> 1.0
>>> hata ile karşılaşsak da karşılaşmasak da bu kod blogu çalışacaktır
```

<br>

## ***raise değimi***

<br>

raise ile duruma göre hata mesajları üretebiliriz. Kullanıcı hatalı işlem yapmak zorunda değil sadece mantık akışına göre kendi belirlediğimiz mesajlara göre kullanıcıyı yönlendirmeyi amaçlayabiliriz. Bunun için hata türelrinden yararlanacağız. Örnekle açıklayalım.

<br>

```py

deger1  =   int(input("birinci değer    : "))
deger2  =   int(input("ikinci değer     : "))


if (deger1 % 2 == 0 ) or (deger2 % 2 == 0):
    raise Exception("degerlerden biri çift sayı")
```

Örnekte de olduğu gibi bir koşul ifadesi kullandık ve raise değimini kullandıktan sonra exception ile hata türünü yazdık , parantezler arasına da mesajımızı yazdık.


istersen try except ifadeleri arasına da yazabilirsin istersen bu yapıyı kullanmadan olası hata türünü belirttikten sonra raise değimi ile  hata mesajı iletebilirsin.

<br>

## ***Assert Değimi***

<br>


Yukarıdaki örnekte hatayı tespit edebilmek için if blogu kullandık. Eğer koşul sağlanırsa raise ile hata mesajını gönderebiliyoruz. Assert de ise ilk başta koşul yazarız virgül ile ayırdıktan sonra hata mesajımızı yazarız eğer True değer dönerse hata kodunu gönderecekti. İf kullandığımız örneğe benziyor . Farkı ise *AssertionError* türündeki hatalar ile ilgileniyor. Daha çok bir hata yapıyoruz ama nerede olduğunu tespit edemiyoruz bunun için kullanaibiliriz. bu değim bir fonksyion değil parantez ile kullanılmamalıdır.


Ayrıca programımızdaki bütün assert ifadeleri yorumlayıı tarafından yok sayılır.programın daha  hızlı çalışması ve çok yer kaplamasını istemiyorsanız ve çok fazla hata varsa  kullanılabilir.


<br>

```py

deger1  =   input("birinci değer    : ")
deger2  =   input("ikinci değer     : ")

assert len(deger1) != 0 and len(deger2) !=0 , "sayılardan birisi boş bırakıldı"

print("giris basarılı")
```
<br>

örnekte eger sayılardan birisi boş girilirse hata mesajı iletilecek ve kodun geriye kalan kısmı okunmayacaktır.






