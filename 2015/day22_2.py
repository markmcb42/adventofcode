import sys

def get_next_action(actions):
    action_str = 'MDSPR'
    tmp = actions[::-1]
    allr = True
    for a in tmp:
        if a != 'R':
            allr = False
    if allr:
        return ['M'] * (len(tmp) + 1)

    for i in range(len(tmp)):
        if tmp[i] == 'R':
            tmp[i] = 'M'
        else:
            pos = action_str.find(tmp[i])
            tmp[i] = action_str[pos+1]
            break

    return tmp[::-1]

def valid_action(action):

    action_str = ''.join(action)
    pos = action_str.find('S')
    prev = 0
    while pos != -1:
        prev = pos
        pos = action_str.find('S', pos+1)
        if pos != -1 and abs(pos - prev) < 5:
            return False

    pos = action_str.find('R')
    prev = 0
    while pos != -1:
        prev = pos
        pos = action_str.find('R', pos+1)
        if pos != -1 and abs(pos - prev) < 4:
            return False

    pos = action_str.find('P')
    prev = 0
    while pos != -1:
        prev = pos
        pos = action_str.find('P', pos+1)
        if pos != -1 and abs(pos - prev) < 5:
            return False

    return True

def sim(actions, part):
    boss_hp, boss_dmg = 71, 10
    #boss_hp, boss_dmg = 55, 8
    hp, mana, armor = 50, 500, 0
    turn, turn_c = 0, 0
    mana_spent = 0
    poison_left, shield_left, recharge_left = 0, 0, 0
    my_turn = 1
    spell_cost = {'M': 53, 'D': 73, 'S': 113, 'P': 173, 'R': 229}
    
    while True:
        if len(actions)-1 < turn_c:
            print('out of moves')
            return 0
        if poison_left:
            poison_left = max(poison_left - 1, 0)
            boss_hp -= 3
        if shield_left:
            shield_left = max(shield_left - 1, 0)
            armor = 7
        else:
            armor = 0        
        if recharge_left:
            recharge_left = max(recharge_left - 1, 0)
            mana += 101
        if my_turn == 1:
            if part == 2:
                hp -= 1
                if hp <= 0:
                    return 0
            action = actions[turn_c]
            mana -= spell_cost[action]
            mana_spent += spell_cost[action]
            if action == 'M':
                boss_hp -= 4
            elif action == 'D':
                boss_hp -= 2
                hp += 2
            elif action == 'S':
                if shield_left:
                    #print('Double Shield')
                    return 0
                shield_left = 6
            elif action == 'P':
                if poison_left:
                    #print('Double poison')
                    return 0
                poison_left = 6
            elif action == 'R':
                if recharge_left:
                    #print('Double recharge')
                    return 0
                recharge_left = 5
            if mana < 0:
                return 0
        if boss_hp <= 0:
            return mana_spent
        if my_turn == -1:
            hp -= max(boss_dmg - armor, 1)
            if hp <= 0:
                return 0
        if my_turn == 1:
            turn_c += 1
        my_turn = -my_turn
        turn += 1

def iterate_actions(pos):
    actions[pos] = 'DSPRM'['MDSPR'.index(actions[pos])]
    if actions[pos] == 'M':
        if pos+1 <= len(actions):
            iterate_actions(pos+1)

for part in (1, 2):
    if part == 1:
        continue

    #actions = ['M'] * 20
    #actions =['M', 'M', 'M', 'M', 'M', 'M', 'M', 'P', 'M', 'M', 'D', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']
    actions = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'P', 'D', 'D', 'D', 'S', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']
    #while not valid_action(actions):
    #    actions = get_next_action(actions)

    min_spent = 1000000
    for i in range(100000000):
        result = sim(actions, part)
        if result:
            min_spent = min(result, min_spent)
            print(actions)
        #actions = get_next_action(actions)
        #while not valid_action(actions):
         #   actions = get_next_action(actions)
        iterate_actions(0)
    print(min_spent)
