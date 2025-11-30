def print_best_weapon(weapon_list: list):
    best = max(weapon_list, key = lambda x: x[1])
    print(best[0])

weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]
print_best_weapon(meele_weapon)

