import random

Attackers = ["Sledge", "Thatcher", "Ash", "Thermite", "Twitch" , "Montagne" , "Glaz" , "Fuze" , "Blitz" , "IQ" , "Buck" , "Capitao" , "Hibana" , "Jackal" , "Ying" , "Zofia" , "Lion" , "Maverick" , "Amaru" , "Kali" , "Ace", "Florles" , "Osaft"]
Defenders = ["Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook" , "Kapkan" , "Tachanka" , "Jäger" , "Bandit" , "Frost" , "Valkyrie" , "Cavera" , "Mira" , "Lesion" , "Ela" , "Vigil" , "Alibi" , "Kaid" , "Mozzie" , "Melusi" , "Thunderbird" , "Thorn"]

zufallszahl_attack = random.randint(0,22)
zufallszahl_defender = random.randint(0,22)
#print(zufallszahl)
print(Attackers[zufallszahl_attack])

if zufallszahl_defender == 1:
    print("Du Hurensohn, nimm mal nicht Clash!!!")
else:
    print(Defenders[zufallszahl_defender])