""" This is functions for game Find a number """
import random


def human_finds(x=10):
    step1=0
    thought = random.randint(1, x)
    print("Men 0 dan 10 gacha bo'lgan bitta sonni o'yladim")
    finded_num = int(input("O'ylagan sonimni topishga xarakat qilib ko'ring\n>>>"))
    ifoda = 1
    while ifoda:
        step1 = step1+1
        if thought == finded_num:
            break
        elif finded_num < thought:
            print("Men o'ylagan son bundan kattaroq.")
        elif finded_num > thought:
            print("Men o'ylagan son bundan kichikroq.")
        finded_num = int(input(">>>"))
    print(f"TOPDINGIZ!!!\nMen o'ylagan sonni {step1} urinishda topdingiz")
    return step1
    
    
def pc_finds(y=10):
    x = 1
    thought_num = random.randint(x, y)
    print(f"1 dan {y} gacha bo'lgan sonni o'ylang")
    input("Tayyor bo'lsangiz 'enter' tugmasini bosing")
    answer = input(f"Men o'ylagan son {thought_num}. Agar to'g'ri bo'lsa(T), o'ylagan soningiz kichikroq(-), kattaroq(+)\n>>>")
    step = 1
    while True:
        if answer.lower() == 't':
            break
        elif answer == '+':
            x = thought_num+1
        elif answer == '-':
            y = thought_num-1
        else:
            print("Iltimos aytilgan qiymatlarni kiriting.\nTo'g'ri(T), kichikroq(-), kattaroq(+)")
        thought_num = random.randint(x, y)
        answer = input(f"Men o'ylagan son {thought_num}. Agar to'g'ri bo'lsa(T), kichikroq(-), kattaroq(+)\n>>>")
        step += 1
    print(f"TOPDIM!!!\nMen siz o'ylagan sonni {step} urinishda topdim")
    return step
        
        
        
        
        
        