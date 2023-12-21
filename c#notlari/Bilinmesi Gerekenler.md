
## Namespace nedir?

kodunuzu bölümlere ayırmanıza yardımcı olan bir mekanizmadır. Namespace'ler, sınıflar, yapılar, arayüzler, enum'lar ve diğer nesneleri gruplamak için kullanılır.

Namespace'ler, C# kodunuzu daha organize bir hale getirerek, okunaklığı arttırır ve isim çakışmalarını önler.

Namespace'lerin amacı, aynı isimli nesnelerin farklı yerlerde kullanılması durumunda karışıklığı önlemektir. Namespace'ler aynı zamanda, kodunuzu başkalarıyla paylaşırken ve farklı kütüphaneleri bir arada kullanırken isim çakışmalarından kaçınmanızı sağlar.

## Dosyalar Arasında Using (import) İşlemi Nasıl Yapılır ?


Sınıflarımızı veya diğer yapılarımızı namespace ler arasında tanımlıyorduk. Mesela iki adet dosyamız olsun bu örnekte farklı klasörlerde farklı dosyalarla yapacam.

Ana klasörümüzde Entity adlı bir klasör daha olsun ve programızım ana klasörün içinde bir c# dosyası

**./Entity/Product.cs**
```csharp
namespace repositoryPattern.Entity
{
    public class myClass1
    {
        public void MyFunction1()

        {
            Console.WriteLine("HelloWorld");
        }
    }
}
```

Yukarıdaki Ana dizinin altında Entity klasörünün içindeki Product.cs Dosyası ve bu dosyanın içindeki namespace tanımlamamıza dikkat edin

**./Program.cs**
```csharp
using repositoryPattern.Entity;

namespace repositoryPattern
{
    public class NewClass
    {
        public static void Main(string[] args)
        {
           myClass1 deneme = new myClass1();
           
           deneme.MyFunction1();
         }
    }
}
```

İlk örnekteki namespace tanımlamasını bu sefer using kullanarak ana proje dosyamıza import etmiş olduk ve bu şekilde Program.cs dosyasında kullanabiliyoruz. Kısacası import işlemi namespacae ler arasında olur.