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

# class Current(Base):
    # id = Column(Integer, primary_key=True)
    # currentClassid = Column(Integer, ForeignKey('current_Player.id'))
    # current_locationid = Column(Integer, ForeignKey('currentlocation.id'))
    # current_name = Column(String(name_Chouce))
    # current_enemy = Coloumn(ForeignKey)
