import random
import time
from pyfiglet import Figlet
from termcolor import colored
from questions import current_player
from art import (ability_whirlwing, snack, ability_starburst, ability_expelliarmus, ability_fireball, ability_lightning, dont_know_what_this_is_but_i_like_it)


class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Enemy:
    def __init__(self, name, hp, attack1, attack2, attack3):
        self.name = name
        self.hp = hp
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

def battle(player, enemy):
    print(f"Player: {player.name} VS Enemy: {enemy.name}")
    print("Battle begins!")

    while player.hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}'s turn:")
        print(f"1. {player.primary_attack}")
        print(f"2. {player.secondary_attack}")
        choice = input("Select an attack: ")

        if choice == "1":
            if current_player.className == "Warrior":
                attack = Attack("Whirlwind Strike", 25)
                print(f'{ability_whirlwing}')
                print(f"{player.name} attacks with {attack.name}!")
            elif current_player.className == "Mage":
                attack = Attack("Serpentine Slash", 25)
                print(f'{snack}')
                print(f"{player.name} attacks with {attack.name}!")
            elif current_player.className == "Slayer":
                attack = Attack("Shizuka", 25)
                print(f"{player.name} attacks with {attack.name}!")
        elif choice == "2":
            if current_player.className == "Warrior":
                attack = Attack("Headstrong", 15)
                print(f'{ability_whirlwing}')
                print(f"{player.name} attacks with {attack.name}!")
            elif current_player.className == "Mage":
                attack = Attack("Expelliarmus", 15)
                print(f'{ability_expelliarmus}')
                print(f"{player.name} attacks with {attack.name}!")
            elif current_player.className == "Slayer":
                attack = Attack("Starburst Stream", 15)
                print(f'{ability_starburst}')
                print(f"{player.name} attacks with {attack.name}!")
        else:
            print("Invalid choice. Try again.")

            continue

        # print(f"{player.name} attacks with Starburst Stream!")
        enemy.hp -= attack.damage
        print(f"{enemy.name} takes {attack.damage} damage. Enemy HP: {enemy.hp}")

        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            print('\n'*10)
            f = Figlet(font='epic')
            print(colored(f.renderText('GOOD SHIT!'),'green'))
            print('\n'*5)
            time.sleep(1)
            break

        print(f"\n{enemy.name}'s turn:")
        time.sleep(1)
        enemy_attack = random.choice([enemy.attack1, enemy.attack2, enemy.attack3])
        if enemy_attack == enemy.attack1:
            print(f"{ability_fireball}")
        elif enemy_attack == enemy.attack2:
            print(f"{ability_lightning}")
        elif enemy_attack == enemy.attack3:
            print(f"{dont_know_what_this_is_but_i_like_it}")
        print(f"{enemy.name} attacks with {enemy_attack.name}!")
        player.hp -= enemy_attack.damage
        print(f"{player.name} takes {enemy_attack.damage} damage. Player HP: {player.hp}")

        if player.hp <= 0:
            print('\n'*10)
            f = Figlet(font='poison')
            print(colored(f.renderText('YOU GOT FUCKED!'),'red'))
            print('\n'*5)
            print(f"{player.name} has been defeated!")
            break

    print("Battle ends!")
    if player.hp <= 0:
        import postbattleloss
    elif player.hp > 0:
        import postbattlevictory

from questions import current_player
player = Player("Slayer", 100)
player = current_player
enemy = Enemy("Blood Fairy", 125, Attack("Fireball", 10), Attack("Lightning Strike", 15), Attack("MoonBlast", 20))
battle(player, enemy)