
## Driver Projeye eklenmesi


Hangi veri tabanını kullanacaksan veri tabanının web sitesine gidip jdbc dosyasını indirmelisin. Indirilecek olan dosya .jar uzantılıdır.

.jar dosyası projede ana dizine at ve projeye bu kütüphaneyi eklemek için aşağıdaki adımları takip et . Burada intellij idea idesini için adımlar var .Farklı bir  ide  kullanıyosan web de araştır.

File => Project Structure =>  Libraries => + => java =>  .jar uzantılı indiriğimiz dosyayı seç



## Bağlantıyı Kurmak


Bağlantıyı kurmak için birkaç bilgiye ihtiyacımız var. 

```java
    public static final String DB_URL = "jdbc:postgresql://localhost/dbName";
    public static final String DB_USERNAME = "username";
    public static final String DB_PASSWORD = "password";
```


- db name veritabanı ismidir. Projede Birden fazla veritabanı olabilir.
- username ve password ise veri tabanına giriş yaparken kullanılan kullanıcı adı ve şifre . Genellikle veritabanını kurarken oluştuurlur.


Bu aşamada Connection ve DriverManager sınıflarına ihtiyacımız var ve olası bir hatayı yakalamak için (try catch yapısı kullanılacak) SQLException sınıfını eklemeliyiz.

```java 
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
```

Connection sınıfıdan bir nesne  oluşturup DriverManeger sınıfında bulunan  getConnection() statik metodunu kullanarak yukarıda oluşturduğumuz değişkeneleri parametre olarak veriyoruz.

```java
  public static void main(String[] args) {
        Connection conn = null;
        
        try {
        
            conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            
        } catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }
    }
```


Try catch yapısını burada kullanıyoruz. getConnection() metodunda sıralama önemlidir.


**Kodlar sırasıyla**
```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnect {
    public static final String DB_URL = "jdbc:mysql://localhost/dbName";
    public static final String DB_USERNAME = "username";
    public static final String DB_PASSWORD = "password";

    public static void main(String[] args) {
        Connection conn = null;
        try {
            conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
        } catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }
    }

}
```

## Kayıt Sorgulamak

Sgl sorgularını veritabanına iletmek için Statement arabiriminden faydalanıyoruz.

```java
public static void main(String[] args) {

	Connection conn = null;
	Statement st = null;
	try {
		conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
		st = conn.createStatement();

		ResultSet resultSet = st.executeQuery("SELECT * FROM film  WHERE replacement_cost > 15  limit 10;");

		while (resultSet.next()) {
			System.out.println("film_id : " + resultSet.getInt("film_id"));
			System.out.println("Adı : " + resultSet.getString("title"));
			System.out.println("açıklama  : " + resultSet.getString("description"));
			System.out.println("yıl : " + resultSet.getInt("release_year"));
			System.out.println("#################");
		}

	} catch (SQLException ex) {
		System.out.println("SQLException: " + ex.getMessage());
		System.out.println("SQLState: " + ex.getSQLState());
		System.out.println("VendorError: " + ex.getErrorCode());
	}

}
```

- **Connection** nesnesi oluşturduk ve **DriverManager** kullanarak veritabanı bağlantısını sağladık. Sorgu yazabilmemiz için ise bir statement nesnesi oluşturduk ve bağlantı kurduğumuz nesnedeki ``createStatement() ``metodu ile sorgu yazacak hale getiriyoruz. 
- ResultSet ile sql sorgusunu yazdıktan sonra gerye bir cevap alabiliyoruz. ``executeQuery()`` metodu ile sql sorguları yazıyoruz ve haliyle oradan bir cevap geleceği için bu verileri resultset ile tutuyoruz.
- ResultSet sınıfında ``next()`` metodu var ve bu metod sayesinde verileri sırasıyla alabiliyoruz. next() metodu okunacak kayıt kalmadığında ``false`` değerini geri döndürür.
- While döngüsünde verirleri alırken resultSet nesnesi kullanılarak  **tablo adlarına göre** veriler alınır. Burada tabloların veri türleri önemlidir. Mesele ilgili tablo integer veri türünde ise ``getInt()`` metodu kullanılır. 


### NOT

Eğer ``resultset.next()`` metodu kullanarak birkaç sorgu ileri gittin ve bu noktada ``resultset.first()``  metodunu kullanarak ilk sorguya dönmek istersen hata alırsın. bunun önüne geçmek için kodunu aşağıdaki gibi güncelle

```java
st = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE , ResultSet.CONCUR_READ_ONLY );
```

## Kayıt Eklemek


### Statement İle Kayıt Eklemek

```java
public static void main(String[] args) {

	Connection conn = null;
	Statement st = null;
	String sql = "INSERT INTO actor (first_name , last_name) VALUES ('abdulrezzak' , 'polatkol')";
	
	try {
		conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
		st = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
		st.executeUpdate(sql);


	} catch (SQLException ex) {
		System.out.println("SQLException: " + ex.getMessage());
		System.out.println("SQLState: " + ex.getSQLState());
		System.out.println("VendorError: " + ex.getErrorCode());
	}

}
```



### PreparedStatement İle Kayıt Eklemek


```java
public static void main(String[] args) {

	Connection conn = null;
	String prstSql = "INSERT INTO actor (first_name , last_name) VALUES (? , ?)";

	try {
		conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
		
		PreparedStatement prst = conn.prepareStatement(prstSql);
		prst.setString(1, "yusuf");
		prst.setString(2, "kahve");

		prst.executeUpdate();

	} catch (SQLException ex) {
		System.out.println("SQLException: " + ex.getMessage());
		System.out.println("SQLState: " + ex.getSQLState());
		System.out.println("VendorError: " + ex.getErrorCode());
	}

}
```

PreparedStatement ile kayıt eklerken parametereler yerine ? eklenir ve bu soru işaretleri daha sonra doldurulur.



## Kayıt Güncellemek

**Statement ile kayıt güncellemek**
```java
 public static void main(String[] args) {
        
        Connection conn = null;
        Statement st = null;
        String stSql = "UPDATE actor SET first_name = 'mehmettttt' WHERE actor_id =1 ";
        try {
            conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            st = conn.createStatement();
            st.executeUpdate(stSql);

        } catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }

    }
```


**Prepared Statement ile kayıt güncellemek**
```java
public static void main(String[] args) {

	Connection conn = null;
	String PrstSql = "UPDATE actor SET first_name = ? WHERE actor_id = ? ";

	try {
		conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
		PreparedStatement pr = conn.prepareStatement(PrstSql);
		pr.setString(1, "arda");
		pr.setInt(2, 1);
		pr.executeUpdate();

	} catch (SQLException ex) {
		System.out.println("SQLException: " + ex.getMessage());
		System.out.println("SQLState: " + ex.getSQLState());
		System.out.println("VendorError: " + ex.getErrorCode());
	}

}
```


## Kayıt Silmek


```java

    public static void main(String[] args) {

        Connection conn = null;
        Statement st = null;

        try {

            conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            st = conn.createStatement();
            st.executeUpdate("DELETE FROM actor WHERE actor_id = 1");

        } catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }

    }
```

```java

    public static void main(String[] args) {

        Connection conn = null;
        String prstSql = "DELETE FROM actor WHERE actor_id = ?";
        try {

            conn = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            PreparedStatement prst = conn.prepareStatement(prstSql);
            prst.setInt(1,2);
            prst.executeUpdate();

        } catch (SQLException ex) {
            System.out.println("SQLException: " + ex.getMessage());
            System.out.println("SQLState: " + ex.getSQLState());
            System.out.println("VendorError: " + ex.getErrorCode());
        }

    }
```

## JDBC ile Transaction Yönetimi

