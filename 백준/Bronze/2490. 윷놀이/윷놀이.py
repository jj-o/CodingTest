import sys
input = sys.stdin.readline

board = []

for _ in range(3):
    board.append(list(map(int,input().split())))

for i in range(3):
    if board[i].count(0) == 1:
        print('A')
    elif board[i].count(0) == 2:
        print('B')
    elif board[i].count(0) == 3:
        print('C')
    elif board[i].count(0) == 4:
        print('D')
    elif board[i].count(1) == 4:
        print('E')