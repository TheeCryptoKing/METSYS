from PyInquirer import prompt, style_from_dict, Token
from art import *

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

post_battle = [
    {
        'type': 'input',
        'name': 'post battle',
        'message': '\nWow! \nWhat a tough adversary! \nI barely managed to escape with my life!'
    },
    {
        'type': 'input',
        'name': 'drop',
        'message': f"\n{skull_on_fire}\nWhat's this? It appeared on the ground as soon as the battle was finished...."
    },
    {
        'type': 'input',
        'name': 'ending',
        'message': f"\n{illuminati}\nHEAR ME YOUNG TRAVELER! \nI HAVE OBSERVED YOUR BRAVERY AND WILLPOWER FROM AFAR. \nI MUST SAY, YOU SHOW GREAT PROMISE."
    }
]

post_battle_answers = prompt(post_battle, style=custom_styles)
