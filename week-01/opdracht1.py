# Oefening 1
# Print de volgende zin "Hello World"

print("hello world")


# Oefening 2
# Verander de waarde van de onderstaande variabelen.
# Print deze daarna 1 voor 1 uit

naam = "joost"
leeftijd = 16
woonstad = "ede"
print(naam)
print(leeftijd)
print(woonstad)
# Oefening 3
# Gebruik nu bovenstaande variabelen om zinnen te bouwen
# Bijvoorbeeld print("Hallo mijn naam is ", naam) of print(f"Mijn naam is {naam}")
print("hallo mijn naam is ", naam)


# Oefening 4
# Maak variabelen aan voor je favoriete game, hoe veel uur je deze hebt gespeeld en welk cijfer je dit spel zou geven
# Print deze daarna in zinnen uit, bijvoorbeeld "Mijn favoriete game is Minecraft" "Ik heb deze game 150 uur gespeeld", "Ik geef deze game een 8.5"
game = "minecraft"
tijd = "1000 uur"
cijfer = 10
print(f"mijn faforiete game is {game}ik heb daar {tijd} in en geef het spel een {cijfer}")

# Oefening 5
# Maak twee variabelen aan, number1 en number2
# Bereken daarna de som (+), het verschil (-) en het product (*) uit van deze nummers.
# Print daarna de uitkomsten uit
number1 = 5
number2 = 10
print(number1 + number2)


# Oefening 6
# Maak een simpel game character met minimaal de volgende variabelen: name, health, level, damage
# Print deze vervolgens uit
# Zorg er daarna voor dat je character 20 damage neemt, print nu de nieuwe waarde van zijn health uit
charactername = "bob"
characterhealth = 30
characterlevel = 1
characterdamage = 5
characterhealth = characterhealth - 20
print(characterhealth)
# Oefening 7
# Ga verder met je character van de vorige oefening. Voeg nu een nieuw variabel "weapon" toe.
# Geef het wapen een naam, verhoog de damage van je character en verhoog het level met 1
# Print daarna de nieuwe waardes uit 
characterweapon = "zwaard"
characterdamage = characterdamage + 10
characterlevel = characterlevel + 1
print(f"level {characterlevel} health {characterhealth} damage {characterdamage} weapon {characterweapon} name {charactername}")
# Oefening 8
# Maak een programma dat een profiel van een gamer laat zien
# Maak minimaal de volgende variabelen: name, age, favouriteGame, hoursPlayed, level, score
# Print al deze informatie netjes uit
# Verhoog daarna de score van het profiel met 250 en print de nieuwe waarde
# Bonus! Voeg zelf 3 nieuwe variabelen toe
print("gamerfiles")
name = "joost"
age = 16
favoutitegame = "minecraft"
hoursplayed = 13478
level = 369
score = 859269
log = (f"name {name}\nage {age}\nfavourite game {favoutitegame}\nplaytime {hoursplayed}\nlevel {level}\nscore {score}")
print (log)
score = score + 250
print(log)