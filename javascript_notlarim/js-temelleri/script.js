// console.log(typeof "hello world");
// console.log(typeof 21);
// console.log(typeof true);

//?-----------------------------------------------------

// ! ÖR:1

// var isim    =   "kadir" ,    soyisim    =   "polatkol",    yas  =   21;
    
// console.log(isim);
// console.log(soyisim);
// console.log(yas);



//?-----------------------------------------------------

// ! ÖR:2

/*

let sayi    =   12
var sayi_degeri =   typeof(sayi)

console.log(sayi_degeri)

*/



//?-----------------------------------------------------

// ! ÖR:3

// var val =   21
// var val_to_string   =   val.toString()

// console.log(typeof(val))
// console.log(typeof(val_to_string))


//?-----------------------------------------------------

// ! ÖR:4

// var val =   6;


// if(true){
//     console.log("sonuç true")
// }
// else{
//     console.log("sonuç false")
// }

//?-----------------------------------------------------

// ! ÖR:5


// var username    =   "kadir"
// var pass        =   "123456"


// if (username == "kadir" && pass =="123456"){
//     console.log("giriş başarılı")
// }
// else if(username == "kadir" || pass=="123456"){
//     console.log("kullanıcı adı veya parola yanlış")
// }
// else{
//     console.log("giriş başarısız")
// }

//?-----------------------------------------------------

// ! ÖR:5 
// local ve global alan örnekleri

// var isim    =   "kadir";

// if(true){
//     var isim    =   "kağan";
//     console.log(isim)
// }

// console.log(isim)

//*-----------------------------------------------------


// let isim    =   "kadir";

// if (true){

//     let isim    =   "kagan";
//     console.log(isim)
// }

// console.log(isim)

//*-----------------------------------------------------

// if (true){
//     let isim    =   "kagan";
// }

// console.log(isim)

//?-----------------------------------------------------

// ! ÖR:6

// // Değişkene sonradan veri atamak

// var isim;
// isim = "kadir";

// //? sonrdan değer tanımlayacağımız zaman tekrardan var veya let ifadesini kullanmıyoruz


//?-----------------------------------------------------

// ! ÖR:6

// lenght metodu


// var isim = "kadir";
// console.log(isim.length);


// var soyisim = "polatkol";
// var result = soyisim.length;

// console.log(result);

//?-----------------------------------------------------

// ! ÖR:7

// eval() metodu


// function deneme(){
//     console.log("deneme mesajı");
// }

// var result  =   eval("deneme()");

// console.log(eval("10 * 100"))


//?-----------------------------------------------------

// ! ÖR:8

// trim() metodu

// var val =   "      Hello World!  "

// console.log(val.trim());



//?-----------------------------------------------------

// ! ÖR:9

// .slice() metodu

var val =   "hello world"

console.log(val.slice());
console.log(val.slice(0,5));

console.log(val.slice(6));
console.log(val.slice(6,9));



