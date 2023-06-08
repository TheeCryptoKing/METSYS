# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session
# from player import Player, Enemy, Location, Abilities
import random

# engine = create_engine('sqlite:///game.db', echo=True)
# session = Session(bind=engine)

# def battle(player, enemy):
#     print(f"Player: {player.name} VS Enemy: {enemy.name}")
#     print("Battle begins!")
    
#     while player.hp > 0 and enemy.hp > 0:
#         print(f"\n{player.name}'s turn:")
#         print("1. Primary Attack")
#         print("2. Secondary Attack")
#         choice = input("Select an attack: ")
        
#         if choice == "1":
#             attack = "Starburst Stream"
#         elif choice == "2":
#             attack = "Starburst Stream"
#         else:
#             print("Invalid choice. Try again.")
#             continue
        
#         print(f"{player.name} attacks with Starburst Stream!")
#         enemy.hp -= 5
#         print(f"{enemy.name} takes 5 damage. Enemy HP: {enemy.hp}")
        
#         if enemy.hp <= 0:
#             print(f"{enemy.name} has been defeated!")
#             break
        
        
#         print(f"\n{enemy.name}'s turn:")
#         enemy_attack = random.choice([enemy.attack1, enemy.attack2])
#         print(f"{enemy.name} attacks with {enemy_attack.name}!")
#         player.hp -= attack.damage
#         print(f"{player.name} takes {attack.damage} damage. Player HP: {player.hp}")
        
#         if player.hp <= 0:
#             print(f"{player.name} has been defeated!")
#             break
    
#     print("Battle ends!")

# player = session.query(Player).filter_by(name="Slayer").first()
# enemy = session.query(Enemy).filter_by(name="Blood Magic Queen").first()
# battle(player, enemy)

# session.close()
from questions import current_player
from art import (ability_whirlwing, snack, ability_starburst, ability_expelliarmus)

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Enemy:
    def __init__(self, name, hp, attack1, attack2):
        self.name = name
        self.hp = hp
        self.attack1 = attack1
        self.attack2 = attack2

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

player = current_player
def battle(player, enemy):
    print(f"Player: {player.name} VS Enemy: {enemy.name}")
    print("Battle begins!")

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}'s turn:")
        print(f"1. {current_player.primary_attack}")
        print(f"2. {current_player.secondary_attack}")
        choice = input("Select an attack: ")

        if choice == "1":
            if player.className == "Warrior":
                attack = Attack("Whirlwind Strike", 25)
                print(f'{ability_whirlwing}')
                print(f"{player.name} attacks with {player.primary_attack}!")
            elif player.className == "Mage":
                attack = Attack("Serpentine Slash", 25)
                print(f'{snack}')
                print(f"{player.name} attacks with {player.primary_attack}!")
            elif player.className == "Slayer":
                attack = Attack("Shizuka", 25)
                print(f"{player.name} attacks with {player.primary_attack}!")
        elif choice == "2":
            if player.className == "Warrior":
                attack = Attack("Headstrong", 25)
                print(f'{ability_whirlwing}')
                print(f"{player.name} attacks with {player.secondary_attack}!")
            elif player.className == "Mage":
                attack = Attack("Expelliarmus", 25)
                print(f'{ability_expelliarmus}')
                print(f"{player.name} attacks with {player.secondary_attack}!")
            elif player.className == "Slayer":
                attack = Attack("Starburst Stream", 25)
                print(f'{ability_starburst}')
                print(f"{player.name} attacks with {player.secondary_attack}!")
        else:
            print("Invalid choice. Try again.")
            continue
        
        enemy.hp -= attack.damage
        print(f"{enemy.name} takes {attack.damage} damage. Enemy HP: {enemy.hp}")

        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            break

        print(f"\n{enemy.name}'s turn:")
        enemy_attack = random.choice([enemy.attack1, enemy.attack2])
        print(f"{enemy.name} attacks with {enemy_attack.name}!")
        player.hp -= enemy_attack.damage
        print(f"{player.name} takes {enemy_attack.damage} damage. Player HP: {player.hp}")

        if player.hp <= 0:
            print(f"{player.name} has been defeated!")
            break

    print("Battle ends!")
    import postbattle


enemy = Enemy("Blood Magic Queen", 150, Attack("Fireball", 10), Attack("Lightning Strike", 15))
battle(player, enemy)