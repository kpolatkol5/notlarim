## ***.array() :***
 
Verilen bir pythonthon listesini numpy dizisine dönüştürür.

```pythonthon
import numpy as np

print(np.array([1,2,3,4,5,6]))

# [1 2 3 4 5 6]
```





## ***.arange() :***
 
Verilen parametreler doğrultusunda numpy dizisi oluşturur.



```python
import numpy as np

print(np.arange(2,15))

# [ 2  3  4  5  6  7  8  9 10 11 12 13 14]
```

## ***.zeros() :***
 
Verilen parametre kadar 0 içeren bir numpy dizisi oluşturur

```python
import numpy as np

print(np.zeros(10))

# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

## ***.ones() :***
 
Verilen parametre kadar 1 içeren bir numpy dizisi oluşturur

```python
import numpy as np

print(np.ones(10))

# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```
## ***.linspace() :***
 
Verilen parametreler doğrultusunda eşit parçaya böler ve bir numpy dizisi geriye döndürür flot sayılar da dahil olabilir.

```python
import numpy as np

print(np.linspace(0,100 , 5))

# [  0.  25.  50.  75. 100.]
```
## ***.random.randint() :***
 
numpy modülünün içerisinde random dosyası var ve bu verilen parametreler arasında rastgele integer sayılar üretilir , eğer üçüncü parametre verirsek üçüncü parametredeki sayı kadar değer üretir ve geriye bir numpy dizisi döndürür.

```python
import numpy as np

print(np.random.randint(0,10))

# 5

print(np.random.randint(0,10 ,3))

# [7 6 2]
```
## ***.random.rand() :***
 
Bu method ise sıfır ile bir arasında rastgele verilen parametre değeri kadar  sayı üretir ve geriye numpy dizisi döndürür. Eğer negatif değerleri de işleme dahil etmek istersen ``` .random.randn() ``` metodunu kullanabilirsin.

```python
import numpy as np

print(np.random.rand(5))

# [0.63552008 0.2795283  0.46259946 0.54413992 0.8021475 ]
```
## ***.reshape() :***

Bir numpy dizisindeki elemanlarla matris oluşturabiliriz ``` reshape() ``` methodunun içerisinde belittiğimiz parametreler ile mesela 5 e 10 luk matris oluşturmak için bu paramtreleri sırasyla girmemiz gerekiyor. 5 satır ve 10 sütün oluşturacaktır. dizimizin eleman sayısının 50 olması gerekiyor. Aşağıdaki örnekte 5 satırdan ve 10 sütundan oluşan bir matris tanımladık.

```python
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

```python
import numpy as np

np_liste = np.arange(0 , 50 )

result = np_liste.reshape(5,10)

print(result.sum(axis=1))# satırların toplar geriye numpy dizisi döndürür.
# [ 45 145 245 345 445]


print(result.sum(axis=0))# sütunları toplar geriye numpy dizisi döndürür.

# [100 105 110 115 120 125 130 135 140 145]
```
## ***.max() | .min():***
 
Bir numpy dizisindeki en büyük elemanı geriye döndürür.(max())
Bir numpy dizisindeki en küçük elemanı geriye döndürür.(min())

```python
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.min())
print(result.max())

# [ 4  0 19  2]
# 0
# 19
```
## ***.mean() :***
Bir numpy dizisindeki değerlerin ortalamasını geriye döndürür.

```python
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.mean())

#[17 25 12 28]
# 20.5 
```
## ***.argmax() | .argmin() :***
 
numpy dizisindeki en büyük elemanın index numarasını geriye döndürür. (``` .argmax() ```)
numpy dizisindeki en küçük elemanın index numarasını geriye döndürür. (``` .argmin() ```)

```python
import numpy as np

result = np.random.randint(0,30,4)

print(result)
print(result.argmax())

# [2 6 8 1]
# 2
```
# numpy Dizilerinin İndexlenmesi


```python
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

Elimizde çok boyutlu bir pythonthon listesi olduğunu varsayalım. Bu listeyi numpy dizisine dönüştürelim veya herhangi bir numpy dizisi olsun fark etmez dizi içerisindeki elemanlara nasıl ulaşacağız örnekle açıklayalım.

```python
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi) # satırlara ayırıyor

# [[ 0  1  2]
#  [50 21 65]
#  [99 21 78]]
```

```python
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[0,1])
# 1

print(numpy_listesi[2,2])

# 78
```

Aralarına virgül koyarak sanki birer listeymiş gibi ekliyoruz pythonthon listesinden farkı ise her bir liste için bir köşeli parantez kullanmıyoruz direkt virgülle istediğimiz değere gelene kadar yazıyoruz.

Eğer bir bir numpy dizinde çok boyutlu dizilerden her listeden belirli elemanları seçmek istersek 

```python
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[:,2])

# [ 2 65 78]
```

Örnekte de olduğu gibi  ```" : "``` işareti oluşturulan tüm satırları seçer (yani her liste için)  ve bu seçilen satırların 2 index numaralı değerini alır geriye bir numpy listesi döndürür.

Son iki örnek arasındaki fark şu ilk örnekte numpy dizisindeki birinci listedeki elemanı seçtik ve onun içinden 2. indexteki elemanı aldık , ikinci örnekte ise tüm listeleri seçtik (: ile) ve  bu seçilenlerden 2. index numarasına sahip elemanları aldık

```python
import numpy as np

numpy_listesi = np.array([[0,1,2] , [50,21, 65 ] , [99 ,21,78] ])

print(numpy_listesi[:,0:2])

# [[ 0  1]
#  [50 21]
#  [99 21]]
```
Yukarıdaki örnekte  yapılan işlem ise tüm satırlarda ilk 2 değeri alır. Yani tüm satırlardan bir ve birden fazla değerleri alabiliyoruz.
# numpy Dizilerinde Matemtiksel İşlemler


Oluşturulmuş diziler arasında matematiksel işlemler yapabilriiz . Mesela iki tane numpy dizisi oluşturalım ve toplama işlemi yapalım.

```python
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

Örnekte de olduğu gibi iki listede index numaralarına göre toplar ve toplamları içeren bir numpy listesi geriye döndürür.
## NOT

TOPLAMA , ÇIKARTMA , ÇARPMA , BÖLME işelmleri yapılabilir
## ***.sin() :***
 
Her bir elemanın sinüs değerini alır ve geriye numpy dizisi döndürür

```python
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.sin(np_liste_1))

# [32 92 33  5 95  2]
# [ 0.55142668 -0.77946607  0.99991186 -0.95892427  0.68326171  0.90929743]
```
## ***.cos() :***

Her bir elemanın cosinüs değerini alır ve geriye numpy dizisi döndürür

```python
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.cos(np_liste_1))

# [96 21  9 20 53 31]
# [-0.18043045 -0.54772926 -0.91113026  0.40808206 -0.91828279  0.91474236]
```
## ***.sqrt() :***
 
Her bir elemanın karekök değerini alır ve geriye numpy dizisi döndürür

```python
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.sqrt(np_liste_1))

# [54 70 55  7  8 54]
# [7.34846923 8.36660027 7.41619849 2.64575131 2.82842712 7.34846923
```
## ***.log() :***
 
Her bir elemanın logaritma değerini alır ve geriye numpy dizisi döndürür

```python
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.log(np_liste_1))

# [92 10 20 28 98 53]
# [4.52178858 2.30258509 2.99573227 3.33220451 4.58496748 3.97029191]
```
## ***.size() :***
 
Elemanlarının sayısını geriye döndürür

```python
import numpy as np

np_liste_1 = np.random.randint(1,100 , 6)

print(np_liste_1)
print(np.size(np_liste_1))

# 6
```

## ***.shape() :***

Oluşturulmuş olan numpy dizisinin kaç boyutlu olduğunu içeren bir tuple geriye döndürür


```python
import numpy as np

c_list = np.array([[[0,2,3],[1,2,3]] , [[32,32,3],[12,21,4]]])

print(np.shape(c_list)) 

# (2, 2, 3)
```
# numpy Dizilerini Birleştirme

Oluşturulmuş iki numpy matsisini yatayda veya dikeyde birleştirebiliriz.

```python
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


#### Dikey Birleştirir
```python
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
#### Yatay Birleştirir
```python
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


Dizinin içerisindeki elemanların bir koşula göre değerlendirip sonuca göre tekrardan numpy dizisi oluşturmasını sağlayabiliriz

#### Koşul

```python
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

#### Koşul (Hangi değerler koşulu sağlar)

```python
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
