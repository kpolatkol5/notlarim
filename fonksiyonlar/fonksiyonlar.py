
#! ÖR-1:

# def us_al(num):

#     print(num**2)

# us_al(5)

#?----------------------------------------------------------
#! ÖR-2:

# def kullanici_ekle(isim, soyisim , yas ):

#     bilgiler    =   """
#     {} isimli kullanıcının bilgileri;

#     Kullanıcının adı            :   {} , 
#     Kullanıcının soyadı         :   {} , 
#     Kullanıcının yaşı           :   {} ,
#     Kullanıcının doğum tarihi   :   {}, 
#     """
#     print(bilgiler.format(isim,isim,soyisim,yas,2022-yas))


# kullanici_ekle("kadir", "polatkol",22)


#?----------------------------------------------------------
#! ÖR-3:
##Eksik parametreli fonksiyon örneği

# def kullanici_ekle(isim, soyisim , yas ):

#     bilgiler    =   f"""
#     {isim} isimli kullanıcının bilgileri;
#     Kullanıcının adı            :   {isim} , 
#     Kullanıcının yaşı           :   {yas} ,
#     Kullanıcının doğum tarihi   :   {2022-yas}, 
#     """
#     print(bilgiler) 
#     # soy isim kullanılmadı


# kullanici_ekle("kadir", "polatkol",22)


#?----------------------------------------------------------
#! ÖR-4:

## Fonksiyonu çağırırken eksik parametre girersek hata alırız.

# def kullanici_ekle(isim, soyisim , yas ):

#     bilgiler    =   """
#     {} isimli kullanıcının bilgileri;

#     Kullanıcının adı            :   {} , 
#     Kullanıcının soyadı         :   {} , 
#     Kullanıcının yaşı           :   {} ,
#     Kullanıcının doğum tarihi   :   {}, 
#     """
#     print(bilgiler.format(isim,isim,soyisim,yas,2022-yas))


# kullanici_ekle("kadir", "polatkol")

#?----------------------------------------------------------
#! ÖR-5:

## Varsayılan parametre tanımlarsak

# def kullanici_ekle(isim = "bilinmiyor", soyisim ="bilinmiyor" , yas = "bilinmiyor" ):

#     bilgiler    =   """
#     {} isimli kullanıcının bilgileri;

#     Kullanıcının adı            :   {} , 
#     Kullanıcının soyadı         :   {} , 
#     Kullanıcının yaşı           :   {} ,
#     Kullanıcının doğum tarihi   :   {}, 
#     """
#     print(bilgiler.format(isim,isim,soyisim,yas, yas  if yas == "bilinmiyor" else 2022-yas ))

#     # Burada hata almamak için doğum tarihi hesaplamasında farklı bir if kullanıldı. Eğer yas paramteresinin değeri "bilinmiyor ise direkt yazdırılacaktır yani if bloğunun sol tarafı çalışır eğer bilinmiyor değil ise if blogunun sağ tarafı çalışır ve işlem yapar"

# kullanici_ekle("kadir", "polatkol",19)


#?----------------------------------------------------------
#! ÖR-6:

## isimli parametre tanımlamak

# def kullanici_ekle(isim = "bilinmiyor", soyisim ="bilinmiyor" , yas = "bilinmiyor" ):

#     bilgiler    =   """
#     {} isimli kullanıcının bilgileri;

#     Kullanıcının adı            :   {} , 
#     Kullanıcının soyadı         :   {} , 
#     Kullanıcının yaşı           :   {} ,
#     Kullanıcının doğum tarihi   :   {}, 
#     """
#     print(bilgiler.format(isim,isim,soyisim,yas, yas  if yas == "bilinmiyor" else 2022-yas ))

# kullanici_ekle(yas=20, soyisim="polatkol", isim="kadir")

#?----------------------------------------------------------
#! ÖR-7:

## (*args)

# def getir(*args):

#     return args
#     # return ilerleyen kısımlarada anlatılacak

# # getir("kadir" ,"polatkol" , "20 " ,20000)

# result  =   getir("kadir" ,"polatkol" , "20 " ,20000)
# print(result)
# print(type(result))


#?----------------------------------------------------------
#! ÖR-8:

# ## (**kwargs)

# def getir(**kwargs):

#     return kwargs
    
# # getir("kadir" ,"polatkol" , "20 " ,20000)

# result  =   getir(isim="kadir" ,soyisim="polatkol" ,yas= "20 " ,dt= 2000)
# print(result)
# print(type(result))


#?----------------------------------------------------------
#! ÖR-9:

# def getir(**kwargs):

#     for par1 , par2 in kwargs.items():
#         print(f"{par1}\t:  {par2}")

# getir(isim="kadir" ,soyisim="polatkol" ,yas= "20 " ,dt= 2000)

# # items() fonksiyonu sözlüklerde anahtar ve değer öğelerini verir for döngüsündeki par1 sözlükteki anahtar değerini temsil ederkn , par2 değeri de anahtarın değerini temsil eder.



#?----------------------------------------------------------
#! ÖR-9:


# def bul(*args, **kwargs):
#     for par1 in args:
#         if par1 in kwargs:
#             print(f"{par1} : {kwargs[par1]}")

# sözlük = {"ad"      : "kadir",
#           "soyad" : "polatkol",
#           "yas": "21"}

# bul("ad", "soyad", "yas", "dt", **sözlük)


#?----------------------------------------------------------
#! ÖR-10:


# def isim_ne():
#     result  =   input("isminiz nedir?")
#     print(f"{result} ")

# result  =   isim_ne()

# print(result)

# print(f"merhaba {result} nasıl gidiyor.")


#?----------------------------------------------------------
#! ÖR-10:

# def isim_ne():
#     result  =   input("isiminiz nedir?   ")

# print(isim_ne())

#?----------------------------------------------------------
#! ÖR-11:

# def isim_ne():
#     result  =   input("isiminiz nedir?   ")
#     return result

# print(isim_ne())

#?----------------------------------------------------------
#! ÖR-12:

# def deger_gir():
#     liste   =   []

#     while True:
#         result  =   input("deger gir(çıkmak için q ya basın) :   ")
    
#         if result == "q":
#             break
#         else:
#             liste.append(result)
    
#     return liste

# result  =   deger_gir()

# print(*result , sep="\n")

#?----------------------------------------------------------
#! ÖR-13:

## GLOBAL ALAN

# result  =   []

# def local_alan():
#     return result.append("bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.")
#     # result global alanda tanımlı local alanda tanımlı değil
# print(result)
# local_alan()
# print(result)


#! ÖR-14:
# result  =   []

# def local_alan():
#     result  = []

#     result.append("bu alan local alandır ve global alnda tanımlanan değişkenlerden farklıdır.")
    
#     return result 
#     # result local alanda tanımlı global alanda tanımlı olan listeye değer aktarılamadı.

# print(result)
# print(local_alan())
# print(result)


#! ÖR-15:

# result  =   []

# def global_liste_degis():
#     result += ["kadir", "polatkol"]
#     return result
    
#     #burada listeye veri eklemedik listeyi yeniden tanımladık , aynı durum karakter dizileri için de geçerlidir.

# print(result)
# global_liste_degis()
# print(result)



#! ÖR-16:

# text    =   "kadir"


# def degistir():
#     global text
    
#     text    +=  " polatkol" 
#     return text

# print(text)
# degistir()
# print(text)

#?----------------------------------------------------------

#! ÖR-17:

# #  abs() fonksiyonu

# print(abs(-98))



#?----------------------------------------------------------

#! ÖR-19:

# print(round(12.4))
# print(round(12.8))
# print(round(97/3, 1))
# print(round(97/3, 2))

#?----------------------------------------------------------

#! ÖR-20:


# liste   =   ["kadir", "polatkol", 21]
# liste2   =   ["kadir", "polatkol", 21 , False]

# print(all(liste))
# print(all(liste))

#?----------------------------------------------------------

#! ÖR-21:

# liste   =   [0 ,False]
# liste2   =   ["kadir", False]

# print(any(liste))
# print(any(liste2))


#?----------------------------------------------------------

#! ÖR-22:

print(bool(12))
print(bool([]))
