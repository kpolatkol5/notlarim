# ***Encapsulation  ( Kapsülleme )***

<br>

Bağı durumlarda sınıf içerisinde tanımladığımız metodların ve niteliklerin  dışarıdan erişilmesini istemeyiz. Bu durumlarda nitelik veya metodlaruımızı gizleriz ve dışarıdan erişilmesini engelleriz. Çünkü bu metdlar sınıf içerisinde önemli bir yeri vardır ve değiştirilmemesi gerekir.

<br>

## ***Gizli Üyeler***

<br>

Üyeleri __nitelik veya _nitelik şeklinde tanımlayabilriz.

<br>

```py
class Arabalar():

    __arac_listesi = []

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil
        self.kullanim   =   f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."

    def __arac_kullanim(self):
        return f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 ,2022)

print(dir(Arabalar))
```

<br>

Örnekte de olduğu gibi tanımlayacağımız değişkenin veya metodun baş kısmında eğer 2 adet alt çizgi varsa bu öğeler gizlidir ve dışarıdan erişilemez sadece sınıf içerisindeki işlerini yaparlar.

Eğer tek bir alt çizgi kullanırsak bu üyerleri yarı gizli üye yapmış oluyoruz ancak bu topluluk açısından dikkate alınabilecek bir şeydir. Tek alt çizgi kullanırsak bu öğrelere dışarıdan erişebilirz ancak kodu okuyan yazılımcı arkadaslarımıza bunun gizli üye olduğunu ve üzerinde işlem yapılmaması gerektiği bilgisini veririr.

<br>


```py
class Arabalar():

    _arac_listesi = []

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.fiyat      =   fiyat
        self.model      =   model
        self.yil        =   yil
        self.__kullanim   =   f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."

    def _arac_kullanim(self):
        return f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 ,2022)

print(dir(Arabalar))
```
<br>

Bu öğelere dışarıdan erişilebilir ancak tek alt çizgi ile mesaj vermiş oluyoruz.

<br>



## ***Gizli Üyeleri Görüntüleme ve Yeniden Tanımlama*** 

<br>

Eğer gizli üyeleri görüntüleme veya değiştirme gibi ihtiyaçlarımız olursa get ve set metodlarını kullanabiliriz

<br>

```py
class Arabalar():

    __arac_listesi = []

    def __init__(self, marka , renk , fiyat , model , yil):
        self.marka      =   marka
        self.renk       =   renk
        self.__fiyat    =   fiyat
        self.model      =   model
        self.yil        =   yil
        self.kullanim   =   f"Bu arac {int(self.yil) - int(self.model)} yıldır kullanılıyor."


    def getAracFiyat(self):
        return self.__fiyat

    def setAracFiyat(self,yeni_fiyat):
        self.__fiyat = yeni_fiyat
        
        return self.__fiyat


araba1  =   Arabalar("bmw", "beyaz", "120000", 2019 ,2022)

print(araba1.getAracFiyat())

print(araba1.setAracFiyat(130000))

>>> 120000
>>> 130000
```

Set metodunu kullanmak pek mantıklı olmayabilir ancak ihtiyacınız olduğuna kullanabilirsiniz.