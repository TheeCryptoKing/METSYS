from sqlalchemy import create_engine, text, select
from sqlalchemy.orm import Session
import ipdb
from player import *

# Need a seed.py, a cli.py, a debug.py
engine = create_engine("sqlite:///game.db", echo=True)
Base.metadata.create_all(engine)
# engine successfully created
# with engine.connect() as connection:
#     result = connection.execute(text('select "Were in buisness"'))
#     print(result.all())

if __name__ == '__main__':
    session = Session(bind=engine)
    # location_id? enemy? location? id = no data, xp and hp being rewriten?
    # conditionals for data
    session.query(Player).delete()
    session.query(Location).delete()
    session.query(Enemy).delete()
    session.commit()
    
    def declare_player():
        # can define playerlocation with player.location 
    # MVP = Str, Spe, hp, xp, Weapon
        Slayer = Player(
                        name="Slayer",
                        location_id=1,
                        Strength=10,
                        Speed=15,
                        Weapon="Dual Katanas",
                        hp=80, 
                        xp=0
                        )
        Warrior = Player(
                        name="Warrior",
                        location_id=1,
                        Strength=15,
                        Speed=10,
                        Weapon="Champions Broadsword", 
                        hp=80, 
                        xp=0
                        )
        Mage = Player(
                    name="Mage", 
                    location_id=1, 
                    Strength=15, 
                    Speed=10, 
                    Weapon="Surasshu", 
                    hp=80, 
                    xp=0)
        session.add_all([Slayer , Warrior, Mage])
        session.commit()


    def declare_FF_enemy():
    # MVP = hp, xp_given, intellect, speed, strength, weapon
        BOSS_FF = Enemy(
            name="Blood Magic Queen",
            location_id=3,
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
            hp=10,
            xp_given=10,
            intellect=18,
            speed=15,
            strength=15,
            weapon="Bood Magic"
            ) 
        Witch = Enemy(
            name="Dark Witch",
            location_id=3,
            hp=15,
            xp_given=15,
            intellect=15,
            speed=15,
            strength=15,
            weapon="Witch Wand"
            )
        session.add_all([BOSS_FF, Harpies, Fairies, Witch ])
        session.commit()


    def declare_locations():
        Home = Location(name="Home")
        Guild = Location(name="Guild")
        FF = Location(name="Fairy Forest")
        session.add_all([Home,Guild,FF])
        session.commit()

    def ability_declare():
        Slayer = session.query(Player).filter_by(name="Slayer").first()
        Slayer.abilities = [
            Abilities(ability_name="Shizuka"),
            Abilities(ability_name="Starburst Stream")
        ]
        Warrior = session.query(Player).filter_by(name="Warrior").first()
        # session.bulksaveobjects
        Warrior.abilities = [
            Abilities(ability_name="Whirlwind Strike"),
            Abilities(ability_name="Headstrong")
        ]
        Mage = session.query(Player).filter_by(name="Mage").first()
        Mage.abilities =  [
            Abilities(ability_name="Serpentine Slash"),
            Abilities(ability_name="Expelliarmus")
        ]
        
        
        
        session.bulk_save_objects(Slayer.abilities)
        session.bulk_save_objects(Warrior.abilities)
        session.bulk_save_objects(Mage.abilities)
        # session.bulk_save_objects([Slayer.abilities, Warrior.abilities, Mage.abilities])
        # session.add_all([Slayer.abilities, Warrior.abilities, Mage.abilities])
        session.commit()
    

    # current_location = session.query(Location).filter_by(name="Home").first()
    # current_player = session.query(Player).filter_by(name="Slayer").first()
    # Assign the current_location to the location attribute of the current_player
    # current_player.location = current_location
    # Commit the changes to the session
    # session.commit()
    
    declare_player()
    # declare_FF_enemy()
    declare_locations()
    # ability_declare()
    
    # place inside cli.py
    # player_choice = input("Choose a player (Slayer, Mage, Warrior): ") 
    # if current_player:
    #     print("Current Player:", current_player.name)
    # else:
    #     print("Invalid input.")
    
    # test data
    player_choice= "Mage"
    player_location= "Home"
    
    # grabs current player and player data 
    current_player = session.scalars(select(Player).where(Player.name.like(player_choice))).first()
    current_location = session.scalars(select(Location).where(Location.name.like(player_location))).first()

    # define locations
    # player.location 
    # enemy.location
    
    # Current location based of player 
    where_you_at = session.scalars(
        select(Player, Location).join(Player.location)
    )
    for player in where_you_at:
        if current_player.name == player.name:
            print(f"{player.name} | {player.location.name}")
            
    ipdb.set_trace()
    session.close()
    # put ipdb where i want to play with it



