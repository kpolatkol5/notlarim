# ***PYTHON DA DOSYA İŞLEMLERİ NEDİR NE İÇİN KULLANILIR.***

<br>

Python ile herhangi bir dosyadan veri okumak verileri değiştirmek veya veri eklemek çıkarmak gibi işlemler yapabiliriz. Peki bunu neden yaparız? Neden dosya işlemlerine ihtiyacımız olur onu öğreneceğiz. Python ile verilerle çok fazla işlem yaparız otomasyon sistemleri veya veri kazımak gibi . Bu sebeple farklı dosyalardaki verilerle mesela json verileri ile çalışırken dosya okuma işlemlerinden sıklıkla faydalanacaksınız.   

<br>

## ***DOSYA OLUŞTRUMAK***
<br>

Python da dosyalar ile çalışırken open fonskiyonundan faydalanacağız . Bu fonskiyonun aldığı birkaç parametreler var bu parametreler sayesinde de dosyaları yeri gelecek python ile dosyadaki verileri okuyacağız değiştireceğiz vs. Ayrıca bu fonksiyon ile dosya da oluşturabiliriz.

***open() fonksiyonu :*** Open fonskiyonu ile yeni bir dosya oluşturubilriz var olan bir dosyayı okuyabilriz  , veri ekleyebiliriz , silebiliriz. Tabi bunu farklı parametreler tanımlayarak yapacağız notların  ilerleyen kısımlarında da buna değineceğim.  

<br>

### NOT: open() fonksiyonunun  ***encoding="utf-8"*** parametresi vardır. Bu parametre türkçe kelimelerin düzgün yazılmasını sağlar. 


<br>


```py
    dosya_olustur  = open("yeni_dosya.txt" , "w" , encoding="utf-8")
```

<br>

- Yukarıdaki örnekte open fonksiyonunu kullandık ve 2 adet parametre belirttik. İlk parametre dosyanın adı ikinci parametre ise dosyayı hangi mod ile işlem yapacağımızı belirttik. Burda ***" w "*** parametresi ile yazma modunda dosyayı açmış olduk.  Bu dosyayı oluştururken terminalde ilgili kökdizinde olduğunuza dikkat edin . Eğer farklı bir kökdizinde  dosya oluşturmak isterseniz  ilk parameteye dosya adı ile beraber kökdizin adını da yazabilrizsinz . Ancak dikkat etmeniz gereken nokta kaçış parametresin dikkat etmeniz gerekiyor. Bir örnek ile açıklayalım.

<br>

```py
    dosya_olustur  = open("C:/Users/Kadir/OneDrive/Masaüstü/projeler/notlar/yeni_dosya.txt" , "w")
    # Ters taksim (\) yerine düz taksim (/)kullanmaya dikkat edin  
```

<br>

### ***İŞTE BAĞZI PARAMETRELER;***

<br>

- ***"w" :*** (write )  :   yazma modudur dosyayı konumda oluşturur
- ***"a" :*** (append)  :   ekleme modu . dosya konumda yoksa oluştrur
- ***"x" :*** (create)  :   oluşturma modu . dosya zaten varsa hata verir.
- ***"r" :*** (read)    :   okuma modu . varsayılan dosya konumda yoksa hata verir.


<br>



Dosya oluştururken dikkat etmemiz gerek kısım eğer o kök dizinde oluşturmak istediğimiz dosya isminde bir dosya yok ise yen ibir dosya oluşturacaktır. Ancak oluşturmak istediğimiz dosya adında bir dosya varsa yeni dosya eklemek yerine varolan dosyada işlem yapacaktır. Open fonksiyonunda yazma parametresi ile işlem yaptığımzda dosyaya bağlanacaktır ve dosyanın içeriğine ekleme yapmadan tüm içeriği silip eklemek istediğimiz içeriği ekleyecektir . Bu komut her seferinde dosyanın içerisindeki veriyi silerek bizim belirttiğimiz veriyi ekleyecektir. Bir örnek ile gösterelim.

<br> 

```py 
    veriler = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis molestias, officiis animi saepe ipsa libero dolorem autem eius fugiat alias est consequatur, excepturi porro repellendus natus recusandae reiciendis nihil perferendis."

    dosya_ac  = open("data.txt" , "w")

    dosya_ac.write(veriler)
```

<br> 

Yukarıdaki örnekte veriler adında bir değişkenin içerisine bir string ifade belirttik. Open fonksiyonu ile dosyayı yazma modu ile açtık. Yukarıdaki örnekte de gördüğünüz gibi yeni bir metod var. ***.write()*** metodu dosyayı açtıktan sonra ekleyeceğimiz veriyi dosyaya yazmak için kullanırız. Open fonksiyonunu tanımladığımız değişkende ***write() metodunu*** kullanırız ve ***.wirite()*** metodnun parantezlerine ise  veriyi tuttuğumuz değişkeni atadık. Tabi isterseniz write()  metodunun parantezleri arasına da veriyi direkt de yazabilirdik ***.dosya_ac.write("lorem ipsum")*** 
  
Dosyayı açıp içerisine birşeyler ekledik. Dosyayla işimiz bittikten sonra kapatmamız gerekir. Eğer kapatmazsak açık kaldığı için kaynakları tüketecektir performans açısından dosyayı kapatman gerkir.Kapatma işlemi için ***.close()*** metodundan faydalanırız. Bu metodu dosyayı açmak için tanımladığımız değişkene tekrar tanımlayrak kullanırız. MESELA;

<br>

```py
    veriler = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis molestias,"

    dosya_ac  = open("data.txt" , "w")

    dosya_ac.write(veriler)

    dosya_ac.close()

```

<br>




## ***DOSYAYI OKUMAK***

<br>

Dosya içerisndeki verileri okuyarak işlemler yapmak isteyebiliriz. Yazma modundayken ***" w "*** paranetresini kullanıyorduk. Okuma yapmak için ise ***" r "*** parametresini kullanırız. Aslında hiçbir parametre belirtmezsek de okuma modunda açacaktır. Bir örnekle açıklayalım.

<br>

```py
    dosya_ac  = open("data.txt" , "r")
    # dosya_ac  = open("data.txt")

    dosyadaki_veri = dosya_ac.read()

    dosya_ac.close()

    print(dosyadaki_veri)
```

<br>

Yukarıdaki örnekte dosyayı açtık ve ***.read()*** metodunu kullandık . Bu metod doyadaki verileri okumamıza imkan veriyor. Bu veriyi bir değişekene atarak ***print()*** fonksiyonu ile ekrana yazdırdığımzda farkı göreceksiniz.


Okuma modunda 3 tane metod vardır ;

1. ***.read()***
2. ***.readline()***
3. ***.readlines()***

<br>
 
Yukarıdaki metodlar okuma işlemi yapar ancak çıktıları farklıdır.


-  ***.read() :*** Bu metodu çalıştrıdığımızda okunan dosyadaki tüm içeriği verecektir.
- ***.readline()*** Bu metod ise dosya içeriğindeki verileri satır satır verecektir.Birkaç kez çağırmak gerekir.
- ***.readlines()*** Bu metod ise dosya içeriğindeki verileri liste şeklinde verir.

<br>

```py
    dosya_ac  = open("data.txt" , "r")

    dosyadaki_veri = dosya_ac.read()

    dosya_ac.close()

    print(dosyadaki_veri)
    >>> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis molestias, officiis animi saepe ipsa libero dolorem autem eius fugiat alias est consequatur, excepturi porro repellendus natus recusandae reiciendis nihil perferendis.
```
<br>

```py
    dosya_ac  = open("data.txt" , "r")

    dosyadaki_veri = dosya_ac.readline()
    print(dosyadaki_veri)

    dosyadaki_veri = dosya_ac.readline()
    print(dosyadaki_veri)

    dosyadaki_veri = dosya_ac.readline()
    print(dosyadaki_veri)

    dosya_ac.close()

    >>> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis molestias, officiis animi saepe ipsa libero dolorem autem eius fugiat alias est consequatur,

        excepturi porro repellendus natus

        recusandae reiciendis nihil perferendis.
```

<br>

```py
    dosya_ac  = open("data.txt" , "r")

    dosyadaki_veri = dosya_ac.readlines()

    print(dosyadaki_veri)

    dosya_ac.close()

    >>> ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Facilis molestias, officiis animi saepe ipsa libero dolorem autem eius fugiat alias est consequatur,\n', 'excepturi porro repellendus natus\n', 'recusandae reiciendis nihil perferendis.']
```

<br>


## ***WİTH NEDİR ?*** 

<br>


Dosyalar ile çalışırken olası hataları önlemek için ya da dosyayı kapatmak için ***.close()***metonu kullanamak sizin için de zor geliyorsa ***with*** kullanabilrisiniz. Dosyada yazma okuma ekleme gibi işlemlerde güvenli bir şekilde dosyayı kapatmak için kullanırız. Bir örnekle açıklayalım.


<br>

```py
    with open("data.txt" , "r") as e : 
        data = e.read()

    print(data)
```

<br>

Normalde dosya işlemelrini nasıl yapıyorsak burda da aynısı geçerli fark ise as değimini kullandık. Normalde bir ***open()*** fonksiyonunu bir değişkene atardık. Burda değişkene atama işlemi yapmadığımız için ***as*** ile buna bir takma ad vermiş olduk.

<br>

## DOSYADAKİ İÇERİKTE GEZİNMEK VE İMLEÇ KAVRAMI

<br>

Okuma modunda da gördüğümüz gibi verileri tek tek çekmeye çalışırsak ***.readline()*** metodu ile dosyadaki veriler artık gelmeyecektir . Tekrar başa sarmayacaktır. Burada biz imlece müdahale edebiliriz. Bunun için birkaç fonksiyon öğreneceğiz. 

<br>

- ***.seek() :*** Bu fonksiyon imelecin kaçıncı bayt konumuna gideceğimizi belirtebiliriz eğer bu değere ***" 0 "*** değerini verisek imleç başa döner.Eğer burada tekrar okuma işlemi yaparsak verileri tekrar alabiliriz.


- ***.tell() :*** Eğer dosyada kaçıncı bayt konumunda olduğumuzu öğrenmek istersej bu metotdan faydalanabilriz. Paramtre vermeden kullanmamız gerekiyor. 


 



<br>

## ***DOSYANIN BAŞINA VERİ EKLEMEK*** 

<br>

Eğer dosyanın başına ekleme yapmak istersek dosyayı hem okuma hem de yazma modunda açmamız gerekir . Çünkü w yani yazma modunda açarsak içerisindeki tüm veriyi silecektir okuma modunda ise veri ekleme işlemi yapamıyorduk. Bunun için dosyalarımızı ***(" r+")*** parametresi ile açacağız

<br>


```py
    with open("data.txt"  , "r+") as e : 
        verileri_al  = e.read()
        #ilk başta tüm verileri alırız 
        e.seek(0)
        #dosyada 0. bayt konumuna geliriz.

        e.write("en başa yeni veriler ekledik\n" + verileri_al)
        # en baştaki verilerin silinemsini önledik ve yeni bir veri eklemiş olduk.

    print(verileri_al)
```

<br>


## ***DOSYANIN ORTASINA VERİ EKLEMEK*** 

<br>

Bir dosyanın ortasına veri eklemek istersek dosyadaki verileri bir liste ile almamız gerekir. Okumamodunda gördüğümüz 3 tane metod vardı . Bunlar ***.read()***  , ***.readline()*** , ***.readlines()*** metodları. Bu metodar arasında readlines() metodu ile verileri biz liste veri türünde alabiliyorduk. Eğer dosyadaki verileri bir listeye atabilirsek bu listenin istediğimiz indexlerine verileri ekleyebiliriz.Bir örnek ile açıklayalım ;


<br>

```py
    with open("data.txt" , "r+") as k :
        data = k.readlines()

        data.insert(1 , "dosyanin ortasina ekle \n")
        data.insert(2 , "dosyanin ortasina ekle2 \n")
        k.seek(0)
        k.writelines(data)


    print(data)
```
<br>

 Yukarıdaki örneği açıklayalım. İlk başta dosyayı hem okuma hem de yazma metodu ile açtık. ***.readlines()*** metodu ile dosya içerisindeki verileri liste veri türünde aldık . daha sonra bu listeye veriler ekledik. ve imleci tekrar başa sardık . Bunu yapmamızın sebebi daha önceden de örneğini vermiştim readlines() metodunda imleç en sonda kalır eğer biz imleci başa sarmazsak tüm verileri en sondan bir daha ekleyecektir.

 Yukarıdaki örnekte ***.writelines()*** adında yeni bir metod gördük. Bu metod liste tipindeki verileri for döngüsü kurmadan verileri tek tek dosyaya yazmamızı sağlıyor. Bunu for döngüsü ile de yapabilirsin ancak adamlar yapmış bize de kullanmak düşer.

<br>

## ***DOSYANIN SONUNA VERİ EKLEMEK*** 

<br>

Bir dosyada işlem yaparken imlecin en sonda kaldığını başa dönemdiğini okuma modununu kullanırken gördük.Tekrar ***" w "*** parametresi ile dosyamızı açarsak içerindeki verilerin silineceğini de biliyoruz. Ancak biz verilerin silinememsini ve dosya içersindeki verilerin sonuna eklenmesini istiyoruz. Bununiçin yeri bir paramtre kullanacağız . ***" a "*** paramtresi dosyanın sonuna içerisndeki verileri silmeden ekleme işlemi yapar. Bir örnekle açıklayalım;

<br>

```py
    with open("data.txt"  , "a") as e : 
        data = e.write("\nyeni veri ekledik")

    with open("data.txt") as r:
        new_data = r.read()

    print(new_data)
    >>> yeni veri ekledik
        yeni veri ekledik # 2. defa çalıştırırsan
```

<br>

İlk başta ilgili dosyamızı ***" a "*** parametresi ile açtık. Normal yazma metodu olan ***.write()*** metodu ile sayfanın sonu verilerimizi eklemiş olduk. Bendaha pratik olması için with değimini kullandım siz dilerseni kullanmaya da bilrisiniz ancak dosyayı tekrardan kapatmayı unutmayın. with değimi tekrar kulladık ve bu sefer okuma modunda açtık. yazma modunda ***" \n "*** ifadesi ile bir alt satıra geçmesini sağladık. Belki fark edemeyebilrisiniz burdaki ters taksim işaretidir ***(" \ ")*** .

<br>

# ***DOSYA METODLARI***

<br>

- Bir dosyanın kapalı olup olmadığını öğrenmek istersen ***.closed()*** niteliğini kullanabilirisin. Dosya kapalı ise ***True*** açıksa **False** değerini geriye döndürür.

```py
    kadir = open("data.txt")

    print(kadir.closed)

    >>> -okuma.py
    >>> False
```


<br>

```py
    kadir = open("data.txt")
    kadir.close()

    print(kadir.closed)

    >>> -okuma.py
    >>> True
```
<br>


- Eğer dosyanın okunabilir bir kipte açılıp açılmadığını öğrenmek istersen ***.readable()*** metodunu kullanabilrisin. True veya False geriye döndürür.

- Aynı şekilde dosyanın Yazma yetkisine sahip olup olmadığını öğrenmek istesen ***.writable()*** metodunu kullanabilirsin bu da True veya False değerlerini geriye döndürür. 

- Eğer dosyanın adını öğrenmek istersen ***.name*** niteliğinden faydalanabilirsin.

- Dosyanın hangi kiple açıldığını öğrenmek istersen (okuma , yazma ) ***.mode*** niteliğinden faydalanabilirsin.

- Dosyanın hangi dil kodlaması ile kodlandığını öğrenmek istersen ***.encoding*** niteliğinden faydalanabilirsin. 

- Dosyaların boyutlarını düşürüp veya arttırmak için ***.turancate()***metodunu kullanabilirsin.Eğer hiçbir parametre vermezsen içeriğin hepsini silecektir. dosyanın kaç byt olmasını istersen bunu parametre olarak verebilrisin mesela  10 byte verdik , belirtiğimiz alan kadarını bırakır ve gerisini siler. 

<br>

```py

    with open("data.txt" , "r+") as k :
        veri = k.read()
        print(veri)

    with open("data.txt" , "r+") as k :
        k.truncate(20)
        yeni_data =  k.read()
        print(yeni_data)

    >>> Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        Lorem ipsum dolor sit amet, consectetur adipisicing elit.

    >>> Lorem ipsum dolor si

```

