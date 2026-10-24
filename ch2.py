import numpy as np


def minimum_edit_distance(source, target):
    m = len(source)
    n = len(target)

    D = np.zeros((m + 1, n + 1))

    for i in range(1, m + 1):
        D[i, 0] = D[i - 1, 0] + 1
    
    for j in range(1, n + 1):
        D[0, j] = D[0, j - 1] + 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            row_cost = D[i - 1, j + 0] + 1
            col_cost = D[i + 0, j - 1] + 1
            swp_cost = D[i - 1, j - 1] + (0 if source[i - 1] == target[j - 1] else 2)

            D[i, j] = min(row_cost, col_cost, swp_cost)

    return D


def calculate_alignment(source, target):
    DEL = 0
    INS = 1
    SWP = 2

    m = len(source)
    n = len(target)

    D = np.zeros((m + 1, n + 1))
    backlinks = np.empty((m + 1, n + 1), dtype=object)

    for i in np.ndindex(backlinks.shape):
        backlinks[i] = []

    for i in range(1, m + 1):
        D[i, 0] = D[i - 1, 0] + 1
        backlinks[i - 1, 0].append(DEL)
    
    for j in range(1, n + 1):
        D[0, j] = D[0, j - 1] + 1
        backlinks[0, j - 1].append(INS)
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            row_value = D[i - 1, j + 0] + 1
            col_value = D[i + 0, j - 1] + 1
            swp_value = D[i - 1, j - 1] + (0 if source[i - 1] == target[j - 1] else 2)

            min_cost = min(row_value, col_value, swp_value)

            if swp_value == min_cost:
                backlinks[i, j].append(SWP)

            if row_value == min_cost:
                backlinks[i, j].append(DEL)

            if col_value == min_cost:
                backlinks[i, j].append(INS)

            D[i, j] = min_cost

    output = [[], []]

    i = m
    j = n

    while i > 0 or j > 0:
        backlink = backlinks[i, j][0]

        if backlink == SWP:
            output[0].insert(0, source[i - 1])
            output[1].insert(0, target[j - 1])
            i -= 1
            j -= 1
        elif backlink == DEL:
            output[0].insert(0, source[i - 1])
            output[1].insert(0, "*")
            i -= 1
        elif backlink == INS:
            output[0].insert(0, "*")
            output[1].insert(0, target[j - 1])
            j -= 1

    return output


def ex2_9():
    source1 = "DRIVE"
    target1 = "DIVERS"

    D1 = minimum_edit_distance(source1, target1)

    print(D1, "\n")
    print(f"{source1} -> {target1} \nD1 = {D1[-1, -1]}\n")

    source2 = "DRIVE"
    target2 = "BRIEF"

    D2 = minimum_edit_distance(source2, target2)

    print(D2, "\n")
    print(f"{source2} -> {target2} \nD2 = {D2[-1, -1]}\n")


def ex2_10():
    source = "INTENTION"
    target = "EXECUTION"

    D = minimum_edit_distance(source, target)

    print(D, "\n")
    print(f"{source} -> {target} \nD = {D[-1, -1]}\n")

    alignment = calculate_alignment(source, target)

    print("".join(alignment[0]))
    print("".join(alignment[1]))


if __name__ == "__main__":
    print("Chapter 2\n")
    
    ex2_9()
    ex2_10()