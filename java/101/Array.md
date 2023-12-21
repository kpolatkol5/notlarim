
## foreach() döngüsü

foreach() döngüsü javascript c# gibi bağzı dillerde **foreach()** olarak tanımlanır ancak javada tanımlama farklı olsa da aynı işi for döngüsü ile yapabiliyoruz

for döngüsünün parantezlerine veri türünü verdikten sonra   ``: array``  şeklinde eklememiz gerekiyor mesela;

```java
int[] array1 = new int[]{1,2,3,4,5};

for (int sayi : array1){
	System.out.println(sayi)
}
```

Çok boyutlu dizilerde kullanımı da aşağıdaki gibidir.

```java
  
int[][] numbers;  
numbers = new int[3][];  
numbers[0] = new int[]{1, 2};  
numbers[1] = new int[]{2, 3};  
numbers[2] = new int[]{3, 4};  
  
for (int[] sayi : numbers) {  
	for (int altBasamak : sayi) {  
		System.out.println(altBasamak);  
	}  
}
```

## Array Sınıfı Ve Metodları

Java Collection Framework'ün bir parçasıdır. Bu sınıf, Java dizilerini dinamik olarak oluşturmak ve bunlara erişmek için statik metotlar sağlar.

```java
import java.util.Arrays;
```

Bu şekilde projeye import edebiliriz.


### Arrays.toString()

Dizi içerisindeki elemanları ekrana yazdırır.
```java
int[] dizi1 = new int[] {12,21,45,3234,14};  
  
System.out.println(Arrays.toString(dizi1));;
```


```bash
[12, 21, 45, 3234, 14]
```


### Arrays.fill()

Dizideki tüm elemanları parametre ile verilen değer ile doldurur.

```java
int[] dizi1 = new int[] {12,21,45,3234,14};  
System.out.println(Arrays.toString(dizi1));

Arrays.fill(dizi1 ,12);  
System.out.println(Arrays.toString(dizi1));
```


```bash
[12, 21, 45, 3234, 14]
[12, 12, 12, 12, 12]
```

### Arrays.sort()

Dizideki elemanları küçükten büyüğe sıralar.

```java
int[] dizi1 = new int[]{12, 21, 45, 3234, 14};  
  
System.out.println(Arrays.toString(dizi1));  
Arrays.sort(dizi1);  
System.out.println(Arrays.toString(dizi1));
```

```bash
[12, 21, 45, 3234, 14]
[12, 14, 21, 45, 3234]
```


### Arrays.binarySearch();

Dizideki bir elemanın indis değerini bulmak için kullanılabilir.

```java
int[] dizi1 = new int[]{12, 21, 45, 3234, 14};  
  
System.out.println(Arrays.binarySearch(dizi1, 21));
```

```bash
1
```


## Arrays.copyOf() 

Bir dizideki elemanları kopyalamakiçin kullanılabilir. 

```java
int[] dizi1 = new int[]{12, 21, 45, 3234, 14};
int[] copydizi1 = Arrays.copyOf(dizi1 , dizi1.length);  
  
System.out.println(Arrays.toString(dizi1));  
System.out.println(Arrays.toString(copydizi1));
```


```bash
[12, 21, 45, 3234, 14]
[12, 21, 45, 3234, 14]
```

### Arrays.copyOfRange() 

Farklı parametreler ile istediğimiz index kadarını kopyalayamak istersek kullanabiliriz.

```java
int[] dizi1 = new int[]{12, 21, 45, 3234, 14};
int[] copyOfRangedizi1 = Arrays.copyOfRange(dizi1 , 2 , 4);  
  
System.out.println(Arrays.toString(dizi1));  
System.out.println(Arrays.toString(copyOfRangedizi1));
```


```bash
[12, 21, 45, 3234, 14]
[45, 3234]
```

Belirtilen son parametredeki elemanı  almaz.yani 2 ve üçüncü indexdeki elemanları getirir.

### Arrays.equals() 

Dizileri karşılaştırır ve birbirleri ile eşit olup olmadığını kontrol eder.

```java
int[] dizi1 = new int[]{12, 21, 45, 3234, 14};  
  
int[] copyOfRangedizi1 = Arrays.copyOfRange(dizi1 , 2 , 4);  
int[] copydizi1 = Arrays.copyOf(dizi1 , dizi1.length);  
  
  
System.out.println(Arrays.equals(dizi1 , copydizi1));  
System.out.println(Arrays.equals(dizi1 , copyOfRangedizi1));
```


```bash
true
false
```


## String metodalrı


### charAt() Metodu


karakter dizisindeki belirtilen indisteki harfi & karakteri getirir. Dizilerdeki köşeli parantez gibi 

```java
String str = "kadir";  
  
System.out.println(String.format("karakter dizisindeki 4. karakter\t: %s" , str.charAt(3)));
```


```bash
karakter dizisindeki 4. karakter	: i
```

### codePointAt() Metodu


Bir karakter dizisinde istenilen indisteki karakterin unicode 'unu verir.

```java
String str = "kadir";  
  
System.out.println(String.format("karakter dizisindeki 2. karakter :\t %s\n2.karakterin ünicode 'u\t: %s", str.charAt(1),str.codePointAt(1)));
```


```bash
karakter dizisindeki 2. karakter :	 a
2.karakterin ünicode 'u	: 97
```






```java
```


```bash
```

```java
```


```bash
```





