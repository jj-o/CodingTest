# M*N 크기의 보드
# 보드를 잘라 8*8의 체스판
# 맨 왼쪽 위 칸이 흰색 or 검은색
# 지민이가 다시 칠해야 하는 정사각형의 최소 갯수
# 검은색과 흰색 번갈아 칠함
# n과 m은 8보다 크거나 같고, 50보다 작거나 같은 자연수
# 다시 칠해야하는 정사각형 최소 갯수
# 보드를 잘라 8*8 체스판

m,n = map(int,input().split())
board = []
count = []
for _ in range(m):
    board.append(input())
for r in range(m-7):
    for c in range(n-7):
        index1,index2=0,0
        for i in range(r,r+8):
            for j in range(c,c+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1,index2))
print(min(count))