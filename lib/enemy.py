pass
# Journal
# Need to get current locatin to connect player id
# Need to get Foreign key's to work properly 
# connect ability and connect world to current player
# unusre if the if condition for __name__ is needed will check later
# need a selectedclass, currentlocation, currentabilities, 
# Created Class id for player to grab with input 

# Need to do
# need to link current_player = current_location  
# need to also link current_player to current_abilities
# need to have it persist in db

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
