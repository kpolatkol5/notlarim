	

## File Sınıfı

Dosya İşlemleri için **File** sınıfından faydalanıyoruz. ```java.io.File```  



- createNewFile()  : yeni bir dosya oluşturmak için kullanılır.

```java
import java.io.File;  
import java.io.IOException;  
  
public class Main {  
	public static void main(String[] args) {  
		  
		// dosya oluşturma işlemi  
		File file = new File("test.txt");  
		
		try {  
		  
		if (!file.createNewFile()) 
			System.out.println("dosya zaten var ");  
		  
		} catch (IOException e) {  
			System.out.println(e.getMessage());  
		}  
	}  
}
```




- delete() : dosyayı silmek için kullanılır.(Fileobject.delete())
- mkdir() : dizin oluşturmak için kullanılır.(tek bir dizin)
- mkdirs() : birden fazla iç içe dizin oluşturmak için kullanılır.
- lists() : dizindeki dosyaların veya dizinlerin listesini geriye döndürür(Array)


## FileInputStream Sınıfı

Dosyadan byte okuma işlemelri bu sınıf ile yapılır. Try blokları arasında yazılması önerilir veya metodu oluştururken ``throws FileNotFoundException``  ile kullan. İki farklı şekilde dosya seçilebilir istersen direkt path ver veya File nesnesi oluştur parametre olarak bu nesneyi ver fark etmez direkt path verirsen zaten **FileInputStream** içerisinde **File objesi** oluşturuyor.

```java
public class Main {  
	public static void main(String[] args) throws FileNotFoundException{  
	  
		String path = "text.txt";  
		  
		try {  
			FileInputStream input = new FileInputStream(path);  
		  
		} catch (FileNotFoundException e) {  
			System.out.println(e.getMessage());  
		}  
	}  
}
```


Şuan sadece obje oluşturduk. Okuma işlemi

`read()` metodunu kullanarak her bir byte'ı sırayla okuruz. `read()` metodu, dosyadan bir byte okur ve bu okunan byte'ı döndürür. Dosyanın sonuna geldiğimizde `read()` metodu -1 değerini döndürür. Bu nedenle, `read()` metodu -1 değerini döndürmedikçe, döngü devam eder ve dosyadaki tüm byte'ları okur.
`read()` metodu, bir `int` değeri döndürür. Bu değer, okunan byte'ın tam sayı değerini temsil eder. Okunan byte, 0 ile 255 arasında bir değer olabilir. Dosyanın sonuna gelindiğinde, `-1` değeri döndürülür.
`close()` metodu, kaynakları serbest bırakır ve dosyanın güvenli bir şekilde kapatılmasını sağlar. Bu, kaynak sızıntısını önlemek için önemlidir.

```java
import java.io.*;  
  
public class Main {  
	public static void main(String[] args) throws FileNotFoundException {  
		  
		String path = "text.txt";  
		  
		try {  
			FileInputStream input = new FileInputStream(path);  
			  
			int val = input.read();  
			do {  
				System.out.println(val);  
				val = input.read();  
				
			} while (val != -1);  
			  
			input.close();  
			  
		} catch (FileNotFoundException e) {  
			System.out.print(e.getMessage());  
			
		} catch (IOException e) {  
			throw new RuntimeException(e);  
		}  
	}  
}  
```

Türkçe karakter veri setlerinde sorun yaratabilir.

### avaliable() metodu :

Bu metod kullanılabilir byte sayısını verir.


```text
asdasdasdasdasdasd
```


```java
public class Main {  
	public static void main(String[] args) throws FileNotFoundException {  
		  
		String path = "denem.txt";  
		  
		try {  
			FileInputStream input = new FileInputStream(path);  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			int val = input.read();  
			  
			do {  
				System.out.print((char) val);  
				val = input.read();  
			}while (val != -1);  
			  
		} catch (FileNotFoundException e) {  
			System.out.print(e.getMessage());  
			  
		} catch (IOException e) {  
			throw new RuntimeException(e);  
		}  
	}  
}
// Kullanılabilir byte sayısı : 18
// asdasdasdasdasdasd
```

### NOT:

avaliable() metodu imleçten sonraki karakterleri sayar eğer read() metodunu kullanarak birkaç adım sonraki karakterlere geçerek avaliable() metodunu kullanırsan sonuç daha farklı çıkacaktır.


```java
public class Main {  
	public static void main(String[] args) throws FileNotFoundException {  
		  
		String path = "denem.txt";  
		  
		try {  
			FileInputStream input = new FileInputStream(path);  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			  
			input.read();  
			input.read();  
			input.read();  
			input.read();  
			input.read();  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			  
		} catch (FileNotFoundException e) {  
			System.out.print(e.getMessage());  
		  
		} catch (IOException e) {  
			throw new RuntimeException(e);  
		}  
	}  
}
// Kullanılabilir byte sayısı : 18
// Kullanılabilir byte sayısı : 13
```



### skip() metodu :

Atlama metodudur. Metod nerede kaldıysa (mesea read() metodu kullanılsıysa) parametrede aldığı değer kadar atlar.


```java
public class Main {  
	public static void main(String[] args) throws FileNotFoundException {  
		  
		String path = "denem.txt";  
		  
		try {  
			FileInputStream input = new FileInputStream(path);  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			  
			input.read();  
			input.read();  
			input.read();  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			input.read();  
			input.read();  
			System.out.println("Kullanılabilir byte sayısı : " + input.available());  
			input.skip(10);  
			System.out.println("Kullanılabilir byte sayısı(skip() metodu kullanıldı) : " + input.available());
		} catch (FileNotFoundException e) {  
			System.out.print(e.getMessage());  
		  
		} catch (IOException e) {  
			throw new RuntimeException(e);  
		}  
	}  
}
// Kullanılabilir byte sayısı : 18
// Kullanılabilir byte sayısı : 15
// Kullanılabilir byte sayısı : 13
// Kullanılabilir byte sayısı(skip() metodu kullanıldı) : 3
```


## FileOutputStream Sınıfı

Dosyalara Byte cinsinden veri yazdırmak için kullanılır.

```java
import java.io.*;
import java.io.FileOutputStream;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {

        String path = "text.txt";
        String outputText = "lorem ipsum sit\n";

        try {

            FileOutputStream output = new FileOutputStream(path , true);
            output.write(outputText.getBytes());

			output.close();
        } catch (FileNotFoundException e) {
            System.out.print(e.getMessage());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
```

Örnkete ``FileOutputStream`` objesi oluşturuken 2 paremetre verdik. ilk parametre yazdıracağımız dosyanın path ' i (eğer dizinde bulamazsa yeni bir tane oluşturur) , ikinci parametre ise imlecin sonuna eklenmeye devam etmesini istersen ``true``  parametresini ekleriz. bu parametre kullanılmaz ise dosya içindeki tüm veriler silinir ve kod akışındaki veri eklenir.

``output.write(outputText.getBytes());`` bu koddaki outputText bizim yazdırmak istediğimiz string ifadedir. getBytes() metodu bu string ifadeyi byte array' e dönüştürür. aşağıdaki şekilde de kullanılabilirdi.

```java
	try {
	
		FileOutputStream output = new FileOutputStream(path , true);
		byte[] strToByte = outputText.getBytes();  
		output.write(strToByte);
	
	
	} catch (FileNotFoundException e) {
		System.out.print(e.getMessage());
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
``` 

Bunun dışında veri yazdıramayız mutlaka byte[] e dönüşmesi gerek. program sonunda da close()  metodu ile kapatmayı unutmayalım. 

  
## ByteArrayInputStream ve ByteArrayOutputStream Sınıfları

Genellikle güvenlik ve kriptolojide kullanılıyor. 




## Serialization ve ObjectStream Sınıfları


Serileştirme işlemi oluşturulan nesneleri JVM dışında kullanmak istediğinde bir sorun olmuyor ancak tekrar dışarıya aktardığımız verileri kullanmak istediğimizde nesnelerin hangi sınıftan türetildiğini nesnelerin veri türünün ne olduğunu  bilemiyoruz. Bu api sayesinde java platformu dışında obje ve nesneleri depolayabiliriz.

## ObjectOutputStream

Serileştirme yapacağımız sınıf
```java
import java.io.Serializable;

public class Car implements Serializable {
    private String name;
    private String model;


    public Car(String name, String model) {
        this.name = name;
        this.model = model;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }
}

```

Serileştirmek istediğimiz sınıfı Serializable interface'i ile implement ediyoruz. Daha sonra dosyayı oluşturacağız

Main.java
```java
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

public class Main {
    public static void main(String[] args) {
        Car araba1 = new Car("bmw" , "2000");
        Car araba2 = new Car("mercedes" , "2002");
        Car araba3 = new Car("mazda" , "2004");

        try {
            FileOutputStream outputFile = new FileOutputStream("araba.txt");
            ObjectOutputStream output = new ObjectOutputStream(outputFile);

            output.writeObject(araba1);
            output.writeObject(araba2);
            output.writeObject(araba3);
            
            output.close();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

ObjectOutputStream sınıfı bir FileOutputStream nesnesi alır. FileOutputStream nesnesi ile oluşturulacak dosyanın path' ini ayarlarız. daha sonra bu nesneyi ``ObjectOutputStream`` e parametre olarak veririz.
``writeObject()`` metodu objeleri dosyaya yazar.

## ObjectInputStream

ObjectInputStream sınıfı bir FileInputStream nesnesi alır. FileInputStream nesnesi ile oluşturulacak dosyanın path' ini ayarlarız. daha sonra bu nesneyi ``ObjectInputStream`` e parametre olarak veririz.
``readObject()`` metodu objeleri teker teker okur.

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {

        Car bmw = new Car("bmw", "2000");
        Car mercedes = new Car("mercedes", "2012");
        Car mazda = new Car("mazda", "2003");

        try {
            FileInputStream file = new FileInputStream("araba.txt");

            ObjectInputStream inputStream = new ObjectInputStream(file);

            Car newCar = (Car) inputStream.readObject();

            while (newCar != null) {
                System.out.println(newCar.getName());
                newCar = (Car) inputStream.readObject();
            }

            file.close();
            inputStream.close();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

    }
}

//bmw
//mercedes
//mazda
//null
```


## BufferedStream


 Diğer stream sınıflarından farklı olarak bellek tamponları kullanır ve performansı arttırır.Verileri tek tek yazmak yerine bir kerede daha büyük bloklar halinde yazarak verimliliği artırır. Bu, daha az disk veya ağ erişimi yaparak verileri hedefe aktarırken performansı iyileştirir.

### Bellek tamponları nedir ?

Veri akış işlemlerinde performansı arttırmak için kullanılan ara bellek alanlarıdır.


## BufferedInputStream

```java
import java.io.*;

public class Main {
    public static void main(String[] args) {

        try {
            FileInputStream file = new FileInputStream("deneme.txt");

            BufferedInputStream inputStream = new BufferedInputStream(file);

            int input = inputStream.read();

            while (input != -1) {
                System.out.print((char) input);
                input = inputStream.read();
            }

            file.close();
            inputStream.close();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```


## BufferedOutputStream

```java
import java.io.*;
import java.nio.charset.StandardCharsets;

public class Main {
    public static void main(String[] args) {
        byte[] output = "BufferedOutputStream".getBytes();

        try {
            FileOutputStream file = new FileOutputStream("kadir.txt");

            BufferedOutputStream outputStream = new BufferedOutputStream(file);

            outputStream.write(output);

            outputStream.close();
            file.close();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```



## InputStreamReader

Giriş akışlarını okumamızı sağlar ve diğerler stream sınıflarından farkı ise karakter seti tanımlayabiliryoruz.Diğer streamlerle çalışabilir.

```java
import java.io.*;
import java.nio.charset.Charset;


public class Main {
    public static void main(String[] args) {
        try {
            FileInputStream file = new FileInputStream("kadir.txt");

            InputStreamReader inputReader = new InputStreamReader(file);
            // InputStreamReader inputReader = new InputStreamReader(file , Charset.forName("Big5-HKSCS") ;
            // charset tanımlamak istersen

            System.out.println(inputReader.getEncoding());

            int i = inputReader.read();
            while (i != -1) {
                System.out.print((char) i);
                i = inputReader.read();
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## OutputStreamWriter

OutputStreamWriter sınıfı, karakter biçimindeki verileri bayt biçimindeki verilere dönüştürmek için kullanılabilir. Writer soyut sınıfını genişletir. Yine bu sınıfta da karakter seti tanımlayabiliyoruz. 

```java
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) {
    
        try{
            FileOutputStream file = new FileOutputStream("kadir.txt");
            OutputStreamWriter output = new OutputStreamWriter(file);

            output.write("Türkçe karakter kullanabilirsin ve byte[]'a dönüştürmene gerek yok");

            output.close();
            file.close();
        }catch (Exception e ){
            System.out.println(e.getMessage());
        }
    }
}
```

## FileReader & FileWriter 🌟

Yukarıda açıkladığımız streamleri içinde barındırıyor. Daha hızlı ve kolay işlem yapmak istersen kullanabilirsin.


```java
import java.io.FileReader;
import java.nio.charset.Charset;

public class Main {
    public static void main(String[] args) {
        try {
            FileReader fileReader = new FileReader("kadir.txt");
//            FileReader fileReader = new FileReader("kadir.txt", Charset.forName("Big5"));

            int i = fileReader.read();
            while (i != -1) {
                System.out.print((char) i);
                i = fileReader.read();
            }


        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```


```java
import java.io.FileWriter;
import java.nio.charset.Charset;

public class Main {
    public static void main(String[] args) {
        try {
            FileWriter fileWriter = new FileWriter("kadir.txt");
//            FileWriter fileWriter = new FileWriter("kadir.txt" , Charset.forName("Big5"));

            fileWriter.write("FileWriter& FileReader daha kolaydır..");


            fileWriter.close();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```




## BufferedReader🌟

Ara sınıftır. Farklı algoritmalar kullanarak büyük verilerle daha hızlı işlem yapar.

```java
import java.io.BufferedReader;
import java.io.FileReader;

public class Main {
    public static void main(String[] args) {
        try {
            FileReader file = new FileReader("kadir.txt");
            BufferedReader reader = new BufferedReader(file);

            String line;

            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
			
			reader.close();  
			file.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

## BufferedWriter🌟

Ara sınıftır. Farklı algoritmalar kullanarak büyük verilerle daha hızlı işlem yapar.

```java
import java.io.BufferedWriter;
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) {

        String data = "BufferedWriter sınıfı";

        try {
            FileWriter file = new FileWriter("kadir.txt" ,true);
            BufferedWriter writer = new BufferedWriter(file);

            writer.write(data);

            writer.close();
            file.close();

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```


## PrintStream

Çıktı verilerini bayt yerine okununabilir biçimde(metin) yazmak için kullanılabilir.Çıktı vermek için yazılmış. FileOutpuStrem yerine direkt dosyanın path ini de parametre olarak verebilirsin.

```java
import java.io.*;


public class Main {
    public static void main(String[] args) {

        try {
            FileOutputStream file = new FileOutputStream("kadir.txt" , true);
            PrintStream output = new PrintStream(file);
            output.print("asdasd\t");
            output.close();
            file.close();
            
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```



## PrintWriter

```java
import java.io.PrintWriter;

public class Main {
    public static void main(String[] args) {

        String data = "printWriter sınıfı";

        try {
            PrintWriter writer = new PrintWriter("kadir.txt");
            writer.print(data);

            writer.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
```

