
## Java Thread’lerin Oluşturulması ve Kullanılması

  

Java'da threadler, paralel ve eşzamanlı programlama yapmanızı sağlayan temel yapı taşlarından biridir. Bir thread, bir Java programının içinde bağımsız olarak çalışabilen bir işlem birimidir. Bir Java programı genellikle en az bir ana thread içerir, ancak bu ana thread dışında ek threadler oluşturarak paralel işlemler gerçekleştirebilirsiniz.

Örneğin, bir Java uygulamasında arka planda bir dosya indirme işlemi yaparken aynı anda kullanıcı arayüzünü güncellemek isteyebilirsiniz. Bu durumda, dosya indirme işlemi ve kullanıcı arayüzü güncellemesi için farklı threadler oluşturabilirsiniz.

Java’da iş parçacığı oluşturmak için “Thread” isminde bir sınıf bulunmaktadır. Böylece, basit anlamda iş parçacığı açmış oluruz. Tabi, unutmamak lazım Thread açmak sisteme maliyeti olan bir iştir.  

Bu maliyetli nesneler ilk başta belli bir miktarda yaratılır ve hazır durumda olacak şekilde havuza konulur. Thread ihtiyacı olanlar bu havuzdan bir Thread’i kullanır ve sisteme geri iade eder. Böylece, performans kazancı yanı sıra kaynak kullanımı da iyi bir hale getirilir.

```java
public class SimpleThread extends Thread { 
	@Override public void run() {
		// o an çalışan Thread'in ismini alıyoruz.
		String threadName = Thread.currentThread().getName();
		
		System.out.println("My summation " + threadName + " is started!");
		
		int total = 0;
		for(int i=0; i < 1000; i++) 
		{
			total += i;
		}
		
		System.out.println("Total: " + total);
	}
}
```


```java
SimpleThread simpleThread2 = new SimpleThread(); simpleThread2.start();
```


  
## Runnable Interface

Runnable arayüzü, Java'da çoklu thread programlamasını desteklemek için kullanılan bir arayüzdür. Bu arayüz, bir sınıfın veya nesnenin çalıştırılabilir bir işlemi temsil etmesini sağlar. Bir sınıf, `Runnable` arayüzünü uygulayarak, içerisinde çalıştırılacak kod parçasını tanımlayabilir ve bu kod parçasını farklı bir thread yürütebilir.  

Bşaka bir class tanımlayalım ve runnable interfaceini implement edelim.

test.java
```java
public class test implements Runnable {
    @Override
    public void run() {
        this.sayHello();
    }
    
    String name;
    int age;

    public test(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    void sayHello() {
        System.out.printf("merhaba %s ", this.name);
        System.out.printf("yaşınız  %d , sayım başlıyor \n", this.age);

        for (int i = 0; i < this.age; i++) {
            System.out.println(i);
        }
        System.out.println("sayım bitti");
    }
}

```

main.java
```java
public class Main {
    public static void main(String[] args) {
        Thread th = new Thread(new test("kadir" , 23));
        Thread th2 = new Thread(new test("yusuf" , 40));

        th.start();
        th2.start();

        System.out.println("hellooooooooooooooo");
    }
}
```



## Thread Durdurmak ve Bekletmek



## Lambda Expression

