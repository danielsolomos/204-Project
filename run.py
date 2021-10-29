
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

import pprint


# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

@proposition(E)
class TeamNumber:

    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f"Team.{self.name},{self.num}"

@proposition(E)
class GameLocation:
    def __init__(self,loc,num) -> None:
        self.loc = loc
        self.num = num

    def __repr__(self) -> str:
        return f"GameLocation.{self.loc},{self.num}"
    
@proposition(E)
class Game:
    def __init__(self, date, team1, team2) -> None:
        self.date = date
        self.team1 = team1
        self.team2 = team2
    
    def __repr__(self) -> str:
        return f"Game.{self.date},{self.team1},{self.team2}"

    width = int(14)
    height = int(3)
    grid = []
    i = int(0)
    for i in range(width):
        grid.append(" ")
    for i in range(height):
        grid.append(" ")
        
@proposition(E)
class Day:
    def __init__(self, day) -> None:
        self.day = day
        
    def __repr__(self) -> str:
        return f"Day.{self.date}"

@proposition(E)
class Team:
    def __init__(self, location, teamNum, teamName) -> None:
        self.location = location
        self.teamNum = teamNum
        self.teamName = teamName
        #teamName is used so when we display the schedule, it displays the team name rather than the number
        
     def __repr__(self) -> str:
        return f"Team.{self.location}, {self.teamNum}, {self.teamName}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)


T1 = Team(input(), 1)
T2 = Team(input(), 2) 
T3 = Team(input(), 3)
T4 = Team(input(), 4)
T5 = Team(input(), 5)
T6 = Team(input(), 6)
T7 = Team(input(), 7)
T8 = Team(input(), 8)

# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
     
    #this constraint makes sure every day has a game, with an away team and a home team
    list week = []
    for y in range(grid):
        x = 0
       week.add(grid[0][y])
    for i in week:
        if (week[i]==null):
            week.remove(week[i])
    if week(length == 14)
        E.add_constraint(grid[0][0] && grid[0][1] && grid[0][2] && grid[0][3] && grid[0][4] && grid[0][5] && grid[0][6] && grid[0][7] && grid[0][8] && grid[0][9]
                         && grid[0][10] && grid[0][11] && grid[0][12] && grid[0][13])
    
    #this constraint checks the grid to make sure that a team cannot play itself and that one team is home and another is away for every game
    for row in grid:
        for column in grid:
            column [0] != column[1]
            column [2] != column[3]
            column [4] != column[5]
            column [6] != column[7]
            column [8] != column[9]
            column [10] != column[11]
            column [12] != column[13]
            constraint.add_exactly_one(E, grid[x,y])
    
    #this constraint checks to make sure a team cannot play a game three days in a row
    for row in grid:
        for column in grid:
            for i in range(13):
                if (i%2==0):
                    if (column[i]==column[i+2]or column[i]==column[i+3]):
                        E.add_constraint(column [i]~ column [i+4] && column[i]~column[i+5])
                else:
                    if(column[i]==column[i+1] or column[i]==column[i+2]):
                        E.add_constraint(column[i]~column[i+3] && column[i]~column[i+4]

    #this constraint checks the grid of games, and creates a new list to track the home and away games
    #The loop then runs through the grid, and if the team has a home game, it would set that teams
    #location on the list to true. There are 16 elements in the list, one for each team to have a home and away
    #when the loop finds the team's game, it sets it to true whether or not it is home or away. 
    list week = []
        for y in range(16):
            x = 0
           week.add(grid[0][y])
        for i in week:
            if (week[i]==null):
                week.remove(week[i])
    for row in grid:
        for column in grid:
            counter = 0:
            for i in range(16):
                if (i%2==0):
                    week[column[i]]=True
                else:
                    week[column[i]+1]=True
    for i in week:
        if(week[i]==True):
            E.add_exactly_one(E,*week)
    
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()
