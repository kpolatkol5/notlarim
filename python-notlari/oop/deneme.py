
data = [
    {
        "marka":"toyota",
        "renk":"beyaz",
        "fiyat":100000,
        "model":2002
    },
        {
        "marka":"mercedes",
        "renk":"beyaz",
        "fiyat":130000,
        "model":2008
    },
        {
        "marka":"bmw",
        "renk":"lacivert",
        "fiyat":180000,
        "model":2008
    },
        {
        "marka":"mazda",
        "renk":"kırmızı",
        "fiyat":150000,
        "model":2017
    },
        {
        "marka":"ford",
        "renk":"gri",
        "fiyat":300000,
        "model":2022
    },
        {
        "marka":"volkswagen ",
        "renk":"beyaz",
        "fiyat":280000,
        "model":2019
    },
]


class Arabalar():
    vergi_orani =   4.5
    zam_orani   =   1.5


    def __init__(self, marka , renk , fiyat , model):
        self.marka  =   marka
        self.renk   =   renk
        self.fiyat  =   fiyat
        self.model  =   model

    def zam_uygula(self):

        return self.fiyat * Arabalar.zam_orani


    def vergi_uygula(self):

        return  self.zam_uygula() * Arabalar.vergi_orani

    @classmethod
    def vergi_orani_guncelle(cls , yeni_oran):
        cls.vergi_orani = yeni_oran


    @classmethod
    def toplu_arac_ekle(cls ,data):
        eklenen_veriler = []

        for i in data:
           eklenen_veriler.append(cls(i["marka"], i["renk"], i["fiyat"], i["model"]))

        return eklenen_veriler

    @staticmethod
    def kok_al(deger):

        return deger ** 0.5


print(Arabalar.kok_al(144))