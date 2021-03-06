from itertools import combinations, groupby
from typing import Collection
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions
import random
import pprint

# Encoding that will store all of your constraints
E = Encoding()

rows = 3
columns = 7
games = []
@proposition(E)
class game:
    def __init__(self,team1,team2):
        self.t1 = team1
        self.t2 = team2
    
    def team1(self):
        return self.t1
    def team2(self):
        return self.t2

    def __repr__(self) -> str:
        return f"{self.t1 + 1} vs {self.t2 + 1}"

@proposition(E)
class day:
    def __init__(self,g1,g2,g3,day_num):
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        self.day_num = day_num
    
    def game1(self):
        if self.g1 == None:
            return game(9,9)
        else:
            return self.g1

    def game2(self):
        if self.g2 == None:
            return game(9,9)
        else:
            return self.g2

    def game3(self):
        if self.g3 == None:
            return game(9,9)
        else:
            return self.g3
    def day(self):
        return self.day_num

    def __repr__(self) -> str:
        return f"Day{self.day_num + 1}: Game 1 = {self.g1}, Game 2 = {self.g2}, Game 3 = {self.g3} \n"

#weekp stands for week proposition
@proposition(E)
class weekp:
    def __init__(self,days, week_num):
        self.da = days
        self.week_n = week_num

    def days(self):
        return self.da
    
    def week_num(self):
        return self.week_n

    def __repr__(self) -> str:
        return f"Week{self.week_n + 1}:\n {self.da}"
#makes a list of every game tat needs to be played
for i in range(8):
    for j in range(8):
        if i != j:
            for k in range(4):
                games.append(game(i,j))

#checks that there is no common team between games                      
def no_same_team(g1, g2):

        if(isinstance(g2, int) or g2 == None or g1 == None):
            return True
        
        if(g1.team1() != g2.team1() and g1.team2() != g2.team1() and g1.team1() != g2.team2() and g1.team2() != g2.team2()):
            return True

        else:
            return False
#Gets a list of common teams between games
def day_has_same_team(d1,d2):
    teams1 = [d1.game1().team1(), d1.game1().team2(), d1.game2().team1(), d1.game2().team2(), d1.game3().team1(), d1.game3().team2()]
    teams2 = [d2.game1().team1(), d2.game1().team2(), d2.game2().team1(), d2.game2().team2(), d2.game3().team1(), d2.game3().team2()]
    same = []
    for x in teams1:
        for y in teams2:
            if(x != 9 and x==y):
                same.append(x)
    
    return same
#Checks days to see if they do not contain a same team
def All_games_filled(day):
    if(day.game2().team1() != 9 and day.game3().team1() != 9):
        teams = []
        teams.append(day.game1().team1())
        teams.append(day.game1().team2())
        teams.append(day.game2().team1())
        teams.append(day.game2().team2())
        teams.append(day.game3().team1())
        teams.append(day.game3().team2())
        if(len(teams) == len(set(teams))):
            return True
        else:
              return False  
    elif(day.game2().team1 != 9 and day.game3().team1 == 9):
        teams = []
        teams.append(day.game1().team1())
        teams.append(day.game1().team2())
        teams.append(day.game2().team1())
        teams.append(day.game2().team2())
        if(len(teams) == len(set(teams))):
            return True
        else:
              return False  
    elif(day.game2().team1() == 9 and day.game3().team1 != 9):
        teams = []
        teams.append(day.game1().team1())
        teams.append(day.game1().team2())
        teams.append(day.game3().team1())
        teams.append(day.game3().team2())
        if(len(teams) == len(set(teams))):
            return True
        else:
              return False  
    else:
        return True
#makes a week, because it randomly makes a schedule weeks, 14,15,16 often do not satisfy the constraints
def make_week(t):
    #set up varriables
    week = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    days = []
    temp = []
    counter = [0,0,0,0,0,0,0,0]
    #get a pool of games for the week
    #if last week just put the last games in
    if t == 15:
        temp = games.copy()
        games.clear()
    #Due to chance the last three weeks may not have enough of certain games to make a working week
    elif t == 14 or t == 13:
        for z in range(14):
            selection = random.choice(games)
            temp.append(selection)
            games.remove(selection)
    #randomly pulls games to fill up a week, does not add games if there are more than 4 of a team already in the week
    else:
        while len(temp) != 10:
            selection = random.choice(games)
            t1 = selection.team1()
            t2 = selection.team2()
            if(counter[t1] != 3 and counter[t2] != 3):
                temp.append(selection)
                games.remove(selection)
                counter[t1] += 1
                counter[t2] += 1
        if t < 8:
            i = 0
            while len(temp) != 14  and i < len(games):
                selection = games[i]
                t1 = selection.team1()
                t2 = selection.team2()
                if(counter[t1] != 4 and counter[t2] != 4):
                    temp.append(selection)
                    games.remove(selection)
                    counter[t1] += 1
                    counter[t2] += 1
                i += 1
        else:
            i = len(games) - 1
            while len(temp) != 14 and i > 0:
                selection = games[i]
                t1 = selection.team1()
                t2 = selection.team2()
                if(counter[t1] != 4 and counter[t2] != 4):
                    temp.append(selection)
                    games.remove(selection)
                    counter[t1] += 1
                    counter[t2] += 1
                i -= 1
        
        if len(temp) < 14:
            selection = random.choice(games)
            temp.append(selection)
            games.remove(selection)
            
    #Put a game in each day
    for x in range(columns):
        selection = random.choice(temp)
        week[0][x] = selection
        temp.remove(selection)
        
    #place the 7 extra games
    while len(temp) != 0:
        test = len(temp)
        for x in range(columns):
            if(isinstance(week[1][x], int) and no_same_team(temp[0], week[0][x])):
                week[1][x] = temp[0]
                temp.remove(temp[0])
                break
        if(len(temp) == test):
            for x in range(columns):
                if(isinstance(week[2][x], int) and no_same_team(temp[0], week[0][x]) and no_same_team(temp[0], week[1][x])):
                  week[2][x] = temp[0]
                  temp.remove(temp[0])
                  break
        if(len(temp) == test):
            for x in range(columns):
                if(isinstance(week[2][x], int)):
                  week[2][x] = temp[0]
                  temp.remove(temp[0])
                  break
        
            
    #Adds the games to the proper days
    current_day = 0
    for x in range(columns):
        if(isinstance(week[1][x], int)):
            if(isinstance(week[2][x], int)):
                days.append(day(week[0][x],None,None,current_day))
            else:
                days.append(day(week[0][x],None,week[2][x],current_day))
        elif(isinstance(week[2][x], int)):
            days.append(day(week[0][x],week[1][x],None,current_day))
        else:
            days.append(day(week[0][x],week[1][x],week[2][x],current_day))
        current_day += 1
    #checks if the days work
    for d in days:
        if All_games_filled(d):
            E.add_constraint(d)
        else:
           E.add_constraint(~d)
    return weekp(days,t)
#checks to see how many arangments a week can have with the given days
def week_solver(week):
    #setup for each week solutions
    li = week.days()
    H = Encoding()
    @proposition(H)
    class day2:
        def __init__(self,position,D):
            self.day = D
            self.pos = position
        def D(self):
            return self.day
        def poistion(self):
            return self.pos

        def __repr__(self) -> str:
            return f"\nDay {self.pos} = Old Day {self.day.day()}"
    
    #gest a list of all positions and days combinations
    combos = []
    for x in range(7):
        for d in li:
            combos.append(day2(x,d))
    

    #can only play 2 days in a row
    #check postion 0, if 0 and 1 not 2
    for x in range (0,7):
            for y in range (7, 14):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(14,21):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
    #check postion 1, if 1 and 2 not 0 or 3
    for x in range (7,14):
            for y in range (14, 21):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(21,28):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
                    for z in range(0,7):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
    #check postion 2, if 2 and 3 not 1 or 4
    for x in range (14,21):
            for y in range (21, 28):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(28,35):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
                    for z in range(7,14):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
    #check postion 3, if 3 and 4 not 2 or 5
    for x in range (21,28):
            for y in range (28, 35):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(35,42):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
                    for z in range(14,21):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
    #check postion 4, if 4 and 5 not 3 or 6
    for x in range (28,35):
            for y in range (35, 42):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(42,49):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
                    for z in range(21,28):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])
    #check postion 5, if 5 and 6 not 4
    for x in range (35,42):
            for y in range (42, 49):
                a = day_has_same_team(combos[x].D(), combos[y].D())
                if a != []:
                    for z in range(28,35):
                        b = day_has_same_team(combos[z].D(), combos[y].D())
                        for i in a:
                            for j in b:
                                if i == j:
                                    H.add_constraint( (combos[x] & combos[y]) >> ~combos[z])

    # can only have one day in each position
    constraint.add_exactly_one(H, combos[0],combos[1],combos[2],combos[3],combos[4],combos[5],combos[6])
    constraint.add_exactly_one(H, combos[7],combos[8],combos[9],combos[10],combos[11],combos[12],combos[13])
    constraint.add_exactly_one(H, combos[14],combos[15],combos[16],combos[17],combos[18],combos[19],combos[20])
    constraint.add_exactly_one(H, combos[21],combos[22],combos[23],combos[24],combos[25],combos[26],combos[27])
    constraint.add_exactly_one(H, combos[28],combos[29],combos[30],combos[31],combos[32],combos[33],combos[34])
    constraint.add_exactly_one(H, combos[35],combos[36],combos[37],combos[38],combos[39],combos[40],combos[41])
    constraint.add_exactly_one(H, combos[42],combos[43],combos[44],combos[45],combos[46],combos[47],combos[48])
    
    #can only have one of each day
    constraint.add_exactly_one(H, combos[0],combos[7],combos[14],combos[21],combos[28],combos[35],combos[42])
    constraint.add_exactly_one(H, combos[1],combos[8],combos[15],combos[22],combos[29],combos[36],combos[43])
    constraint.add_exactly_one(H, combos[2],combos[9],combos[16],combos[23],combos[30],combos[37],combos[44])
    constraint.add_exactly_one(H, combos[3],combos[10],combos[17],combos[24],combos[31],combos[38],combos[45])
    constraint.add_exactly_one(H, combos[4],combos[11],combos[18],combos[25],combos[32],combos[39],combos[46])
    constraint.add_exactly_one(H, combos[5],combos[12],combos[19],combos[26],combos[33],combos[40],combos[47])
    constraint.add_exactly_one(H, combos[6],combos[13],combos[20],combos[27],combos[34],combos[41],combos[48])
    return H.compile()



if __name__ == "__main__":

    #make a schedule of 16 weeks
    sch = []
    for x in range(16):
        sch.append(make_week(x))

    # print the weeks and how many solutions they have
    for i in sch:
       print(i,"\n")
       A = week_solver(i)
       print("week Solutions: %s" % count_solutions(A))

    T = E.compile()
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))

