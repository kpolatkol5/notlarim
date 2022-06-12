# ***DOM NERİR?***

<br>

Document  Object Model (Belge Nesne Modeli) dilden bağımsız programlama arayüzüdür. Her bir HTML elemanı için web IDL kullanılarak bir arayüz tanımlamaktadır.Tarayıcılar bu arayüzleri kullanarak her bir html elemanı ve diğer özel durumlar için nesne (object) oluştururlar. Bu nesleler Windows nesnesinin alt nesnesi olan document nesnesi altında hiyerarşik yapıda oluşturulmaktadır.

<br><hr>

## ***document.getElementById();***

<br>

<br><hr>


## ***document.getElementByName();***

<br> 

<br><hr>


## ***document.getElementByTagName();***

<br> 


Kendisine verilen parametreler ile dom da belirtilen tag (etiket) adına sahip tüm  elemanların refaransını elde etmek için kullanılır.Birden fazla eleman varsa döngü ile alınabilir.


Sayfadaki tüm taglara erişmeke istersek ;

```js
    document.getElementByTagName("*")
```


<br><hr>


## ***document.getElementByClassName();***

<br> 


Kendisine verilen parametreler ile dom da belirtilen class adına sahip tüm  elemanların refaransını elde etmek için kullanılır.Birden fazla eleman varsa döngü ile alınabilir.


 


<br><hr>

## ***doctype***

<br> 

Belge türü referansını elde etmek için kullanılır

```js
var result  =   document.doctype.name;
console.log(result)
```

<br><hr>

## ***documentElement***

<br> 

Html etiketinin referansını element nesnesi halinde elde etmek için kullanılır.


```js
var result  =   document.documentElement.nodeName;
console.log(result)
```

<br><hr>

## ***charakterSet***

<br> 

Dom (belgenin) katakter kodlamasının refaransı elde etmek için kullanılır.

```js
var result  =   document.characterSet;
console.log(result)

>>> UTF-8
```

<br><hr>

## ***readySate***

<br> 

Belgenin tarayıcı tarafından yüklenip yüklenmediğini kontrol eder. local alanda çalıştığımızda sürekli ***loading*** döndürür.Sunucuda çalıştığında bu durum ***complate*** olarak değişecektir.  
<br>

HTML
```html
<button id="button-1" type="button" onclick="ornek()">Tıkla</button>

```

JAVASCİPT
```js
function ornek (){
    var result  =   document.readyState;
    document.getElementById("button-1").innerHTML=result;
}
```

<br><hr>

## ***hasFocus() :***

<br> 

Belge odağını kontrol eder. Eğe tarayıcı dahilinde bir yere tıklarsan ***true*** farklı bir yere tıklarsan ***false*** değeri döndürür.

<br>


JAVASCİPT
```js
setInterval("odak_kontrol()",1000);   

function odak_kontrol(){

    var islem   =   document.hasFocus();

    if (document.hasFocus()){
        document.write(islem + " ");
    }else{
        document.write(islem + " ");
    }
}
```

<br><hr>


## ***plugins :***

<br> 

Tarayıcadaki tüm eklentilerin referanslarını almak için kullanılır. Birden fazla eklenti varsa döngü ile alınabilir.
***navigator*** nesnesinden faydalanırız.


<br>


JAVASCİPT
```js
var result  =   navigator.plugins.length;

for (var i=0 ; i < result ; i++ ){

    console.log( navigator.plugins[i].name); 
}
```

<br><hr>



## ***createAttribute() :***

<br> 

Belge içerisindeki elemanlara yeri özellikler oluşturur ve bu özellikleri geriye döndürür.***(class , type , href gibi)***

<br> 

- ***setAttributeNode  :***   createAttribute metodu ile oluşturulan özellikleri uygular.



<br>

HTML
```html
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>

<button onclick="ornek()">Tıkla</button>
```


JAVASCİPT
```js
function ornek() { 

    var element_sec =   document.getElementsByTagName("p")[0];
    var ozellik = document.createAttribute("style");
    
    ozellik.value="font-size:50px";
    element_sec.setAttributeNode(ozellik);

 }
```

<br><hr>


## ***createELement() :***

<br> 

Belge içeriisnde html elementi oluşturmak için kullanılır. html node objesi geriye döndürür.

<br>

- ***createTextNode()  :*** createElement() ile oluşturulan elemanına metin eklemek için kullanılır. Oluşturulan metni geriye döndürür.

- ***appendChild() :*** Oluşturulan düğümü herhangi bir html elemanına eklemek için kullanılır.Elemanı en sonra ekler.


<br>

```js
var result  =   document.createElement("P");
var text    = document.createTextNode("Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatibus illo,");

result.appendChild(text);

document.body.appendChild(result);// body etiketine oluşturduğumuz elementi ekleriz
console.log(result);
```



<br><hr>


## ***createComment() :***

<br> 

Belge içerine açıklama (yorum satırı oluşturur) oluşturtur.

<br>

JAVASCİPT
```js
var comment_text    =   "Javascipt ile oluşturuldu";
var comment         =   document.createComment(comment_text);

var ekle            =   document.body.appendChild(comment);

console.log(ekle)
```

<br><hr>


## ***addEventListener() :***

<br> 

Belgeye event (olay) işaretleyicisi eklemek için kullanılır.Eğer ilgili olay gerçekleştirilirse tanımlanan fonksiyonlar çalışır.


<br>


HTML
```html
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quo reiciendis doloremque porro sed illo id tenetur soluta deserunt possimus a animi excepturi vel esse placeat aliquid quis, debitis aperiam in.</p>

<button id="buton1">Tıkla</button>
```


JAVASCİPT
```js
var buton_element   =   document.getElementById("buton1");

document.addEventListener("click", function () {
    let element     =   document.getElementsByTagName("p")[0];

    element.innerHTML="Tıklandı"
  })

```

<br><hr>



## ***removeEventListener() :***

<br> 

Belgeye event (olay) işaretleyicisini silmek için kullanılır.


<br>


HTML
```html
<button id="buton1">Tıkla</button>
```


JAVASCİPT
```js
var button  =   document.getElementById("buton1");

document.addEventListener("click" ,yazdir);

function yazdir () {
      alert("tıklama olayı gerçekleşti");
  }

button.addEventListener("click" , function(){
    document.removeEventListener("click",yazdir);
    console.log("event silindi");
})

```

<br><hr>
