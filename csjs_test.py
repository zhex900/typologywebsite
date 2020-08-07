import random

ptypes = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
ptype = ptypes[0]

pos = [1,1,1,1,1,1,1,1,1,0]
neg = [0,0,0,0,0,0,0,0,0,1]

averagesumlist = []
def deduce_dichotomy(ptype, typel, dichotomy_list):
    chosen_dichotomy = dichotomy_list.pop(random.choice(list(range(len(dichotomy_list)))))
    print(chosen_dichotomy)
    print(dichotomy_list)
    types_to_pop = []
    if chosen_dichotomy == 0:
        #initiating vs responding
        if ptype[0] == 'E':
            init_res = random.choice(pos)
        else:
            init_res = random.choice(neg)
        for i in list(range(len(typel))):
            print(i)
            if (init_res == 1 and not typel[i][0] == 'E') or (init_res == 0 and typel[i][0] == 'E'):
                types_to_pop.append(i)
    if chosen_dichotomy == 1:
        #direct vs informative
        if (ptype[1] == 'N' and ptype[3] == 'J') or (ptype[1:3] == 'ST'):
            dir_inf = random.choice(pos)
        else:
            dir_inf = random.choice(neg)
        for i in list(range(len(typel))):
            if (dir_inf == 1 and not ((typel[i][1] == 'N' and typel[i][3] == 'J') or (typel[i][1:3] == 'ST'))) or (dir_inf == 0 and ((typel[i][1] == 'N' and typel[i][3] == 'J') or (typel[i][1:3] == 'ST'))):
                types_to_pop.append(i) 
    if chosen_dichotomy == 2:
        #control vs movement
        if (ptype[0:2] == 'IN' and ptype[3] == 'P') or (ptype[0:2] == 'EN' and ptype[3] == 'J') or ptype[0:3] == 'ISF' or ptype[0:3] == 'EST':
            cont_move = random.choice(pos)
        else:
            cont_move = random.choice(neg)
        for i in list(range(len(typel))):
            if (cont_move == 1 and not ((typel[i][0:2] == 'IN' and typel[i][3] == 'P') or (typel[i][0:2] == 'EN' and typel[i][3] == 'J') or typel[i][0:3] == 'ISF' or typel[i][0:3] == 'EST')) or (cont_move == 0 and ((typel[i][0:2] == 'IN' and typel[i][3] == 'P') or (typel[i][0:2] == 'EN' and typel[i][3] == 'J') or typel[i][0:3] == 'ISF' or typel[i][0:3] == 'EST')):
                types_to_pop.append(i)
    if chosen_dichotomy == 3:
        #abstract vs concrete
        if ptype[1] == 'N':
            abs_con = random.choice(pos)
        else:
            abs_con = random.choice(neg)
        for i in list(range(len(typel))):
            if (abs_con == 1 and not (typel[i][1] == 'N')) or (abs_con == 0 and (typel[i][1] == 'N')):
                types_to_pop.append(i)
    if chosen_dichotomy == 4:
        #affiliative vs pragmatic
        if ptype[1:3] == 'NF' or (ptype[1] == 'S' and ptype[3] == 'J'):
            aff_prag = random.choice(pos)
        else:
            aff_prag = random.choice(neg)
        for i in list(range(len(typel)-1)):
            if (aff_prag == 1 and not (typel[i][1:3] == 'NF' or (typel[i][1] == 'S' and typel[i][3] == 'J'))) or (aff_prag == 0 and (typel[i][1:3] == 'NF' or (typel[i][1] == 'S' and typel[i][3] == 'J'))):
                types_to_pop.append(i)
    if chosen_dichotomy == 5:
        #systematic vs interest
        if ptype[1:3] == 'NT' or (ptype[1] == 'S' and ptype[3] == 'J'):
            syst_int = random.choice(pos)
        else:
            syst_int = random.choice(neg)
        for i in list(range(len(typel))):
            if (syst_int == 1 and not (typel[i][1:3] == 'NT' or (typel[i][1] == 'S' and typel[i][3] == 'J'))) or (syst_int == 0 and (typel[i][1:3] == 'NT' or (typel[i][1] == 'S' and typel[i][3] == 'J'))):
                types_to_pop.append(i)
    if chosen_dichotomy == 6:
        #tife vs fite
        if ptype[2:] == 'TP' or ptype[2:] == 'FJ':
            tife_fite = random.choice(pos)
        else:
            tife_fite = random.choice(neg)
        for i in list(range(len(typel))):
            if (tife_fite == 1 and not (typel[i][2:] == 'TP' or typel[i][2:] == 'FJ')) or (tife_fite == 0 and (typel[i][2:] == 'TP' or typel[i][2:] == 'FJ')):
                types_to_pop.append(i)
    if chosen_dichotomy == 7:
        #sine vs nise
        if (ptype[1] == 'N' and ptype[3] == 'P') or (ptype[1] == 'S' and ptype[3] == 'J'):
            sine_nise = random.choice(pos)
        else:
            sine_nise = random.choice(neg)
        for i in list(range(len(typel))):
            if (sine_nise == 1 and not ((typel[i][1] == 'N' and typel[i][3] == 'P') or (typel[i][1] == 'S' and typel[i][3] == 'J'))) or (sine_nise == 0 and ((typel[i][1] == 'N' and typel[i][3] == 'P') or (typel[i][1] == 'S' and typel[i][3] == 'J'))):
                types_to_pop.append(i)
    types_to_pop.reverse()
    for i in types_to_pop:
        typel.pop(i)
    print(typel)
    print(dichotomy_list)
    return typel, dichotomy_list

def get_multipliers(input):
    multiplier_one = input + 0.5
    multiplier_two = 2 - multiplier_one
    return multiplier_one, multiplier_two

ptypelist = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
dichotomies = [0,1,2,3,4,5,6,7]
while len(ptypelist) > 1:
    ptypelist, dichotomies = deduce_dichotomy(ptype, ptypelist, dichotomies)
    #remove dichotomies that do not effect 
    

print(ptypelist[0])
"""
for thing  in range(100):
    correct = 0
    for iteration in range(1000):
        ptypelist = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
        dichotomies = [0,1,2,3,4,5,6,7]
        while len(ptypelist) > 1:
            ptypelist, dichotomies = deduce_dichotomy(ptype, ptypelist, dichotomies)
        
        if ptypelist[0] == ptype:
            correct += 1
    print(correct)
    averagesumlist.append(correct)

average = sum(averagesumlist) / 100
print(average)
"""