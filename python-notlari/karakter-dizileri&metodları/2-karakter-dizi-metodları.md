
### ***join() Metodu :***

<br>

Karakter dizilerinde split() metodu parantez içerisinde belirttiğimiz karakterlere göre parçalıyor ve geriye bir liste döndürüyordu. Bu metod da bu işlemin tam tersini yapar.Bir liste veya parçalanmış karakterleri belirli parçalar ile birleştirmemizi sağlıyor. 

Bu metodun kullanımı biraz farklıdır. Örnekle açıklayalımm.

<br>

```py
deneme  =   ["join", "metodu","ornegi"]

donustur    =   "-".join(deneme)

print(donustur)

>>> join-metodu-ornegi
```

<br>

```py
deneme  =   ("join","metodu" ,"ornegi")

birlesitir  =   "--".join(deneme)

print(birlesitir)

>>> join--metodu--ornegi
```

<br><hr>


### ***count() Metodu :***

<br>

Bu metod karakter dizilerinde parantez içerisinde belirttiğimiz karakterin kaç keç geçtiğini sorgular ve bu sayıyı geriye döndürür.


<br>

```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.count("a"))
print(deneme.count("d"))
print(deneme.count("i"))

>>> 8
>>> 3
>>> 7
```

<br>


Bu metodun aldığı 2 parametre ise karakter dizisinin kaçıncı indeksinden itibaren saymaya başlayacağını belirtebiliriz. Yani 2. parametreye 2 yazarsak karakter dizisinin 2. indeksinden saymaya başlayacaktır 2. indeksten öncesi ile ilgilenmeyecektir.


<br>

```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.count("a" ,20))
print(deneme.count("d",20))
print(deneme.count("i",20))

>>> 6
>>> 2
>>> 7
```


<br><hr>


### ***index() Metodu :***

<br>

Karakter dizilerinde parantez içerisinde belirttiğimiz karakteri arar ve ilk karşılaştığı karakterin index numarasını geriye döndürür. Toplamda üç adet paramtre alır. ilk parametre aranacak karakter , ikinci parametre karakter dizisinde aramaya hangi indeksde başlayacağını , son olarak üçüncü parametrede ise hangi indeks de aramayı bitireceğimizi belirtiriz. Bir örnekle açıklıyalım.


<br>

```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.index("a"))

>>> 14
```

<br>

```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.index("a" , 15 ,23))

>>> 16
```

<br><hr>


### ***rindex() Metodu :***

<br>

index metodu ile aynı işi yapıyor. İndex metodunda ilgili karakteri soldan sağa doğru aramaya başlarken  bu metot da sağdan sola doğru arar. index metodu ile özellikleri aynıdır

<br>


```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.rindex("a"))

>>> 75
```

<br>

```py
deneme  =   "count metodu karakter dizilerinde parametre ile belirtilen karakterleri sayar"

print(deneme.rindex("a" , 40 , 73))

>>> 62
```

örnekte de olduğu gibi başlangıç ve bitiş değerlerinin sırası aynı ancak taramaya en sondan başlar.ilk parametre başlangıç parametresi ikinci parametre ise bitiş parametresidir.

Eğer aranan karakerler bulunamazsa *ValueError* hatası verecektir.

<br><hr>


### ***find() Metodu :***

<br>

index metodu ile özellikleri aynıdır. tek farkı index metodunda *ValueError* hatası verirken , find() metodunda eğer aranan karakter bulunmazsa geriye ***-1*** değerini döndürür.


<br><hr>

### ***rfind() Metodu :***

<br>

rindex metodu ile özellikleri aynıdır. tek farkı rindex metodunda *ValueError* hatası verirken , rfind() metodunda eğer aranan karakter bulunmazsa geriye ***-1*** değerini döndürür.


<br>

<br><hr>

### ***center() Metodu :***

<br>

Bu metod karakter dizilerini ortalamamızı sağlar. iki adet parametre alır. Birinci parametre aralık uzunluğu , ikinci parametre boşluk yerine doldurulacak olan karakteri belirleyebiliriz. Örnekle açıklayalım.

<br>


```py
deneme  =   "center metodu karakter dizilerini ortalar"

print(len(deneme))

deneme = deneme.center(45,"-")

print(deneme)

>>> 41
>>> --center metodu karakter dizilerini ortalar--
```


<br>


Ancak burada dikkat etmemiz gereken nokta karakterin uzunluğu. Center() metodu nun ilk parametresi ile verdiğimiz değer eğer karaketer uzunluğundan büyükse eşit şekilde sağdan ve soldan boşluk bırakır.


<br><hr>

### ***rjust() Metodu :***

<br>

Bu metod karakter dizilerini sağa hizlar. Parantez içerisinde parametre olarak boşluk genişliğini veririz ve bu parametreyi verirken işlemin istediğimiz gibi sonuç vermesi için karakter dizisinin uzunluğundan büyük bir değer vermeliyiz. Çünkü karakter dizisnin uznlugunu hesaplar ve eğer parantez içerisinde belirttiğimiz genişlik değerinden  büyükse karakterleri sağa yaslar ve fazla boşlugu sol tarafa ekler. İkinci parametresi boşluklar yerine geçecek olan karakteri belirlememizi sağlar. Bir örnekle açıklayalım

<br>


```py
deneme  =   "rjust metodu sağa hizalar"

print(len(deneme))
print(deneme.rjust(40 , "-"))

>>> 25
>>> ---------------rjust metodu sağa hizalar
```

<br><hr>

### ***ljust() Metodu :***

<br>

rjust() metodu ile ayni özelliklere sahiptir. sadece ljust metodu karakter dizini sola yaslar ve fazla boşlugu karakter dizisinin sağ tarafına ekler. Bu metodun da ikinci parametresi boşluklar yerine geçecek olan karakteri belirlememizi sağlar.



<br>

```py
deneme  =   "ljust metodu sola hizalar"

print(len(deneme))
print(deneme.ljust(40 , "-"))

>>> ljust metodu sola hizalar---------------
```

<br><hr>

### ***zfill() Metodu :***

<br>


Karakter dizilerinin soluna parantez içerisinde belirttiğimiz karakter kadar sıfır eklememizi sağlar.

<br>

```py
deneme  =   "zfill metodu karakter dizilerinin soluna sıfır ekler"

print(len(deneme))
print(deneme.zfill(54))

>>> 52
>>> 00zfill metodu karakter dizilerinin soluna sıfır ekle
```
