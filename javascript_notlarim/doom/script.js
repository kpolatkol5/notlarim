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