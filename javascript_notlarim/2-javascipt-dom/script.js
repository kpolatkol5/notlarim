//!  ÖR 1

/*

var result  =   document.characterSet;
console.log(result)

*/

// ?-------------------------------------------------------------
//!  ÖR 2

// .readyState örneği

/*

function ornek (){
        var result  =   document.readyState;
        document.getElementById("button-1").innerHTML=result;
    }
    
*/

// ?-------------------------------------------------------------

//!  ÖR 3

// hasFocus() örneği

/*
setInterval("odak_kontrol()",1000);   

function odak_kontrol(){
    
    var islem   =   document.hasFocus();
    
    if (document.hasFocus()){
        document.write(islem + " ");
    }else{
        document.write(islem + " ");
    }
}
*/

// ?-------------------------------------------------------------

//!  ÖR 4

//  plugins metodu

/*

 var result  =   navigator.plugins.length;

for (var i=0 ; i < result ;i++  ){

    console.log( navigator.plugins[i].name) ; 

}

 */

// ?-------------------------------------------------------------

//!  ÖR 5

//  createAttribute() örneği

/*

function ornek() {

    var element_sec = document.getElementsByTagName("p")[0];
    var ozellik = document.createAttribute("style");

    ozellik.value = "font-size:50px";
    element_sec.setAttributeNode(ozellik);

}
*/


// ?-------------------------------------------------------------

//!  ÖR 6

//  createElemet() örneği

/*
var result  =   document.createElement("P");
var text    = document.createTextNode("Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus illo,");

result.appendChild(text);

document.body.appendChild(result);
console.log(result);
*/


// ?-------------------------------------------------------------

//!  ÖR 7

//  createComment() örneği

/*

var comment_text    =   "Javascipt ile oluşturuldu";
var comment         =   document.createComment(comment_text);

var ekle            =   document.body.appendChild(comment);

console.log(ekle)

*/


// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*
var buton_element   =   document.getElementById("buton1");

document.addEventListener("click", function () {
    let element     =   document.getElementsByTagName("p")[0];

    element.innerHTML="Tıklandı"
  })

*/



  // ?-------------------------------------------------------------

//!  ÖR 9

// removeEventListener()örneği

var button  =   document.getElementById("buton1");

document.addEventListener("click" ,yazdir);

function yazdir () {
      alert("tıklama olayı gerçekleşti");
  }

button.addEventListener("click" , function(){
    document.removeEventListener("click",yazdir);
    console.log("event silindi");
})

/*

*/






// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/
// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/
// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/
// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/
// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/
// ?-------------------------------------------------------------

//!  ÖR 8

// addEventListener()örneği


/*

*/