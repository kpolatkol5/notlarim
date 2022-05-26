# ***JAVASCRİPT'DE CONSOL***

Konsola bir şeyler yazdırmanın birkaç yolu var ;
<br>

```js
    console.log("hello world");
    alert("hello world");
```

<br>

## ***DEĞİŞKEN VE SABİT TANIMLAMAK***

<br>


***let*** ve ***var*** ile değişkenleri tanımlıyoruz. ***const*** ile sabit tanımlıyoruz.

<br>

```js
    var name_1      =   "kadir";
    let name_2      =   "kadir";
    const name_3    =   "kadir";
```

<br>

### ***TEK BİR İFADE İLE BİRDEN FAZLA DEĞİŞKEN OLUŞTURMA***



<br>

```js
    var isim    =   "kadir" ,    soyisim    =   "polatkol",    yas  =   21;
    
    console.log(isim);
    console.log(soyisim);
    console.log(yas);

    >>> kadir
    >>> polatkol
    >>> 21
```
<br>

### ***DEĞİŞKENE SONRADAN VERİ ATAMAK***

<br>

```js
    var isim;
    isim  =  "kadir";

    // sonrdan değer tanımlayacağımız zaman tekrardan var veya let ifadesini kullanmıyoruz.
```

<br>

### ***GLOBAL VE LOCAL ALANLAR***

Bütün script kodlarının arasındaki alan bizim için ***GLOBAL ALANDIR***  heryerden erişilebilir.***" { } "*** süslü parantez ile belirttiğimiz alanlar local alan olarak tanımlanır. Global alana her yerden erişilebilir ancak local alanda tanımlanan değerler o alana özgüdür. Bir örnekle açıklayalım.


<br>


```js
    var isim    =   "kadir";

    if(true){
        var isim    =   "kağan";
        console.log(isim)
    }

    console.log(isim)

    >>> kağan
    >>> kağan
```

<br>

Yukarıdaki örnekte var ile tanımladığımız değişkenin local alanda değerinin değiştiğini gördük. Tanımlama yöntemlerinden ***let*** ifadesini kullanırsak local alanda tanımlanan değişkenin değeri sadece o alanda tanımlandığını ve çalıştığını görebiliriz. Let ile var ın arasındaki fark budur. Bir örnekle açıklayalım. 

<br>

```js
    let isim    =   "kadir";

    if (true){
        
        let isim    =   "kagan";
        console.log(isim)
    }

    console.log(isim)

    >>> kagan
    >>> kadir
```

<br>

İfadeyi let ile tanımladık ve local alandaki değerin gloabal alandan etkilenmediğini gördük. Aynı değişkeni bir de gloabal alanda ekrana yazdırdığımızda  var ile let arasındaki farkı daha net görebiliriz.Son bir örnekle bu konuyu bitirelim.


<br>

```js
    if (true){
        let isim    =   "kagan";
    }

    console.log(isim);

    >>> ReferenceError: isim is not defined
```


<br><hr>

## ***DEĞİŞKEN İÇERİĞİNİN VERİ TÜRÜ***

<br>

***typeof :*** Bir değişkenin veri türünü geriye döndüren bir operatördür.



<br>

```js
    console.log(typeof "hello world");
    console.log(typeof 21);
    console.log(typeof true);

    >>> string
    >>> number
    >>> boolean
```

<br>

***İkinci kullanılan yöntem;***

<br>



```js
    let sayi    =   12
    var sayi_degeri =   typeof(sayi)

    console.log(sayi_degeri)

    >>> number
```
<br><hr>




# ***DEĞİŞKEN TÜR DÖNÜŞÜMLERİ***

<br>


### ***.toString() :***  

<br>

Verileri string ifadeye dönüştürür

<br>

```js
    var val =   21
    var val_to_string   =   val.toString()

    console.log(typeof(val))
    console.log(typeof(val_to_string))

    >>> number
    >>> string
```

<br><hr>


# ***OPERATÖRLER***

<br>

- " ***\+*** "      :   ***TOPLAMA İŞLEMİ YAPAR***
- " ***\-*** "      :   ***ÇIKARTMA İŞLEMİ YAPAR***
- " ***\**** "      :   ***ÇARPMA İŞLEMİ YAPAR***
- " ***/*** "       :   ***BÖLME İŞLEMİ YAPAR***
- " ***%*** "       :   ***BÖLÜM SONUCUNDA KALANI DÖNDÜRÜR***
- " ***++*** "      :   ***ARTTIRMA OPERATÖRÜDÜR DEĞİŞKENDEKİ DEĞERİ BİR ARTIRIR***
- " ***--*** "      :   ***AZALTMA OPERATÖRÜDÜR DEĞİŞKENDEKİ DEĞERİ BİR AZALTIR***
- " ***+=*** "      :   ***TOPLAMA VE ATAMA İŞLEMİ YAPAR***
- " ***-=*** "      :   ***ÇIKARTMA VE ATAMA İŞLEMİ YAPAR***
- " ***\*=*** "     :   ***ÇARPMA VE ATAMA İŞLEMİ YAPAR***
- " ***/=*** "      :   ***BÖLME VE ATAMA İŞLEMİ YAPAR***
- " ***%=*** "      :   ***MOD ALMA VE ATAMA İŞLEMİ YAPAR***
- " **==** "        :   ***KARŞILAŞTIRMA OPERATÖRÜDÜR DEĞERLERİN BİRBİRİNE EŞİT OLMASI GEREKİR***
- " ***!=*** "      :   ***EŞİT DEĞİL*** 
- " ***===*** "     :   ***DENKLİK OPERATÖRÜDÜR DEĞERLERİN VE VERİ TÜRLERİNİN EŞİT OLMASI GEREKMEKTEDİR***
- " ***<*** "       :   ***KÜÇÜK OLDUĞU DURUMLARDA TRUE DEĞERİNİ DÖNDÜRÜR***
- " ***<=*** "      :   ***KÜÇÜK VE EŞİT OLDUĞU DURUMLARDA TRUE DEĞERİNİ DÖNDÜRÜR***
- " ***>*** "       :   ***BÜYÜK OLDUĞU DURUMLARDA TRUE DEĞERİNİ DÖNDÜRÜR***
- " ***>=*** "      :   ***BÜYÜK EŞİT OLDUĞU DURUMLARDA TRUE DEĞERİNİ DÖNDÜRÜR***
- " ***&&*** "      :   VE OPERATÖRÜDÜR İKİ DEĞERDEN BİRİNİN FALSE OLMASI DURUMUNDA FALSE DEĞERİ DÖNDÜRÜR
- " ***||*** "      :   VEYA OPERATÖRÜDÜR İKİ DEĞERDEN BİR TANESİ BİLE TRUE DEĞERİ VARSA TRUE DEĞERİNİ DÖNDÜRÜR


<br>


# ***DEĞİŞKENLERDE ÖNTANIMLI METODLAR***

<br>

## ***.lenght Metodu :***

<br>

Değişken içeriğinin karakter sayısını geriye döndürür.


<br>

```js
    var isim = "kadir";
    console.log(isim.length);

    var soyisim = "polatkol";
    var result = soyisim.length;

    console.log(result);

    >>> 5
    >>> 8
```

<br><hr>


## ***eval() Metodu :***

<br>

Kendisine parametre olarak verilen değerleri javascipt kodlarına çevirerek komut gibi çalışıtır ve değeri geriye döndürür.

<br>

```js
    function deneme(){
        console.log("deneme mesajı");
    }

    var result  =   eval("deneme()");
    
    >>> deneme
```
<br>

```js
    console.log(eval("10 * 100"));
    
    >>> 1000
```
<br><hr>


## ***.trim() Metodu :***

<br>

Değişken içerisindeki başındaki ve sonundaki boşluk karakterlerini temizler ve değeri geriye döndürür.

<br>

```js
var val =   "      Hello World  !"

console.log(val.trim());

>>> Hello World  !
```

<br><hr>


## ***slice() Metodu :***

<br>

Verilen parametreler ile değişkendeki verileri kopyalar ve kopyaladığı değeri geriye döndürür. ilk parametre ***başlangıç parametresi*** ikinci parametre ise ***bitiş parametresidir***.

<br>

```js
    var val =   "hello world"

    console.log(val.slice());
    console.log(val.slice(0,5));

    console.log(val.slice(6));
    console.log(val.slice(6,9));

    >>>  hello world
    >>>  hello
    >>>  world
    >>>  wor
```
<br><hr>


## ***subsitring() Metodu :***

<br>














<br><hr>

## ***KOŞUL İFADELERİ (if else)***

<br>


Koşul ifadelerinde parantezler arasına true veya false üretecek değerleri kullanırız. Bu sayede koşul ifadelerini kullanarak birtakım işlemleri kodların akışına göre değerlendirebiliriz.

<br>

```js
    if(true){
        console.log("sonuç true")
    }
    else{
        console.log("sonuç false")
    }

    >>> sonuç true
    //  eğer if değerinin içerisindeki değer false olsaydı else kod blogu çalışacaktı
```


<br>

```js
    var username    =   "kadir"
    var pass        =   "123456"


    if (username == "kadir" && pass =="123456"){
        console.log("giriş başarılı")
    }
    else if(username == "kadir" || pass=="123456"){
        console.log("kullanıcı adı veya parola yanlış")
    }
    else{
        console.log("giriş başarısız")
    }   
```

<br>

