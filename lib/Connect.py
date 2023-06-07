from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session
import ipdb
from player import *

engine = create_engine("sqlite:///game.db", echo=True)
Base.metadata.create_all(engine)

# seed.py
# to check engine successfully created
# with engine.connect() as connection:
#     result = connection.execute(text('select "Were in buisness"'))
#     print(result.all())

if __name__ == '__main__':
    session = Session(bind=engine)
    session.query(Player).delete()
    session.query(Location).delete()
    session.query(Enemy).delete()
    session.query(Abilities).delete()
    session.commit()
    
    
    def declare_locations():
        Home = Location(name="Home")
        Guild = Location(name="Guild")
        FF = Location(name="Fairy Forest")
        session.add_all([Home,Guild,FF])
        session.commit()
        
    ability_declare = [
        Abilities(name="Shizuka"),
        Abilities(name="Starburst Stream"),
        Abilities(name="Whirlwind_Strike"),
        Abilities(name="Headstrong"),
        Abilities(name="Serpentine Slash"),
        Abilities(name="Expelliarmus"),
        # Villians
        Abilities(name="Blood Siphon"),
        Abilities(name="Blood Scypth Swirl"),
        Abilities(name="TigerClaw Slash"),
        Abilities(name="Harpies Song"),
        Abilities(name="MoonBeam"),
        Abilities(name="Blood Shard Barrage"),
        Abilities(name="Lightning Strike"),
        Abilities(name="Fireball")
    ]
    session.bulk_save_objects(ability_declare)
    session.commit()
    
    def declare_player():
    # exisits but no column player.location
    # MVP = Str, Spe, hp, xp, Weapon
        Slayer = Player(
                        name="Slayer",
                        # primary_attack=1,
                        # secondary_attack=2,
                        location_id=1,
                        Strength=10,
                        Speed=15,
                        Weapon="Dual Katanas",
                        hp=80, 
                        intellect=0,
                        xp=0
                        )
        Warrior = Player(
                        name="Warrior",
                        # primary_attack=3,
                        # secondary_attack=4,
                        location_id=1,
                        Strength=15,
                        Speed=10,
                        Weapon="Champions Broadsword", 
                        hp=80, 
                        intellect=0,
                        xp=0
                        )
        Mage = Player(
                    name="Mage", 
                    # primary_attack=5,
                    # secondary_attack=6,
                    location_id=1, 
                    Strength=15, 
                    Speed=10, 
                    Weapon="Surasshu", 
                    hp=80, 
                    intellect=15,
                    xp=0
                    )
        session.add_all([Slayer , Warrior, Mage])
        session.commit()


    def declare_FF_enemy():
    # MVP = hp, xp_given, intellect, speed, strength, weapon, BOSS_FF and Fairies
    # exisits but no column for enemy.location
        # ENEMY order name, location_id, location, primary_attack, secondary_attack, hp, xp_given, intellect, speed, strength, weapon
        BOSS_FF = Enemy(
            name="Blood Magic Queen",
            location_id=3,
            # primary_attack=7,
            # secondary_attack=8,
            hp=40, 
            xp_given=30,
            intellect=50,
            speed=25,
            strength=25,
            weapon="Blood Scythe"
            ) 
        Harpies = Enemy(
            name="TigerClaw Harpy",
            location_id=3,
            # primary_attack=9,
            # secondary_attack=10,
            hp=20,
            xp_given=20,
            intellect=20,
            speed=20,
            strength=20,
            weapon="TigerClaws"
            )
        Fairies = Enemy(
            name="Blood Magic Fairy",
            location_id=3,
            # primary_attack=11,
            # secondary_attack=12,
            hp=10,
            xp_given=10,
            intellect=18,
            speed=15,
            strength=15,
            weapon="Bood Magic"
            ) 
        Witchs = Enemy(
            name="Dark Witch",
            location_id=3,
            # primary_attack=13,
            # secondary_attack=14,
            hp=15,
            xp_given=15,
            intellect=15,
            speed=15,
            strength=15,
            weapon="Witch Wand"
            )
        session.add_all([BOSS_FF, Harpies, Fairies, Witchs])
        session.commit()

    
    declare_locations()
    declare_player()
    declare_FF_enemy()

    
    # place inside cli.py
    # player_choice = input("Choose a player (Slayer, Mage, Warrior): ") 
    # if current_player:
    #     print("Current Player:", current_player.name)
    # else:
    #     print("Invalid input.")
    
    # test data
    player_choice= "Mage"
    player_location= "Home"
    
    # CURRENT PLAYER
    current_player = session.scalars(select(Player).where(Player.name.like(player_choice))).first()
    
    # CURRENT LOCATION
    current_location = session.scalars(select(Location).where(Location.name.like(player_location))).first()
    
    # join function for PLAYER and ABILITIES 
    # DEFINED BY PLAYER.ID
    # dem_hero_attack1 = session.scalars(
    #     select(Player, Abilities).join(Player.primary_attack)
    # )
    # dem_hero_attack2 = session.scalars(
    #     select(Player, Abilities).join(Player.secondary_attack)
    # )
    # # test data for PLAYER ABILITIES 
    # for player in dem_hero_attack1:
    #     print(f"{player.name} | {player.primary_attack}")
    # for player in dem_hero_attack2:
    #     print(f"{player.name} | {player.secondary_attack}")
        

    # # join function for ENEMY and ABILITIES
    # # DEFINED BY ENEMY.ID
    # dem_enemy_attack1 = session.scalars(
    #     select(Enemy, Abilities).join(Enemy.primary_attack)
    # )
    # dem_enemy_attack2 = session.scalars(
    #     select(Enemy, Abilities).join(Enemy.secondary_attack)
    # )
    # test data for ENEMY ABILITIES
    # for enemy in dem_enemy_attack1:
    #     print(f"{enemy.name} | {enemy.primary_attack}")
    # for enemy in dem_enemy_attack1:
    #     print(f"{enemy.name} | {enemy.secondary_attack}")

    # CURRENT ENEMY LOCATION 
    Evil_peoples_hood = session.scalars(
        select(Enemy, Location).join(Enemy.location)
    )
    # test data for function 
    for enemy in Evil_peoples_hood:
        print(f"{enemy.name} | {enemy.location.name}")
    
    # CURRENT PLAYER LOCATION  
    where_you_at = session.scalars(
        select(Player, Location).join(Player.location)
    )
    # test data for function 
    for player in where_you_at:
        if current_player.name == player.name:
            print(f"{player.name} | {player.location.name}")
            
    ipdb.set_trace()
    session.close()
    # put ipdb where i want to play with it



