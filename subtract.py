import os
os.system('cls')

player_number = int(input("Base number?: "))
player_number1 = int(input("Subtrahend?: "))
def calculate_player_number(base, multiplier):
    result = base - multiplier
    return result
print(calculate_player_number(player_number, player_number1))
