
import random 

# Pickable Player HP and Health
Warlock = "Warlock"
Paladin = "Paladin"
orc = "Orc"


#Player HP

Warlock_hp = 600
Paladin_hp = 500
orc_hp = 1000


#Player Attacks

Warlock_dmg = {"Shadow ball": 75, "Eldritch blast": 500, "Abyss":50, "Meteor shower": 200 }
Paladin_dmg = {"Light shower": 100, "Divine Sense": 50, "Divine Health": 150, "Aura":50}
orc_dmg = {"Brute force": 150, "Gruumsh's Fury": 300 ,"Battle Cry": 50, "Eye of Gruumsh": 50}





# 3 Enemies to face HP and Health

Winged_suitHP  = 1500
Winged_suitAK = {"Winged Slash": 75, "Screen": 50, "Diamond Dancing": 100, "High Flight" 80}

Fluffy_HP = 2000
Fluffy_ak = {"Consume": 50, "Slap": 75, "Double Slap": 150, "Slam": 100} 

Ghost_ak= {"Destiny Bond": 300, "Spectral Thief": 30, "Realm consume": 150, "Glare": 75}
Ghost_HP = 3000

Potion = 50



# Main screen


while True:
    print("1) Warlock")
    print("2) Paladin")
    print("3) Orc")
    character = (str(input("Choose your character: ")))
    if character == "1":
        character = Warlock
        my_hp = Warlock_hp
        my_damage = random.choice(Warlock_dmg.keys())      
        print("\nYou have chosen the character: Warlock \n Health: 600")
        break
    elif character == "2":
        character = Paladin
        my_damage = random.choice(Paladin_dmg.keys())
        my_hp = Paladin_hp
        print("\nYou have chosen the character: Paladin \n Health: 500")
        break
    elif character == "3":
        character = orc
        my_hp = orc_hp
        my_damage = random.choice(orc_dmg.keys())
        print("\nYou have chosen the character: Orc \n Health: 1000")
        break
    else:
        print("Character not avaliable")


print(".........")
print("..........")

print("A new foe has appeared")



#Battle instance 1 /////////////////////////////////////////////
while True:
    input_str = print(input("Press Enter to attack: "))
    if input_str == "":
        attack_name = my_damage
        Winged_suitHP = Winged_suitHP - my_damage
        print("The", character, "used", attack_name, "and inflicted", my_damage, "damage!")
        print("The Enemy is at", Winged_suitHP, "Health")
        if Winged_suitHP <= 0:
            print("The Enemy has lose the battle")
            break
    else:
        print("Invalid input, please press Enter to attack.")

while True:
    my_hp = my_hp - random.choice(Winged_suitAK.keys())
    print("\nThe", character, "has been damaged by the Dragon!")
    print("The", character, "has", my_hp, "health left.")
    if my_hp <= 0:
        print("The", character, "has died.")
        break

#////////////////////////////////////////////////////////////

# Battle instance 2

print("Battle has Ended")
print(".........")
print("..........")

print("A new foe has appeared")


while True:
    my_hp = my_hp - random.choice(Fluffy_ak.keys())
    print("\nThe", character, "has been damaged by the Dragon!")
    print("The", character, "has", my_hp, "health left.")
    if my_hp <= 0:
        print("The", character, "has died.")
        break

while True:
    input_str = print(input("Press Enter to attack: "))
    if input_str == "":
        attack_name = my_damage
        Fluffy_HP = Fluffy_HP - my_damage
        print("The", character, "used", attack_name, "and inflicted", my_damage, "damage!")
        print("The Enemy is at", Fluffy_HP, "Health")
        if Fluffy_HP <= 0:
            print("The Enemy has lose the battle")
            break
    else:
        print("Invalid input, please press Enter to attack.")

print("Battle has Ended")
print(".........")
print("..........")

print("A new foe has appeared")

# Battle instance 3


while True:
    my_hp = my_hp - random.choice(Ghost_ak.keys())
    print("\nThe", character, "has been damaged by the Dragon!")
    print("The", character, "has", my_hp, "health left.")
    if my_hp <= 0:
        print("The", character, "has died.")
        break


while True:
    input_str = print(input("Press Enter to attack: "))
    if input_str == "":
        attack_name = my_damage
        Ghost_HP  = Ghost_HP  - my_damage
        print("The", character, "used", attack_name, "and inflicted", my_damage, "damage!")
        print("The Enemy is at", Ghost_HP , "Health")
        if Ghost_HP  <= 0:
            print("The Enemy has lose the battle")
            break
    else:
        print("Invalid input, please press Enter to attack.")



#Endgame
print(" All enemies defeated, Game over")