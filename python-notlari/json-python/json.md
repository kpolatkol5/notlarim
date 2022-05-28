# JSON MODÜLÜ - PYTHON

<br>

## JSON NEDİR KULLANIMI
<br>

- JSON farklı diller arasında iletişimi sağlam için geliştirilmiş , her platformun anladığı basit veri formatıdır.  
- jsnon veri formatında her öğe arası " **,** " ile ayrılır. 

<br>

### İki türlü json kullanımı var

1. Anahtar değer;
        
```py
    #string veri türünde 
    result = '{"firstname":"kadir","lastname":"polatkol",}'
``` 

<br>

2. Sadece değer;
```py
    #string veri türünde 
    result = '{"kadir","polatkol"}'
``` 
<br><hr>

## JSON MODÜLÜ
<br>

- JSON veri formatı pythonda string veri formatında gelir ve **JSON MODÜLÜ** ile bu string veri formatını dictionary (sözlük) formatına dönüştürürüz.

```python
#Sözlük yapısı bu şekilde
    users = {
        "firtname":"kadir",
        "lastname":"polatkol",
        "programming languages":["python","php","c++"],
    }
```
<br>

- JSON veri formatıda bu yapıya benzer şekilde gelir ve bunu dictionary yapısına çevirerek kullanabiliriz.

<br>

- Json modülünde 4 temel fonksiyon vardır. Bunlardan 2 si python ile json oluşturuken diğer ikisi ise json dosyalarını çözer yani sözlük formatına dönüştürür.
  
## JSON FORMATI OLUŞTURAN FONKSİYONLAR

1. ***json.dump() :*** Bu fonksiyon çıktıyı bir dosyaya aktarır. Bu fonksiyon bir değer döndürmez bir dosyanın yolunu belirtiriz ve json dosyalarını oraya aktarır. Tabiki python da oluşturuduğumuz dictionary (sözlük) yapısını ilgili dosyaya json formatında aktaracaktır.  ***json.dump*** ile ***json.dumps*** ' un alabileceği parametreler aynıdır. 

<br>

2. ***json.dumps() :*** Bu  fonksiyon str tipinde bir değer döndürür dosyaya aktarmaya gerek yoktur bir dictionary yapısını json formatına dönüüştürebiliriz.


### ***json.dump()  ve json.dumps() fonksiyonunun alabileceği parametreler ;*** 

<br>

- ***skipkeys :*** json dosyası oluştururken anahtar veya değerler "str , int , float " değilse hata verecektir . Bu parametrenin varsayılanı ***False*** 'tır . Eğer bu parametreyi ***True*** olrak tanımlayacak olursak hata vermek yerine o öğeyi (anahtar değer çiftini) atlar.

- ***ensure_ascii :*** Varsayılan olarak değeri ***True*** ' dur. Bu parametreyi ***False*** olarak tanımlayacak olursak ASCII tablosuna uymayan karakterlerden kaçınır. 
<br>

<br>

### NOT: ASCII nedir ?

- Bilgisayarlar sadece ikili bilgiyi anlar ve hafızasındaki her şeyi  ikili biçiminde saklar.Örneğin bir bilgisayar “A” karakterinin ne anlama geldiğini bilemez bu karakterler bilgisayar içinde ikili basamak dizisiyle temsil edilir. Bu karakterlerin her biri 8 bitlik dizi kodlarına ayrılmıştır.

![ASCII tablo](img/ascii.jpg)

<br><hr>

- ***indent :*** Varsayılan olarak ***None*** değerini alır. Ve çıktıları dip dibe verir mesela ;

```py 
    print(json.dumps({"Users":{"firtstname":"Kadir","lastname":"polatkol"}}, indent=None))
    >>> {"Users": {"firtstname": "Kadir", "lastname": "polatkol"}}


    print(json.dumps({"Users":{"firtstname":"Kadir","lastname":"polatkol"}}, indent=2))
    # indent parametresindeki değere göre girinti verecektir.(negatif ve ondalılı değerler hariç)
    >>>{
         "Users": {
             "firtstname": "Kadir",
             "lastname": "polatkol"
         }
        }
    print(json.dumps({"Users":{"firtstname":"Kadir","lastname":"polatkol"}}, indent="/n"))
    # dosyayı bir boşluk brakarak oluşturur. 
    
```


- ***separators :*** Bu parametre verilen değeri öğeler arasında ayraç olarak kullanır. Verilen değer tuple tipinde olmalıdır. Varsayılan olarak şu kullanılır: (“,”, “: “) 


```py
    import json

    json.dumps(["üzüm"],ensure_ascii=True)
    >>> '["\\u00fcz\\u00fcm"]'

    json.dumps(["üroloji"],ensure_ascii=False)
    >>> '["üroloji"]'
```

<br><hr>


## JSON FORMATINI SÖZLÜK FORMATINA DÖNÜŞTÜREN FONKSİYONLAR

<br>


1. ***json.load() :*** Bu fonksiyon sadece dosyadaki JSON verilerini python verisine(sözlük) dönüştürür.
2. ***json.loads() :*** Bu fonksiyon JSON verilerini paramtre olarak alır ve  python verisine(sözlük) dönüştürür.

<br>

## PARAMETRELER ;


- ***object_hook :*** Döndürülen verilerin veri tiplerini dönüştürür.

```py
    json.loads('{"mezuniyet": "üniversite", "Bölüm": "Tıp"}',object_hook=list)
    #çıktıyı liste tipinde verecektir
    >>> ['mezuniyet', 'Bölüm']
```
<br>

- ***parse_int :***  İnt tipindeki değerlerin Python koduna dönüştürülürken hangi tipin kullanılması gerektiğini belirler.


```py
    json.loads('{"Satılan": 54, "Kalan": 46}',parse_int=float)
    >>> {'Satılan': 54.0, 'Kalan': 46.0}
```
<br>

- ***parse_float :***  Float tipindeki değerlerin Python koduna dönüştürülürken hangi tipin kullanılması gerektiğini belirler.

```py
    json.loads('[23, 45.2, "yazbel", 512.128]',parse_int=bool,parse_float=list)
    >>> [True, ['4', '5', '.', '2'], 'yazbel', ['5', '1', '2', '.', '1', '2', '8']]
    # intiger degerleri boolean veri tipine dönüştürürken float veri tipindeki değerleri ise listeye aldı.
```
<br>




## ÖRNEK :

### ***json.load() :*** 

```py
    with open("ornek.json") as f:
        veri = json.load(f)
        print(veri)
        print(veri["user1"]["lastname"])
```


### ***json.dump() :***

```py
    data = {
        "user1":{"firstname":"Kadir","lastname":"polatkol"},
        "user2":{"firstname":"kamil","lastname":"polatkol"},
        "user3":{"firstname":"yusuf","lastname":"polatkol"}
    }   

    with open("ornek.json","w") as f :
        json.dump(data, f , indent=2)
        # 2 birim girinti bırakarak yazdıracaktır
```