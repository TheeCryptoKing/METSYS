from PyInquirer import prompt, style_from_dict, Token
from art import (
                guild_art,
                slayer_weapon,
                warrior_weapon,
                mage_weapon,
                forest_gate,
                city_view,
                forest_path,
                pathway_view,
                hello_traveler,
                ominous_tree
                )

from player import *
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///game.db')
Session = sessionmaker(bind=engine)
session = Session()

# MVP
# Tuple needed, ReadMe needed 
# Store db entries in a tuple
# Generates a Pygments style fo reach cn use colors, backgrounds, etc 
# Token class provided, used to define and style different elements in rendered prompts like above
# ListPrompt # ChcekBoxPrompt # RawlistPrompt # ExpandPrompt #

# Still cant get strings to load for me 
selectedClass = None
selectedWeapon = None
selectedEnemy = None

custom_styles = style_from_dict(
    {
        Token.Separator: "#6C6C6C",
        Token.QuestionMark: "#78350F bold",
        Token.Selected: "#FAFAF9",
        Token.Pointer: "#D9480F bold",
        Token.Instructions: "",
        Token.Answer: "#005F00",
        Token.Question: "#005F00",
    }
)
new_page = ('\n' * 1)
name_question = [
    {
        'type': 'input',
        'name': 'name',
        'message': f"{new_page}{hello_traveler} \nHello there young traveler! \nI see you are a little lost in these vast woods. \nFear not, I am Greem, the greatest guide this city has to offer. \nWhat is your name?",
    },
]
name_answer = prompt(name_question, style=custom_styles)
name = name_answer['name']
introduction_questions = [
    {
        'type': 'input',
        'name': 'follow me',
        'message': f"{new_page}{name}, you look quite strong I must say, would you care to follow me to the guild?\nPress enter to follow Greem..."
    },
]
introduction_answer = prompt(introduction_questions, style=custom_styles)
guild_questions = [
    {
        'type': 'input',
        'name': 'welcome',
        'message': f"{new_page}{guild_art}\nWelcome to the guild of METSYS! \nWe fuel the fire in young and aspiring adventurers across the land. \nTo get you started, please head over to the registration booth to file a class \nPress enter to continue..."
    },
    {
        'type': 'input',
        'name': 'base stats',
        'message': f"{new_page}It looks like you have already received some training, your base stats are quite developed. \n Hp: 10 \n Strength: 10 \n Speed: 10 \n Agility: 10 \n Intelligence: 10 \n Vitality: 10 \n Xp: 0 \n Press enter to continue..."
    },
    {
        "type": "list",
        "name": "class",
        "message": f"{new_page}Picking a class is a vital point in an adventurer's journey. \nIt will allow you to harness your potential and focus on the stats you wish to develop\nPlease choose which path you will follow in your endeavors.\nSlayer: {slayer_weapon} \nWarrior: {warrior_weapon} \nMage: {mage_weapon}",
        'choices': ['Slayer', 'Warrior', 'Mage']
    },
    {
        'type': 'list',
        'name': 'weapon',
        'message': f"{new_page}Slayer: {slayer_weapon} \nA wise choice indeed. These lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Slayer selection.",
        'when': lambda answers: answers['class'] == 'Slayer',
        'choices': ['Enma', 'Zangetsu', 'Demon Dwellers']
    },
    {
        'type': 'list',
        'name': 'weapon',
        'message': f"{new_page}Warrior: {warrior_weapon} \nA wise choice indeed. These lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Warrior selection.",
        'when': lambda answers: answers['class'] == 'Warrior',
        'choices': ['Excalibur', 'Dragon Slayer', 'Rune 2h Sword']
    },
    {
        'type': 'list',
        'name': 'weapon',
        'message': f"{new_page}Mage: {mage_weapon} \nA wise choice indeed. These lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Mage selection.",
        'when': lambda answers: answers['class'] == 'Mage',
        'choices': ['Wizard Staff', 'The Elder Wand', 'Energy Sword']
    }
]
guild_answers = prompt(guild_questions, style=custom_styles)
class_choice = guild_answers['class']
weapon = guild_answers['weapon']

goodbye_questions = [
    {
        'type': 'input',
        'name': 'selected',
        'message': f"{new_page}For a {class_choice} such as yourself, {weapon} is a great choice. \n Press enter to continue..."
    },
    {
        'type': 'input',
        'name': 'goodbye',
        'message': f"{new_page}{city_view}\nWell then! It was great meeting you {name}. \nIf you follow these houses and head straight down this road you'll arrive at the gates to the Magic Forest. \nI wish you great luck in these turbulent lands.\nPress enter to continue..."
    },
    {
        'type': 'input',
        'name': 'gate',
        'message': f"{new_page}{forest_gate}\nWow these gates are majestic! The Magic Forest must be beyond here.\nPress enter to venture into the Magic Forest..."
    }
]
goodbye_answers = prompt(goodbye_questions, style=custom_styles)


pathway_questions = [
    {
        'type': 'input',
        'name': 'pathway',
        'message': f"{new_page}{forest_path}\nAhhhh, I'm feeling pretty nervous. I boosted my stats by choosing the {class_choice} class and I got {weapon} from Greem.\nI'm more ready now than I'll ever be..."
    },
    {
        'type': 'input',
        'name': 'view',
        'message': f"{new_page}{pathway_view}\nWow the view from this path is incredible! \nIt seems the magical energy of the fairies inhabiting this land is causing the night sky to by so colorful."
    },
    {
        'type': 'input',
        'name': 'otw battle',
        'message': f"{new_page}{ominous_tree}\nThere is an ominous air around here. \nSomething might be lurking in the shadows by that tree..."
    }
]

pathway_answers = prompt(pathway_questions, style=custom_styles)

pre_battle_blood_fairy = [
    {
        'type': 'input',
        'name': 'seeing monster',
        'message': f"{new_page}Woahhh!!! \nThat's a beast of a monster. \nIt's a Blood Fairy!!!"
    }
]
pre_battle_dark_witch = [
    {
        'type': 'input',
        'name': 'seeing monster',
        'message': f"{new_page}Woahhh!!! \nThat's a beast of a monster. \nIt's a Dark Witch!!!"
    }
]

pre_battle_blood_fairy_answers = prompt(pre_battle_blood_fairy, style=custom_styles)
pre_battle_dark_witch_answers = prompt(pre_battle_dark_witch, style=custom_styles)
