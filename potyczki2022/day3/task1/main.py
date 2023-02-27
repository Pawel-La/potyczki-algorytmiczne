def main():
    def get_cycle(start_index):
        cycle = []
        while not is_used[start_index]:
            is_used[start_index] = True
            cycle.append(start_index + 1)
            start_index = indexes_sorted_by_height_increasingly[start_index] - 1
        return list(reversed(cycle))

    def get_switches(switches_1, switches_2):
        switches = []
        if switches_1:
            s = [el[0] for el in switches_1]
            temp = [el[1] for el in switches_1]
            temp.reverse()
            switches.append(s + temp)
        if switches_2:
            s = [el[0] for el in switches_2]
            temp = [el[1] for el in switches_2]
            temp.reverse()
            switches.append(s + temp)
        return switches

    NUMBER_OF_STUDENTS = int(input())
    heights_with_indexes = \
        [(int(input()), i+1) for i in range(NUMBER_OF_STUDENTS)]
    indexes_sorted_by_height_increasingly = \
        [el[1] for el in sorted(heights_with_indexes)]
    is_used = [False for _ in range(NUMBER_OF_STUDENTS)]

    i = 0
    cycles = []
    while i < NUMBER_OF_STUDENTS:
        if is_used[i]:
            i += 1
            continue
        cycles.append(get_cycle(i))

    case_1 = []
    case_2 = []
    for cycle in cycles:
        if len(cycle) <= 1:
            continue
        if len(cycle) == 2:
            case_1.append((cycle[0], cycle[1]))
        else:
            for i in range(1, (len(cycle) + 1) // 2):
                case_1.append((cycle[i], cycle[len(cycle) - i]))

            case_2.append((cycle[0], cycle[1]))
            for i in range(2, (len(cycle) + 2) // 2):
                case_2.append((cycle[i], cycle[len(cycle) - i + 1]))

    switches = get_switches(case_1, case_2)
    print(len(switches))
    for switch in switches:
        print(len(switch))
        print(*switch)


if __name__ == '__main__':
    main()
