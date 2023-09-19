wizard = "Wizard"
elf = "Elf"
human = "Human"

Wizard_HP = 70
ELF_HP = 100
HUMAN_HP = 150

Wizard_DMG = 150
ELF_DMG = 100
HUMAN_DMG = 20

DRAGON_HP = 300
dragon_damage = 50

ENEMY1_HP = 80
ENEMY1_DMG = 30

ENEMY2_HP = 120
ENEMY2_DMG = 40

ENEMY3_HP = 150
ENEMY3_DMG = 50

ENEMY4_HP = 200
ENEMY4_DMG = 60

# Define a function to fight an enemy
def fight_enemy(enemy, enemy_hp, enemy_damage):
    while True:
        enemy_hp -= my_damage
        print(f"\nThe {character} damaged the {enemy}!")
        print(f"The {enemy} is at {enemy_hp} Health")
        if enemy_hp <= 0:
            print(f"The {enemy} has lost the battle")
            return True
        my_hp -= enemy_damage
        print(f"\nThe {character} has been damaged by the {enemy}!")
        print(f"The {character} has {my_hp} Health left")
        if my_hp <= 0:
            print(f"The {character} has Died")
            return False

# Choose a character
while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose your character: ")
    if character == "1":
        character = wizard
        my_hp = Wizard_HP
        my_damage = Wizard_DMG
        print(f"\nYou have chosen the character: Wizard \n Health: {Wizard_HP} \n Damage: {Wizard_DMG}")
        break
    elif character == "2":
        character = elf
        my_damage = ELF_DMG
        my_hp = ELF_HP
        print(f"\nYou have chosen the character: Elf \n Health: {ELF_HP}\n Damage: {ELF_DMG}")
        break
    elif character == "3":
        character = human
        my_hp = HUMAN_HP
        my_damage = HUMAN_DMG
        print(f"\nYou have chosen the character: Human \n Health: {HUMAN_HP}\n Damage: {HUMAN_DMG}")
        break
    else:
        print("Unknown Character")

# Fight enemies one by one until the game is finished
enemies = [("Dragon", DRAGON_HP, dragon_damage),
           ("Enemy 1", ENEMY1_HP, ENEMY1_DMG),
           ("Enemy 2", ENEMY2_HP, ENEMY2_DMG),
           ("Enemy 3", ENEMY3_HP, ENEMY3_DMG),
           ("Enemy 4", ENEMY4_HP, ENEMY4_DMG)]

for enemy, enemy_hp, enemy_damage in enemies:
    print(f"\nYou are facing a {enemy} with {enemy_hp} health and {enemy_damage} damage!")
    if fight_enemy(enemy, enemy_hp, enemy_damage):
        print(f"\nCongratulations! You defeated the {enemy}!")
    else:
        print("Game Over")
        break


print( 'Success!')