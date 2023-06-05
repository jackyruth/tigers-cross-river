# Implement Depth First Search Algorithm for the River Crossing Riddle
"""
Game Setup: Left Shore -> River -> Right Shore
The left shore alone uniquely identifies the state of the game
"""
from enum import Enum
import copy

class c(Enum):
    tA = 1
    tB = 2
    tC = 3
    cA = 4
    cB = 5
    boat = 6

chars = [x for x in c]
rowers_list = [c.tA, c.tB, c.tC]

def valid_bank(bank):
    bank_list = []
    for i in bank:
        if i == c.tA:
            bank_list.append("tiger1")
        elif i == c.tB:
            bank_list.append("tiger2")
        elif i == c.tC:
            bank_list.append("tiger3")
        elif i == c.cA:
            bank_list.append("cub1")
        elif i == c.cB:
            bank_list.append("cub2")
        elif i == c.boat:
            bank_list.append("boat")
        else:
            print("ERROR, UNEXPECTED PERSON")

    tigers = [i for i in bank_list if i.startswith("tiger")]
    cubs = [i for i in bank_list if i.startswith("cub")]

    # If no tiger, then valid
    if tigers == []:
        return True
    
    # Go through each cub
    for cub in cubs:
        # If cub is not with its tiger, then invalid
        if cub.replace("cub", "tiger") not in tigers:
            return False

    return True

### Algorithm ###
def visit(v):
    for i in c:
        if i in v:
            print(i.name, end=" ")
        else:
            print(len(i.name)*" ", end=" ")
    print("\n")

def encode(v):
    return tuple(set(v))

def Game(v):
    """
    Input: An ordered tuple 'v' showing who is on the left shore
    Output: A list of ordered tuples, showing the valid next moves
    """
    ls = list(v)
    rs = [i for i in c if i not in ls]

    valid_moves = []
    if c.boat in ls:
        sb = copy.deepcopy(ls)
        db = copy.deepcopy(rs)
        left_shore = True
    else:
        sb = copy.deepcopy(rs)
        db = copy.deepcopy(ls)
        left_shore = False

    rowers = [i for i in sb if i in rowers_list] # rowers on the shore
    for rower in rowers:
        passengers = [i for i in sb if i is not rower] # passengers on the shore
        passengers.append(0) # There can also be no passengers
        if c.boat in passengers:
            passengers.remove(c.boat)

        for passenger in passengers:
            tmp_sb = copy.deepcopy(sb)
            tmp_db = copy.deepcopy(db)
            tmp_sb.remove(rower)
            tmp_db.append(rower)

            if passenger != 0:
                tmp_sb.remove(passenger)
                tmp_db.append(passenger)

            if(not valid_bank(tmp_sb)):
                continue

            if(not valid_bank(tmp_db)):
                continue
            
            if c.boat in tmp_sb:
                tmp_sb.remove(c.boat)
                tmp_db.append(c.boat)
            else:
                tmp_sb.append(c.boat)
                tmp_db.remove(c.boat)

            if left_shore:
                valid_moves.append(tmp_sb)
            else:
                valid_moves.append(tmp_db)

    return valid_moves


def BFS(Game, v):
    queue  = [encode(v)] 
    marked = {}
    prev = {}
    while len(queue) > 0:
        v = queue.pop(0)
        if v not in marked.keys():
            marked[v] = True
            for w in Game(v):
                y = encode(w)
                if y not in marked.keys():
                    queue.append(y)
                    prev[y] = v
    return prev

def reconstructPath(s, e, prev):
    path = []

    node = encode(e)
    while node != encode(s):
        path.append(node)
        node = prev[node]
    
    path.append(node)
    path.reverse()
    return path


if __name__ == "__main__":
    prev = BFS(Game, chars)
    path = reconstructPath(chars, [], prev)
    print(25*"="+"START"+25*"=")
    n = 0
    for i in path:
        n+=1
        ls = list(i)
        rs = [i for i in c if i not in ls]
        print("Step: " + str(n))
        visit(ls)
        visit(rs)
        print(50*"-")
