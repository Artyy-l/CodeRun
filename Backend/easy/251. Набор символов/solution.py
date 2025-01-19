def main():
    s = input()
    c = set(input())
    minim = 101
    for i in range(len(s)):
        for j in range(i, len(s)):
            symbols = c.copy()
            flag = True
            for k in range(i, j + 1):
                if s[k] not in c:
                    flag = False
                    break
                if s[k] in symbols:
                    symbols.remove(s[k])
            if flag and symbols == set():
                minim = min(minim, j - i + 1)
    if minim == 101:
        print(0)
    else:
        print(minim)


if __name__ == '__main__':
    main()
