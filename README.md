## <img src=lib/imgs/option-2.png>

---

# Game Description

A CLI App RPG where you must beat the system and conquer a world trying to conquer you. Your character is a stranger in a universe filled with Fairies and potentialy more....... You must Pick a Class to determine the type of Warrior you want to be. You are unfamiliar of this world but you cannot put your tongue on why exactly. Their is a lingering essence of something Dark. You will Travel to Fairy Forest and Battle Blood Fairies and Blood Witches only for them to lead you to a Their Blood Fairy Queen and reveal a Skull of truth which is one of 3 Skulls in exsistence, that apparently are a key for something very Ancient...... You will travel cross different areas in the map Fairy Forest, Orc Mountain, and Demon Dungeon and see if you are strong enough to conquer all those who oppose you and your search for truth.  Forge your path. Slay the villians. Claim the Skull of Truth. Conquer this World. Beat The System.

# STEPS TO PLAY

- Fork and git clone this repository into your local machine.
- Please open your CLI (Preferrably VSC)
- Open your Terminal and follow along

<h1> Install </h1>
Type Into Terminal:

1. pipenv install
2. pipenv install sqlalchemy
3. pipenv install PyInquirer
4. pipenv install prompt_toolkit==1.0.14
5. pipenv install pyfiglet
6. pipenv install termcolor
7. pipenv shell

<h1>Run The Game</h1>
Type Into the Terminal:
- cd lib
- python play.py

<h1>TroubleShooting</h1>
<p>
###AFTER INSTALLING ALL FILES####<br>
If game.db not loading data Follow these steps:<br>

delete:<br>
ALL FILES INSIDE migrations, <br>
ALL pycache, <br>
and ALL DBS(INSIDE AND OUTSIDE LIB)<br>

<h4>In Terminal:</h4>
open METSYS<br>
</p>

<h4>inside METSYS folder/Repo Run Commands in order:</h4>
<!-- 1.pip uninstall prompt toolkit <br>
2.pip install prompt_toolkit==1.0.14<br> -->
3.alembic upgrade head<br>
4.alembic revision --autogenerate -m "Repairing Db"<br>
5.cd inside lib<br>
5.alembic upgrade head<br>
6.$python lib/Connect.py<br>
7.$python play.py
Should be All Good :)
</p>

## $${\color{green} Enjoy The Experience! }$$
