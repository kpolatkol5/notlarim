# Nupy Nedir 



## ***.array() :***
<br><hr> <br>
Verilen bir python listesini numpy dizisine dönüştürür.

<br>

```py
import numpy as np

print(np.array([1,2,3,4,5,6]))

# [1 2 3 4 5 6]
```


<br>


## ***.arange() :***
<br><hr> <br>
Verilen parametreler doğrultusunda numpy dizisi oluşturur.

<br>

```py
import numpy as np

print(np.arange(2,15))

# [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
```


<br>

## ***.zeros() :***
<br><hr> <br>
Verilen parametre kadar 0 içeren bir numpy dizisi oluşturur

<br>

```py
import numpy as np

print(np.zeros(10))

# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```


<br>


## ***.ones() :***
<br><hr> <br>
Verilen parametre kadar 1 içeren bir numpy dizisi oluşturur

<br>

```py
import numpy as np

print(np.ones(10))

# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```


<br>


## ***.linspace() :***
<br><hr> <br>
Verilen parametreler doğrultusunda eşit parçaya böler ve bir numpy dizisi geriye döndürür flot sayılar da dahil olabilir.
<br>

```py
import numpy as np

print(np.linspace(0,100 , 5))

# [  0.  25.  50.  75. 100.]
```


<br>

## ***.random.randint() :***
<br><hr> <br>

Numpy modülünün içerisinde random dosyası var ve bu verilen parametreler arasında rastgele integer sayılar üretilir , eğer üçüncü parametre verirsek üçüncü parametredeki sayı kadar değer üretir ve geriye bir numpy dizisi döndürür.


<br>

```py
import numpy as np

print(np.random.randint(0,10))

# 5

print(np.random.randint(0,10 ,3))

# [7 6 2]
```


<br>

## ***.random.rand() :***
<br><hr> <br>

Bu method ise sıfır ile bir arasında rastgele verilen parametre değeri kadar  sayı üretir ve geriye numpy dizisi döndürür. Eğer negatif değerleri de işleme dahil etmek istersen ``` .random.randn() ``` metodunu kullanabilirsin.

<br>

```py
import numpy as np

print(np.random.rand(5))

# [0.63552008 0.2795283  0.46259946 0.54413992 0.8021475 ]
```


<br>


## ***.reshape() :***
<br><hr> <br>


Bir numpy dizisindeki elemanlarla matris oluşturabiliriz ``` reshape() ``` methodunun içerisinde belittiğimiz parametreler ile mesela 5 e 10 luk matris oluşturmak için bu paramtreleri sırasyla girmemiz gerekiyor. 5 satır ve 10 sütün oluşturacaktır. dizimizin eleman sayısının 50 olması gerekiyor. Aşağıdaki örnekte 5 satırdan ve 10 sütundan oluşan bir matris tanımladık.

<br>


```py
import numpy as np

np_liste = np.arange(0 , 50 )

result = np_liste.reshape(5,10)


# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]
```

Oluşturulan matriste satırlar ve sütunlarla işlemler yapabiliriz. Örneğin satırlar arasında toplama veya sütunlar arasında toplama işlemi yapabiliriz.


```py
import numpy as np

np_liste = np.arange(0 , 50 )

result = np_liste.reshape(5,10)

print(result.sum(axis=1))# satırların toplar geriye numpy dizisi döndürür.
# [ 45 145 245 345 445]


print(result.sum(axis=0))# sütunları toplar geriye numpy dizisi döndürür.

# [100 105 110 115 120 125 130 135 140 145]
```

<br>

## ***.max() | .min():***
<br><hr> <br>

Bir numpy dizisindeki en büyük elemanı geriye döndürür.(max())
Bir numpy dizisindeki en küçük elemanı geriye döndürür.(min())


<br>

```py
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.min())
print(result.max())

# [ 4  0 19  2]
# 0
# 19
```


<br>

## ***.mean() :***
<br><hr> <br>

Bir numpy dizisindeki değerlerin ortalamasını geriye döndürür.


<br>

```py
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.mean())

#[17 25 12 28]
# 20.5 
```


<br>


## ***.argmax() | .argmin() :***
<br><hr> <br>

Numpy dizisindeki en büyük elemanın index numarasını geriye döndürür. (``` .argmax() ```)
Numpy dizisindeki en küçük elemanın index numarasını geriye döndürür. (``` .argmin() ```)


<br>

```py
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.argmax())

# [2 6 8 1]
# 2
```


<br>

# Numpy Dizilerinin İndexlenmesi
<br>

```py
import numpy as np

result2 = np.arange(10) 
print(result2)

print(result2[0])
print(result2[2])
print(result2[-1])
print(result2[0:4]) #ilk dört değeri alırız
print(result2[3:]) #üçüncü index ile geriye kalan tüm listeyi alırız
print(result2[::-1]) # listeyi tesine döndürür ve geriye döndürür
```

<br>


Elimizde çok boyutlu bir python listesi olduğunu varsayalım. Bu listeyi numpy dizisine dönüştürelim veya herhangi bir numpy dizisi olsun fark etmez dizi içerisindeki elemanlara nasıl ulaşacağız örnekle açıklayalım.

<br>



```py
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi) # satırlara ayırıyor

# [[ 0  1  2]
#  [50 21 65]
#  [99 21 78]]
```

<br>


```py
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[0,1])
# 1

print(numpy_listesi[2,2])

# 78
```
<br>

Aralarına virgül koyarak sanki birer listeymiş gibi ekliyoruz python listesinden farkı ise her bir liste için bir köşeli parantez kullanmıyoruz direkt virgülle istediğimiz değere gelene kadar yazıyoruz.

<br>

Eğer bir bir numpy dizinde çok boyutlu dizilerden her listeden belirli elemanları seçmek istersek 

<br>

```py
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[:,2])

# [ 2 65 78]
```

<br>

Örnekte de olduğu gibi  ```" : "``` işareti oluşturulan tüm satırları seçer (yani her liste için)  ve bu seçilen satırların 2 index numaralı değerini alır geriye bir numpy listesi döndürür.


Son iki örnek arasındaki fark şu ilk örnekte numpy dizisindeki birinci listedeki elemanı seçtik ve onun içinden 2. indexteki elemanı aldık , ikinci örnekte ise tüm listeleri seçtik (: ile) ve  bu seçilenlerden 2. index numarasına sahip elemanları aldık


<br>

```py
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[:,0:2])

# [[ 0  1]
#  [50 21]
#  [99 21]]
```
Yukarıdaki örnekte  yapılan işlem ise tüm satırlarda ilk 2 değeri alır. Yani tüm satırlardan bir ve birden fazla değerleri alabiliyoruz.

<br>

# Numpy Dizilerinde Matemtiksel İşlemler


<br>

Oluşturulmuş diziler arasında matematiksel işlemler yapabilriiz . Mesela iki tane numpy dizisi oluşturalım ve toplama işlemi yapalım.

<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)
np_liste_2 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np_liste_2)

print(f" iki listenin toplamı  : {np_liste_1 + np_liste_2}")

# [ 2 43 46  8  5 90]
# [23  7 46 57  8 43]
#  iki listenin toplamı  : [ 25  50  92  65  13 133]
```

<br>

Örnekte de olduğu gibi iki listede index numaralarına göre toplar ve toplamları içeren bir numpy listesi geriye döndürür.

<br>

- ### ```NOT :```  TOPLAMA , ÇIKARTMA , ÇARPMA , BÖLME işelmleri yapılabilir

<br>



## ***.sin() :***
<br><hr> <br>

Her bir elemanın sinüs değerini alır ve geriye numpy dizisi döndürür

<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.sin(np_liste_1))

# [32 92 33  5 95  2]
# [ 0.55142668 -0.77946607  0.99991186 -0.95892427  0.68326171  0.90929743]
```


<br>

## ***.cos() :***
<br><hr> <br>

Her bir elemanın cosinüs değerini alır ve geriye numpy dizisi döndürür

<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.cos(np_liste_1))

# [96 21  9 20 53 31]
# [-0.18043045 -0.54772926 -0.91113026  0.40808206 -0.91828279  0.91474236]
```


<br>





## ***.sqrt() :***
<br><hr> <br>

Her bir elemanın karekök değerini alır ve geriye numpy dizisi döndürür

<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.sqrt(np_liste_1))

# [54 70 55  7  8 54]
# [7.34846923 8.36660027 7.41619849 2.64575131 2.82842712 7.34846923
```


<br>

## ***.log() :***
<br><hr> <br>

Her bir elemanın logaritma değerini alır ve geriye numpy dizisi döndürür

<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.log(np_liste_1))

# [92 10 20 28 98 53]
# [4.52178858 2.30258509 2.99573227 3.33220451 4.58496748 3.97029191]
```



<br>

## ***.size() :***
<br><hr> <br>

Elemanlarının sayısını geriye döndürür


<br>

```py
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.size(np_liste_1))

# 6
```


<br>

## ***.shape() :***
<br><hr> <br>

Oluşturulmuş olan numpy dizisinin kaç boyutlu olduğunu içeren bir tuple geriye döndürür


<br>

```py
import numpy as np

c_list = np.array([[[0,2,3],[1,2,3]] , [[32,32,3],[12,21,4]]])

print(np.shape(c_list)) 

# (2, 2, 3)
```


<br>




# Numpy Dizilerini Birleştirme


<br>

Oluşturulmuş iki numpy matsisini yatayda veya dikeyde birleştirebiliriz.



<br>

```py
import numpy as np


number1 = np.arange(6)

number2 = np.arange(20,26)

result1 = number1.reshape(2,3)
result2 = number2.reshape(2,3)

print(result1)
print(result2)

# [[0 1 2]
#  [3 4 5]]
# [[20 21 22]
#  [23 24 25]]
```


<br>


<br>

```Dikey Birleştirir```
```py
import numpy as np

number1 = np.arange(6)

number2 = np.arange(20,26)

result1 = number1.reshape(2,3)
result2 = number2.reshape(2,3)


dizi_birlesir_dikey = np.vstack((result1 ,result2))

print(dizi_birlesir_dikey)


# [[ 0  1  2]
#  [ 3  4  5]
#  [20 21 22]
#  [23 24 25]]
```


<br>


```Yatay Birleştirir```
```py
import numpy as np


number1 = np.arange(6)

number2 = np.arange(20,26)

result1 = number1.reshape(2,3)
result2 = number2.reshape(2,3)


dizi_birlesir_dikey = np.hstack((result1 ,result2))

print(dizi_birlesir_dikey)

# [[ 0  1  2 20 21 22]
#  [ 3  4  5 23 24 25]]
```


<br>


Dizinin içerisindeki elemanların bir koşula göre değerlendirip sonuca göre tekrardan numpy dizisi oluşturmasını sağlayabiliriz

<br>

```Koşul```
```py
import numpy as np


number1 = np.arange(6)

result1 = number1.reshape(2,3)

print(result1)

print(result1 > 2)

# [[0 1 2]
#  [3 4 5]]
# [[False False False]
#  [ True  True  True]]
```


<br>


```Koşul (Hangi değerler koşulu sağlar)```

```py
import numpy as np


number1 = np.arange(6)

result1 = number1.reshape(2,3)

cift = result1 %2 == 0

print(result1)
print(result1[cift])



# [[0 1 2]
#  [3 4 5]]

# [0 2 4]
```
