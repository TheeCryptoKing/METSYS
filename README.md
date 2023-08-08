## <img src=lib/imgs/option-2.png>
# STEPS TO PLAY

- Fork and git clone this repository into your local machine.
- Please open your CLI (Preferrably VSC)
- Open your Terminal and follow along


## Install & Run 
Type Into Terminal:
1. Install Environment 
```
pipenv install
```
2. Enter Shell
```
pipenv shell
```
Type Following Commands in Terminal:
3. Enter lib Folder
```
cd lib
```
4. Run Game
```
python play.py
```

---
# Game Description

A CLI App RPG where you must beat the system and conquer a world trying to conquer you. Your character is a stranger in a universe filled with Fairies and potentialy more....... You must Pick a Class to determine the type of Warrior you want to be. You are unfamiliar of this world but you cannot put your tongue on why exactly. Their is a lingering essence of something Dark. You will Travel to Fairy Forest and Battle Blood Fairies and Blood Witches only for them to lead you to a Their Blood Fairy Queen and reveal a Skull of truth which is one of 3 Skulls in exsistence, that apparently are a key for something very Ancient...... You will travel cross different areas in the map Fairy Forest, Orc Mountain, and Demon Dungeon and see if you are strong enough to conquer all those who oppose you and your search for truth.  Forge your path. Slay the villians. Claim the Skull of Truth. Conquer this World. Beat The System.

# TroubleShooting
If game.db not loading data Follow these steps:<br>
FOLLOW STEPS AFTER INSTALLING ENV ALL FILES<br>
1. Inside VSCode enter explorer, open METSYS, open lib, finally open up migrations<br>
2. DELETE ALL pycache<br>
3. DELETE ALL game.db's<br>
4. go to terminal cd inside METSYS 
### Inside METSYS folder/Repo Run Commands in order:
1. alembic upgrade head<br>
2. alembic revision --autogenerate -m "Repairing Db"<br>
3. alembic upgrade head<br>
4. cd inside lib<br>
5. $python Connect.py<br>
6. $python play.py
   Should be All Good :)

# RoadMap
- Build Tables
   -Characters 
   -Quests
   -Shop 
   -Inventory 
   -Weapons 
   -Guild 
   -Battle 
   -Armor 
   -Companions 
   -Enemeis 
   -Bosses
   -Menu
   -~~Locations~~
   -ABilities 
   -Current_Player

 - Define Battle, Abilites and w/Stats
 - Define Characters/NPC's and Connected Lore
 - Define Inventory and items available
 - Define Guild, Shop, and Quests
 - Enemies dopping gold and Xp
 - Xp system determined and boosting stats  
 - Define Weapons, Armor, Comapnions tables w/Stats
 - Define Bosses and Enemies w/Stats 
 - Define and Build quests and prompts w/Battles and w/Final Boss

 - Functionality Needed For:
 - Current_Player to update all stats and moves based weapons, charms and companions
 - Battle to calculate Attack, work for interacting charms(loading every 3 moves), 
 - Guild shop items delteing after bought 
 - Random Feature for enemies 
 - Quests leading down specfic prompt path 
 - Menu for Attack, Block , Iventory, or Flee in battle, have auto loaded block(based on character Class load) based on Quest 
 - Weapon dropped by enemies and Custom moves with every Weapon 
 - Armor and boosted stats for full set or indivdual pieces TBA 
 - Need 3 skulls for Final Boss 
 - Creat NPC's and Lore building NPC's


 - Second Playthrough Random Bosses and need to Find REDACTED to WIN AND FIND REDACTED
 - All enemies harder and veil lifted with all new enemies
 - Second Playthrough Enemies Table 
 - all Random and Special Guests Battles functionality 
 - Find REDACTED after beating all REDACTED 






## $${\color{green} Enjoy The Experience! }$$
