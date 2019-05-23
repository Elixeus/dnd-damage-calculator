def avg_damage(ac, n_d6, prof, mod, base_damage):
    '''ac: Armor Class
n_d6: number of d6 dice for rogue's sneak attack
prof: proficiency bonus, starts with +2 and gets larger as levels go up
mod: dexerity modifier (+3 in my case)
base_damage: base damage of the weapon (my rapier and longbow both do 1d8 base damage so 8 for me)
    '''
    ac *= 1.0
    prof *= 1.0
    mod *= 1.0
    reg_to_hit = 1 - (ac - prof - mod) / 20
    adv_to_hit = 1 - (1 - reg_to_hit)**2

    longbow_extra_to_hit = 1 - (ac - prof - mod + 5) / 20  # d20 - 5 to take the +10 extra damage
    longbow_extra_to_hit_adv = 1 - (1 - longbow_extra_to_hit) ** 2

    reg_damage = (base_damage + 1.0)/2 + 3.5 * n_d6 + mod
    extra_longbow_damage = (base_damage + 1.0) / 2 + 3.5 * n_d6 + mod + 10

    avg_reg_damage = reg_to_hit * reg_damage
    avg_adv_damage = adv_to_hit * reg_damage
    
    avg_2_attacks_1_adv = reg_to_hit*adv_to_hit * 2 * reg_damage
    avg_2_attacks_2_adv = adv_to_hit **2 * 2 * reg_damage

    avg_longbow_extra_damage = longbow_extra_to_hit * extra_longbow_damage
    avg_longbow_extra_damage_adv = longbow_extra_to_hit_adv * extra_longbow_damage
    print('average regular damage: {}'.format(avg_reg_damage))
    print('average damage w/ advantage: {}'.format(avg_adv_damage))
    print('average 2 attacks (1 advantage) damage: {}'.format(avg_2_attacks_1_adv))
    print('average 2 attacks (2 advantage) damage: {}'.format(avg_2_attacks_2_adv))
    print('average longbow extra damage: {}'.format(avg_longbow_extra_damage))
    print('average longbow extra damage w/ advantage: {}'.format(avg_longbow_extra_damage_adv))
