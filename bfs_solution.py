# Guaranteed Optimal Solution to the River Crossing Riddle
"""
The River Crossing Riddle
=========================
There are three tigers and three cubs.
Each tiger is a parent to exactly one of the cubs.

The tigers and cubs are trying to cross a river.
There is a boat next to the shore capable of carrying at most two animals at a time.
All three tigers know how to row the boat, but only one of the cubs knows, the other two cubs can only be passengers.

The tigers are merciless and will eat any cub that is not with its parent.
For example, 'tiger A' will eat 'cub b' if 'tiger B' is on the other side of the river.

How does the entire group cross the river safely?
"""

from enum import Enum
import copy

#======== Specific Game Rules ========#
# Starting Printout
def print_start():
    str1 = " River Crossing Riddle "
    eqlen = 15
    print("\n\n\n")
    print(eqlen*"="+str1+eqlen*"=")
    print()
    print("\t\tThree tigers: A, B, C")
    print("\t\tThree cubs: a, b, c")
    print("\t\tBoat rowers: A, B, C, a")
    print()
    print((eqlen+len(str1)+eqlen)*"=")
    print()

# Define the characters
class c(Enum):
    A = 1
    a = 4
    B = 2
    b = 5
    C = 3
    c = 6
    boat = 7

# Initialize the characters and the rowers
chars = [x for x in c]
rowers_list = [c.A, c.B, c.C, c.a]

# Check if the bank is valid
def valid_bank(bank):
    bank_list = []
    for i in bank:
        if i == c.A:
            bank_list.append("tiger1")
        elif i == c.B:
            bank_list.append("tiger2")
        elif i == c.C:
            bank_list.append("tiger3")
        elif i == c.a:
            bank_list.append("cub1")
        elif i == c.b:
            bank_list.append("cub2")
        elif i == c.c:
            bank_list.append("cub3")
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

#============================================================#
#=========== The Solution (Do not change) ===================#
#============================================================#

#=== Helper Functions ===#
# Print the visited vertex
def visit(lb,rb):
    lb_padded = []
    rb_padded = []
    for i in c:
        if i in lb:
            lb_padded.append(i.name)
        else:
            lb_padded.append(" ")
        if i in rb:
            rb_padded.append(i.name)
        else:
            rb_padded.append(" ")
    
    for i in range(len(c)):
        print("\t\t"+lb_padded[i] + "\t | \t" + rb_padded[i])

# Produce a unique encoding for the vertex
def encode(v):
    return tuple(set(v))

#====== The Game ======#
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

#=== Breadth First Search ===#
def breadth_first_search(Game, v):
    queue  = [encode(v)] 
    marked = {}
    edges = {}
    while len(queue) > 0:
        v = queue.pop(0)
        if v not in marked.keys():
            marked[v] = True
            for w in Game(v):
                y = encode(w)
                if y not in marked.keys():
                    queue.append(y)
                    edges[y] = v
    return edges

#== Get Shortest Path ==#
def get_shortest_path(s, e, edges):
    path = []

    node = encode(e)
    while node != encode(s):
        path.append(node)
        node = edges[node]
    
    path.append(node)
    path.reverse()
    return path

#========= Main =========#
if __name__ == "__main__":
    edges = breadth_first_search(Game, chars)
    path = get_shortest_path(chars, [], edges)

    print_start()
    print("left shore\t\triver\t\tright shore")
    n = 0
    if(path[0] != encode(chars)):
        print("No solution found!")
    else:
        for i in path:
            n+=1
            ls = list(i)
            rs = [i for i in c if i not in ls]
            print()
            visit(ls,rs)
            if len(ls) > 0:
                print(5*"-"+"Step: " + str(n)+40*"-")
            else:
                print("\n\nAll tigers & their cubs have crossed the river safely!")
