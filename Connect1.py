from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from lib.player import *

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
    # def delete_data():
    #     session.query(Player).delete()
    #     session.query(Enemy).delete()
    #     session.commit()

    # def declare_player():
    # MVP = Str, Spe, hp, xp, Weapon
    Slayer = Player(name="Slayer", Strength=10, Speed=15, Weapon="Dual Katanas", hp=80, xp=0)
    Warrior = Player(name="Warrior", Strength=15, Speed=10, Weapon="Champions Broadsword", hp=80, xp=0)
    Mage = Player(name="Mage", Strength=15, Speed=10, Weapon="Surasshu", hp=80, xp=0)
    session.add_all([Slayer , Warrior, Mage])
    session.commit()

    # def declare_FF_enemy():
    # # MVP = hp, xp_given, intellect, speed, strength, weapon
    #     BOSS_FF = Enemy(name="Blood Magic Queen", hp=40, xp_given=30, intellect=50, speed=25, strength=25, weapon="Blood Scythe") 
    #     Harpies = Enemy(name="TigerClaw Harpy", hp=20, xp_given=20, intellect=20, speed=20, strength=20, weapon="TigerClaws")
    #     Fairies = Enemy(name="Blood Magic Fairy", hp=10, xp_given=10, intellect=18, speed=15, strength=15, weapon="Bood Magic") 
    #     Witch = Enemy(name="Dark Witch", hp=15, xp_given=15, intellect=15, speed=15, strength=15, weapon="Witch Wand")
    #     session.add_all([BOSS_FF, Harpies, Fairies, Witch])
    #     session.commit()


    # def declare_locations():
    #     Home = Location(name="Home")
    #     Guild = Location(name="Guild")
    #     FF = Location(name="Fairy Forest")
    #     session.add_all([Home,Guild,FF])
    #     session.commit()

    # def ability_declare():
    #     Slayer = session.query(Player).filter_by(name="Slayer").first()
    #     Slayer.abilities = [
    #         Abilities(ability_name="Shizuka"),
    #         Abilities(ability_name="Starburst Stream")
    #     ]
    #     Warrior = session.query(Player).filter_by(name="Warrior").first()
    #     Warrior.abilities = [
    #         Abilities(ability_name="Whirlwind Strike"),
    #         Abilities(ability_name="Headstrong")
    #     ]
    #     Mage = session.query(Player).filter_by(name="Mage").first()
    #     Mage.abilities =  [
    #         Abilities(ability_name="Serpentine Slash"),
    #         Abilities(ability_name="Expelliarmus")
    #     ]
    #     session.add_all([Slayer.abilities, Warrior.abilities, Mage.abilities])
    #     session.commit()
    

    # delete_data()
    # declare_player()
    # declare_FF_enemy()
    # declare_locations()
    # ability_declare()


    session.close()



