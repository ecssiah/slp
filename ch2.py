import numpy as np

def minimum_edit_distance_matrix(source, target):
    n = len(source)
    m = len(target)

    D = np.zeros((n + 1, m + 1))

    for i in range(1, n + 1):
        D[i, 0] = D[i - 1, 0] + 1
    
    for j in range(1, m + 1):
        D[0, j] = D[0, j - 1] + 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            row_cost = D[i - 1, j + 0] + 1
            col_cost = D[i + 0, j - 1] + 1
            swp_cost = D[i - 1, j - 1] + (0 if source[i - 1] == target[j - 1] else 2)

            D[i, j] = min(row_cost, col_cost, swp_cost)

    return D

def minimum_edit_distance(D):
    return D[-1, -1]

def alignment(source, target):
    ROW = 0
    COL = 1
    SWP = 2

    n = len(source)
    m = len(target)

    D = np.zeros((n + 1, m + 1))
    backlinks = np.empty((n + 1, m + 1), dtype=object)

    for i in np.ndindex(backlinks.shape):
        backlinks[i] = []

    for i in range(1, n + 1):
        D[i, 0] = D[i - 1, 0] + 1
        backlinks[i - 1, 0].append(ROW)
    
    for j in range(1, m + 1):
        D[0, j] = D[0, j - 1] + 1
        backlinks[0, j - 1].append(COL)
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            row_value = D[i - 1, j + 0] + 1
            col_value = D[i + 0, j - 1] + 1
            swp_value = D[i - 1, j - 1] + (0 if source[i - 1] == target[j - 1] else 2)

            min_cost = min(row_value, col_value, swp_value)

            if swp_value == min_cost:
                backlinks[i, j].append(SWP)

            if row_value == min_cost:
                backlinks[i, j].append(ROW)

            if col_value == min_cost:
                backlinks[i, j].append(COL)

            D[i, j] = min_cost

    source_line = ""
    target_line = ""

    i = n
    j = m

    while i != 0 or j != 0:
        backlink = backlinks[i, j][0]

        if backlink == SWP:
            source_line = source[i - 1] + source_line
            target_line = target[j - 1] + target_line
            i -= 1
            j -= 1
        elif backlink == ROW:
            source_line = source[i - 1] + source_line
            target_line = "*"           + target_line
            i -= 1
        elif backlink == COL:
            source_line = "*"           + source_line
            target_line = target[j - 1] + target_line
            j -= 1

    print(source_line)
    print(target_line)

def ex2_9():
    source1 = "DRIVE"
    target1 = "DIVERS"

    D1 = minimum_edit_distance_matrix(source1, target1)
    distance1 = minimum_edit_distance(D1)

    print(D1)
    print(f"{source1} -> {target1} \nD1 = {distance1}\n")

    source2 = "DRIVE"
    target2 = "BRIEF"

    D2 = minimum_edit_distance_matrix(source2, target2)
    distance2 = minimum_edit_distance(D2)

    print(D2)
    print(f"{source2} -> {target2} \nD2 = {distance2}\n")

def ex2_10():
    source = "MICHAEL"
    target = "CYANNA"

    D = minimum_edit_distance_matrix(source, target)
    distance = minimum_edit_distance(D)

    print(D)
    print(f"{source} -> {target} \nD = {distance}\n")

    alignment(source, target)

if __name__ == "__main__":
    ex2_9()
    ex2_10()