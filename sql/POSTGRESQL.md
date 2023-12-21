
## STRING FUNCTIONS


CONCAT
FORMAT
LENGHT
LEFT 
RIGHT 
LOWER 
UPPER
POSITION
TRIM 
SUBSITRING 
REVERSE 
REPLECE 
REGEXP_MATCHES
REGEXP_REPLACE
REPEAT


## REGEX

SQL'de, genellikle `REGEXP` veya `RLIKE` operatörleri kullanılarak regex ifadeleriyle çalışabilirsiniz. İşte bazı yaygın regex operatörleri ve anlamları:

1. `.` (Nokta): Herhangi bir tek karakteri temsil eder.
    
    - Örnek: `a.c` ifadesi "abc", "a1c", "axc" gibi dizeleri eşleştirir.
2. `*` (Yıldız): Önceki karakterin 0 veya daha fazla tekrarını temsil eder.
    
    - Örnek: `ab*c` ifadesi "ac", "abc", "abbc" gibi dizeleri eşleştirir.
3. `+` (Artı): Önceki karakterin 1 veya daha fazla tekrarını temsil eder.
    
    - Örnek: `ab+c` ifadesi "abc", "abbc" gibi dizeleri eşleştirir, ancak "ac" eşleşmez.
4. `?` (Soru işareti): Önceki karakterin 0 veya 1 tekrarını temsil eder.
    
    - Örnek: `ab?c` ifadesi "ac" ve "abc" gibi dizeleri eşleştirir.
5. `[]` (Köşeli parantezler): Belirli karakterlerin herhangi birini temsil eder.
    
    - Örnek: `[aeiou]` ifadesi herhangi bir ünlü harfi eşleştirir.
6. `[^]` (Ünlem ve köşeli parantezler): Belirli karakterlerin hiçbirini temsil eder.
    
    - Örnek: `[^0-9]` ifadesi rakam olmayan herhangi bir karakteri eşleştirir.
7. `|` (Dikey çizgi): Alternatifleri belirtmek için kullanılır.
    
    - Örnek: `a|b` ifadesi "a" veya "b" karakterlerini eşleştirir.
8. `()` (Parantezler): Gruplama için kullanılır.
    
    - Örnek: `(abc)+` ifadesi "abc", "abcabc" gibi bir veya daha fazla "abc" gruplarını eşleştirir.
9. `\` (Ters eğik çizgi): Özel karakterleri kaçırmak veya özel karakterleri kullanmak için kullanılır.
    
    - Örnek: `\.` ifadesi nokta karakterini eşleştirir, çünkü nokta normalde herhangi bir karakteri temsil ederken, `\` ile kaçırıldığında tam bir nokta karakteri olur.
10. `^` (Başlangıç işareti): Dizinin başlangıcını ifade eder.
    
    - Örnek: `^abc` ifadesi "abc" ile başlayan dizeleri eşleştirir.
11. `$` (Bitiş işareti): Dizinin sonunu ifade eder.
    
    - Örnek: `abc$` ifadesi "abc" ile biten dizeleri eşleştirir.














if (N % 2 == 1)

       {Console.WriteLine( "Weird");}

       else if (N>=2  && N <=5)

       {Console.WriteLine("Not Weird");}

       else if (N>=6 && N<=20)

       {Console.WriteLine("Weird");}

       else if (N % 2 == 0 && N > 20) 

       {Console.WriteLine("Not Weird");}
