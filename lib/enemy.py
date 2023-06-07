pass
# Kwame's Journal 

# Currently Done 
# Location Table
# currentplayer to currentlocation


# Need to Finish
# Player Table W/ ABilities
# Enemy Table W/ Abilities
# Ability Table
# Cli prompts and imput specification 
# Save functionality? 

# 2 ways to grab data eithe rmake all numbered pairs and connect to id can do with prim and sec being declared
# or down a straight list and grab but if down a straight list i have to call each one individually and connect them to id still 
# would need to rearrange code to define this way?
# which would be easier to grab? 1st can connect to id and hae back populate table even, but have to define

# Writing out functionality for CURRRENT ABILITIES 
# for Player needs to be defined by:
# Selected player
# needs to be back populate player by abilities 
# How should be called? ids both moves
# 
# for enemy needs to be same

# writing functionality for Enemy 

# Need to get current locatin to connect player id
# Need to get Foreign key's to work properly 
# connect ability and connect world to current player
# unusre if the if condition for __name__ is needed will check later
# need a selectedclass, currentlocation, currentabilities, 
# Created Class id for player to grab with input 


# Need a current Enenmy as well
# Define current player class 
# Only need to select ids to connect data 
# needs to grab id to grab data and select data based on input
# needs to have input for activityy and based of where location is Location.name 
# allow player to grab id of said 
# DONE with player_choice

# Define current abilities
# connect id  for player usong a foreign key 
# can just back populate for enemy and player lest get functionality working for player first then impliment 

# define enemy location 
# for MVP fight fairy 
# middle prompt
# fight Blood Queen Fairy

# might need a current table
# Maybe
# win or lose idk 
# what stats do you want with a add stats funtion destermined with a session.add() and session.commit
# retry when die and get upgrade if lose

# End screen when win 


# Learningcode
# 1st lesson
# where_you_at = session.scalars(
#     select(Player, Location).join(Player.location)
# )
    # Output from selct for Sql code SELECT player.id, player.name, player.location_id, player."Strength", player."Speed", player."Weapon", player.hp, player.xp, location.id AS id_1, location.name AS name_1 
    # from player JOIN location ON location.id = player.location_id

# 2nd lesson 
# current_player = session.scalars(select(Player).where(Player.name.like(player_choice))).first()
    # scalars = refrence in a single row
    # line is refrence single row, select form database Player where Player name is like (input provided) and return the first match 

    # next resort fro foreignkey
    # owner = Coloumn(String(), ForeignKey('owners.name'))
    
# 3rd lesson
# back_populates populates and carries data
# the foreignkey is just establishing bidimensional access
# foreignkey var = back_population variable

# Scrapped ideas
    # Slayer.abilities = 1."Shizuka", 2."Starburst Stream"
    # Warrior.abilities = 3. "Whirlwind Strike" , 4."Headstrong"
    # Mage.abilities = 5."Serpentine Slash", 6."Expelliarmus"
    # BOSS_FF.abilities = 7. "Blood Siphon", 8."Blood Scypth Swirl"
    # Harpies.abilities = 9."TigerClaw Slash" , 10. "Harpies Song"
    # Fairies.abilities = 11."MoonBeam" , 12."Blood Shard Barrage"
    # Witchs.abilities = 13. "Lightning Strike", 14."Fireball"
# class Current(Base):
    # id = Column(Integer, primary_key=True)
    # currentClassid = Column(Integer, ForeignKey('current_Player.id'))
    # current_locationid = Column(Integer, ForeignKey('currentlocation.id'))
    # current_name = Column(String(name_Chouce))
    # current_enemy = Coloumn(ForeignKey)

# abilities_id = Column(Integer, ForeignKey('abilities.id'))
# abilities = relationship("Abilities", back_populates='player')

# abilities_id = Column(Integer, ForeignKey('abilities.id'))
# abilities = relationship("Abilities", back_populates='enemy')

    #     Slayer = session.query(Player).filter_by(name="Slayer").first()
    #     Slayer.abilities = [1,2]
    
    #     create link to abilities table join, refrencing list very complicating to retrieve data
    #     Slayer.abilities = [
    #         Abilities(ability_name="Shizuka"),
    #         Abilities(ability_name="Starburst Stream")
    #     ]
    #     Warrior = session.query(Player).filter_by(name="Warrior").first()
    #     # session.bulksaveobjects
    #     Warrior.abilities = [
    #         Abilities(ability_name="Whirlwind Strike"),
    #         Abilities(ability_name="Headstrong")
    #     ]
    #     Mage = session.query(Player).filter_by(name="Mage").first()
    #     Mage.abilities =  [
    #         Abilities(ability_name="Serpentine Slash"),
    #         Abilities(ability_name="Expelliarmus")
    #     ]

        # BOSS_FF = session.query(Enemy).filter_by(name="BOSS_FF").first()
        # BOSS_FF.abilities = [
        #     # blood syphon can take hp from Player
        #     # or MVP just alot of Attack
        #     Abilities(abilities="Blood Siphon"),
        #     Abilities(abilities="Blood Scypth Swirl")
        # ]
        # Harpies = session.query(Enemy).filter_by(name="Mage").first()
        # Harpies.abilities = [
        #     Abilities(abilities="TigerClaw Slash"),
        #     Abilities(abilities="Harpies Song")
        # ]
        # Fairies = session.query(Enemy).filter_by(name="Mage").first()
        # Fairies.abilities = [
        #     Abilities(abilities="MoonBeam"),
        #     Abilities(abilities="Blood Shard Barrage")
        # ]
        # Witch = session.query(Enemy).filter_by(name="Mage").first()
        # Witch.abilities = [
        #     Abilities(abilities="Lightning Strike"),
        #     Abilities(abilities="Fireball")
        # ]
        
    
        # Slayer_2 = Player.Slayer.secondary_attack(name="Starburst Stream"),
        # Warrior_1 = Player.Warrior.primary_attack(name="Whirlwind Strike"),
        # Warrior_2 = Player.Mage.secondary_attack(name="Headstrong"),
        # Boss_FF_1 = Enemy.BOSS_FF.primary_attack(name="Blood Siphon"),
        # Boss_FF_2 = Enemy.BOSS_FF.secondary_attack(name="Blood Scypth Swirl"),
        # Harpies_1 = Enemy.Harpies.primary_attack(name="TigerClaw Slash"),
        # Harpies_2 = Enemy.Harpies.secondary_attack(name="Harpies Song"),
        # Fairies_1 = Enemy.Fairies.primary_attack(name="MoonBeam"),
        # Fairies_2 = Enemy.Fairies.secondary_attack(name="Blood Shard Barrage"),
        # Witchs_1 = Enemy.Witchs.primary_attack(name="Lightning Strike"),
        # Witchs_2 = Enemy.Witchs.secondary_attack(name="Fireball")
        
        #         Slayer = Abilities(
        #     attack1="Shizuka",
        #     attack2="Starburst Stream",
        #     player_id=1,
        #     enemy_id=None)
        # Warrior = Abilities(
        #     attack1="Whirlwind Strike", 
        #     attack2="Headstrong",
        #     player_id=2,
        #     enemy_id=None)
        # Mage = Abilities(
        #     attack1="Serpentine Slash",
        #     attack2="Expelliarmus",
        #     player_id=3,
        #     enemy_id=None)
        
        # # Villians
        # Bld_Magic_Queen = Abilities(
        #     attack1="Blood Siphon",
        #     attack2="Blood Scypth Swirl",
        #     player_id=None,
        #     enemy_id=1)
        # Harpies = Abilities(
        #     attack1="TigerClaw Slash",
        #     attack2="Harpies Song",
        #     player_id=None,
        #     enemy_id=2)
        # Fairies = Abilities(
        #     attack1="MoonBeam",
        #     attack2="Blood Shard Barrage",
        #     player_id=None,
        #     enemy_id=3)
        # Witchs = Abilities(
        #     attack1="Lightning Strike",
        #     attack2="Fireball",
        #     player_id=None,
        #     enemy_id=4)
        
        
            # Player class
    # primary_attack = Column(String, ForeignKey('abilities.attack1'))
    # attack1 = relationship("Abilities", back_populates='player')
    # secondary_attack = Column(String, ForeignKey('abilities.attack2'))
    # attack2 = relationship("Abilities", back_populates='player')
    # weapon_ability = Column(String, ForeignKey('abilities.Wability'))
    # companion_ability = Column(String, ForeignKey('abilities.Cability'))
    
        # Enemy class
    # primary_attack = Column(String, ForeignKey('abilities.attack1'))
    # attack1 = relationship("Abilities", back_populates='enemy')
    # secondary_attack = Column(String, ForeignKey('abilities.attack2'))
    # attack2 = relationship("Abilities", back_populates='enemy')
    # weapon_ability = Column(String, ForeignKey('abilities.Wability'))
    # companion_ability = Column(String, ForeignKey('abilities.Cability'))
    
    # Abilities Class
        # attack1 = Column(String, nullable=True)
    # attack2 = Column(String, nullabel=True)
    # Wability = Column(String, default=None)
    # Cability = Column(String, default=None)
    # player_id = Column(Integer, ForeignKey('player.id'), nullable=True)
    # player = relationship("Player", back_populates='abilities')
    # enemy_id = Column(Integer, ForeignKey('enemy.id'), nullable=True)
    # enemy = relationship("Enemy", back_populates='abilities')
    
    # primary_attack=1,
    # secondary_attack=2,
    # to 16
    
        # def ability_declare():
    #     # attributes: prim, sec, name, attack
    #     # Heroes
    #     # Stop over complicating things
    #     Shizuka = Abilities(name="Shizuka"),
    #     Starburst_stream = Abilities(name="Starburst Stream"),
    #     Whirlwind_strike = Abilities(name="Whirlwind_Strike"),
    #     Headstrong = Abilities(name="Headstrong"),
    #     Serpentine_slash = Abilities(name="Serpentine Slash"),
    #     Expelliarmus = Abilities(name="Expelliarmus"),
    #     # Villians
    #     Blood_siphon = Abilities(name="Blood Siphon"),
    #     Blood_scypth_swirl = Abilities(name="Blood Scypth Swirl"),
    #     TigerClaw_slash = Abilities(name="TigerClaw Slash"),
    #     Harpies_song = Abilities(name="Harpies Song"),
    #     Moonbeam = Abilities(name="MoonBeam"),
    #     Blood_shard_barrage = Abilities(name="Blood Shard Barrage"),
    #     Lightning_strike = Abilities(name="Lightning Strike"),
    #     Fireball = Abilities(name="Fireball")

        # session.bulk_save_objects(Shizuka)
        # session.bulk_save_objects(Starburst_stream)
        # session.bulk_save_objects(Whirlwind_strike)
        # session.bulk_save_objects(Headstrong)
        # session.bulk_save_objects(Serpentine_slash)
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.bulk_save_objects([Slayer])
        # session.commit()
        # ability_declare()

    