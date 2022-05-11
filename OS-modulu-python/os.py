import os

# print(os.name)

# print(os.sep)

# os_imlec    =   os.sep

# meyveler    =   ["muz","kivi" , "karpuz"]

# liste       =   os_imlec.join(meyveler)

# print(liste)


# print(os.getcwd())

# --------------------------------------------------------------


# #   ÖR1:
# gidilecek_konum     =   "C:/Users/Kadir/OneDrive/Masaüstü/projeler/frontend"

# konumum             =   os.getcwd()

# print(konumum)
# #şuanki bulunduğum konum

# os.chdir(gidilecek_konum)
# #istediğim konuma gittim

# print(os.getcwd())
# # istediğim konuma gittiğimin kanıtı 



# --------------------------------------------------------------
# # #   ÖR2:




# print("Şuan içinde bulunuduğumuz dizin : " , os.getcwd())

# print("dosya isimleri; ", *os.listdir() , sep ="\n")
# # yıldız sayesinde tüm elemanları tek tek aldık , eğer ilk defa görüyorsanız araştırmanızı tavsiye ederim


# --------------------------------------------------------------

# #   ÖR3:


# print(os.listdir(os.getcwd()))

# print(os.listdir("."))

# print(os.listdir(os.curdir))



# # ancak

# print(os.getcwd())

# print(os.curdir)
 
## --------------------------------------------------------------

# #   ÖR4:

# print(os.pardir)

## --------------------------------------------------------------
# #   ÖR5:

# print(os.listdir(os.getcwd()))
# # dizindeki dosyaları listeledik

# os.startfile("os-deneme.txt")
# # notepad ile açacaktır

## --------------------------------------------------------------
# #   ÖR6:

# os.mkdir("yeni-dizin")
# # Bulunduğumuz dizinde oluşturacaktır.

# os.mkdir("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")
# # ben masaüstü yolunu verdim siz de kendi bilgisayarınızda bunu yapabilrisiniz. ters taksime dikkt ediniz.

## --------------------------------------------------------------
# #   ÖR7:

# os.makedirs("C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/yenidizin1/yenidizin2")


## --------------------------------------------------------------
# #   ÖR8:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

# os.chdir(konum)
# print(os.getcwd())

# os.rename("yenidizin1", "rename_ile_degistirildi")
# print(os.listdir())




## --------------------------------------------------------------
# #   ÖR9:



# konum   =   "D:/yeni-dizin"

# os.chdir(konum)
# print(os.getcwd())
# # konumda belirtiğimiz dizine gittik

# print(os.listdir())
# #konumdaki dosyalara bakalım

# os.chdir("rename_ile_degistirildi")
# print(os.getcwd())
# print(os.listdir())
# # alt dizine gittik ve bu alt dizindeki dizinleri listeledik


# os.remove("beni_sil")
# print(os.listdir())


## --------------------------------------------------------------
# #   ÖR10:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/dizin-1/dizin-2/dizin-3"

# os.removedirs(konum)



## --------------------------------------------------------------
# #   ÖR11:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt"

# text_info   = os.stat(konum)

# print("dosyanın son erisilme tarihi : {}".format(text_info.st_atime))
# print("oluştrulma tarihi : {} ".format(text_info.st_ctime))
# print("dosyanın en sonki değiştirilme tarihi : {}" .format(text_info.st_mtime))
# print("dosyanın boyutu : {}".format(text_info.st_size))#byte


## --------------------------------------------------------------
# #   ÖR12:


# os.system("calc.exe")#hesap makinasınıu açar

# os.system("appwiz.cpl")#program ekle veya kaldır ekranını açar


## --------------------------------------------------------------
# #   ÖR13:

# sistem  =   os.environ
# # print(sistem)
# # bir sözlük geriye döndürür

# for i in sistem:
#     print("{} \t : {}".format(i , sistem[i]) )



## --------------------------------------------------------------
# #   ÖR14:


# dosya_yolu  =   os.path.abspath("os.md")

# print(dosya_yolu)
# # bir dosyanın tam yolunun ne olduğunu söyler



## --------------------------------------------------------------
# #   ÖR15:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"

# print(os.path.dirname(konum))


## --------------------------------------------------------------
# #   ÖR16:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
# print(os.path.exists(konum))

## --------------------------------------------------------------
# #   ÖR17:

# print(os.path.expanduser("~"))


## --------------------------------------------------------------
# #   ÖR18:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/os.md"
# konum2   =   "C:/Users/Kadir/OneDrive/Masaüstü/düzenlenecek-notlar/OS-modulu-python/"

# print(os.path.isdir(konum))
# print(os.path.isdir(konum2))


## --------------------------------------------------------------
# #   ÖR19:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

# yeni_konum   =  os.path.join(konum,"dizin1" , "dizin2")

# # print(konum)
# # print(yeni_konum)

# #eski konumla yeni konumu kıyaslayalım

# os.chdir(konum)
# print(os.listdir())


## --------------------------------------------------------------
# #   ÖR20:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin"

# result  =   os.path.split(konum) 

# print(konum)
# print(result)
# print(type(result))



## --------------------------------------------------------------
# # #   ÖR20:

# konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/os.txt"

# son_eleman  =   os.path.split(konum)   

# ayir    =    os.path.splitext(son_eleman[1])

# print(konum)
# print(son_eleman)
# print(ayir)
# print(type(ayir))


## --------------------------------------------------------------
# # #   ÖR21:

konum   =   "C:/Users/Kadir/OneDrive/Masaüstü/yeni-dizin/"


for i in os.walk(konum):
    print(i)