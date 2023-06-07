from PyInquirer import prompt, style_from_dict, Token
from art import guild_art, slayer_weapon, warrior_weapon, mage_weapon, forest_gate

custom_styles = style_from_dict(
    {
        Token.Separator: "#6C6C6C",
        Token.QuestionMark: "#78350f bold",
        Token.Selected: "#fafaf9",
        Token.Pointer: "#d9480f bold",
        Token.Instructions: "",
        Token.Answer: "#005f00",
        Token.Question: "#005f00",
    }
)


name_question = [
    {
        'type': 'input',
        'name': 'name',
        'message': 
        f"\nHello there! \nI see you are a little lost young traveler. \nFear not, I am Greem, the greatest guide this city has to offer. \nWhat is your name?",
    },
]


name_answer = prompt(name_question, style=custom_styles)
name = name_answer['name']

introduction_questions = [
    {
        'type': 'input',
        'name': 'follow me',
        'message': f"\n{name}, you look quite strong I must say, would you care to follow me to the guild?\nPress enter to follow Greem..."
    },
]

introduction_answer = prompt(introduction_questions)


guild_questions = [
    {
        'type': 'input',
        'name': 'welcome',
        'message': f"\n{guild_art}\nWelcome to the guild of METSYS! \nWe fuel the fire in young and aspiring adventurers across the land. \nTo get you started, please head over to the registration booth to file a class \nPress enter to continue..."
    },
    {
        'type': 'input',
        'name': 'base_stats',
        'message': "\nIt looks like you have already received some training, your base stats are quite developed. \n Hp: 10 \n Strength: 10 \n Speed: 10 \n Agility: 10 \n Intelligence: 10 \n Vitality: 10 \n Xp: 0 \n Press enter to continue..."
    },
    {
        'type': 'list',
        'name': 'class',
        'message': f"\nPicking a class is a vital point in an adventurer's journey. It will allow you to harness your potential and focus on the stats you wish to develop.\nPlease choose which path you will follow in your endeavors.\nSlayer: {slayer_weapon} \nWarrior: {warrior_weapon} \nMage: {mage_weapon}",
        'choices': ["Slayer", "Warrior", "Mage"]
    },
    {
        'type': 'list',
        'name': 'weapon',
        'message': "\nA wise choice indeed. \nThese lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Slayer selection.",
        'when': lambda answers: answers['class'] == 'Slayer',
        'choices': ['Enma', 'Zangetsu', 'Demon Dwellers']
    },
    {

        'type': 'list',
        'name': 'weapon',
        'message': "\nA wise choice indeed. \nThese lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Warrior selection.",
        'when': lambda answers: answers['class'] == 'Warrior',
        'choices': ['Excalibur', 'Dragon Slayer', 'Rune 2h Sword']
    },
    {
        
        'type': 'list',
        'name': 'weapon',
        'message': "\nA wise choice indeed. \nThese lands are crawling with dangerous monsters and I would hope to see you again. \nPlease choose a weapon from our Mage selection.",
        'when': lambda answers: answers['class'] == 'Mage',
        'choices': ['Wizard Staff', 'The Elder Wand', 'Energy Sword']
    }
]

guild_answers = prompt(guild_questions)
player_choice = guild_answers['class']
weapon = guild_answers['weapon']



goodbye_questions = [

    {
        'type': 'input',
        'name': 'selected',
        'message': f"\nFor a {player_choice} such as yourself, {weapon} is a great choice. \n Press enter to continue..."
    },
    {
        'type': 'input',
        'name': 'goodbye',
        'message': f"\nWell then! It was great meeting you {name}. \nIf you head straight down this road you'll arrive at the gates to the forest. \nI wish you great luck in these turbulent lands.\nPress enter to continue..."
    },
    {
        'type': 'input',
        'name': 'gate',
        'message': f"{forest_gate}\nDamn yo, look at these mf gates"
    }
]

goodbye_answers = prompt(goodbye_questions)





