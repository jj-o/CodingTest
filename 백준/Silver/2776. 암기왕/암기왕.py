T = int(input())

for j in range(T):
    n = int(input())
    note1 = set(map(int,input().split()))
    m = int(input())
    note2 = list(map(int,input().split()))


    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)