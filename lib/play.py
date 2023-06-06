from pyfiglet import Figlet
from termcolor import colored


print('\n'*10)
f = Figlet(font='poison')
print(colored(f.renderText('METSYS'),'green'))
print('\n'*5)
print('\t\t press enter to begin your adventure')
ch = input('')
if ch == '':
    print('\n'*17)
    print(r"""
         ^  ^  ^   ^      ___I_      ^  ^   ^  ^  ^   ^  ^
        /|\/|\/|\ /|\    /\-_--\    /|\/|\ /|\/|\/|\ /|\/|\
        /|\/|\/|\ /|\   /  \_-__\   /|\/|\ /|\/|\/|\ /|\/|\
        /|\/|\/|\ /|\   |[]| [] |   /|\/|\ /|\/|\/|\ /|\/|\
    """)
    print('\n'*1)
    import questions
    
  


