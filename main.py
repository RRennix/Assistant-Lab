# 1.We will import some modules, keyboard was for a future use, but it's descontinued for now
#import keyboard
import funçoes
# Extra.Just the version, when I write it, it was on alpha 6.1
print('§§§§§LAB a6.2§§§§§')
# 2.A loop function to make it run while the user wants
while True:
    # 3.The magic it's here, the prompt, the command, the input
    a = input('Digite algo:')
    # 4. If you don't want to play, there is the exit door
    if 'sair' in a:
        break
    # 6.else, there is the real work that we saw in funçoes.py
    else:
        funçoes.search(a)
        funçoes.open(a)
        