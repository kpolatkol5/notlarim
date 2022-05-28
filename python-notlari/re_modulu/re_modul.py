import re

#! ÖR-1 :

# text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type"

# result  =   re.match("Lorem", text)

# # print(result)  # geriye bir obje döndürdüğünü görebilirsiniz.

# print(dir(result))
# # bu objedeki metodları görüntülemek istersek.


#?-----------------------------------------------------------------------------------------

#! ÖR-2 :


# text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

# result  =   re.match("Lorem", text)

# print(result)
# print(result.span())    #ifadenin sorgu dizisindeki yeri
# print(result.group())   #aradığımız ifade


#?-----------------------------------------------------------------------------------------

#! ÖR-3 :


# text    =   "Lorem Ipsum is simply dummy Lorem text of the printing and typesetting industry."
# text2    =   "Ipsum is simply dummy Lorem text of the printing and typesetting industry."

# result  =   re.search("Lorem", text)
# result2  =   re.search("Lorem", text2)

# print(f" text1 :  {result.group()} , {result.span()} " )
# print(f" text2 :  {result2.group()} , {result2.span()} " )



#?-----------------------------------------------------------------------------------------

#! ÖR-4 :

# text    =   "Lorem kadir Ipsum kader is simply dummy Lorem text kadar of the printing and typesetting industry."

# for i in text.split(" "):
#     result  =   re.search("kad[iea]r", i)

#     if result:
#         print(result.group())

#?-----------------------------------------------------------------------------------------

#! ÖR-5 :

# text    =   "Lorem kadirden Ipsum kaderdir is simply dummy Lorem text kadardır of the printing and typesetting industry."

# for i in text.split(" "):
#     result  =   re.search("kad[iea]rd[eiı]", i)

#     if result:
#         print(result.group())



#?-----------------------------------------------------------------------------------------

#! ÖR-6 :

# text    =   "Lorem kadiri Ipsum kader2 is simply dummy Lorem text kadarA of the printing and typesetting industry."

# for i in text.split(" "):
#     result  =   re.match("kad[iea]r.", i)

#     if result:
#         print(result.group())


#?-----------------------------------------------------------------------------------------

#! ÖR-7 :



# liste = ["12ASst", "q21wesat", "saVwsdaat","kaaat"]

# for i in liste:
#     if re.match(".*at",i):
#         print(i)

#?-----------------------------------------------------------------------------------------

#! ÖR-8 :


# liste = ["aaahmet", "messssshmet", "met", "kezban"]

# for i in liste:
#     if re.match(".+met",i):
#         print(i)


#?-----------------------------------------------------------------------------------------

#! ÖR-9 :

# text    =   "st sat saat saaat kadir"

# for i in text.split(" "):
#     if re.match("sa?t", i):
#         print(i)




#?-----------------------------------------------------------------------------------------

#! ÖR-9 :

# text    =   "st sat saat saaat kadir"

# for i in text.split(" "):
#     if re.match("sa{2}t", i):
#         print(i)

#?-----------------------------------------------------------------------------------------

#! ÖR-10 :


# text    =   "st sat saat saaat kadir"

# for i in text.split(" "):
#     if re.match("sa{1,2}t", i):
#         print(i)

#?-----------------------------------------------------------------------------------------

#! ÖR-10 :


# text        =   "st sat saat saaat kadir"

# result      =   re.search("^s.", text)
# result2     =   re.search("^k.*", text)

# print(result)
# print(result2)



#?-----------------------------------------------------------------------------------------

#! ÖR-11 :

# text      =   "kadir st sat saat saaat"


# for i in text.split():
#     result  =   re.search("^k.", i)
#     if result:
#         print(result.group())

#?-----------------------------------------------------------------------------------------

#! ÖR-12 :


# text      =   "kadir st sat saat kadir saaat"


# for i in text.split():
#     result  =   re.search("^k.*", i)
#     if result:
#         print(result.group())


#?-----------------------------------------------------------------------------------------

#! ÖR-13 :

# text      =   "kAdir st sat saat ka2dir  kadir kaDir2 saaat"

# for i in text.split():
#     result  =   re.search("k[^A-Z][^0-9].*", i)
#     if result:
#         print(result.group())


#?-----------------------------------------------------------------------------------------

#! ÖR-14 :

# text    =   "kadir3  asda kadar5 turşu falan3 34 python3"

# for i in text.split(" "):
#     result  =   re.search(".*[0-9]$", i)
#     if result:
#         print(result.group())


#?-----------------------------------------------------------------------------------------

#! ÖR-15 :


# text    =   "10+ google+ parol+ Kadir kadir+ topla+"

# for i in text.split():
#     result  =   re.search("[a-z].*\+$)|[A-Z].*", i)
#     if result:
#         print(result.group())

# #* çeviri : Birinci ifade kalıbında sadece küçük harfle başlayan ve sonu + ile biten karakterleri aldık
# # *çeviri2 : İkinci ifadede ise Büyük harfle başlayan karakterleri ayıkladık.


#?-----------------------------------------------------------------------------------------

#! ÖR-16 :


# text    =   "10+ google parol Kadir kadir topla"


# result  =   re.search("[K-k]adir", text)
# print(result)

#?-----------------------------------------------------------------------------------------

#! ÖR-17 :


# text    =   "10+  google+ parol+ Kadir Kadirsdfgs+ kadir+ topla+"

# for i in text.split():
#     result  =   re.search("([K-k]adir)\+$", i)
#     if result:
#         print(result.group())

#?-----------------------------------------------------------------------------------------

#! ÖR-18 :

# text    =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"


# for i in text.split(" "):
#     result  =   re.search("(Lorem Ipsum)|(is)|(simply)|(dummy text)|(of)|(the printing and)|(typesetting)|(industry)", i)
#     if result:
#         print(f"sonuç:   {result.group()}")
#     else:
#         print("sonuç:   yok")

#?-----------------------------------------------------------------------------------------

#! ÖR-19 :

# text     =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

# result  =   re.search("(Lorem) (Ipsum) (is) (simply) (dummy) (text) (of) (the) (printing) (and) (typesetting) (industry)", text)


# print(result)
# print(result.group())
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))

#?-----------------------------------------------------------------------------------------

#! ÖR-20 :

# text     =   "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

# result  =   re.search("(Lorem) (Ipsum) (is) (simply) (dummy) (text) (of) (the) (printing) (and) (typesetting) (industry)", text)


# print(result.groups())




#?-----------------------------------------------------------------------------------------

#! ÖR-20 :



# text     =   "Lorem Ipsum is simply 2Dummy text of 5the printing and typesetting industry"


# derle   =   re.compile("\d[A-Z].*")

# for i in text.split(" "):
#     result  =   derle.search(i)
#     if result:
#         print(result.group())


#?-----------------------------------------------------------------------------------------

#! ÖR-21 :

# text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"


# derle   =   re.compile("(lorem)" , re.IGNORECASE)

# for i in text.split(" "):
#     result  =   derle.search(i)
#     if result:
#         print(result.group())



#?-----------------------------------------------------------------------------------------

#! ÖR-22 :

# text     =   "Lorem Ipsum is simply dummy text of\n lorem the printing and typesetting loRem industry"

# derle   =   re.compile("(lorem).*" , re.IGNORECASE)

# print(derle.search(text).group())



#?-----------------------------------------------------------------------------------------

#! ÖR-22 :

# text     =   "Lorem Ipsum is simply dummy text of\n lorem the printing and typesetting loRem industry"

# derle   =   re.compile("(lorem).*" , re.DOTALL)

# print(derle.search(text).group())



#?-----------------------------------------------------------------------------------------

#! ÖR-23 :

# text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"

# derle   =   re.compile("lorem" , re.IGNORECASE)

# liste=[]

# for i in text.split(" "):
#     result  =   derle.search(i)

#     if result:
#         result  =   derle.sub("Kadir", i)
#         liste.append(result)
#         # EŞLEŞME VARSA EŞLEŞEN KELİMEYİ DEĞİŞTİRİP LİSTEYE EKLEYECEKTİR
#     else:
#         liste.append(i)
#         # EĞER EŞLEŞME YOKSA DEĞİŞTİRECEĞİMİZ BİR KARAKTER DE YOKTUR O YÜZDEN DİREKT EKLEDİK.
        
# print(liste)

#?-----------------------------------------------------------------------------------------

#! ÖR-24 :

text     =   "Lorem Ipsum is simply dummy text of lorem the printing and typesetting loRem industry"

derle   =   re.compile("lorem" , re.IGNORECASE)

liste=[]

for i in text.split(" "):
    result  =   derle.search(i)

    if result:
        result  =   derle.subn("Kadir", i)
        liste.append(result[0])
        print(result[1])
        # EŞLEŞME VARSA EŞLEŞEN KELİMEYİ DEĞİŞTİRİP LİSTEYE EKLEYECEKTİR

    else:
        liste.append(i)
        # EĞER EŞLEŞME YOKSA DEĞİŞTİRECEĞİMİZ BİR KARAKTER DE YOKTUR O YÜZDEN DİREKT EKLEDİK.
        
print(liste)
