def factorize(x):
    primes = {}
    i = 2
    while x > 1:
        while x % i == 0:
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1
            x //= i
        i += 1

        if 1 < x < i ** 2:
            if x in primes:
                primes[x] += 1
            else:
                primes[x] = 1
            return primes
    return primes


def main():
    x, y = map(int, input().split())
    if x == 0 or y < x or y % x != 0:
        print(0)
        return

    primes_x = factorize(x)
    primes_y = factorize(y)
    ans = 1

    # заметим, что НОК делится на НОД, то есть y делится на x
    for p in primes_y:
        a = primes_y[p]
        b = 0
        if p in primes_x:
            b = primes_x[p]

        if a != b:
            ans *= 2
    print(ans)


if __name__ == '__main__':
    main()
