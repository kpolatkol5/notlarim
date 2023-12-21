
Dizilerin daha gelişmiş ve esnek bir alternatifidir.Programların daha verimli ve esnek bir şekilde verileri depolamasına ve yönetmesine olanak tanır. Dizilerde dizinin boyutunu belirlememiz gerekiyordu ve değer ataması yapmak için dizilerin index numarasına göre atama yapabiliyoruz. Koleksiyonlarda ise dizi boyutu tanımlamaya gerek yoktur.İki başlıkta incelenebilir. Tip güveli ve Genel koleksiyonlar vardır. 

Tip güvenli koleksiyonlarda veri türü belirtilir ve sadece o türler aktarılır. String ,integer , object gibi veri türleri hatta bir sınıfın elemanlarını tutumak isteyebilririz.Genel koleksiyonlarda ise veri türü farketmeksizin tüm elemanları kabul eder.

## ArrayList

Tip güvenli değildir. Veri türü farketmeksizin verileri kabul eder.


```csharp
 class Program
    {
        public static void Main(string[] args)
        {
            ArrayList koleksiyon = new ArrayList();
            
            koleksiyon.Add("Hatay");
            koleksiyon.Add("Dörtyol");
            koleksiyon.Add(31);
            koleksiyon.Add(true);  
            
            foreach (var item in koleksiyon)
            {
                Console.WriteLine(item.GetType());
            }
        }
    }
    //System.String
	//System.String
	//System.Int32
	//System.Boolean
```


## Tip Güvenli Koleksiyonlar

**<>**  bu ifade arasına veri türü değeri girilir. integer string veya herhangi bir nesnenin objeleri veri türü olarak tanımlanabilir.


```csharp
 class Program
    {
        public static void Main(string[] args)
        {
		    List<int> koleksiyon = new List<int>();
            koleksiyon.Add(31);
            koleksiyon.Add(213);
            koleksiyon.Add(345);
            
            foreach (var item in koleksiyon)
            {
                Console.WriteLine(item.GetType());
                Console.WriteLine(item);
                Console.WriteLine("--------------------");
            }
        }
    }
    //System.Int32
	//31
	//--------------------
	//System.Int32
	//213
	//--------------------
	//System.Int32
	//345
	//--------------------
```

## Metodları

### Add()

Listenin sonuna bir öğe ekler.

```csharp
List<string> mylist = new List<string>();
mylist.Add("elma");
mylist.Add("armut");
```

### Remove()

Belirtilen öğeyi listeden kaldırır.

```csharp
mylist.Remove("elma");
```

### Insert()

Belirtilen konuma bir öğe ekler.
```csharp
mylist.Insert(1, "portakal");
```

### Contains()

Belirtilen öğenin listeye dahil olup olmadığını kontrol eder.
```csharp
bool isExist = mylist.Contains("armut");
```



### IndexOf()

Belirtilen öğenin index numarasını geriye döndürür.

```csharp
int index = mylist.IndexOf("portakal");
```

### Count()

Listenin öğe sayısını döndürür.

```csharp
int count = mylist.Count;
```

### Clear()

Listeyi temizler ve tüm öğeleri kaldırır.

```csharp
mylist.Clear();
```

### ToArray()

Listenin öğelerini bir diziye kopyalar.

```csharp
string[] myarray = mylist.ToArray();
```

### Find()

Listenin öğelerini bir diziye kopyalar.

```csharp
string result = mylist.Find(s => s.StartsWith("a"));
```

### FindAll()

Belirli bir koşulu karşılayan tüm öğeleri içeren bir koleksiyonu döndürür.

```csharp
List<string> myfilteredlist = mylist.FindAll(s => s.Length > 4);
```


## Dictionary

Sözlük koleksiyonlarının  anahtar ve değer elemanları var. Tip korumalıdır. 


Bir sözlük tanımlaması yapacak olursak;
```csharp
	Dictionary<int , Person> sozluk = new Dictionary<int, Person>();
```


Person sınıfım
```csharp
   public class Person
    {
        public string Isim { get; set; }
        public string Soyisim { get; set; }
        public string Memleket { get; set; }
        public int Posta_kodu { get; set; } 
  

        public Person(string isim, string soyisim, string memleket, int posta_kodu)
        {
            this.Isim = isim;
            this.Soyisim = soyisim;
            this.Memleket = memleket;
            this.Posta_kodu = posta_kodu;
        }  

        public string GetPerson()
        {
            return $"Personel isim ve soy isimi : {this.Isim} {this.Soyisim} -- Memleketi ve Posta Kodu : {this.Memleket}-{this.Posta_kodu}";
        }
    }
```


Artık sözlük taımladık elemalar ekleyip çıakrtabilriz.Listelerde olduğu gibi ortak metodlara sahipler
```csharp
     sozluk.Add(1,new Person("yasin" , "Bulut" , "Hatay" , 31600));
```

foreach döngüsü ile sözlükteki elemanları yazdırabilriirz.

```csharp
	foreach (var item in sozluk)
		{
			Console.WriteLine($"Personel id : {item.Key} ==> {item.Value.GetPerson()}");
		}
```

## Çok Boyutlu Dictionary


ikinci bir boyut tanımlamak istersen aşağıdaki örneği referans al.
```csharp
Dictionary<int, Dictionary<string, string>> sozluk1 = new Dictionary<int, Dictionary<string, string>>();
```

Örnekte ilk eleman integer ikinci eleman ise türü Dictionary olarak belirttik.bu ikinci eleamn da sonuçta sözlğk olduğu için bunların da anahtar ve değerlerin veri türünü belirliyoruz.Bu collection a eleman eklemek istersek;

```csharp
	sozluk1.Add(1, new Dictionary<string, string>(){
		{"n1","s1"},
		{"n2","s2"},
		{"n3","s3"},
	});
	sozluk1.Add(2, new Dictionary<string, string>(){
		{"2-n1","2-s1"},
		{"2-n2","2-s2"},
		{"2-n3","2-s3"},
	});
```


Bu örneği Foreach döngüsü ile ekrana yazdırmayı deneyelim.

```csharp
foreach (var item in sozluk1)
	{
		Console.WriteLine(item.Key);
		Console.WriteLine("İkinci BOyuttaki elemanlar");
		
		foreach (var boyut2 in item.Value)
		{
			Console.WriteLine($"key => {boyut2.Key} : Value => {boyut2.Value}");
		}
		
		Console.WriteLine("*****************");
	}
```

**Çıktı**
```bash
1
İkinci BOyuttaki elemanlar
key => n1 : Value => s1
key => n2 : Value => s2
key => n3 : Value => s3
*****************
2
İkinci BOyuttaki elemanlar
key => 2-n1 : Value => 2-s1
key => 2-n2 : Value => 2-s2
key => 2-n3 : Value => 2-s3
*****************
```

