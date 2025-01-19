def main():
    n, m = map(int, input().split())
    buy = list(map(int, input().split()))
    sell = list(map(int, input().split()))
    buy.sort()
    sell.sort(reverse=True)
    profit = 0
    for i in range(min(len(buy), len(sell))):
        if buy[i] > sell[i]:
            print(profit)
            return
        profit += sell[i] - buy[i]
    print(profit)


if __name__ == '__main__':
    main()
