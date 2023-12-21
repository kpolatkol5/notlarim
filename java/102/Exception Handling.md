Javada tüm istisnalar bir sınıftan türetilmiştir(Throwable).

## RuntimeException Nedir?

Java'da tanımlanan unchecked exception türlerinin genel bir üst sınıfıdır. Bu sınıfın altında bulunan istisna türleri, programcı tarafından yakalanıp işlenmesi zorunlu tutulmayan istisnalardır. Genellikle programcının dikkatsizliklerinden veya beklenmeyen koşullardan kaynaklanan hataları temsil eder. Bu tür hatalar, derleme zamanında kontrol edilmezler ve programın normal akışını bozarlar.

## Javada İstisnalar İki Kategoride İncelenebilir. 


### 1- Unchecked Exceptions (Kontrol edilmeyen istisnalar)

Derleme sırasında ortaya çıkan hatalar. RuntimeException sınıfından türeyen istisna türleridir. Bu tür istisnalar, derleme zamanında kontrol edilmezler.

### 2- Checked Exceptions (Kontrol edilen istisnalar) 

Derleme aşamasında tespit edilebilen hatalar. RuntimeException sınıfından türemeyen istisna türlerini kapsar. Bu tür istisnalar, derleme zamanında kontrol edilir ve programcı tarafından yakalanıp işlenmeleri gerekmektedir. Checked exceptions'lar, "try-catch" bloklarıyla veya "throws" ifadesiyle yakalanabilir veya yönlendirilebilir.


HackerRank sorusunun çözümü (Java Exception Handling)

```java
long power(int n, int p) throws Exception {
/*
     Metotun imzasında "throws Exception" ifadesi bulunuyor. Bu ifade, metotun 
     bir istisna (exception) fırlatabileceğini belirtir. Burada "throws" ifadesi 
     ile birlikte "Exception" sınıfı belirtilmiştir, yani herhangi bir türden 
     istisna fırlatılabileceği belirtilmiştir. Bu, metodu kullanan kodun bu 
     istisnaları yakalaması veya bunlarla başa çıkması gerektiği anlamına gelir.
     Metot içindeki hata durumları, istisna fırlatarak işaretlenebilir.
*/

    // Eğer n veya p sıfır ise istisna fırlatılır ve hata mesajı belirtilir.
    if (n == 0 || p == 0) {
        throw new Exception("n ve p sıfır olmamalıdır.");
    }

    // Eğer n veya p negatif ise istisna fırlatılır ve hata mesajı belirtilir.
    else if (n < 0 || p < 0) {
        throw new Exception("n veya p negatif olmamalıdır.");
    }else if(p ==0){
        return 1;
    }

    // Üs alma işlemi için gerekli hesaplamalar yapılır.
    long result = 1;
    for (int i = 0; i < p; i++) {
        result *= n;
    }

    // Sonuç döndürülür.
    return result;
}

```


`long power(int n, int p) throws Exception` şeklinde bir metot tanımlaması yapıldığında, metod normalde bir değer döndürmek zorunda olmasına rağmen, belirtilen hata durumlarıyla karşılaşıldığında sadece istisna (exception) fırlatır.

Metodun normal çalışması durumunda, üs alma işlemi tamamlanır ve sonuç olan `result` değişkeni döndürülür. Ancak, `throws Exception` ifadesi ile belirtilen hata durumları meydana geldiğinde, metot istisna fırlatır ve geri kalan işlemler atlanır.

Bu durumda, `result` değişkeni okunmaz ve geriye dönüş değeri olarak kullanılmaz. Metotun çağrıldığı yerde, bu istisnaların yakalanması ve uygun şekilde ele alınması gerekmektedir. Eğer istisnalar yakalanmazsa, programın normal akışı kesilir ve istisna dışarıya fırlatılır.

Özet olarak, `throws Exception` ifadesiyle belirtilen hata durumlarında metot sadece istisna fırlatır ve geriye değer döndürmez. İstisnaları yakalayan kod bloğunda hata durumu ele alınmalı ve istenen işlemler gerçekleştirilmelidir.


## Özel Hata Ayıklama (Exception) Oluşturma
