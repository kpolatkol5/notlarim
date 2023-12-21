
## Recursive Fonksiyonlar

Recursive fonksiyonlar, bir fonksiyonun kendini doğrudan veya dolaylı olarak çağırdığı fonksiyonlardır. Bu fonksiyonlar, matematiksel bir problemin veya algoritmanın çözümünde kullanılabilirler. Recursive fonksiyonlar, problemi daha küçük parçalara bölmek ve bu parçaları tekrarlayarak çözmek için kullanılır.

```java
public class Recursive {  
	static int f(int n) {  
		System.out.println(n);  
		if (n == 1) {  
			return 1;  
		}  
	  
		int result = n + f(n - 1);  
		System.out.println("result ==> " + result);  
		return result;  
	}  
	  
	public static void main(String[] args) {  
		System.out.println(f(4));  
	}  
}
```

**ÇIKTI** 
```bash
4
3
2
1
result ==> 3
result ==> 6
result ==> 10
10
```


***AÇIKLAMASI:***

Aşağıdaki görseli açıklayacak olursak. Aslında her sefersinde fonksiyon kendisini çağırıyor eğer if blogu çalışmazsa sonsuz döngüye girer. Her bir adım için bellekte alan açılır f(4) f(3) f(2) f(1) birer boyut gibi düşün.ilk fonksiyon en son deger döndüren fonksiyon oluyor. return ifadelerini takip ederseniz daha iyi anlaşılacaktır. 

![](assets/f(4).png)

Recursive fonksiyonların çalışma mantığı, her çağrıda bir önceki çağrıya geri dönüş yaparak sonuca ulaşmasıdır. Fonksiyon, kendini çağırdığı her seferde bir önceki çağrının tamamlanmasını bekleyerek çalışır.

```csharp

```



