with open("data.txt" , "r+") as k :
    veri = k.read()
    print(veri)

with open("data.txt" , "r+") as k :
    k.truncate(20)
    yeni_data =  k.read()
    print(yeni_data)