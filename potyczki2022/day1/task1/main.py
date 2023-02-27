def main():
    n = int(input())
    tests = input()
    step = n // 10
    count = 0

    for i in range(10):
        if 'N' in tests[step * i: step * (i+1)]:
            continue
        count += 1

    print(count)
    return 0


if __name__ == '__main__':
    main()
