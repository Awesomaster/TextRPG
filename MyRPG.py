import random
import time
import datetime
import scrambler
import os
#import terrain
import pygame

starttime = datetime.datetime.now()
def dateandtime():
    print('Current Time:',datetime.datetime.now())
    
def currenttime():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    print('Current Time:',st)

dateandtime()

items = ''
itemsfile = open(os.path.join('data', 'items.txt'), 'r')
num = len(itemsfile.readlines())
itemsfile = open(os.path.join('data', 'items.txt'), 'r')
for i in range(num):
    items += itemsfile.readline().strip()+' '
itemsfile.close()
name = ''
password = ''
users = []
userdict = {}
userdictlowers = []

# ------------------------ ENTERING THE WORLD ------------------------

def inituserpass():
    userpasser = open(os.path.join('data', 'userpass.txt'), 'r')
    userpass = userpasser.readlines()
    users = []
    userdict = {}
    for i in range(len(userpass)):
        users.append(userpass[i].split())
        userdict[users[i][0]] = users[i][1]
    userpasser.close()
    return userdict

userdict = inituserpass()
userdictlowers = []
for i in userdict.keys():
        userdictlowers.append(i.lower())

while True:
    log = str(input('Are you logging in or creating a new account? (login or create) ')).lower()
    if log == 'login':
        while True:
            name = str(input('What is thine name? '))
            if name in userdict.keys():
                while password == '':
                    password = str(input('What is your password? '))
                    if password == userdict[name]:
                        print('Why hello there', name + '. Welcome back to the world of codeia')
                    else:
                        print('PASSWORD INCORRECT')
                        password = ''
                break
        break

    elif log == 'create':
        while True:
            newname = str(input('What would you like your name to be? '))
            if newname.lower() in userdictlowers:
                print('Sorry that name is already taken :P')
            else:
                break
        newpass = str(input('What would you like your password to be? '))
        create = open('data/userpass.txt', 'a')
        create.write(newname+' '+newpass+' '+'\n')
        create.close()
        userdict = inituserpass()
        save_data = open(os.path.join('userdata', (newname + '.txt')), 'w')
        save_data.write(items)
        save_data.close()
        print('Welcome traveler, to the world of codeia')



# ------------------------ INITIALISING INV ------------------------

char_inv = {}
opening = open(os.path.join('userdata', (name + '.txt')), 'r')
char_data = scrambler.unscramble(opening.readline()).strip().split()
opening.close()

print(char_data)
def initialise_inv(data, output):
    for i in range(len(data)):
        stuff = data[i].split(':')
        if stuff[0] == 'note':
            output[stuff[0]] = str(stuff[1])
        else:
            output[stuff[0]] = int(stuff[1])   

initialise_inv(char_data, char_inv)

def new_char():
    char_inv['hp'] = 50
    char_inv['maxhp'] = 50
    char_inv['lvl'] = 1
    char_inv['coin'] = 100
    char_inv['smldgr'] = 1
    char_inv['new'] = 1
    char_inv['maxxp'] = 100
    char_inv['note'] = 'Empty'

if char_inv['new'] == 0:
    new_char()

# ------------------------ WITHIN THE WORLD ------------------------

gods_list = ['Agron', '']

# Minerals are used to craft items such as swords and armour.
# There will be a second line of the inv for resources, which will have all the minerals and their quantity
mineral_list = ['stone', 'copper', 'iron', 'gold', 'diamond']

# Rarity is inversley propotional to its probibility of showing up
mineral_rarity_dict = {'stone':0.8, 'copper':0.075, 'iron':0.075, 'gold':0.04, 'diamond':0.01}

# 1st element of the value is the items buy price, 2nd is its sell price
mineral_buysell_dict = {'stone':[5, 2], 'copper':[50, 10], 'iron':[50, 10], 'gold':[250, 50], 'diamond':[500, 100]}

forageable_list = ['mushroom', 'berry', 'wood', 'potato', 'lemon', 'carrot', '', '', '']
forageable_rarity_dict = {}

other_list = ['idk']

item_list = ['Greatsword', 'Sword', 'Dagger', 'Spear', 'Shield', 'Staff','Longbow', 'Bow', 'Shortbow', 'Crossbow']

legendary_item_list = ['Burning Talon of Agron']

item_value_dict = {}

def add(item, quantity):
    char_inv[item] += quantity

def remove(item, quantity):
    char_inv[item] -= quantity

def inv():
    for i in char_inv.keys():
        if i == 'new':
            print('Inventory:')
        elif char_inv[i] > 0:
            print(i.upper()+':', char_inv[i])

def mine():
    quantity = random.randint(1,char_inv['luk']+1)
    randlist = []
    for i in range(len(mineral_rarity_dict)):
        mineral = str(list(mineral_rarity_dict.keys())[i])
        randlist += [mineral]*(int(mineral_rarity_dict[mineral]*100))
    mineral = random.choice(randlist)
    add(mineral, quantity)
    if (quantity > 1) and (mineral == diamond):
        print('You mined up '+str(quantity)+' '+mineral+'s')
    else:
        print('You mined up '+str(quantity)+' '+mineral)
    save()
    return

'''
def multimine(n):
    quantity_dict = {'stone':0, 'copper':0, 'iron':0, 'gold':0, 'diamond':0}
    for i in range(n):
        quantity = random.randint(1,char_inv['luk']+1)
        randlist = []
        for i in range(len(mineral_rarity_dict)):
            mineral = str(list(mineral_rarity_dict.keys())[i])
            randlist += [mineral]*(int(mineral_rarity_dict[mineral]*100))
        mineral = random.choice(randlist)
        quantity_dict[mineral] += 1
        add(mineral, quantity)
    line = str('Wow! You mined up '+str(quantity_dict['stone'])+' stone, '+ str(quantity_dict['copper'])+ ' copper, '+ str(quantity_dict['iron'])+ ' iron, '+ str(quantity_dict['gold'])+ ' gold and '+ str(quantity_dict['diamond'])+ ' diamond')
    if quantity_dict['diamond']>1:
        print(line+'s')
    else:
        print(line)
    save()
    return
'''

def chop():
    add('wood', 1)
    save()
    print('Some wood has indeed been chopped by'+name+'.')
    return

def forage():
    return

def fish():
    return

def adv():
    return

def search():
    return

def move(direction, amount):
    return

def sell(item, quantity):
    if char_inv[item] >= quantity:
        if item in mineral_list:
            coinearned = int(mineral_buysell_dict[item][1])*quantity
            add('coin', coinearned)
            remove(item, quantity)
        else:
            #WRITE ELIF CASES
            coin+=0
        print('You sold',str(quantity), item, 'for', str(coinearned)+'.')
    else:
        print('You do not have enough',item+'.')
    save()
    return

def sellall(item):
    quantity = char_inv[item]
    if item in mineral_list:
        coinearned = int(mineral_buysell_dict[item][1])*quantity
        add('coin', coinearned)
        remove(item, quantity)
    else:
        #WRITE ELIF CASES
        coin+=0
    print('You sold all',str(quantity), 'of your', item, 'for', str(coinearned)+'.')
    save()
    return

def buy(item, quantity):
    return

def writenote():
    inp = input('What is your note?')
    char_inv['note'] =  str(inp).replace(' ','~')
    return

def save():
    # Save the characters stats
    char_inv_str = ''
    for i in char_inv:
        char_inv_str += i + ':' + str(char_inv.get(i)) + ' '
    char_inv_str = char_inv_str[0:-1]
    
    char_inv_str = scrambler.scramble(char_inv_str)

    # Save the characters resources
    saveit = open(os.path.join('userdata', (name + '.txt')), 'w')
    saveit.write(char_inv_str)
    saveit.close()

print('Game Saved! You have been playing for', str(datetime.datetime.now()-starttime))
save()
