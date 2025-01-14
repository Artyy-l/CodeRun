import sys


def main():
    N = int(input())
    K = int(input())

    # dp[i][0] - вероятность того, что N делится на 6 спустя i ходов
    # dp[i][1] - вероятность того, что N делится на 5 спуспят i ходов
    dp = [[0, 0] for i in range(K + 1)]
    dp[0][0] = int(N % 6 == 0)
    dp[0][1] = int(N % 5 == 0)

    n = len(str(N))
    cnt5 = sum([int(x) == 5 for x in str(N)])
    summa = sum([int(x) for x in str(N)])
    cnt2 = sum([int(x) % 2 == 0 for x in str(N)])
    if summa % 3 != 0:
        cnt2 = 0

    for i in range(1, K + 1):
        dp[i][0] = dp[i - 1][0] * ((n - 2) / n) + (1 - dp[i - 1][0]) * 2 * cnt2 / (n * (n - 1))
        if cnt2 > 1:
            dp[i][0] += dp[i - 1][0] * 2 * (cnt2 - 1) / (n * (n - 1))
        dp[i][1] = dp[i - 1][1] * ((n - 2) / n) + (1 - dp[i - 1][1]) * 2 * cnt5 / (n * (n - 1))
        if cnt5 > 1:
            dp[i][1] += dp[i - 1][1] * 2 * (cnt5 - 1) / (n * (n - 1))

    print(dp[K][0] + dp[K][1])


if __name__ == '__main__':
    main()
