```python

"""
Name:Ernest Hernandez
Assignment: Test 3 - Final
Date Due: May 10th, 12:00pm
E-Mail: ernest1721@yahoo.com
"""

#Question 1

def dirReduc(l):
    list = l
    start = (0,0)
    path = {"NORTH": (0,1), "SOUTH": (0,-1), "EAST": (1,0), "WEST": (-1, 0),
    "NORTHEAST": (1,1), "NORTHWEST": (-1,1), "SOUTHEAST": (1,-1), "SOUTHWEST": (-1,-1)}
    end = []

    for i in list:
        if i == "NORTH":
            start = (start[0], start[1] + 1)
        elif i == "SOUTH":
            start = (start[0], start[1] - 1)
        elif i == "EAST":
            start = (start[0] + 1, start[1])
        else:
            start = (start[0] - 1, start[1])

    for key in path:
        if start == path[key]:
            end = [key]
    return end


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "EAST"]))

#Question 2

#Link to code this solution is based on
#https://jiaminglin.gitbooks.io/codewars-exercises/content/vasya_-_clerk.html

def tickets(l):
    list = l
    change = [0, 0]

    for i in list:
        if i == 25:
            change[0]+=1
        elif i == 50:
            change[0]-=1
            change[1]+=1
        else:
            if change[0] >= 1 and change[1] >= 1:
                change[0]-=1
                change[1]-=1
            elif change[1] == 0 and change[0] >= 3:
                change[0]-=3
            else:
                change[0]-=3
        if change[0] < 0 or change[1] < 0:
            return 'Not enough change'
    return 'Yes'


print(tickets([25, 25, 50, 100]) )
print(tickets([25, 50, 25, 50, 100]) )

#Question 3
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "[%d,%d]" % (self.x, self.y)
    

class Shape(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Square(Shape):
    """
    Square class inherits from Shape
    Only takes one value for side length
    """
    def __init__(self, p1, p2 = None):
        super(Square, self).__init__(p1, p2 = None)
    
    def area(self):
        return(self.p1 * self.p1)
    
    def perimeter(self):
        return ((self.p1 + self.p1) * 2)

class Rectangle(Shape):
    """
    Rectangle class inherits from Shape
    Takes in two values for length and width
    """
    def __init__(self, p1, p2):
        super(Rectangle, self).__init__(p1, p2)
    
    def area(self):
        return(self.p1 * self.p2)
    
    def perimeter(self):
        return((self.p1 + self.p2) * 2)

class Cube(Square):
    """
    Cube class inherits from Square
    Takes in one value for side length
    """
    def __init__(self, p1, p2 = None):
        super(Cube, self).__init__(p1, p2 = None)
    
    def area(self):
        return(self.p1 * self.p1 * self.p1)
    
    def surfaceArea(self):
        return((self.p1 * self.p1) * 6)
        

aSquare = Square(5)
aRectangle = Rectangle(3,4)
aCube = Cube(5)

print(aSquare.area() )
print(aSquare.perimeter() )

print(aRectangle.area() )
print(aRectangle.perimeter() )

print(aCube.area() )
print(aCube.surfaceArea() )

#Question 4

def dupCount(s):
    s = s.lower()
    new = []
    dup = []
    count = 0

    for i in s:
        if i not in new:
            new.append(i)
        elif i not in dup:
            dup.append(i)
            count+=1
    if count == 0:
        return (count, 'No duplicates')
    else:
        return (count, dup)


print(dupCount('abcde') )
print(dupCount('aabccdee1223') )

#Question 5

def counter(l):
    begin = l[0]
    for i in range(len(l) ):
        if begin != l[i]:
            return l[i]
        else:
            begin+=1
    return None

print(counter([1,2,3,4,6,7,8]) )
print(counter([-3,-2,-1,0,1,2,3]) )

#Question 6

class Person(object):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)

class Parent(Person):
    """
    Parent class inherits from Person class
    Takes first and last name as parameters
    """
    def __init__(self, firstname, lastname):
        super(Parent,self).__init__(firstname, lastname)
        self.children = []

    def addKid(self, firstname):
        self.children.append(Child(self, firstname) )
    
class Child(Person):
    """
    Child class also inherits from Person class
    Takes first name and parents name as parameters
    Last name is taken from parents last name
    """
    def __init__(self, firstname, parent):
        super(Parent,self).__init__(firstname, parent.lastname)
        self.parent = parent

#Question 7

import random

class RouletteWheel(object):
    """
    RouletteWheel class assigns number and color for the wheel.
    Spin function returns number and color for a randomized spin
    """
    def __init__(self):
        self.wheel = {'Green':['0','00'],
        'Red':['1','3','5','7','9','12','14','16','18','19','21','23','25','27','30','32','34','36'],
        'Black':['2','4','6','8','10','11','13','15','17','20','22','24','26','28','29','31','33','35']}
        
    def spin(self):
        result = {}
        spin = random.randint(0,36)
        if spin == 0:
            if random.randint(0,1) == 0:
                spin = '00'
            else:
                spin = '0'
        else:
            spin = str(spin)
        
        for key in self.wheel:
            if spin in self.wheel[key]:
                result = {'Number':int(spin), 'Color':key}
                return result

class RouletteTable(object):
    """
    RouletteTable has attribute that is an instance of RouletteWheel
    placeBet function takes in bet and returns winnings or losses
    """
    def __init__(self):
        super(RouletteTable,self).__init__()
    
    def placeBet(self, player_bet, player_bet_amount):
        bet = player_bet
        bet_amount = player_bet_amount
        result = RouletteWheel().spin()
        if len(bet) == 1:
            #if bet is a single number
            if type(bet[0]) is int:
                result = result['Number']
                if bet[0] == result:
                    #Return winnings
                    #Example: return(35 * bet)
                    pass
                else:
                    #Return losses
                    #Example: return -bet
                    pass
            else:
                #if bet is 'Black' or 'Red'
                if bet[0] == 'Black' or bet[0] == 'Red':
                    result = result['Color']
                    if bet[0] == result:
                        #Return winnings
                        pass
                    else:
                        #Return losses
                        pass
                else:
                    #if bet is 'Even' or 'Odd
                    result = result['Number'] % 2
                    if (bet[0] == 'Even' and result == 0) or (bet[0] == 'Odd' and result == 1):
                        #Return winnings
                        pass
                    else:
                        #Return losses
                        pass
                    
        elif len(bet) == 2:
            #if bet is 2 adjecent numbers
            result = result['Number']
            if result in bet:
                #Return winnings
                pass
            else:
                #Return losses
                pass

        elif len(bet) == 4:
            #if bet is placed on corner
            pass

        elif len(bet) == 12:
            #bet is on column or a dozen section
            pass

        #Error handling
        else:
            pass

class Player(RouletteTable):
    def __init__(self, name):
        super(Player,self).__init__()
        self.name = name
        self.total_bank = 0
        self.current_bet = 0
        self.current_bet_amount = 0
    
    def Bank(self, change):
        #updates bank after bets
        self.total_bank = self.total_bank + change

class Game(object):
    def __init__(self):
        self.Players = []
    
    def addPlayer(self, players):
        if not type(players) == list:
            self.Players.append(players)
        else:
            for p in players:
                self.Players.append(p)
    
    def runGame(self):
        #Main game loops
        random.shuffle(self.players)
        #Gets bet info
        for player in self.players:
            player.current_bet = input('What is', player.name, 'bet?')
            player.current_bet_amount = input('How much is', player.name, 'betting?')
        
        #Updates after win/loss
        for p in self.players:
            change = p.placeBet(player.current_bet, player.current_bet_amount)
            p.Bank(change)
```
