

### Property Ve Metod Kavramı

Sınıf içerisidnde tanımladığımız değişkenler property olarak adlarndırılır. Sınıf içerisinde üretilecek olan neslerler üzerinde  işlem yapacaksak  metodları kullanabiliriz. Mesela Araba sınıfımız var bu sınıfta aracın vergi işlemlerini hesaplayan bir metod yazılabilir. Property ise marka model renk gibi tanımlamalar olabilir.

Visual Studio da sınıflar içerinde property tanımlmak için snippet var. ``prop`` (Diğer idelerde veya editörlerde de olabilir)



```csharp
using System;

namespace HelloWorld
{
    class Araba
    {
        public string Marka { get; set; }
        public int Model { get; set; }
        public int Fiyat{ get; set; }

    }


    class HelloWorld
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World");

            Araba araba1 = new Araba();

            araba1.Marka = "bmw";
            araba1.Model= 2015;
            araba1.Fiyat = 100000;

            string result = $"aracın markası = {araba1.Marka} , aracın Modeli = {araba1.Model} , Aracın fiyat = {araba1.Fiyat}";

            Console.WriteLine(result);

        }

    }

}

```

Bir namespace içerisinde birden fazla sınıf tanımlanabilir. 

Property tanımlarken sonuçta bir değişken olduğu için veri türünü belirliyoruz. Public tanımlaması ise bu property ' ye her yerden ulaşabilmemizi sağlıyor.

***{ get; set; }*** :  Bir property' nin getirme (get) ve ayarlama (set) işlemlerini otomatik olarak gerçekleştirmesini sağlar.    ``  araba1.Marka``  dediğimizde get metodu çalışırken , ``  araba1.Marka = "bmw";``  dediğimizde de set metodu çalışır.


***Obje oluşturmanın başka bir yolu***
 
```csharp
	Araba araba1 = new Araba()
	{
		Marka = "bmw",
		Model = 2015,
		Fiyat = 10000,
	};

```


Ayrıca oluşturduğumuz her bir nesne için artık dizi de tanımlanabilir. 


```csharp
	Araba araba1 = new Araba();

	araba1.Marka = "bmw";
	araba1.Model = 2015;
	araba1.Fiyat = 100000;

	Araba araba2 = new Araba()
	{
		Marka = "mercedes",
		Model = 2017,
		Fiyat =98300,
	};

	Araba araba3 = new Araba()
	{
		Marka = "mazda",
		Model = 2018,
		Fiyat = 9831300,
	};


	Araba[] arabalar = new Araba[3];


	arabalar[0] = araba1;
	arabalar[1] = araba2;
	arabalar[2] = araba3;

	Console.WriteLine(arabalar.Length);
	//3
```


Normalde bir dizi oluştururken integer veya string gibi veri türlerinde oluşturuyorduk ve integer türünde bir dizi oluşturursak sadece o türün elemanları dizi içerisinde olabiliyordu. Burada da sadece araba sınıfından üretilen nesneleri barındırabilirirz.

```csharp

namespace HelloWorld
{
    class Araba
    {
        public string Marka { get; set; }
        public int Model { get; set; }
        public int Fiyat { get; set; }
    }


    class Person
    {
        public string name { get; set; }
    }


	class HelloWorld
    {
        public static void Main(string[] args)
         {
		    Araba araba1 = new Araba();
			{
	            Marka = "bmw",
	            Model = 2015,
	            Fiyat = 100000,
            }

            Araba araba2 = new Araba()
            {
                Marka = "mercedes",
                Model = 2017,
                Fiyat = 98300,
            };

            Araba araba3 = new Araba()
            {
                Marka = "mazda",
                Model = 2018,
                Fiyat = 9831300,
            };

            Person p1 = new Person()
            {
                name = "kadir",
            };


            Araba[] arabalar = new Araba[4];


            arabalar[0] = araba1;
            arabalar[1] = araba2;
            arabalar[2] = araba3;
            //arabalar[3] = 21;//Bu ifade de hata verecektir
            // arabalar[3] = "Bu ifade de hata verecektir";
            arabalar[3] = p1; //Bu ifade de hata verecektir
            Console.WriteLine(arabalar.Length);
	}
}
```

Bu tanımlama yanlıştır alınacak hata aşağıda.

***Error CS0029	Cannot implicitly convert type 'HelloWorld.Person' to 'HelloWorld.Araba'***


## Metodlar


## 1- Geri Dönen Metotlar

Geri dönen metotlar, belirtilen veri türünde geriye değer döndürür. Mesela;

```csharp
int Topla(int a,int b) 
{
	return a + b;
}

int result = Topla(9, 21);

//int result = Topla(b : 21 , a : 9);
// paramtere ismini belirterek de kullanılabilir

Console.WriteLine(result);
```

Örnekte de olduğu gibi metod geriye integer türünde bir değer döndürüryor bu yüzden motodun önüne    ``int``   tanımlaması yaptık. Metod dan geriye dönen değeri bir değişken üzerinde depolanabilir. ve Metod parametreleri belirlenirken mutlaka parametrenin de veri türü tanımlanması gereklidir.

## 2- Void 

Void tanımlaması metodun geriye deger döndürmeyeceğini belirtir.Bu metodlar parametre alabilir ancak geriye bir değer döndürmezler.

```csharp
void EkranaYazdir(string x)
{
	Console.WriteLine(x);
}

EkranaYazdir("merhaba");
//merhaba
```

## 3-Örnek Metotlar

Örnek metodları objeler üzerinde işlem yapar ve çağırılmadan çalışmazlar. Bir nesne örneği üzerinde çalışır ve nesnenin özelliklerine erişebilir.

```csharp
    class Araba
    {
        public int Fiyat { get; set; }
        
        public int kdvhesapla()
        {
            return (this.Fiyat * 18) / 100;
        }
    }
```

kdvHesapla() bir örnek metodudur. Parametre almayan bir metoddur. Örnek metodları tanımlarken eger geriye bir değer döndürecekse ``return``  değimi kullanılır ve metodun türü belirtilmelidir. Yukarıdaki örnekte geriye integer deger döndürdüğü için ``public in kdvHesapla()`` tanımlaması yaptık. ``this`` ise örneği temsil eder yani sınıftan üretilen her bir obje için bu metod kullanılabilir örneğin ;

```csharp
   class HelloWorld
    {
        public static void Main(string[] args)
        {
			Araba araba3 = new Araba()
			{
				Marka = "mazda",
				Model = 2018,
				Fiyat = 100,
			};

			Console.WriteLine(araba3.kdvhesapla());
			//18
        }
    }
```


## 4- Static (Sınıf) Metotları

Statik metotlar, bir sınıfın örneği üzerinde çalışmayan metotlardır. Genellikle yardımcı programlar veya genel işlevler sağlarlar. Statik bir metot, örnek oluşturmadan doğrudan sınıf adıyla çağrılabilir. Örneğin:

```csharp
    class Matematik
    {
        public static int EnBuyukSayi(int a, int b)
        {
            return (a > b) ? a : b;
        }
    }
```


Burada EnBuyukSayi() metodunun sınıfın örnekleriyle bir bağlantısı yoktur. Zaten  işlem yapacak olduğumuzda bu metodlara örnekler üzerinden değil sınıf üzerinden ulaşırız. Bir dizi yardımcı metodlara ihtiyacımız varsa static metodlar tanımlayarak işlemlerimizi yapabiliriz.

Başka bir örnek;

```csharp
  public class Person
    {

        public static string CompanyName = "ttc";
        public static string CompanyAdress = "Hatay-Dortyol";

        public static void CompanyDetail()
        {
            Console.WriteLine($"Şirket adı : {Person.CompanyName} , Şirket Adresi {Person.CompanyAdress}");
        }
    }    
```

```csharp
    class HelloWorld
        {

            public static void Main(string[] args)
            {
                Person.CompanyDetail();
         
            }
 
        }
	//Şirket adı : ttc , Şirket Adresi Hatay-Dortyol
```

Örnekte de olduğu gibi static metodlara sınıf üzerinden erişiyoruz.
İnstance sınıf üzerinden static alanlar ve metodlar tanımlanabilir ancak static sınıf üzerinde instance metod veya alan tanımlayamayız. Static sınıfların altındaki tanımlamaların hepsi static metod veya static alan olmak zorundadır.

Static sınıflar nesne üretemez.Yardımcı metodlar tanımlayarak kullanabilirirz. Mesela Math sınıfı güzel bir örnektir. Oradaki metodları kullanmak için Math sınıfı üzerinden metodlara erişebiliyoruz.


## 5- Aşırı Yükleme Metotları:

Aşırı yükleme metotları, aynı isimde ama farklı parametrelerle birden fazla kez tanımlanan metotlardır. Bu tür metotlar, aynı işlevi farklı veri tipleri veya sayılarıyla gerçekleştirmek için kullanılır. metod overloading da denilebilir.Mesela bir person sınıfımız olsun ve aynı isimde 2 metod tanımlayalım ve farklı sayıda parametre alsın.

```csharp
    class Person
    {
        public string name { get; set; }

        public void EkranaYazdir(int x)
        {
            Console.WriteLine("Bu fonksiyon bir parametre alıyor " + x);

        }
        public void EkranaYazdir(int x, int y)
        {
            Console.WriteLine("Bu fonksiyon iki parametre alıyor " + x + " " + y);

        }
    }
```

Public değimi diğer sınıflardan da erişilebilirsin diye tanımlandığını ve void tanımlanması ile ise geriye bir değer döndürmeyeğini biliyoruz. Başka bir sınıfta bu sınıfı örnekleyelim ve iki metodu da çalıştıralım.


```csharp
	    class HelloWorld
    {
   
        public static void Main(string[] args)
        {
            Console.WriteLine("Hello World");


            Person p1 = new Person();

            p1.EkranaYazdir(9);
            p1.EkranaYazdir(9, 2);
        }
    
		//  Hello World
		//  Bu fonksiyon bir parametre alıyor 9
		//  Bu fonksiyon iki parametre alıyor 9 2
    }
```

## 5- Yapıcı  Metotları:

Yapıcı metodlar nesne oluştuğunda arka planda otomatik çalışırlar.Nesne oluştuğunda otomatik olarak oluşturulmasını istediğimiz özellikleri tanımlayabiliriz.Her sınıfta defalt yapıcı metod bulunur. Herhangi bir ilk değer atması yapmadığımızda "0 , false, null" gibi değerler atar.

Yapılandırma metodlarının isimleri sınıf ismi ile aynı olmak zorundadır.Geriye değer döndürmezler.

```csharp
class Matematik
{
	public double PiSayisi;
	public double EulerSayisi;
	
	public Matematik()
		{
			PiSayisi = 3.1415;
			EulerSayisi = 2.7182;
		}
}
```

**public Matematik()** yapılandırma metodudur. Yapılandırma metodları nesne oluşturulduğu anda çalışırlar ve bu metodlar aşırı yükleme metodu olabilir. Parametre sayısı ve parametrelerin tipinden en az birisinin farklı olması şartıyla birden fazla yapıcı metot tanımlanabilir.

```csharp
    public class Person
    {
        public string Name { get; set; }
        public int Age { get; set; }

        public Person(string name)
        {
            Name = name;
            Age = 0;
        }

        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }
    }
```



```csharp
// Person sınıfının bir örneği oluşturuluyor.
Person person1 = new Person("John Doe");
Console.WriteLine("Person1: Name = {0}, Age = {1}", person1.Name, person1.Age);

// Person sınıfının bir başka örneği oluşturuluyor.
Person person2 = new Person("Jane Doe", 30);
Console.WriteLine("Person2: Name = {0}, Age = {1}", person2.Name, person2.Age);
```

## Properties

Set ve Get metotlarını birer kontrol mekanizması olarak düşünebiliriz. Olası problemleri önlemek, işlemleri güvenilir ve kontrollü bir şekilde gerçekleştirmek için Set ve Get metotlarını kullanırız.

**GET metodu:**  Bir özelliğin değerini döndürmek için kullanılır ve özelliğin okunabilir olduğu anlamına gelir. GET metodu, özellik için döndürülecek değeri belirler ve bu değeri özelliğin kullanıcılarına sunar.

**SET metodu:**  Bir özelliğin değerini değiştirmek için kullanılır ve özelliğin yazılabilir olduğu anlamına gelir. SET metodu, özellik için alınacak yeni değeri belirler ve bu değeri özelliğin arkasındaki alan (backing field) içine yerleştirir.


```csharp
    public class Person
    {
        private int _age;
        public int Age
        {
            get
            {
                return _age;

            }
            set
            {
                if (value < 0)
                {
                    Console.WriteLine("Yaş negatif olamaz");
                    this.Age = 0;
                }
                else
                {
                    value = this._age;
                }
            }

        }
    }
```


```csharp
    class HelloWorld
        {

            public static void Main(string[] args)
            {
                Person p1 = new Person();

                p1.Age = -1;

                Console.WriteLine(p1.Age);
            }
 
        }

}
```

## Inheritance (Kalıtım)


Bir sınıfın başka bir sınıfın özelliklerini ve davranışlarını miras almasıdır . Bizi kod tekarından kurtarır ve kodlarımızın okunulabilirliğini arttırır.Child sınıf, Parent sınıf içerisindeki değişkenleri ve metotları kendi içerisinde tanımlanmış gibi kullanabilir. Ancak Parent sınıf, child sınıftaki değişkenleri ve metotları kullanamaz.

Mesela Person Sınıfımız;

```csharp
    public class Person

    {

        public static string ComapanyAderess = "hatay Dortyol";
        public static string ComapanyName = "ttc";

        public string Name { get; set; }
        public string Surname { get; set; }
        private int _age { get; set; } 

        public int Age

        {
            get
            {
                return _age; 

            }

            set
            {
                if (value < 18)

                {
                    Console.WriteLine("yaş 18 den küçük olamaz");
                }
                else
                {
                    value = this._age;
                }
            }
        }

        public double Salary { get; set; }

        public Person(string name, string surname, int age, double salary)

        {
		    this.Name = name;
            this.Surname = name;
            this.Age = age;
            this.Salary = salary;
            Console.WriteLine("Person Sınıfı yapıcı metodu çalıştı");
        }
        public static void CompanyDetail()

        {
            Console.WriteLine($"Şirketn adresi : {Person.ComapanyAderess} ve İsmi : {Person.ComapanyName} "); 

        } 
    }
```


Worker sınıfımız da Person sınıfından türetilen bir sınıf olsun.

```csharp
 public class Worker : Person

    {

        public int WorkerId { get; set; }

        public int WorkerFoodPrice { get; set; }

        public Worker(string name, string surname, int age, double salary, int WorkerId, int WorkerFoodPrice) : base(name, surname, age, salary)

        {

            this.WorkerFoodPrice = WorkerFoodPrice;

            this.WorkerId = WorkerId;

            Console.WriteLine("Worker Sınıfı yapıcı metodu çalıştı");

        }

    }
```

İki sınıfımıza da dikkatli incelerseniz yapılandırma metodlarında bir fark var. ``:base()``  tanımlamasındaki paremetreler Parent sınıfında ve child sınıfında ortak olan parametreler. base tanımlaması ile Parent sınfındaki Yapılandırma metodu çalışır ve bu parametreler aslında üst sınıfa gider. Ek olarak eklediğimiz iki parametre var bu alanları ayrıca ekledik. Name Surname Salary gibi tanımlamaları tekrar yapmamıza gerek kalmadı.

İki sınıfında yapılandırma metodunda Ekrana yazdırma metodu var Person Sınıfının  örneğini oluşturduğumuzda sadece Person sınfındaki ekrana yazdırma metodu çalışırken Worker sınıfında ise hem Worker sınıfındaki  hem de Person sınıfındaki ekrarana yazdırma metodunun çalıştığını görebilirsiniz.


Parent sınıfta bir metodumuz olduğunu varsayalım aynı metodu child sınıfta da kullanmamız gerekiyor ancak paramtere farkı olabilir veya metodda bağzı değişikliklere ihtiyacımız olabilir . Bu duruma Parant sınıftaki ilgili metodu ezmemiz yani override etmemiz gerekiyor. Bunu yapabilmemiz için parent sınıfta ilgili sınıfa ``virtual`` değimi eklememiz ve child sınıfta da ``override`` değimini eklememiz gerekiyor. Örnekle açıklayalım;


Person Sınıfındaki Costs() metodu
```csharp
        public virtual void  Costs()

        {

            Console.WriteLine($"Personelin günlük maliyeti : {this.Salary - Person.Taxes}");

        }
```


Worker sınıfındaki Cost() metodu

```csharp
        public override void Costs()

        {

            Console.WriteLine($"Çalışanın günlük maliyeti : {this.Salary - Worker.Taxes - (this.WorkerFoodPrice*30)}");

        }
```


Main Class
```csharp
    class HelloWorld
    {
        public static void Main(string[] args)

        {
            Person p1 = new Person(
                name: "kadir",
                surname: "polatkol",
                age: 19,
                salary: 1900
            );
            
            Worker w1 = new Worker(
                name: "arda",
                surname: "polatkol",
                age: 19,
                salary:1900,
                WorkerId: 1,
                WorkerFoodPrice: 20
            );
            
            p1.Costs();
            w1.Costs();
        }
    }
```


## Abstract Sınıflar


Abstract sınıflar diğer sınıfların ortak özelliklerini tanımlamak ve alt sınıfların bu özellikleri uygulamasını sağlamak için kullanılır. Soyut sınıf olarak türkçeye çevrileribilir. Bu sınıflar kalıtım yoluyla  türetilen sınıflar tarafafından genişletilmek , yerleri doldurulması gerekir. Kısaca diğer sınfıların temelini oluşturur Base sınıf da denilebilir. Abstract sınfılarda tanımlanana metodlar diğer sınıflarda mutlaka override edilmesi gerekir.

Abstract sınıflarda virtual anahtar kelimesini kullanmanıza gerek yoktur.Abstract sınıfların içinde tanımlanan metotlar zaten ezilebilir (override edilebilir) olacağı için virtual anahtar kelimesine ihtiyaç duyulmaz.

Abstact metodlar abstract sınıflarda tanımlanabilir

```csharp
    public abstract class BaseClassEX
    {
       public abstract void Metod2();
        public abstract void Metod3();
    }
```


Abstract class bu şekilde tanımlanır.Bu sınıfı genişletelim


```csharp
    public abstract class BaseClassEX
    {
       public abstract void Metod2();
        public abstract void Metod3();
    }

	public class Deneme2 : BaseClassEX
	{
		public override void Metod2()
	
		{
			Console.WriteLine("hello");
		}
		public override void Metod3()
		{
			Console.WriteLine("hello");
		}
	
	}
```

Abstract sınfıta tanımaldığımız tüm metodları child sınıfta override etmezsek hata alırız mutlaka override edilmesi gerekiyor.

Abstract sınıflarda normal metodlar da tanımlanabilir.Abstract sınıfta bir yapıcı metod tanımlanır ancak bu yapıcı metod nesne üretmek için değil değişken tanımlamak için kullanılır. Diğer child sınıflarda yapıcı metod eklenir. Alınan parametreler base sınıfına gönderilip işlem yaptırılabilir. Şu durumda yani abstract sınıfta hala nesne üretemiyoruz ancak metod oluşturup diğer türetilen sınıflarda da kullanabiliyoruz.


## Interface



Bir sınıfın belirli bir işlevselliği sağladığına dair bir sözleşme veya sözleşmelerdir. Belirli bir arayüz veya metotları uyguladığından emin olmak için kullanılabilir. Bir interface, bir veya daha fazla metodu ve özellikleri tanımlayabilir. Abstarct sınıflara benzer ancak farklı kavramlardır. İkisi de sınıfın davranışlarını ve yönetimine yardımıcı olurlar. İnterface de örneklendirilemez ancak bir sınfa birden fazla interface uygulanabilir. Abstract sınıflar da ise bir sınıf yalnızca bir abstract sınıftan inherit edilebilirdiç

### Özetle Abstract Sınıflarla Farkı

Abstract sınıfların temel işlevlerini ve özelliklerini tanımlamaya ve kendisinden miras alan sınıfların özelliklerini genişletmeye izin verirken, interface'ler, bir sınıfın belirli bir işlevselliği sağladığına dair bir sözleşme veya şablon sağlar. Interface'lerin üyeleri tümü soyut metotlar veya özelliklerdir ve bir sınıf birden fazla interface'yi uygulayabilir.




