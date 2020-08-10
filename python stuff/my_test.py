import random

ptypes = ['INTJ', 'INTP', 'ENTJ', 'ENTP', 'INFJ', 'INFP', 'ENFJ', 'ENFP', 'ISTJ', 'ISFJ', 'ESTJ', 'ESFJ', 'ISTP', 'ISFP', 'ESTP', 'ESFP']
ptype = ptypes[0]

pos = [1,1,1,1,1,1,1,1,1,0]
neg = [0,0,0,0,0,0,0,0,0,1]

averagesumlist = []
for thing  in range(100):
    correct = 0
    for iteration in range(10):
        #initiating vs responding
        if ptype[0] == 'E':
            init_res = random.choice(pos)
        else:
            init_res = random.choice(neg)
        #direct vs informative
        if (ptype[1] == 'N' and ptype[3] == 'J') or (ptype[1:3] == 'ST'):
            dir_inf = random.choice(pos)
        else:
            dir_inf = random.choice(neg)
        #control vs movement
        if (ptype[0:2] == 'IN' and ptype[3] == 'P') or (ptype[0:2] == 'EN' and ptype[3] == 'J') or ptype[0:3] == 'ISF' or ptype[0:3] == 'EST':
            cont_move = random.choice(pos)
        else:
            cont_move = random.choice(neg)
        #abstract vs concrete
        if ptype[1] == 'N':
            abs_con = random.choice(pos)
        else:
            abs_con = random.choice(neg)
        #affiliative vs pragmatic
        if ptype[1:3] == 'NF' or (ptype[1] == 'S' and ptype[3] == 'J'):
            aff_prag = random.choice(pos)
        else:
            aff_prag = random.choice(neg)
        #systematic vs interest
        if ptype[1:3] == 'NT' or (ptype[1] == 'S' and ptype[3] == 'J'):
            syst_int = random.choice(pos)
        else:
            syst_int = random.choice(neg)
        #tife vs fite
        if ptype[2:] == 'TP' or ptype[2:] == 'FJ':
            tife_fite = random.choice(pos)
        else:
            tife_fite = random.choice(neg)
        #sine vs nise
        if (ptype[1] == 'N' and ptype[3] == 'P') or (ptype[1] == 'S' and ptype[3] == 'J'):
            sine_nise = random.choice(pos)
        else:
            sine_nise = random.choice(neg)

        def get_multipliers(input):
            multiplier_one = input + 0.5
            multiplier_two = 2 - multiplier_one
            return multiplier_one, multiplier_two

        initiating, responding = get_multipliers(init_res)
        direct, informative = get_multipliers(dir_inf)
        control, movement = get_multipliers(cont_move)
        abstract, concrete = get_multipliers(abs_con)
        affiliative, pragmatic = get_multipliers(aff_prag)
        systematic, interest = get_multipliers(syst_int)
        tife, fite = get_multipliers(tife_fite)
        sine, nise = get_multipliers(sine_nise)

        type_grid = [ [ 1 for i in range(4) ] for j in range(4) ]
        #print(type_grid)

        for x in range(0,4):
            for y in range(0,4):
                #multiply initiating/responding
                if x <= 1:
                    type_grid[x][y] = type_grid[x][y] * responding
                else:
                    type_grid[x][y] = type_grid[x][y] * initiating
                #multiply direct/informative
                if x == 0 or x == 2:
                    type_grid[x][y] = type_grid[x][y] * direct
                else:
                    type_grid[x][y] = type_grid[x][y] * informative
                #multiply control/movement
                if x == 1 or x == 2:
                    type_grid[x][y] = type_grid[x][y] * control
                else:
                    type_grid[x][y] = type_grid[x][y] * movement
                #multiply abstract/concrete
                if y >= 2:
                    type_grid[x][y] = type_grid[x][y] * abstract
                else:
                    type_grid[x][y] = type_grid[x][y] * concrete
                #multiply affiliative/pragmatic
                if y == 1 or y == 2:
                    type_grid[x][y] = type_grid[x][y] * affiliative
                else:
                    type_grid[x][y] = type_grid[x][y] * pragmatic
                #multiply systematic/interest
                if y == 1 or y == 3:
                    type_grid[x][y] = type_grid[x][y] * systematic
                else:
                    type_grid[x][y] = type_grid[x][y] * interest
                #multiply tife/fite
                if ((y == 0 or y == 2) and (x == 0 or x == 2)) or ((y == 1 or y == 3) and (x == 1 or x == 3)):
                    type_grid[x][y] = type_grid[x][y] * tife 
                else:
                    type_grid[x][y] = type_grid[x][y] * fite
                #multiply sine/nise
                if  (y >= 2 and (x == 1 or x == 3)) or y == 1:
                    type_grid[x][y] = type_grid[x][y] * sine 
                else:
                    type_grid[x][y] = type_grid[x][y] * nise

        print(ptype)
        for i in [3,2,1,0]:
            for j in [0,1,2,3]:
                print(round(type_grid[j][i], 2), end = "  ")
            print()
        
        if type_grid[0][3] >= 3:
            correct += 1
    #print(correct)
    averagesumlist.append(correct)

average = sum(averagesumlist) / 100
print(average)