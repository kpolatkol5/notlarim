# ***Karakter Dizileri***

<br>

Strin veri tütündeki veri yapılarına karaketer dizileri denir. İngilizcede karakter dizizlerinin karşılığı ***string*** 'dir. Basitçe String ifadelere örnek vermek gerekirse.

<br>

```py
val =   "String değerler tıraklar arasına yazılır. tek tırnak veya çift tırnak kullanılabilir"

print(type(val))

>>> <class 'str'>
```

<br>

Karakter dizilerinin kullanımı metodalrı önemli bir kondur. Bu kısmın önemsiz görüp atlamayın. Unutmayın küçük kodlar bir araya gelerek büyük programları oluşturuyor.


<br><hr>

## ***Karakter Dizilerine Ulaşmak ve İndex Kavramı***


Karakter dizileri tek bir parça olarak işlem yapılabilir. Dışarıdan müdahale etmeden karakter dizilerinin istediğimiz kısımalrına ulaşamıyoruz. Bu imkansız demiyorum ancak dışarıdan müdahale etmemiz gerekiyor. Mesela karakter dizisinin her bir öğesini döngü ile tek tek alıp koşullar belirterek istediğimiz işlemi yaptırabiliriz. Veya sıkça kullandığımız split metodu var ve bu metod yardımı ile karakter dizilerini istediğimiz kısımlardan parçalayıp bir listeye atarız ve döngüyle işleem yaparız. Zaten string metotaları da bu yüzden var. String metodlara geçmeden önce index kavramını anlatalım.

<br>

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"


print(val[0])
print(val[1])
print(val[2])
print(val[3])
print(val[4])
print(val[5])
print(val[6])


>>> T
>>> e
>>> k
>>>  
>>> t
>>> ı
>>> r
```
<br>

Örnekte de olduğu gibi string değişkenimizi yazdık ve print metodu ile değişkeni yazdırırken köşeli parantezlere birtakım sayılar yazdık. İşte işlem yapacağımız strıng değişkenimizin hemen yanına köşeli parantezler kullanarak ulaşmak istediğimiz index numarasını yazdık. index numaraları her zaman 0 'dan başlar. Eğer 1 yazarsanız ilk karakteri değil aslında ikinci karakteri çağırmış olursunuz. Zaten örnekte de bunu net bir şekilde görebilirsiniz

```py
print(val[0])
>>> T
```

<br>

****Karakter dizilerini döngüler ile de alabiliriz.****

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

for i in range(len(val)):
    print(val[i])
```
<br>

Örnekte range fonksiyonunu kullandık ve bu fonksiyon bize bir aralık veriyordu. len fonksyionu ile string değişkenimizin karakter sayısını hesapladık. rance fonksiyonuna da bu parametreyi verirsek 0 ile karakter sayısı kadar aralık belirtmiş oluruz.

Daha sonra her bir i değeri karakter sayısındaki index numarasını temsil ettiği için karakter dizisinin sırasıyla tüm index numaralarına erişebiliriz.

<br>

***Döngü kullanmadan tüm karaketerleri tek tek ekrana yazdırmak istersek.***

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print(*val , sep="\n")
```


<br>

###  ***Son İndexdeki Elemanlara Ulaşmak***

<br>

İndex numaralarını hep pozitif değer vermiştik Eğer negatif değerler verirsek bu sefer sıranın sonundan almaya başlayacaktır.

<br>

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"


print(val[-1])
print(val[-2])
print(val[-3])
print(val[-4])
print(val[-5])

>>> r
>>> i
>>> l
>>> i
>>> b
```

<br>

-1 son öğeyi temsil eder negatif sayılar azaldıkça sondan başa doğru index numarası ilerler.


<br>

## ***Karakter Dizilerini Parçalamak***


<br>

Karakter dizilerini parçalamak için index de de olduğu gibi köşeli parantezleri kullanıyoruz. Hangi indexler arasındaki karakteri almak istersek köşeli parantez içerisinde iki nokta ile belirtiyoruz. Bir örnekle açıklayalım.

<br>






```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print("ilk dört karakteri alacaktır: ",val[0:4])
print("ilk beş karakteri alacaktır: ",val[:5])


>>> ilk dört karakteri alacaktır:  Tek 
>>> son dört karakteri alacaktır:  Tek t
```

<br>

index numaraları saymaya sıfırdan başladığıgı için son karakter sırasını her zaman bir fazlasnı belirtiriz.


Eğer ikinci parametreyi negatif değer verirsek o kısmı atar. Zaten formül ilk parametrenin başlangıç noktası ikinci parametrenin ise bitiş noktaı olması. Bitiş değerini negatif sayı verirsek o index e kadar olan kısmı almış olacağız.

<br>

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print("Son kelimeyi almayacaktır.",val[0:-14])
#son kelimemiz 14 karakter ve -14 ile en sonran saymaya başladık 

>>> Son kelimeyi almayacaktır. Tek tırnak , çift tırnak veya üç tırnak 
```

<br>

## Karakter Dizilerini Tersten Yazdırmak

<br>

Tersten yazdırmak için bu sefer iki noktayı iki kez kullanıp -1 yazmamız gerek.

<br>

```py

val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print("tersten yazdıracaktır.",val[::-1])

>>> tersten yazdıracaktır. rilibalınalluk kanrıt çü ayev kanrıt tfiç , kanrıt keT
```

<br>

Bu ifade ile en son karakterden başla ve ilk karaktere doğru tek tek geriye doğru yazdır.


Eğer bir karaketer dizisinde istediğimiz kısmları tersten almak istersek üçüncü parametre belirtmemiz gerekiyor. ilk iki parametrenin görevi sabit olup üçüncü parametre ise atlama parametresidir. Atlama sayısını negatif değer verirsek geriye doğru saymaya başlayacaktır. Örnekle açıklayalım.



<br>

```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print("İstediğimiz kısımları tersten yazdıracaktır:",val[9:3:-1] , sep="")

>>> İstediğimiz kısımları tersten yazdıracaktır:kanrıt
```



<br>


üçüncü parametreyi pozitif değer verseydik ters çevirmeden yazdıracaktı. Eğer 2 değerini verseydik iki index atlayarak yazdıracaktı.


```py
val =   "Tek tırnak , çift tırnak veya üç tırnak kullanılabilir"

print("iki karakter atlayarak ayıklayacaktır:",val[0:6:2] , sep="")

>>> iki karakter atlayarak ayıklayacaktır:Tkt
```

<br><hr>

## Karakter Dizilerinin Metotları

<br>


### ***replace() Metodu:***

karakter dizilerinde istediğimiz karakter veya karakterlerin değiştirmemizi sağlar. Aslında karakter dizileri değiştirilemeyen veri türleridir. Bu da karakter dizisine atadığımız herhangi bir verinin değiştirilmesini istersek bunu yeniden tanımlamamız gerekir. Bu metod karakter dizisindeki istediğimiz karakterleri silip onun yerine tekrar istediğimiz karakterleri tanımlamamızı sağlıyor. İlk parametre karakter dizisinde aranacak olan karakter , ikinci parametre ise değiştirecek olduğumuz karakteri tanımlarız. Yani ilk karakteri arar ve bulursa ikinci parametredeki tanımladığımız karakterle değiştirir. Üçüncü parametre ise bu değiştirme işlemini kaç kez yapacağımızı belirtiriz. Eğer üçüncü parametre belirtmezsek bu ilemi tüm karakterler için yapar.

<br>

```py
val =   "Tek tırnak , çift tırnak TTT veya üç tırnak kullanılabilir"

val =   val.replace("T", "t" ,3 )

print(val)

>>> tek tırnak , çift tırnak ttT veya üç tırnak kullanılabilir
```

<br>

Örnekte de olduğu gibi değişkenimizde 4 tane büyük T harfi vardı ve biz ilk üç tanesini küçük t harfine dönüştürdük. Bu sefer üçüncü parametre belirtmeyelim.

<br>

```py
val =   "Tek tırnak , çift tırnak TTT veya üç tırnak kullanılabilir"

val =   val.replace("T", "t" )

print(val)

>>> tek tırnak , çift tırnak ttt veya üç tırnak kullanılabilir
```
<br>


Tüm karakterleri dönüştürmüş olduk.

<br> <hr>


### ***split() Metodu:***

<br>

Karakter dizilerini istediğimiz noktalardan böler ve bölünen parçaları bir listeye atar. ikinci parametre belirlemek için birinci parametreyi belirlememiz gerekiyor ikinci parametre ise bölme işlemini kaç kez uygulayacağımız belirlememizi sağlıyor.

<br>



```py
val =   "Tek, tırnak , çift tırnak, TTT veya üç, tırnak kullanılabilir"

val =   val.split("," ,3)

print(val)

>>> ['Tek', ' tırnak ', ' çift tırnak', ' TTT veya üç, tırnak kullanılabilir']
```

<br>

örnekte de olduğu gibi karakter dizisini virgüllerden ayırdık ve ilk üç virgül için bölme işlemi yaptık . Eger hiçbir parametre vermeseydik.

<br>


```py
val =   "Tek tırnak çift tırnak TTT veya üç tırnak kullanılabilir"

val =   val.split()

print(val)

>>> ['Tek', 'tırnak', 'çift', 'tırnak', 'TTT', 'veya', 'üç', 'tırnak', 'kullanılabilir']
```

<br><hr>

### ***rspilt() :***

<br>

spilt metodu ile aynı işi yapar sadece spilt metodunda soldan sağa doğru okunuken bu metod sağesinde karakter dizileri sağdan sola doğru okunur.


<br>

```py
val =   "Tek tırnak çift tırnak TTT veya üç tırnak, kullanılabilir"

val =   val.rsplit(",")

print(val)

>>> ['Tek tırnak çift tırnak TTT veya üç tırnak', ' kullanılabilir']
```

<br><hr>


### ***splitlines() Metodu :***

<br>

Bu metod ise paragraf gibi uzun karakter dizilerinde kullanılır ve satır bölmesi yapar. Eğer ***True*** parametresi ile kullanırsanız \n kaçış karakterini de görüntüleyebilirsiniz. Yani her bir satır bitiminde \n kaçış dizisi de uygulanacaktır.


<br>

```py
val =   """
Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır 
metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir 
hurufat numune kitabı oluşturmak üzere bir yazı galerisini 
alarak karıştırdığı 1500'lerden beri endüstri standardı sahte 
metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını
sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik
dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da
içeren Letraset yapraklarının yayınlanması ile ve yakın 
zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren 
masaüstü yayıncılık yazılımları ile popüler olmuştur.
"""
val =   val.splitlines()
print(len(val))

for i in val:
    print(i)

>>> 11
>>> 
>>> Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır 
>>> metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir 
>>> hurufat numune kitabı oluşturmak üzere bir yazı galerisini 
>>> alarak karıştırdığı 1500'lerden beri endüstri standardı sahte 
>>> metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını
>>> sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik
>>> dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da
>>> içeren Letraset yapraklarının yayınlanması ile ve yakın 
>>> zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren 
>>> masaüstü yayıncılık yazılımları ile popüler olmuştur.
```


<br><hr>

### ***lower() Metodu :***

<br>

Karakter dizisindeki istisnalar hariç bütün harfleri küçük harfe dönüştürüyor. Büyük I harfini küçük i 'ye dönüştürüyor. Daha doğrusu türkçe karakterlerde problemler olabiliyor. Önce metodu anlatalım daha sonra çözümüne geçelim.

<br>

```py
val =   "BüYüK HarfLeRin HEPsiNi DöNÜştÜrebilir."

print(val.lower())

>>> büyük harflerin hepsini dönüştürebilir
```

<br>

Örnekte de olduğu gibi büyük harflerin hepsini küçük harfe dönüştürebilir.Eğer dönüştürmelerde sorun çıkmamasını isterseniz ilk başta karakterleri replace() metodu ile karakter dönüşümlerini yaparız. Daha sonra lower() metodunu kullanabiliriz.

<br><hr>

### ***upper() Metodu :***

<br>

Lover metodunun tam tersidir. Bu da küçük harfelrin tamamını Büüyük harfe dönüştürür.


<br>

```py
val =   "tum KüçüK KaRaKterlerİ Büyük KarakterlerE DönüŞtürecektİR"

print(val.upper())

>>> TUM KÜÇÜK KARAKTERLERİ BÜYÜK KARAKTERLERE DÖNÜŞTÜRECEKTİR
```

<br><hr>

### ***islower() Metodu :***

<br>

Karakter dizilerinde tüm harflerin küçük harften oluşup oluşmadığını sorgulamamızı sağlıyor. Eğer tüm karakterler küçük harften oluşmuşsa geriye true değerini döndürecektir.



<br>

```py
val     =   "tüm hArfLer küçük olmadığı içİn FALSE değeri döndürecektir"
val2    =   "tüm harfler küçük olduğu için true değeri döndürecektir"

print(val.islower())
print(val2.islower())

>>> False
>>> True
```


<br><hr>

### ***isupper() Metodu :***

<br>

Karakter dizilerinde tüm harflerin büyük harften oluşup oluşmadığını sorgulamamızı sağlıyor. Eğer tüm karakterler büyük harften oluşmuşsa geriye true değerini döndürecektir.



<br>

```py
val     =   "tüm hArfLer büyük olmadığı içİn FALSE değeri döndürecektir"
val2    =   "TÜM HARFLER BÜYÜK OLDUĞU IÇIN TRUE DEĞERI DÖNDÜRECEKTIR"

print(val.isupper())
print(val2.isupper())

>>> False
>>> True
```

<br><hr>

### ***endswith() Metodu :***

<br>

Karakter dizilerinde hangi karakterle bittiğini sorgulamamızı sağlar. Parantezleri arasına sorgulamak istediğimiz karakterleri yazıyoruz ve eğer ki karakterler eşleşiyorsa geriye true değeri döndürecektir.


<br>




```py
val     =   "endswith metodu son karakterleri inceler"

print(val.endswith("r"))
print(val.endswith("ler"))
print(val.endswith("inceler"))
print(val.endswith("incelemez"))

>>> True
>>> True
>>> True
>>> False
```

<br>

Eğer dosyalar ile çalışıyoranız endswith metodu ile dosyaların uzantılarını rahatlıkla alabilirsiniz.



<br><hr>

### ***startswith() Metodu :***

<br>

Endswith metodunun tam tersini yapar. Bu metod karakter dizilerinin sonuna bakmaz başına bakar. Parantez içerisinde yadığımız karakter değerleri uyuşuyorsa geriye ture değeri döndürür.


<br>


```py
val     =   "startswith metodu ilk karakterleri inceler"

print(val.startswith("s"))
print(val.startswith("S"))
print(val.startswith("startswith"))
print(val.startswith("endswith"))


>>> True
>>> False
>>> True
>>> False
```
<br>

***NOT***

Bu iki metodun da büyük harf küçük harf duyarlı olduğunu unutmayın..


<br><hr>

### ***capitalize() Metodu :***

<br>

Karakter dizilerinin sadece ilk harfini büyük harf yapar.

<br>

```py
val     =   "capitalize metodu sadece ilk harfi büyük harf yapar"

print(val.capitalize())

>>> Capitalize metodu ilk harfleri büyük harf yapar
```

<br><hr>

### ***title() Metodu :***

<br>


Birden fazla oluşan karakter dizilerinde tüm karakterlerin ilk harfini büyük harf yapar.

<br>


```py
val     =   "title metodu tüm karakterlerin ilk harfini büyük harf yapar"

print(val.title())

>>> Title Metodu Tüm Karakterlerin Ilk Harfini Büyük Harf Yapar
```

<br><hr>

### ***swapcase() Metodu :***

<br>

Bu metod ise karakter dizilerindeki büyük harfleri küçük harfe küçük harfleri ise büyük harfe dönüştrür.

<br>



```py
val     =   "Swapcase Metodu Büyük Harfleri Küçük Harfe Küçük Harfleri Büyük Harfe Dönüştürür."

print(val.swapcase())

>>> sWAPCASE mETODU bÜYÜK hARFLERI kÜÇÜK hARFE kÜÇÜK hARFLERI bÜYÜK hARFE dÖNÜŞTÜRÜR.
```


<br><hr>

### ***strip() Metodu :***

<br>

Bu metod karakter dizilerinin başı ve sonu ile ilgilenir. Varsayılan olarak karakter dizilerindeki boşluk karakterleri ve bağzı kaçış karakterlerini temizler. Bu kaçış karakterleri \t , \n , \r , \v , \f gibi. Eğer parantez içerisni herhangi bir değer girerseniz bu değerleri karakter dizisinin başında ve sonunda arar. Bulabilrise bu karakterleri siler bulamazsa hiçbir işlem yapmaz.

<br>



```py
val     =   "  sağ ve soldaki boşlukları temizler  " 

print(val.strip())

>>> sağ ve soldaki boşlukları temizler
```

<br>


```py
val     =  ">parantez içerisinde belirttiğimiz karakterleri sağdan ve soldan siler>"

print(val.strip(">"))

>>> parantez içerisinde belirttiğimiz karakterleri sağdan ve soldan siler
```

<br><hr>

### ***lstrip() Metodu :***

<br>


Karakter dizisinin sadece sol kısımları ile ilgilenir. Parantez içerisinde belirttiğiniz karakter eğer karakter dizisinin solunda yer alıyorsa bu karkterleri silecektir. Aynı değer sağ tarafında da olabilir. lstrip() metodu sadace karkter dizilerinin sol kısmı ile ilgilenir.

<br>

```py
val     =  ">parantez içerisinde belirttiğimiz karakterleri sadece soldan siler>"

print(val.lstrip(">"))

>>> parantez içerisinde belirttiğimiz karakterleri sadece soldan siler>
```

<br><hr>

### ***rstrip() Metodu :***

<br>

lstrip() metodunun tam tersidir. Karakter dizisinin sağ kısmı ile ilgilenir. Eğer parantezleri arasına kırpmak istediğimiz karkteri yazarsak ve incelediğimiz ilgili karkater dizisinin sağ kısmında yer alıyorsa bu karakterleri kırpacaktır.


<br>



```py
val     =  ">parantez içerisinde belirttiğimiz karakterleri sadece sağdan siler>"

print(val.rstrip(">"))


>>> >parantez içerisinde belirttiğimiz karakterleri sadece sağdan siler
```




