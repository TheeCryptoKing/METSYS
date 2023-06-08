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


post_battle_victory = [
    {
        'type': 'input',
        'name': 'post battle',
        'message': f"\n{warrior}\nWow! \nWhat a tough adversary! \nI barely managed to escape with my life..."
    },
    {
        'type': 'input',
        'name': 'drop',
        'message': f"\n{skull_on_fire}\n\nWhat's this? It appeared on the ground as soon as the battle was finished...."
    },
    {
        'type': 'input',
        'name': 'descent',
        'message': f"\n{illuminati}\n\nHEAR ME YOUNG TRAVELER! \nI HAVE OBSERVED YOUR BRAVERY AND WILLPOWER FROM AFAR. \nI MUST SAY, YOU SHOW GREAT PROMISE! \nHAVE THIS ENCHANTED FLAMING SKULL! \nONLY BY EMERGING VICTORIOUS AGAINST ADVERSITY HAS IT CHOSEN TO APPEAR BEFORE YOU NOW..."
    },
    {
        'type': 'input',
        'name': 'skull acquired',
        'message': f"\n{gift}\nUhhhh... \nWhat the hell am I supposed to do with it?! \nIt's just a giant skull..."
    },
    {
        'type': 'input',
        'name': 'convo',
        'message': f"\n{illuminati}\nAHHEM... \nAHH OF COURSE! \nHOW COULD I FORGET! \nUHHHHHHH \nyou have to eat it..."
    },
    {
        'type': 'input',
        'name': 'convo2',
        'message': f"\n{warrior}\nYou're joking right?"
    },
    {
        'type': 'input',
        'name': 'convo3',
        'message': f"\n{illuminati}\n..."
    },
    {
        'type': 'input',
        'name': 'convo4',
        'message': f"\n{munch}\nThis tastes like ass..."
    },
    {
        'type': 'input',
        'name': 'effects',
        'message': f"\n{transformation}\nWoah!!! \nWhat's happening?!"
    },
    {
        'type': 'input',
        'name': 'convo5',
        'message': f"\n{illuminati}\nYou are transcending beyond human understanding. \nGoodbye traveler, Congratulations for escaping the METSYS... \nOr should I say the SYSTEM..."
    },
    {
        'type': 'input',
        'name': 'ending',
        'message': f"\n{escape}\nHuh? \nWhat was he talking about? \nSYSTEM? \nWhere did everything go? \nAm I in space? \nWhere the hell am I going?!"
    },
    {
        'type': 'input',
        'name': 'ending',
        'message': f"\n{broke_4th_wall}\nWoah! \nWhat is this place? \nIs this what he meant by 'escaping the SYSTEM'? \nThis must be the real world..."
    }
]

post_battle_victory_answers = prompt(post_battle_victory, style=custom_styles)
