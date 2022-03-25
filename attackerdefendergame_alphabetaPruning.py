#using a-b pruning
#taking the input from user
import math
import random
import numpy as np

def start():    
    studentID=None
    min=None
    max=None
    while True: 
        try:
            studentID=int(input("My BracU Student ID: "))
            if len(str(studentID))!=8:
                print("Student IDs have exactly 8 digits")
                continue
            break
        except: 
            print("Student IDs have no alphabets/spaces in them.")

    while True:
        try:
            min, max=input("Attacker bullet range (min and max in integer seperated by a space): ").split(' ')
            if (min<max)!=True:
                print("Minimum value comes first.")
                continue
            break
        except: 
            print("Min and Max should be in integer seperated by a space only (Example: 1 100)")

    return studentID, min, max

#defining the defender method
#Properties: -Tries to get the lowest damage -Gets an initial HP from the given student ID
def totalHP(givenID):
    givenID=str(givenID)
    horsePower=int(givenID[7]+givenID[6])
    return horsePower

def totalTurns(givenID):
    givenID=str(givenID)
    tTurns=int(givenID[0])*2           #attacker gets the equal no. of turns that the defender does
    return tTurns

def branches(givenID):
    givenID=str(givenID)
    choices=int(givenID[2])
    return choices

def leaves(givenBranches, givenDepth):
    noOfLeaves=int(math.pow(givenBranches, givenDepth))
    return noOfLeaves

def damage(minimum, maximum, endBranches):
    minimum, maximum, endBranches=int(minimum), int(maximum), int(endBranches)
    attackerChoices=[]
    baseChoices=[None]*endBranches
    at=minimum
    while at<=maximum:
        attackerChoices.append(at)
        at+=1
    for i in range(len(baseChoices)):
        baseChoices[i]=(random.choice(attackerChoices))
    return baseChoices
        
def defender(choices, takeAtOnce):
    if type(choices) is not list:
        return choices
    if len(choices)==takeAtOnce:
        return min(choices)
    chunksOfChoices=np.array_split(choices, takeAtOnce)
    print(chunksOfChoices)
    newChoices=[]
    for i in range(len(chunksOfChoices)):
        # The only difference with the MinMax version is here -Logic: If b[0]<=min(a), don't bother checking the rest of the elements in b array-
        print(chunksOfChoices[i], newChoices)
        if len(newChoices)!=0 and chunksOfChoices[i][0]<=all(newChoices):
            print("Pruned")
            continue
        else:
            newChoices.append(min(chunksOfChoices[i]))
        #----------------------------------------------------------------------------------------------------------------------------------------
    return newChoices
    

#defining the attacker method
def attacker(choices, takeAtOnce):
    if type(choices) is not list:
        return choices
    if len(choices)==takeAtOnce:
        return max(choices)
    chunksOfChoices=np.array_split(choices, takeAtOnce)
    print(chunksOfChoices)
    newChoices=[]
    for i in range(len(chunksOfChoices)):
        # The only difference with the MinMax version is here -Logic: If b[0]>=max(a), don't bother checking the rest of the elements in b array-
        print(chunksOfChoices[i], newChoices)
        if len(newChoices)!=0 and chunksOfChoices[i][0]>=all(newChoices):
            print("Pruned")
            continue
        else:
            newChoices.append(max(chunksOfChoices[i]))
        #----------------------------------------------------------------------------------------------------------------------------------------
    return newChoices
    

def play(initialChoices, grouping, turns):
    theChoices=initialChoices
    level=turns
    while level>=0:
        theChoices=defender(theChoices, grouping)
        theChoices=attacker(theChoices, grouping)
        level-=2
    return theChoices

sID, leastDamage, mostDamage=start()
print(sID,'\n'+leastDamage, mostDamage)
initialHP=totalHP(sID)
depth=totalTurns(sID)
noOfBranches=branches(sID)
noOfBaseChoices=leaves(noOfBranches, depth)
arsenal=damage(leastDamage, mostDamage, noOfBaseChoices)
theChoice=int(play(arsenal, noOfBranches, depth))
remainingHP=initialHP-theChoice
print(f"Initial HP: {initialHP}\nNo. of moves: {depth}\nChoice in each step: {noOfBranches}\nInitial Choices for the defender: {noOfBaseChoices}\nBullets in the gun: {arsenal}\nLast move: {theChoice}\nRemaining HP: {remainingHP}" )

