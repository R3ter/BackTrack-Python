from typing import List, Tuple, Set, Optional


# We define the types of a partial picture and a constraint (for type checking).
Picture = List[List[int]]
Constraint = Tuple[int, int, int]


# helper for both max_seen_cells and min_seen_cells, will work on min_seen_cells when the parametre min is True
def seen_cells_helper(picture, row, col, direction, min=False):
    num = 0
    if direction == "R+":
        col += 1
    elif direction == "R-":
        col -= 1
    elif direction == "U+":
        row += 1
    elif direction == "U-":
        row -= 1
    if row >= len(picture) or col >= len(picture[0]) or row < 0 or col < 0 or picture[row][col] == 0:
        return num
    if min and picture[row][col] == -1:
        return 0
    if picture[row][col] == 1 or picture[row][col] == -1:
        num = 1
    return seen_cells_helper(picture, row, col, direction)+num


def max_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0:
        return 0
    return (1 + seen_cells_helper(picture, row, col, "R+")
            + seen_cells_helper(picture, row, col, "R-")
            + seen_cells_helper(picture, row, col, "U+")
            + seen_cells_helper(picture, row, col, "U-"))


#print(max_seen_cells([[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]], 0, 0))


def min_seen_cells(picture: Picture, row: int, col: int) -> int:
    if picture[row][col] == 0:
        return 0
    return (1 + seen_cells_helper(picture, row, col, "R+", True)
            + seen_cells_helper(picture, row, col, "U+", True)
            + seen_cells_helper(picture, row, col, "R-", True)
            + seen_cells_helper(picture, row, col, "U-", True))


picture1 = [[-1, 0, 1, -1], [0, 1, -1, 1], [1, 0, 1, 0]]
picture2 = [[0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 0]]


def check_constraints(picture: Picture, constraints_set: Set[Constraint]) -> int:
    for val in constraints_set:
        min_seen = min_seen_cells(picture, val[0], val[1])
        max_seen = max_seen_cells(picture, val[0], val[1])
        if val[2] > max_seen or val[2] < min_seen:
            result = 0
            break
        elif val[2] >= min_seen and val[2] <= max_seen and picture[val[0]][val[1]] == -1:
            result = 2
            break
        elif val[2] == min_seen or val[2] == max_seen:
            result = 1

    return result


print(check_constraints(picture1, {(0, 3, 5), (1, 2, 5), (2, 0, 1)}),
      check_constraints(picture2, {(0, 3, 3), (1, 2, 5), (2, 0, 1)}),
      check_constraints(picture1, {(0, 3, 3), (1, 2, 5), (2, 0, 1)})
      )

def valid_placement(picture,constraints_set):
    for i in range(len(picture)):
        for k in i:
            for s in constraints_set:

                if ((i in range(s[0]-s[2]+1,s[0]+s[2]) and k==s[1]) or (k in range(s[1]-s[2]+1,s[1]+s[2]) and i ==s[0])) and picture[i][k] ==  0 :
                    return True
        

                


def solve_puzzle(constraints_set: Set[Constraint], n: int, m: int) -> Optional[Picture]:
    picture = [[0 for i in range(m)] for k in range(n)]

    def helper(constraints_set, picture, count=0):
        if check_constraints(picture, constraints_set) == 1 or not constraints_set:
            return picture
        pop_const = constraints_set.pop()
        for i in helper(constraints_set,picture):
            picture[pop_const[0]][pop_const[1]] = 1
            

            
           
        


print(solve_puzzle(({(0, 3, 3), (1, 2, 5), (2, 0, 1), (0, 0, 0)}), 3, 4))


def how_many_solutions(constraints_set: Set[Constraint], n: int, m: int) -> int:
    ...


def generate_puzzle(picture: Picture) -> Set[Constraint]:
    ...
