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

post_battle_loss = [
    {
    'type': 'input',
    'name': 'return',
    'message': f"\n{gnome}\nYOU'VE BEEN GNOMED\nReturn to the System..."
    }
]

post_battle_loss_answers = prompt(post_battle_loss, style = custom_styles)