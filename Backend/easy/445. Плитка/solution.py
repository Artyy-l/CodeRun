import sys


def main():
    # W + B = nm и m ≤ sqrt(2**6) < 10**4
    # напишем неоптимальное переборное решение

    B, W = map(int, input().split())
    # m ≥ 3, так как W ≥ 1
    for m in range(3, 10 ** 4):
        if (W + B) % m == 0:
            n = (W + B) // m
            if (n >= m) and (W == (n - 2) * (m - 2)):
                print(n, m)
                return


if __name__ == '__main__':
    main()
