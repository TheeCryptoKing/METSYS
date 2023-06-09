from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session
# import ipdb
from player import *

engine = create_engine("sqlite:///game.db", echo=True)
Base.metadata.create_all(engine)

# seed.py
# to check engine successfully created
# with engine.connect() as connection:
#     result = connection.execute(text('select "Were in buisness"'))
#     print(result.all())

################DEFINE ENGINE AND PARAMETERS##################
if __name__ == '__main__':
    session = Session(bind=engine)
    session.query(Player).delete()
    session.query(Location).delete()
    session.query(Enemy).delete()
    session.query(Abilities).delete()
    session.commit()
   
    ####################DECLARE LOCATIONS##################
    def declare_locations():
        Home = Location(name="Home")
        Guild = Location(name="Guild")
        FF = Location(name="Fairy Forest")
        session.add_all([Home,Guild,FF])
        session.commit()
   
    #####################DECLARE ABILITIES####################
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
   
    #########################DECLARE PLAYERS#####################
    def declare_player():
    # exisits but no column player.location
    # MVP = Str, Spe, hp, xp, Weapon
        Slayer = Player(
                        className="Slayer",
                        location_id=1,
                        primary_attack=1,
                        secondary_attack=2,
                        Strength=10,
                        Speed=15,
                        Weapon="Dual Katanas",
                        hp=80,
                        intellect=0,
                        xp=0
                        )
        Warrior = Player(
                        className="Warrior",
                        location_id=1,
                        primary_attack=3,
                        secondary_attack=4,
                        Strength=15,
                        Speed=10,
                        Weapon="Champions Broadsword",
                        hp=80,
                        intellect=0,
                        xp=0
                        )
        Mage = Player(
                    className="Mage",
                    location_id=1,
                    primary_attack=5,
                    secondary_attack=6,
                    Strength=15,
                    Speed=10,
                    Weapon="Surasshu",
                    hp=80,
                    intellect=15,
                    xp=0
                    )
        session.add_all([Slayer , Warrior, Mage])
        session.commit()

##########################DECLARE FAIRY FOREST ENEMIES################
    def declare_FF_enemy():
    # MVP = hp, xp_given, intellect, speed, strength, weapon, BOSS_FF and Fairies
    # exisits but no column for enemy.location
        # ENEMY order name, location_id, location, primary_attack, secondary_attack, hp, xp_given, intellect, speed, strength, weapon
        BOSS_FF = Enemy(
            name="Blood Magic Queen",
            location_id=3,
            _primary_attack_=7,
            _secondary_attack_=8,
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
            _primary_attack_=9,
            _secondary_attack_=10,
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
            _primary_attack_=11,
            _secondary_attack_=12,
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
            _primary_attack_=13,
            _secondary_attack_=14,
            hp=15,
            xp_given=15,
            intellect=15,
            speed=15,
            strength=15,
            weapon="Witch Wand"
            )
        session.add_all([BOSS_FF, Harpies, Fairies, Witchs])
        session.commit()

##################INVOKE FUNCTIONS################
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
    # player_choice= "Mage"
    # player_location= "Home"
    # Opps_be_buggin= "Blood Magic Fairy"
   
    player_choice= None,
    player_location= None,
    Opps_be_buggin = None
   
    ################## CURRENT PLAYER ####################
    # FOR PLAYER INPUT #
    # current_player = session.scalars(select(Player).where(Player.className.like(player_choice))).first()
    # if current_player:
    #     print("Current Player:", current_player.name)
    # else:
    #     print("Invalid input.")
    ################### CURRENT LOCATION #####################
    # FOR PLAYER INPUT #
    current_location = session.scalars(select(Location).where(Location.name.like(player_location))).first()
   
    #################### CURRENT ENEMY ########################
    current_enemy = session.scalars(select(Enemy).where(Enemy.name.like(Opps_be_buggin)))
    if current_enemy:
        print("Current Enemy", current_enemy.name)
    else:
        print("Invalid input.")
       
   
    ###################### JOIN PLAYER & ABILITIES ########################
    dem_hero_attackOne = session.scalars(
        select(Player, Abilities).join(Player.attack1)
    )
    dem_hero_attackTwo = session.scalars(
        select(Player, Abilities).join(Player.attack2)
    )
    # # test data for PLAYER ABILITIES
    # for hero in dem_hero_attackOne:
    #     print(f"{hero.name} | {hero.attack1.name}")
    # for hero in dem_hero_attackTwo:
    #     print(f"{hero.name} | {hero.attack2.name}")
       

    ################### JOIN ENEMY & ABILITES ##########################
    dem_enemy_attack1 = session.scalars(
        select(Enemy, Abilities).join(Enemy.attack3)
    )
    dem_enemy_attack2 = session.scalars(
        select(Enemy, Abilities).join(Enemy.attack4)
    )
    # # test data for ENEMY ABILITIES
    # for enemy in dem_enemy_attack1:
    #     print(f"{enemy.name} | {enemy.attack1.name}")
    # for enemy in dem_enemy_attack1:
    #     print(f"{enemy.name} | {enemy.attack2.name}")

    ############################# CURRENT ENEMY LOCATION ####################
    Evil_peoples_hood = session.scalars(
        select(Enemy, Location).join(Enemy.location)
    )
    # test data for function
    for enemy in Evil_peoples_hood:
        # if current_enemy2.name == enemy.name:
            print(f"{enemy.name} | {enemy.location.name}")
   
    ############################### CURRENT PLAYER LOCATION #################
    where_you_at = session.scalars(
        select(Player, Location).join(Player.location)
    )
    # test data for function
    for player in where_you_at:
        # if current_player.className == player.className:
            print(f"{player.className} | {player.location.name}")
           

    session.close()

