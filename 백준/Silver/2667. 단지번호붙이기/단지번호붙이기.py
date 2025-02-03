# 1단지의 번호를 모두 새기고 다음 단지로 넘어가니까 dfs

import sys
input = sys.stdin.readline

n = int(input())
field = [list(map(int,input().strip())) for _ in range(n)] # strip을 써야 /n을 없앰앰
dr,dc = [-1,0,1,0],[0,-1,0,1]
visited = [[False]*n for _ in range(n)]
count = 0 # 단지의 숫자


def danzi(r,c):
    num_cnt = 1
    visited[r][c] = True # visited True 처리 꼭 하기
    for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if nr<0 or nc<0 or nr>=n or nc>=n: # continue는 반복문 내에서만 사용 가능
            continue

        if not visited[nr][nc] and field[nr][nc] == 1:
            visited[nr][nc] = True
            field[nr][nc] = count + 1 # 오류를 막음
            num_cnt += danzi(nr,nc) # dfs함수 안에 dfs함수 안에 ``` 가지치기 -> 결국 모든 합이 됨
    return num_cnt

result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and field[i][j] == 1:

            r = danzi(i,j)
            result.append(r)
            count += 1

print(len(result))

result.sort()
for r in result:
    print(r)
