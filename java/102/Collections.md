Birden çok öğeyi saklamak, yönetmek ve işlemek için kullanılan bir framework veya API'dir. Java Collections Framework, çeşitli koleksiyon türlerini sağlar ve bu koleksiyonlarla çalışmak için bir dizi sınıf ve arabirim sunar.


1. ArrayList: Boyutu dinamik olarak büyüyebilen bir dizi koleksiyonunu uygular. Elemanlara indeks kullanarak erişmek hızlıdır.
    
2. LinkedList: Bağlantılı bir liste koleksiyonunu uygular. Elemanlar birbirine bağlı düğümlerle temsil edilir ve ekleme/silme işlemleri hızlıdır.
    
3. HashSet: Benzersiz elemanların bir kümesini uygular. Sıralama önemli değildir ve hızlı bir şekilde eleman ekleme/silme işlemleri yapılabilir.
    
4. TreeSet: Sıralı bir küme koleksiyonunu uygular. Elemanlar, doğal sıralama veya özel bir karşılaştırıcıya göre sıralanabilir.
    
5. HashMap: Anahtar-değer çiftlerini bir harita koleksiyonu olarak uygular. Anahtarlar benzersiz olmalıdır ve her anahtar bir değerle eşleştirilir. Hızlı anahtar-tabanlı erişim sağlar.
6. TreeMap: Anahtarları sıralı bir şekilde saklayan bir harita koleksiyonunu uygular. Doğal sıralama veya özel bir karşılaştırıcıya göre anahtarları sıralar. Sıralı bir anahtar-tabanlı erişim sağlar.
    
7. PriorityQueue: Öncelikli bir kuyruk koleksiyonunu uygular. Elemanlar, belirli bir öncelik düzenine göre sıralanır ve her seferinde en yüksek önceliğe sahip eleman erişilebilir. Öncelikli işlemleri yönetmek için kullanılır.


### En çok Kullanılan metodlar

Bazı metotları şunlardır:

1. add(element): ArrayList'e belirtilen elemanı ekler.
2. add(index, element): Belirtilen indekse belirtilen elemanı ekler.
3. remove(index): Belirtilen indeksteki elemanı ArrayList'ten kaldırır.
4. get(index): Belirtilen indeksteki elemanı döndürür.
5. set(index, element): Belirtilen indeksteki elemanı belirtilen elemanla değiştirir.
6. size(): ArrayList'in boyutunu döndürür.
7. clear(): ArrayList'i boşaltır, tüm elemanları kaldırır.
8. contains(element): Belirtilen elemanın ArrayList'te bulunup bulunmadığını kontrol eder.
9. indexOf(element): Belirtilen elemanın ilk kez geçtiği indeksi döndürür.
10. isEmpty(): ArrayList'in boş olup olmadığını kontrol eder.
11. toArray(): ArrayList'in bir diziye dönüştürülmesini sağlar.
12. subList(fromIndex, toIndex): Belirtilen aralıktaki elemanları içeren yeni bir alt liste döndürür.
13. addAll(collection): Belirtilen koleksiyonun tüm elemanlarını ArrayList'e ekler.
14. removeAll(collection): Belirtilen koleksiyondaki tüm elemanları ArrayList'ten kaldırır.


## Treeset

Veri kümesine konulan elemanların verdiğiniz kurala göre sıralanmasını sağlar. Bunun sağlanabilmesi için kullanacağınız sınıfın “sıralanabilir” olması gerekmektedir. Bir sınıfın sıralanabilir olması için “Comparable” interface’den kalıtım alıp “compareTo” metodunu doldurma 
main
```java
import java.util.TreeSet;  
  
public class Main {  
	public static void main(String[] args) {  
	  
	  
		TreeSet<Worker> workerList = new TreeSet<>(new WorkerOrder());  
		workerList.add(new Worker("kadir" , "Human resources" , 2100));  
		workerList.add(new Worker("kadir" , "Human resources" , 2100));  
		workerList.add(new Worker("ahmet" , "Human resources" , 2100));  
		workerList.add(new Worker("mehmet" , "Human resources" , 2100));  
		workerList.add(new Worker("mehmet" , "Human resources" , 2100));  
		workerList.add(new Worker("ali" , "Human resources" , 2100));  
		workerList.add(new Worker("veli" , "Human resources" , 2100));  
			  
		for (Worker worker : workerList) {  
			System.out.println(worker.getName());  
		}  
		  
		  
	}  
}
```

workerOrder
```java
import java.util.Comparator;  
  
public class WorkerOrder implements Comparator<Worker> {  
	@Override  
	public int compare(Worker o1, Worker o2) {  
		return o1.getName().compareTo(o2.getName());  
	}  
}
```



# Map İnterface & HashMap



## HashMap

Hashmap lerde bir sıralama garantisi yok . Değerler hashlenir ve bu hash e göre sıralanır.



- containsKey() :  Anahtar değerlerin listesini verir (SET)
- containsValue() :  Value değeri  HashMap içerisinde aranır,  varsa geriye true değeri döndürür.
- get() : Anahtar değeri verilen value ' yu geri döndürür.
- put() :  iki parametre alır. Anahtar ve değer ile eleman eklenir.
- remove() : parametre olarak anahatar değeri verilir ve siler.
-  size(): HashMap in eleman sayısını geri döndürür.
- replace() : 2 paramtere alır . İlk paramtere değiştirilecek olan anahtar değeri ikinci ise değiştirilecek olan valur değeridir.
- keySet() :  Anahtar değerlerinin listesini Döndürür(HasSet)


```java
import java.util.HashMap;  
  
public class Main {  
	public static void main(String[] args) {  
	  
		HashMap<String , String > country = new HashMap<>();  
		  
		country.put("TR" , "Türkiye");  
		country.put("USA" , "Amerika");  
		country.put("EN" , "İngiltere");  
		  
		  
		System.out.println(country.get("TR"));  
		country.replace("TR" , "Turkey");  
		System.out.println(country.keySet());  
		System.out.println(country.containsKey("USA"));  
		System.out.println(country.containsValue("İngiltere"));  
		System.out.println(country.size());  
		System.out.println(country.remove("TR"));  
		  
		System.out.println(country);  
	  
	}  
}
```

**Çıktı:**
```bash
Türkiye
[USA, EN, TR]
true
true
3
Turkey
{USA=Amerika, EN=İngiltere}
```

<hr>

## LinkedHashMap & TreeMap


LinkedHashMap lerde girilen sıra neyse aynı şekilde çıkıyor. TreeMap lerde ise kendi sıramızı Comparator implemantasyonu ile yapabiliyoruz.




```java
public class Main{
	public stati void main(String[] args){
		
	}
}
```

```java
public class Main{
	public stati void main(String[] args){
		
	}
}

```


```java
public class Main{
	public stati void main(String[] args){
		
	}
}
```
