import json

# json to dic

# with open("ornek.json") as f:
#     veri = json.load(f)

#     print(veri["user1"]["lastname"])



# dic to JSON
data = {
    "user1":{"firstname":"Kadir","lastname":"polatkol"},
    "user2":{"firstname":"kamil","lastname":"polatkol"},
    "user3":{"firstname":"yusuf","lastname":"polatkol"}
}   

with open("ornek.json","w") as f :
    json.dump(data, f , indent=2)
    # 2 birim girinti bırakarak yazdıracaktır