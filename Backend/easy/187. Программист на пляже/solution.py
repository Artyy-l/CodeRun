def main():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        minim = arr[0] ^ arr[1]
        for i in range(1, n):
            j = i - 1
            while j >= 0 and (arr[i] - arr[j]) < minim:
                minim = min(minim, arr[i] ^ arr[j])
                j -= 1
        print(minim)


if __name__ == '__main__':
    main()
