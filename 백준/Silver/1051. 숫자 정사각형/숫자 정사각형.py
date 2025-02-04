# n m 크기의 직사각형
# 각 칸에는 한 자리 숫자
# 꼭지점에 쓰여있는 수가 모두 같은 가장 큰 정사각형
# 정사각형은 행 또는 열에 평행해야 한다.

n,m = map(int,input().split())
squre = []
for _ in range(n):
    squre.append(input())

small_edge = min(n,m)

# 최대의 한 변의 길이부터 하나씩 줄여나가면서 최대 길이를 구한다.
# row 축 : 
# col 축
for edge in range(small_edge-1,-1,-1):
    for r in range(n-edge):
        for c in range(m-edge):
            if (squre[r][c] == squre[r][c+edge] and
                squre[r][c] == squre[r+edge][c] and
                squre[r][c] == squre[r+edge][c+edge]):
                max_size = (edge+1) ** 2
                print(max_size)
                exit() # 프로그램 자체가 종료 # break를 하면 현재 루프만 종료됨