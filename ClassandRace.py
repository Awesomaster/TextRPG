import random
#Classes and races
print('Here is your raid team. Good luck')
lvl = random.randint(6,95)
for i in range(5):
    health = 0
    coin = 0
    lvl += random.randint(-5,5)
    strength = 0
    luck = 0
    wisdom = 0
    agility = 0

    class_list = ['death knight', 'demon hunter', 'druid', 'hunter', 'mage', 'monk', 'paladin', 'priest', 'rogue', 'shaman', 'warlock', 'warrior']
    race_list = ['human', 'dwarf', 'night elf', 'gnome', 'worgen', 'panderen', 'orc', 'undead', 'tauren', 'troll', 'blood elf', 'goblin']
    # Generic adjectives
    generic_adjective_list = ['heroic', 'masterful', 'old', 'ancient']
    # Class adjectives
    death_knight_adjective_list = ['']
    demon_hunter_adjective_list = ['']
    druid_adjective_list = ['']
    hunter_adjective_list = ['fierce', 'vicious', 'cut-throat']
    mage_adjective_list = ['']
    monk_adjective_list = ['']
    paladin_adjective_list = ['']
    priest_adjective_list = ['']
    rogue_adjective_list = ['sneaky', 'swift', 'shifty', 'silent', 'crafty']
    shaman_adjective_list = ['']
    warlock_adjective_list = ['']
    warrior_adjective_list = ['agressive', 'threatening']
    # Race adjectives
    dwarf_adjective_list = ['short', '']
    night_elf_adjective_list = ['insane', '']
    gnome_adjective_list = ['short', 'miniscule', 'tiny', '']
    panderen_adjective_list = ['peaceful', 'large']
    orc_adjective_list = ['agressive', 'scary', 'threatening']
    undead_adjective_list = ['slow', 'etherial', 'skinless', 'fragile', 'spooky']
    goblin_adjective_list = ['ugly', '']

    # ----------
    # Generic Names
    generic_name_list = ['Helgar']
    # Race Names

    # ----------
    # Generic Titles
    generic_title_list = ['the great', 'the fantabulous', 'the world ender', 'the courageous', 'the weak']
    # Class Titles

    # Race Titles
    drawrf_title_list = ['the iron stomach']



    # ----------
    random.shuffle(class_list)
    random.shuffle(race_list)

    adjective_list = generic_adjective_list
    Race = race_list[0]
    Class = class_list[0]
    if Race == 'human':
        health += random.randint(0,30)
        strength += random.randint(0,5)
        luck += random.randint(0,5)
        wisdom += random.randint(0,5)
        agility += random.randint(0,5)
    elif Race == 'dwarf':
        health += random.randint(20,30)
        strength += 5
        luck += 1
        wisdom += 1
        agility += 1
        for i in dwarf_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'night elf':
        health += random.randint(10,15)
        strength += 1
        luck += 1
        wisdom += 5
        agility += 3
        for i in night_elf_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'gnome':
        health += random.randint(20,25)
        strength += 4
        luck += 2
        wisdom += 1
        agility += 4
        for i in gnome_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'worgen':
        health += random.randint(15,20)
        strength += 4
        luck += 1
        wisdom += 1
        agility += 4
    elif Race == 'panderen':
        health += random.randint(25,35)
        strength += 3
        luck += 3
        wisdom += 4
        agility += 1
        for i in panderen_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'orc':
        health += random.randint(20,35)
        strength += 5
        luck += 1
        wisdom += 1
        agility += 2
        for i in orc_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'undead':
        health += random.randint(10,15)
        strength += 1
        luck += 4
        wisdom += 2
        agility += 3
        for i in undead_adjective_list:
            if i != '':
                adjective_list.append(i)
    elif Race == 'tauren':
        health += random.randint(20,25)
        strength += 3
        luck += 1
        wisdom += 1
        agility += 4
    elif Race == 'troll':
        health += random.randint(25,40)
        strength += 5
        luck += 1
        wisdom += 1
        agility += 1
    elif Race == 'blood elf':
        health += random.randint(5,15)
        strength += 1
        luck += 3
        wisdom += 5
        agility += 3
    elif Race == 'goblin':
        health += random.randint(10,20)
        strength += 2
        luck += 3
        wisdom += 1
        agility += 5
        for i in goblin_adjective_list:
            if i != '':
                adjective_list.append(i)
                
    # -------------------------------------------------------------------

    # MOnk
    # Paladin
    # Priest
    # Rogue
    # Shaman
    # Warlock
    # Warrior
    if Class == 'death knight':
        health += random.randint(20,25)
        strength += 5
        luck += 5
        wisdom += 5
        agility += 5
    elif Class == 'demon hunter':
        health += random.randint(10,15)
        strength += 4
        luck += 2
        wisdom += 3
        agility += 3
    elif Class == 'druid':
        health += random.randint(10,15)
        strength += 4
        luck += 1
        wisdom += 3
        agility += 0
        for i in druid_adjective_list:
            if i != '':
                adjective_list.append(i)
                adjective_list.append(i)
    elif Class == 'hunter':
        health += random.randint(0,5)
        strength += 4
        luck += 1
        wisdom += 1
        agility += 4
        for i in hunter_adjective_list:
            if i != '':
                adjective_list.append(i)
                adjective_list.append(i)
    elif Class == 'mage':
        health += 0
        strength += 0
        luck += 2
        wisdom += 5
        agility += 1
    elif Class == 'monk':
        health += random.randint(0,10)
        strength += 3
        luck += 1
        wisdom += 2
        agility += 5
    elif Class == 'paladin':
        health += random.randint(20,25)
        strength += 5
        luck += 3
        wisdom += 4
        agility += 0
    elif Class == 'priest':
        health += random.randint(0,10)
        strength += 0
        luck += 5
        wisdom += 5
        agility += 1
    elif Class == 'rogue':
        health += 0
        strength += 2
        luck += 2
        wisdom += 3
        agility += 5
        for i in rogue_adjective_list:
            if i != '':
                adjective_list.append(i)
                adjective_list.append(i)
    elif Class == 'shaman':
        health += random.randint(0,10)
        strength += 0
        luck += 2
        wisdom += 4
        agility += 3
    elif Class == 'warlock':
        health += random.randint(0,10)
        strength += 0
        luck += 3
        wisdom += 5
        agility += 2
    elif Class == 'warrior':
        health += random.randint(10,15)
        strength += 5
        luck += 2
        wisdom += 0
        agility += 2
        for i in warrior_adjective_list:
            if i != '':
                adjective_list.append(i)
                adjective_list.append(i)

    random.shuffle(adjective_list)
    Adjective = adjective_list[0]
    if Adjective[0] in 'aeiou':
        Firstword = 'an'
    else:
        Firstword = 'a'

    print('You have', Firstword, Adjective, Race, Class)#, 'named', Name, Title)

    health += random.randint(10,15)
    strength += random.randint(0,2)
    luck += random.randint(0,2)
    wisdom += random.randint(0,2)
    agility += random.randint(0,2)
    print('Level:', str(lvl))
    print('Health:', str(health*10+random.randint(-5,5)))
    print('Strength:', str(int(strength/12*100)))
    print('Wisdom:', str(int(wisdom/12*100)))
    print('Agility:', str(int(agility/12*100)))
    print('Luck:', str(int(luck/12*100)))
    print()
    # adjectives based on stats?
