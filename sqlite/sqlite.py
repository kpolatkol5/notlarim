import sqlite3 as db 


# db = db.connect("data.sqlite")

# im = db.cursor()

# im.execute(""" CREATE TABLE IF NOT EXISTS town (town_name , city) """)

# im.execute(""" INSERT INTO town VALUES ('iskenderun' , 'hatay') """)
# im.execute(""" INSERT INTO town VALUES ('ANtakya' , 'hatay') """)

# db.commit()
# db.close()

# ---------------------------------------------------------------------------
#ÖRNEK 2


# #BİR SÖZLÜKTEN VERİTABANINA VERİ EKLEME İŞLEMİ

# veriler = {
    
#     "1" : ['Antakya','Hatay'],
#     "2" : ['isknedrun', 'Hatay'],
#     "3" : ['Payas', 'Hatay'],
#     "4" : ['Hassa', 'Hatay']
# }


# db = db.connect("database.sqlite")


# im = db.cursor()

# im.execute(""" CREATE TABLE IF NOT EXISTS town (id  , town_name , city) """)

# for i in veriler:
#     im.execute(""" INSERT INTO town VALUES ("{}" , "{}" , "{}" )""".format(i , veriler[i][0] , veriler[i][1]))

# db.commit()
# db.close()


# NOT: bu kodları her çalıştırdığında sözlük yapısındaki verileri veritabanına ekleyecektir bunun önüne geçmek istersen .Veri eklemek için bir fonksiyon tanımlayabilrisin

# ---------------------------------------------------------------------------

# # Verilerin çekilmesi

# db = db.connect("database.sqlite")

# im = db.cursor()

# im.execute(""" CREATE TABLE IF NOT EXISTS town (id , town_name , city) """)

# im.execute(""" INSERT INTO town VALUES ("5" , " Erzin" , "Hatay") """)
# db.commit()

# im.execute(""" SELECT * FROM  town """)

# tum_veriler = im.fetchall()

# db.close()


# print(tum_veriler)

# ---------------------------------------------------------------------------

# # TOBLALARIN İSİMLERİNİ ÖĞRENMEK

# db = db.connect("database.sqlite")

# im = db.cursor()
# im.execute("SELECT name FROM sqlite_master")

# tablo_adlari = im.fetchall()

# db.commit()
# db.close()

# print(tablo_adlari)



# ---------------------------------------------------------------------------

# # Verilerin Tek Tek Çekilmesi


# db = db.connect("database.sqlite") 

# im = db.cursor()

# im.execute("SELECT * FROM town")

# tek_getir = im.fetchone()
# print(tek_getir)

# tek_getir = im.fetchone()
# print(tek_getir)

# tek_getir = im.fetchone()
# print(tek_getir)

# tek_getir = im.fetchone()
# print(tek_getir)

# tek_getir = im.fetchone()
# print(tek_getir)

# tek_getir = im.fetchone()
# print(tek_getir)

# # bu kısımda artık veri kalmadı ve none değerini dönerdi eğer veri tabanına veri ekleme veya çıkartma işlemi yapmadığınız sürece bunu görebilirsiniz . Kısacası eğer getirecek veri kalmazsa None değerini döndürür

# tek_getir = im.fetchone()
# print(tek_getir)

# db.close()


# ---------------------------------------------------------------------------

# # Seçtiğimiz verilerin belirtilen kadarını almak



# db = db.connect("database.sqlite") 

# im = db.cursor()

# im.execute(""" SELECT *  FROM town""")

# istenen_kadar = im.fetchmany(3)

# print(istenen_kadar)

# db.close()

# ---------------------------------------------------------------------------


# VERİLERİN FİLİTRELENMESİ

db = db.connect("database.sqlite")

im = db.cursor()

im.execute(""" SELECT * FROM town WHERE city = "Hatay" """)
# im.execute(""" SELECT * FROM town WHERE id = "5" """)

hatay_verileri = im.fetchall() 

print(hatay_verileri)
db.close()

