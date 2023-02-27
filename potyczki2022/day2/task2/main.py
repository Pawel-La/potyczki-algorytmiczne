def main():
    def k_bigger_than_3():
        print("TAK")
        result = [x + 1 for x in range(k - 1)]
        if INDEX == k - 2:
            result.pop(0)
            result.append(k)
        elif INDEX == k - 1:
            for x in range(2):
                if INDEX + x < len(income):
                    result.pop(0)
                    result.append(INDEX + x)
        elif INDEX >= k:
            for x in range(3):
                if INDEX + x < len(income):
                    result.pop(0)
                    result.append(INDEX + x)
        print(*result)

    def k_equals_3(left_min, right_max):
        for j in range(len(income) - 1):
            if income[j] >= right_max[j + 1]:
                print("TAK")
                if j == 0:
                    print(j + 1, j + 2)
                else:
                    print(j, j + 1)
                return 0
        for j in range(1, len(income)):
            if left_min[j - 1] >= income[j]:
                print("TAK")
                if j == len(income) - 1:
                    print(j - 1, j)
                else:
                    print(j, j + 1)
                return 0
        print("NIE")

    def k_equals_2(left_min, right_max):
        for j in range(len(income) - 1):
            if left_min[j] >= right_max[j + 1]:
                print("TAK")
                print(j + 1)
                return 0
        print("NIE")

    def solve():
        if INDEX == len(income) - 1:
            print("NIE")
        elif k > 3:
            k_bigger_than_3()
        else:
            left_min = get_left_min()
            right_max = get_right_max()
            if k == 2:
                k_equals_2(left_min, right_max)
            elif k == 3:
                k_equals_3(left_min, right_max)

    def get_left_min():
        l_min = [0 for _ in range(len(income))]
        l_min[0] = income[0]
        for j in range(1, len(income)):
            l_min[j] = min(l_min[j - 1], income[j])
        return l_min

    def get_right_max():
        r_max = [0 for _ in range(len(income))]
        r_max[-1] = income[-1]
        for j in range(len(income) - 2, -1, -1):
            r_max[j] = max(r_max[j + 1], income[j])
        return r_max

    _, k = input().split()
    k = int(k)
    income = [int(x) for x in input().split()]

    INDEX = 0
    for INDEX in range(len(income) - 1):
        if income[INDEX] >= income[INDEX+1]:
            break

    solve()


if __name__ == '__main__':
    main()
