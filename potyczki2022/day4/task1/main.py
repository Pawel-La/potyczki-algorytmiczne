import numpy as np


def main():
    # ---------------------- INPUT PART ----------------------------------------
    n, m = input().split()
    n, m = int(n), int(m)
    tab = np.empty((n, m)).astype(str)

    for i in range(n):
        s = input().split()[0]
        for j in range(m):
            tab[i][j] = s[j]

    _ = int(input())
    xdd = preprocess(input())
    moves = np.array([x for x in xdd]).astype(str)
    # ------------------------ ROWS AND COLS INIT ------------------------------
    rows = ["" for _ in range(n)]
    cols = ["" for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if tab[i][j] != '.':
                rows[i] += tab[i][j]

    for i in range(m):
        for j in range(n):
            if tab[j][i] != '.':
                cols[i] += tab[j][i]
    # ------------------------ SOLVE PART --------------------------------------
    left1_right2 = 0
    for move in moves:
        if move == 'G':
            for i in range(n):
                rows[i] = ""
            for col in cols:
                for x in range(len(col)):
                    rows[x] += col[x]
        elif move == 'D':
            for i in range(n):
                rows[i] = ""
            for col in cols:
                for x in range(len(col)):
                    rows[-len(col) + x] += col[x]
        if move == 'L':
            left1_right2 = 1
            for i in range(m):
                cols[i] = ""
            for row in rows:
                for x in range(len(row)):
                    cols[x] += row[x]
        elif move == 'P':
            left1_right2 = 2
            for i in range(m):
                cols[i] = ""
            for row in rows:
                for x in range(len(row)):
                    cols[-len(row) + x] += row[x]
    # ------------------------ FINAL PART --------------------------------------
    final_tab = np.full(shape=(n, m), fill_value='.').astype(str)
    for i in range(len(rows)):
        if rows[i] == '':
            continue
        if left1_right2 == 2:
            for j in range(len(rows[i])):
                final_tab[i][j - len(rows[i])] = rows[i][j]
        else:
            for j in range(len(rows[i])):
                final_tab[i][j] = rows[i][j]

    for row in final_tab:
        print(*row, sep='')


def preprocess(s):
    pre_result = ""
    i = 0

    while i < len(s):
        j = i + 1
        if s[i] == "L" or s[i] == "P":
            while j < len(s) and (s[j] == "P" or s[j] == "L"):
                j += 1
            pre_result += s[j - 1]
            i = j
        elif s[i] == "G" or s[i] == "D":
            while j < len(s) and (s[j] == "G" or s[j] == "D"):
                j += 1
            pre_result += s[j - 1]
            i = j

    if len(pre_result) == 1:
        return [pre_result]

    top1_bottom2 = 0
    left1_right2 = 0
    result = []
    if pre_result[0] == "P" or pre_result[1] == "P":
        left1_right2 = 2
    if pre_result[0] == "L" or pre_result[1] == "L":
        left1_right2 = 1
    if pre_result[0] == "G" or pre_result[1] == "G":
        top1_bottom2 = 1
    if pre_result[0] == "D" or pre_result[1] == "D":
        top1_bottom2 = 2

    for x in range(2, len(pre_result)):
        i = pre_result[x]
        if i == 'G':
            if len(result) and result[-1] == 'D':
                result.pop()
            elif top1_bottom2 == 2:
                result.append(i)
            top1_bottom2 = 1
        elif i == 'D':
            if len(result) and result[-1] == 'G':
                result.pop()
            elif top1_bottom2 == 1:
                result.append(i)
            top1_bottom2 = 2
        elif i == 'L':
            if len(result) and result[-1] == 'P':
                result.pop()
            elif left1_right2 == 2:
                result.append(i)
            left1_right2 = 1
        else:
            if len(result) and result[-1] == 'L':
                result.pop()
            elif left1_right2 == 1:
                result.append(i)
            left1_right2 = 2

    result = [pre_result[0], pre_result[1]] + result

    return result


if __name__ == '__main__':
    main()
