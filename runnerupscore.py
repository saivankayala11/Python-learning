if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(set(arr))
    scores.sort()
    if len(scores) >= 2:
        print(scores[-2])
    else:
        print("no runnerup exist")


