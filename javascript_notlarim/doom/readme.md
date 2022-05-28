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