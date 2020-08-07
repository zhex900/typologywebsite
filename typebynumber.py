import random

p_type_n = [0, 1, 2, 3, 
            4, 5, 6, 7, 
            8, 9, 10, 11,
            12, 13, 14, 15]

cols = [[0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15]]
rows = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]] 

init = cols[2] + cols[3]
resp = cols[0] + cols[1]

dire = cols[0] + cols[2]
info = cols[1] + cols[3]

cont = cols[1] + cols[2]
move = cols[0] + cols[3]

abst = rows[0] + rows[1]
conc = rows[2] + rows[3]

affl = rows[1] + rows[2]
prag = rows[0] + rows[3]

syst = rows[0] + rows[2]
intr = rows[1] + rows[3]

tife = [1, 3, 4, 6, 9, 11, 12, 14]
fite = [0, 2, 5, 7, 8, 10, 13, 15]

sine = [1, 3, 5, 7] + rows[2]
nise = [0, 2, 4, 6] + rows[3]

type_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dichotomy_list = [[init, resp], [dire, info], [cont, move], [abst, conc], [affl, prag], [syst, intr], [tife, fite], [sine, nise]]

#a simple function to create a list responsible for accuracy(chance = accuracy(9, 10) will have an accuracy of 9/10)
def accuracy(correct, total):
    return [[0 for i in range(correct)] + [1 for i in range(total - correct)], [1 for i in range(correct)] + [0 for i in range(total - correct)]]

# This function simulates CSJ's current method of typing through his test,
# where the user is only allowed to select dichotomies not excluded
# by previously answered questions.
def find_type_by_deduction(ptype, remaining_types, dichotomy_list):
    remaining_dichotomies = [i for i in dichotomy_list]
    #the code within the while statement repeats until a single type has been deduced
    while len(remaining_types) > 1:
        #simulate person chosing a dichotomy
        chosen_dichotomy = remaining_dichotomies.pop(random.choice(list(range(len(remaining_dichotomies)))))
        types_to_remove = []
        #apply a 90% chance to getting the dichotomy right (simulating user error) 
        if ptype in chosen_dichotomy[0]:
            types_to_remove = chosen_dichotomy[random.choice(chance[1])]
        elif ptype in chosen_dichotomy[1]:
            types_to_remove = chosen_dichotomy[random.choice(chance[0])]
        #remove all types that are not in the chosen dichotomy from the running
        remaining_types = [i for i in remaining_types if i not in types_to_remove]
        #remove any redundant dichotomies
        dichotomies_to_remove = []
        for item in remaining_dichotomies:
            #if none of the remaining types are in item[0] or in item[1], remove that item from the remaining dichotomies
            if not any([i in remaining_types for i in item[0]]) or not any([i in remaining_types for i in item[1]]):
                dichotomies_to_remove.append(item)
        for item in dichotomies_to_remove:
            remaining_dichotomies.remove(item)
    return remaining_types[0]

def get_colrow_chance(lst, a, b, c):
    output = 0
    if lst[0:2] == [a,b]:
        output += 1
    if lst[1:3] == [b,c]:
        output += 1
    if [lst[0], lst[2]] == [a,c]:
        output += 1
    return output

# This function simulates an alternative method of typing through a test,
# where the user selects all dichotomies before the result is produced.
def find_type_by_tally(ptype, dichotomy_list):
    tally_list = [0 for i in range(16)]
    
    correct_lstcoldichs = []
    lstcoldichs = [] #short for list of column dychotomies
    for i in range(3):
        if ptype in dichotomy_list[i][0]:
            lstcoldichs.append(random.choice(chance[0]))
            correct_lstcoldichs.append(0)
        if ptype in dichotomy_list[i][1]:
            lstcoldichs.append(random.choice(chance[1]))
            correct_lstcoldichs.append(1) 
    if lstcoldichs != correct_lstcoldichs:
        shuffled_count_to_three = [i for i in range(3)]
        random.shuffle(shuffled_count_to_three)
        if random.choice(chance[1]) == 1:
            for i in shuffled_count_to_three:
                if lstcoldichs[i] != correct_lstcoldichs[i]:
                    lstcoldichs[i] = abs(lstcoldichs[i] - 1)
        else:
            lstcoldichs[shuffled_count_to_three[0]] = abs(lstcoldichs[shuffled_count_to_three[0]] - 1)
    col_chances = [0, 0, 0, 0]
    col_chances[0] = get_colrow_chance(lstcoldichs, 1, 0, 1)
    col_chances[1] = get_colrow_chance(lstcoldichs, 1, 1, 0)
    col_chances[2] = get_colrow_chance(lstcoldichs, 0, 0, 0)
    col_chances[3] = get_colrow_chance(lstcoldichs, 0, 1, 1)
    for i in range(4):
        for j in cols[i]:
            tally_list[j] += col_chances[i]
    
    correct_lstrowdichs = []
    lstrowdichs = [] #short for list of row dychotomies
    for i in range(3):
        if ptype in dichotomy_list[i + 3][0]:
            lstrowdichs.append(random.choice(chance[0]))
            correct_lstrowdichs.append(0)
        if ptype in dichotomy_list[i + 3][1]:
            lstrowdichs.append(random.choice(chance[1]))
            correct_lstrowdichs.append(1)
    if lstrowdichs != correct_lstrowdichs: 
        shuffled_count_to_three = [i for i in range(3)]
        random.shuffle(shuffled_count_to_three)
        if random.choice(chance[1]) == 1:
            for i in shuffled_count_to_three:
                if lstrowdichs[i] != correct_lstrowdichs[i]:
                    lstrowdichs[i] = abs(lstrowdichs[i] - 1)
        else:
            lstrowdichs[shuffled_count_to_three[0]] = abs(lstrowdichs[shuffled_count_to_three[0]] - 1) 
    row_chances = [0, 0, 0, 0]
    row_chances[0] = get_colrow_chance(lstrowdichs, 0, 1, 0)
    row_chances[1] = get_colrow_chance(lstrowdichs, 0, 0, 1)
    row_chances[2] = get_colrow_chance(lstrowdichs, 1, 0, 0)
    row_chances[3] = get_colrow_chance(lstrowdichs, 1, 1, 1)
    for i in range(4):
        for j in rows[i]:
            tally_list[j] += row_chances[i]
    """
    if ptype in dichotomy_list[6][0] and random.choice(chance[1]) == 1:
        for i in dichotomy_list[6][0]:
            tally_list[i] += 1
    else:
        for i in dichotomy_list[6][1]:
            tally_list[i] += 1
    if ptype in dichotomy_list[7][0] and random.choice(chance[1]) == 1:
        for i in dichotomy_list[7][0]:
            tally_list[i] += 1
    else:
        for i in dichotomy_list[7][1]:
            tally_list[i] += 1
    """
    greatest_value = max(tally_list)
    if tally_list.count(greatest_value) == 1:
        return tally_list.index(greatest_value)
    else:
        return 16

chance = accuracy(9, 10)
num_correct_ded = []
for i in range(1000):
    ptype = random.choice(type_list)
    found_type = find_type_by_deduction(ptype, type_list, dichotomy_list)
    if found_type == ptype:
        num_correct_ded.append(1)

num_correct_tal = []
for i in range(1000):
    ptype = random.choice(type_list)
    found_type = find_type_by_tally(ptype, dichotomy_list)
    #print(found_type)
    if found_type == ptype:
        num_correct_tal.append(1)

print(sum(num_correct_tal))
print(sum(num_correct_ded))