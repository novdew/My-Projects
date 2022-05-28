""" This is a main file of game Find a number """

# Importing functions
import functions as fun


# Starting game
print("Keling o'ylagan sonni topish o'ynaymiz")
ifoda=1


# Main code of game
while ifoda:
    pr_steps = fun.human_finds()
    print("\nKeling endi siz o'ylaysiz men topaman")
    pc_steps = fun.pc_finds()
    
    if pr_steps < pc_steps:
        print(f'\nSiz {pr_steps} urinish bilan meni yutdingiz')
    elif pr_steps > pc_steps:
        print(f'\nMen {pc_steps} urinish bilan sizni yutdim')
    elif pr_steps == pc_steps:
        print(f'\nDurrang!\n Ikkalamiz ham {pr_steps} urinishda topdik')
    
    ifoda = int(input("Yana o'ynaymizmi. Ha(1), Yo'q(0)\n>"))

