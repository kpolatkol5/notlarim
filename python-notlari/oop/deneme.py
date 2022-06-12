class Arabalar():

    toplam_arac =   []

    def __init__(self ,aracin_markasi, renk , fiyat):

        self.aracin_markasi       =   aracin_markasi       
        self.renk                 =   renk     
        self.fiyat                =   fiyat        
        self.toplam_arac          =   []
        # print(self.aracin_markasi,self.renk , self.fiyat)

        Arabalar.toplam_arac.append(self.aracin_markasi)


araba1  =   Arabalar(aracin_markasi="mazda", renk = "kırmızı", fiyat = 120000)
araba2  =   Arabalar(aracin_markasi="toyota", renk = "mavi", fiyat = 100000)


print(araba1.toplam_arac)
print(araba2.toplam_arac)
# ilk başta örnek niteliklerindeki toplam arac listesi boş


araba1.toplam_arac.append("araba1 nesnesinden eklendi")
#daha sonra sadece araba1 nesnesindeki toplam arac listesine değer eklendi

print(f"araba1 nesnesindeki toplam arac listesi: {araba1.toplam_arac}")
print(f"araba2 nesnesindeki toplam arac listesi: {araba2.toplam_arac}")
# sadece araba1 e eklenen değer araba 2 nesnesine eklenmediğini sadece araba1 
# e özel olduğunu görebilirsiniz



print(f"sınıf nitliğindeki toplam arac listesindeki değerler : {Arabalar.toplam_arac} ")









# print(f"Objeler üzerinden ulaşmaya çalışmak: {araba1.toplam_arac}")
# print(f"Objeler üzerinden ulaşmaya çalışmak: {araba2.toplam_arac}")
# print(f"Sınıf üzerinden sınıf niteliklerine: {Arabalar.toplam_arac}")