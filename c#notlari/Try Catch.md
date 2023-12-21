
Hata yönetimi için kullanılan bir yapıdır. "try-catch" yapısı, bir kod bloğunda hata oluşması durumunda programın çökmesini engelleyerek hatanın yönetilmesine olanak sağlar.Mesela bir dizi var elimizde ve dizinin oluşturulan boyutundan fazla eleman eklersek hata alırız ve  program çöker. Bu tür hataların yönetebilmemiz için try-catch yapısını kullanırız.

```csharp
string[] deneme = new string[4];

deneme[0] = "deger";
deneme[1] = "deger";
deneme[2] = "deger";
deneme[3] = "deger";
deneme[4] = "deger";
```

bu tanımlamada mesela alacağımız hata ``System.IndexOutOfRangeException`` . Bu tanımlamada hata oluşabileceğini tahmin ediyoruz ve bu kod bloklarını try-catch blokları arasına alalım.

```csharp
class Program
{
	public static void Main(string[] args)
	{
		try
		{
			string[] deneme = new string[4];
			deneme[0] = "deger";
			deneme[1] = "deger";
			deneme[2] = "deger";
			deneme[3] = "deger";  
			deneme[4] = "deger";
		}
		catch (Exception exception)
		{
			Console.WriteLine("Bu genel bir hata alanıdır. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  " + exception.Message);                
		}
	}
}
```

try bloguna hata alınması olası kod bloklarımıız yazarız ve cath de ise oluşacak hataları yakalar ve mantık akışımıza göre ister hataları yönetir ister kullanıcıya bu hatanın neyden kaynaklandığını gösteririrz.

Exception Genel bir hata sınıfıdır ve bu sınıfı kullanırsak olası tüm hataları yakalar. Eğer spesifik bir hatayla ilgileniyorsak catch bloklarının sayısını arttırarak ilgili hata kodlarımızı catch blokalrında kullanabiliriz. ikinci bir tanımlama olan exception tanımlamasını bir değişken olarak düşünebiliriz. Oraya istediğimiz ismi yazabilririz. bu da yakalanan hata nesnesinin değerlerine metodlarına ulaşabiliriz.
Mesela ``exception.Message`` ile bu hata nesnesinin mesaj kısmına ulaştık. Bu örneğin çıktısı aşağıdaki gibi olacaktır.

```bash
Bu genel bir hata alanıdır. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  Index was outside the bounds of the array.
```


**ÖR:**
```csharp
public static void Main(string[] args)
	{
		try
		{
			string[] deneme = new string[4];
			deneme[0] = "deger";
			deneme[1] = "deger";
			deneme[2] = "deger";
			deneme[3] = "deger";  
			deneme[4] = "deger";
		}
		catch (IndexOutOfRangeException exception)
		{
			Console.WriteLine($"Bu alan sandece '{exception.GetType().Name}'  dan gelen hataları yakalar. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  " + exception.Message);                
		}
		catch (Exception exception)
		{
			Console.WriteLine("Bu genel bir hata alanıdır. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  " + exception.Message);                
		}
```

**Çıktı**
```bash
Bu alan sandece 'IndexOutOfRangeException'  dan gelen hataları yakalar. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  Index was outside the bounds of the array.
```

Örnekte de olduğu gibi ilk önce hangi hatayı alırsa o blog çalışır ve diğer kod blokları çalışmaz.Eğer ne olursa olsun çalışmasını istediğin bir blog istersen ``Finally`` değimini kullanabilirsin.
 
### finally

Hata olsa da olmasa da bu alan çalışır.

```csharp
class Program
    {
        public static void Main(string[] args)
        {
            try
            {
                string[] deneme = new string[4];
                deneme[0] = "deger";
                deneme[1] = "deger";
                deneme[2] = "deger";
                deneme[3] = "deger";  
                deneme[4] = "deger";
            }
            catch (IndexOutOfRangeException exception)
            {
                Console.WriteLine($"Bu alan sandece '{exception.GetType().Name}'  dan gelen hataları yakalar. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  " + exception.Message);                
            }
            catch (Exception exception)
            {
                Console.WriteLine("Bu genel bir hata alanıdır. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  " + exception.Message);                
            }
            finally
            {
                Console.WriteLine("İşlem bu kadar");
            }
        }
    }
```

**Çıktı**
```bash
Bu alan sandece 'IndexOutOfRangeException'  dan gelen hataları yakalar. Tüm hata kodları Exception sınıfından üretilmiştir... Hata mesajı =>  Index was outside the bounds of the array.
İşlem bu kadar
```


## Kendi Hata Sınıfımızı Yazalım

```csharp
namespace try_catch.customException
{
    public class CiftMi : Exception
    {
    }
}
```

Farklı bir dizinde farklı bir sınıf oluşturduk ve bu sınıfı exception sınıfına genişlettik.

```csharp
using try_catch.customException;
using System;
namespace try_catch
{
	class Program
	{
		public static void Main(string[] args)
		{
		  Console.Write("Bİr sayı giriniz :");
			int say = int.Parse( Console.ReadLine());
			
			if (say %2 !=0)
			{
				throw new CiftMi();
			}
			else
			{
				Console.WriteLine("Çift sayı girdiniz:");
			}
	   
		}
	}
}
```

Çok basit bir örnek ama girilen sayı çift mi tek mi bunun deniyoruz. Bunu try catch blokalrı arasında da kullanabilirdik.

```csharp
try
	{
		Console.Write("Bİr sayı giriniz :");
		int say = int.Parse(Console.ReadLine());
		if (say % 2 != 0)
		{
			throw new CiftMi();
		}
		
		else
		{
			Console.WriteLine("Çift sayı girdiniz:");
		}
	}
	
	catch (CiftMi exception)
	{
		Console.WriteLine(exception.Message +" ==> "+ exception.GetType().Name );
	}
```

```bash
Exception of type 'try_catch.customException.CiftMi' was thrown. ==> CiftMi
```

Peki tanımladığımız sınıf içerisindeki elemanları nasıl ezeceğiz. Mesala message tanımlamak istersek nasıl yapacaz.

```csharp
namespace try_catch.customException
{
    public class CiftMi : Exception
    {
        public CiftMi(string message) : base(message)
        {

        }
    }
}
```

```csharp
try
	{
		Console.Write("Bİr sayı giriniz :");
		int say = int.Parse(Console.ReadLine());
		if (say % 2 != 0)
		{
			throw new CiftMi("Tek sayı giremezsin...");
		}
		
		else
		{
			Console.WriteLine("Çift sayı girdiniz:");
		}
	}
	
	catch (CiftMi exception)
	{
		Console.WriteLine(exception.Message +" ==> "+ exception.GetType().Name );
	}
```


```bash
Bİr sayı giriniz :1
Tek sayı giremezsin... ==> CiftMi
```


