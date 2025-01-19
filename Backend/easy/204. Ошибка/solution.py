def main():
    n = int(input())
    summa = 0
    arr = []
    for i in range(n):
        a, b = map(int, input().split())
        summa += a * b
        arr += [a * b]
    for x in arr:
        print(x / summa)


if __name__ == '__main__':
    main()
