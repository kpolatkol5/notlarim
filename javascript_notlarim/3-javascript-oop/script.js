 
 /*
 let sinif = {
     text: "javacript ile sınıf oluşturalım",
     nesne_tabanli_programlama_dilleri: {
         1: "python",
         2: "c#",
         3: "php",
         4: "javascrit",
     },
     sinif_metodu: function () {
         return "sınıfa içerisinde tanımlanan ve o sınıf hakkında bilgi veren fonksiyonlrar clas method denir"
     }
 }

 console.log(sinif.text);
 console.log(sinif.nesne_tabanli_programlama_dilleri);
 console.log(sinif.sinif_metodu());

 */


//  ?------------------------------------------------------------------------

// ! ÖR-2



 var mevcut = [];

 function Sinif(ogrenci_adi, ogrenci_soyadi, ogrenci_cinsiyeti, ogrenci_yasi){

    this.ogrenci_adi            =   ogrenci_adi;
    this.ogrenci_soyadi         =  ogrenci_soyadi;
    this.ogrenci_cinsiyeti      =   ogrenci_cinsiyeti;
    this.ogrenci_yasi           =   ogrenci_yasi;

    mevcut.push([this.ogrenci_adi, this.ogrenci_soyadi,this.ogrenci_cinsiyeti ,this.ogrenci_yasi]);

    this.erkek_mi   =   function(){
            return this.ogrenci_cinsiyeti === "erkek";
    }
 }


 let ogrenci_1 =    new Sinif("kadir", "polatkol" ,"erkek" , 22);
 let ogrenci_2 =    new Sinif("ahmet", "can" ,"erkek" , 22);
 let ogrenci_3 =    new Sinif("burak", "ertunc" ,"erkek" , 24);
 let ogrenci_4 =    new Sinif("sule", "tunc" ,"kız" , 11);


 console.log(mevcut);
 console.log(ogrenci_1.erkek_mi());




//  ?------------------------------------------------------------------------

// ! ÖR-3


// prototype kullanımı



/*

var mevcut = [];

function Sinif(ogrenci_adi, ogrenci_soyadi, ogrenci_cinsiyeti, ogrenci_yasi){

   this.ogrenci_adi            =   ogrenci_adi;
   this.ogrenci_soyadi         =  ogrenci_soyadi;
   this.ogrenci_cinsiyeti      =   ogrenci_cinsiyeti;
   this.ogrenci_yasi           =   ogrenci_yasi;

   mevcut.push([this.ogrenci_adi, this.ogrenci_soyadi,this.ogrenci_cinsiyeti ,this.ogrenci_yasi]);

}

Sinif.prototype.erkek_mi = function(){
    return this.ogrenci_cinsiyeti === "erkek";
}



let ogrenci_1 =    new Sinif("kadir", "polatkol" ,"erkek" , 22);
let ogrenci_2 =    new Sinif("ahmet", "can" ,"erkek" , 22);
let ogrenci_3 =    new Sinif("burak", "ertunc" ,"erkek" , 24);
let ogrenci_4 =    new Sinif("sule", "tunc" ,"kız" , 11);


console.log(mevcut);
console.log(ogrenci_1.erkek_mi());

 */
