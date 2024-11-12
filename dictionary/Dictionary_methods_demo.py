'''

player1 = {
    "id" : 1,
    "name" : "cristiano ronaldo",
    "yearofBirth" : 1985,
    "nationality" : "portugal",
    "current_team" : "portugal",
    "history" : "juevntus , Real Madrid , protugal"
}

player1 = {
    "id" : 2,
    "name" : "Lionel messi",
    "yearofBirth" : 1987,
    "nationality" : "Argentina",
    "current_team" : "Barcelona",
    "history" : "Barcelona,argantina,Portugal"
}

'''

players = {}



id = input("oyuncu id : ")
ad = input("oyuncu ad : ")
YearofBirth = input("doğum yılı : ")
Nationality = input("uyruk : ")
current_team = input("takım : ")
history = input("oyuncu geçmişi : ")

players.update ({
    "id" : {
        "name" : ad,
        "Yeadofbirth" : YearofBirth,
        "nationality" : Nationality,
        "current_team" : current_team,
        "history" : history.split(',') # girilen değerleri virgül ile ayırır
    }
})

id = input("oyuncu id : ")
ad = input("oyuncu ad : ")
YearofBirth = input("doğum yılı : ")
Nationality = input("uyruk : ")
current_team = input("takım : ")
history = input("oyuncu geçmişi : ")

players.update ({
    "id" : {
        "name" : ad,
        "Yeadofbirth" : YearofBirth,
        "nationality" : Nationality,
        "current_team" : current_team,
        "history" : history.split(',') # girilen değerleri virgül ile ayırır
    }
})

id = input("aramak istediğiniz oyuncu id : ")
player = players.get(id) # ilgili key getirilir.

print(f'name : {player.get("name")}')


id = input("silmek istediğiniz oyuncu id : ")
players.pop(id)

print(players)
# print(players)
