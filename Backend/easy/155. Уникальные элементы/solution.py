import sys


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt_numbers = {}
    for x in arr:
        if x in cnt_numbers:
            cnt_numbers[x] += 1
        else:
            cnt_numbers[x] = 1
    
    cnt = 0
    for x in cnt_numbers:
        if cnt_numbers[x] == 1:
           cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()
