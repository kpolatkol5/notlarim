
## Sabit tanımlamak 


Java'da **"final"** deyimi, önüne yazıldığı öğenin değerini bir kez tanımlandıktan sonra değiştirilemeyeceğini söyler. Bu yüzden programımız içerisinde "**sabit**" tanımlamak için kullanılır.


```java
public static final int YAS =12;  
  
public static void main(String[] args) {  
  
	System.out.println(Solution.YAS);  
	  
  
}
```

static tanımlamamızın sebebi main metodunda kullanabilmektir. Sonradan değiştirilemeyeceği için public değimi ile kullanılabilir.

### **JARGON**

Sabit tanımlarken isimler büyük harflerle yazılır. Sabit adı birden fazla sözcükten oluşuyorsa, sözcükler altçizgi ( _ ) ile birbirlerinden ayrılır. Örneğin en fazla kayıt sayısını ifade edecek sabitin adı şöyle verilebilir: **PATIKA_DEV_JAVA_102**_


## Encapsulation (Kapsülleme)

Sınıf içerisinde tanımlanan alanları setter ve getter metodları ile  değiştirilebilmesini ve okunabilmesini sağlıyoruz.Bir koruma kalkanı olarak düşün istenmeyen değerlerin aktarılmasını önlemek için tanımlıyoruz. Mesela bir ürünün değeri negatif bir sayı olamaz veya yaş negatif bir sayı olamaz.Bu tür önlemeri getter ve setter metodları ile alıyoruz.

Sınıf içerisindeki alanlar ``private`` olarak tanımlanır.Setter ve getter metodları bu alanlara ulaşabilir. sınıf dışında da private alanlara ulaşılmayacağı için getter ve setter metodları aracılığı ile ulaşılır. getter metodu sınıftaki alanı geriye döndürür. setter metodu ise sınftaki private alanı değiştrmek için kullanılır bu metodda koşul belirtebiliriz.

Kapsülleme, sınıfın içindeki verilerin erişimini kontrol etmek için kullanılabildiğinden, kapsülleme, verilerin doğrudan erişimine izin vermez, ancak sınıfın public  metodları aracılığıyla bu verilere erişim sağlanır. Bu şekilde, sınıfın iç yapısı gizlenebilir ve kullanıcılara yalnızca arayüz sunulabilir.Kapsülleme kullanılarak abstraction (soyutlama) uygulanabilir.

Getter metodları geriye bir değer döndürürler Ancak setter metodları geriye değer döndürmez işlem yaparlar bu yüzden setter metodları void değimi ile yazılır.

```java
public class Book {  
  
	private String Name;  
	private int Piece;  
	private double Price;  
	  
	public Book(String name, int piece, double price) {  
		Name = name;  
		Piece = piece;  
		Price = price;  
	}  
	  
	public String getName() {  
		return Name;  
	}  
	  
	public void setName(String name) {  
		if (name.strip().length() >= 10) {  
			this.Name = name;  
		}else {  
			System.out.println("10 karakterden daha uzun olmalıdır");  
		}  
	}
}
```


Main
```java
public static void main(String[] args) {  
  
	Book b1 = new Book("ı", 12, 1231.0);  
	System.out.println(b1.getName());  
	  
	b1.setName("kadir polatkol");  
	System.out.println(b1.getName());  
}
```

```bash
ı
kadir polatkol
```


## Sınıflar arası ilişkiler



### Bağımlılık (Dependency)

Bir sınıf başka bir sınıfın metodunu kullanıyorsa veya bu sınıfın içerinde bir örneğini oluşturuyorsa iki sınıf birbirine bağımlıdır.Örneğin, bir Araba sınıfı, bir Motor sınıfı tarafından kullanılıyorsa, Araba sınıfı Motor sınıfına bağımlıdır ve "uses a" ilişkisi vardır. Ayrıca, Araba sınıfı, bir Tekerlek sınıfını içeriyorsa, yine Araba sınıfı Tekerlek sınıfına bağımlıdır ve "has-a" ilişkisi vardır.

Araba uses a Motor (Araba sınıfı motor sınıfına bağlı)
```java
public class Araba {
   private Motor motor;
   
   public Araba() {
      motor = new Motor();
   }
   
   public void calistir() {
      motor.calistir();
   }
}

public class Motor {
   public void calistir() {
      System.out.println("Motor çalışıyor...");
   }
}
```


### Birleştirme (composition)


bir sınıfın başka bir sınıfın örneklerini içermesi anlamına gelir.Birleştirme, bir sınıfın özelliklerini, diğer sınıfın özellikleri ile birleştirmek için kullanılabilir. Örneğin, bir Araba sınıfı, bir Motor sınıfını içerirken, Motor sınıfı Araba sınıfının bir parçasıdır ve Araba sınıfı, Motor sınıfının özelliklerini kullanır.


Araba has a Motor (Arabanın bir motoru var)

```java
public class Araba {
   private Motor motor;
   
   public Araba() {
      motor = new Motor();
   }
   
   public void calistir() {
      motor.calistir();
   }
   
   public void durdur() {
      motor.durdur();
   }
}

public class Motor {
   public void calistir() {
      System.out.println("Motor çalışıyor...");
   }
   
   public void durdur() {
      System.out.println("Motor durduruldu...");
   }
}

```

Araba sınıfı, Motor sınıfını içeriyor ve Araba sınıfının "calistir()" ve "durdur()" metodları, Motor sınıfının "calistir()" ve "durdur()" metodlarını çağırıyor. Bu, Araba sınıfının Motor sınıfının özelliklerini içerdiğini ve kullanabildiğini gösteriyor.


### Kalıtım (Inheritance) / "is a" İlişkisi



Kalıtım için ``extends``  değimi kullanılır. super class üst sınıf sub class alt yani kalıtılan sınıftır. sub class ın  contractor ında super() fonksiyonu ile super class a atfta bulunulur ve super class ın contractor u çalışacağı için ilgili alanlar super fonksiyonunda yazılır.

```java
public class Calisan {  
  
	private String AdSoyad;  
	private String Mail;  
	private String Mpno;  
	private int Yas;  
	  
	public Calisan(String adSoyad, String mail, String mpno, int yas) {  
	AdSoyad = adSoyad;  
	Mail = mail;  
	Mpno = mpno;  
	Yas = yas;  
	}
}
```





```java
public class Akademisyen extends Calisan {  
	String Branch;  
	String DersKodu;  
  
	Akademisyen(String adSoyad, String mail, String mpno, int yas, String branch, String dersKodu) {  
	super(adSoyad, mail, mpno, yas);  
	this.Branch = branch;  
	this.DersKodu = dersKodu;  
	  
	}  
}
```

kalıtım işlemi extends değimi ile yapılıyor ve super() metodu ile üst sınıfa atıfta bulunuyoruz ortak olan alanlar **String adSoyad, String mail, String mpno, int yas,** gibi parametreler super class a gider ve oradaki yapılandırma metodunda işlenir. akademisyen sınıfına özel alanlar varsa en son o parametreler de eklenir ve bu kıısm zaten bildiğimiz gibi.



### Override (Metod Ezme)

Alt sınıfın içine doğrudan ya da dolaylı ata sınıflarından gelen bir (ya da daha fazla) yöntemin aynısının (aynı yöntem adı ve aynı parametre listesi) kodlanmasına verilen addır. ``@override`` değimi ile birlikte kullanılır. Amaç şu üst sınıftaki fonksiyon bizim işimize yarıyor ancak değiştirilmesi gerekiyor yani aynı isimde fonksiyonu baştan tanımlamak ezmek anlamına gelir.

### Polymorphism (Çok Biçimlilik) İlkesi

Aynı görevin veya işin farklı yollarla yapılabilmesini ifade eder. Nesne, aynı davranışı farklı formlar ve görünüşler ile yerine getirebilir.

### INTERFACE
 
Java'da soyutlamayı sağlamanın bir başka yolu "interface" tanımlamaktır. "interface" 'ler abstract sınıflara göre soyutlama oranı çok yüksektir. Çünkü, "interface" içinde sadece soyut fonksiyonlar tanımlayabilirsiniz. Metot gövdesi olan normal fonksiyonlar tanımlayamazsınız.

İçerisinde sadece ``final`` tanımlayabilirsin o da değiştirlemeyeceği için.

Bir sınıf "interface"den kalıtım alıyorsa "implements" anahtar kelimesi kullanılır. Örnek bir tanımlamaya göz atalım.

# Generic Class

İlkel veri tipleri üzerinden çalışmazlar Wrapper class ve Kendi yazdığımız Class lar üzerinde çalışırlar.Farklı türlerdeki verileri depolamak veya işlemek için kullanılan sınıflardır.

BOX
```java
	public class Box<T> {  
	private T item;  
	  
	public void setItem(T item) {  
		this.item = item;  
	}  
	  
	public T getItem() {  
		return item;  
	}  
}
```

Main
```java
public static void main(String[] args) {  

	Box<String> stringBox = new Box<>();  
	stringBox.setItem("Hello");  
	String str = stringBox.getItem();  
	System.out.println(str);  
	  
	Box<Integer> integerBox = new Box<>();  
	integerBox.setItem(10);  
	int num = integerBox.getItem();  
	System.out.println(num);  
}  
```

# Generic Metodlar

Farklı türlerde verileri işleyebilen ve tekrar kullanılabilir metotlar oluşturmanıza olanak tanır. Generic metotlar, bir veya birden fazla parametre tipi alabilir ve bu parametreleri işleyen işlemleri gerçekleştirebilir.


```java
public class GenericMethods {

    // Tek bir tip için generic metot
    public <T> void printArray(T[] array) {
        for (T element : array) {
            System.out.println(element);
        }
    }

    // Birden fazla tip için generic metot
    public <T, U> void displayPair(T first, U second) {
        System.out.println("First: " + first);
        System.out.println("Second: " + second);
    }

    public static void main(String[] args) {
        GenericMethods genericMethods = new GenericMethods();

        // Dizi için generic metodu kullanma
        Integer[] intArray = {1, 2, 3, 4, 5};
        genericMethods.printArray(intArray);

        String[] stringArray = {"Hello", "World"};
        genericMethods.printArray(stringArray);

        // İki farklı tipte parametre için generic metodu kullanma
        genericMethods.displayPair(10, "Java");
        genericMethods.displayPair(true, 3.14);
    }
}

```

# Generic Interface



# Generic Bounded Types
