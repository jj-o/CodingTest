# 1은 집이 있는 곳, 0은 집이 없는 곳
# 집이 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
# 지도의 크기 N이 입력되고, N개의 자료(0또는 1)가 입력됨

n = int(input())

maps = []
for _ in range(n):
    maps.append(list(map(int,input())))
    
# 방문여부를 확인하여 무한 루프에 빠지는 것을 예방
visited = [[False]*n for _ in range(n)]

def dfs(x,y):
    # False 와 0은 둘 다 False로 평가될 수 있는 값이지만, dfs에서는 숫자적 합산이 되지 않도록 해야 하므로, return 0이 더 적절하다.
    if x<0 or y<0 or x>=n or y>=n or maps[x][y]==0 or visited[x][y]:
        return 0 
    
    visited[x][y] = True
    count = 1
    
# 내부의 수를 어떻게 count 하지??
    
    count += dfs(x,y-1)
    count += dfs(x,y+1)
    count += dfs(x-1,y)
    count += dfs(x+1,y)
    return count

result = []
for i in range(n):
    for j in range(n):
        if maps[i][j]==1 and not visited[i][j]:
            result.append(dfs(i,j))

result.sort()
print(len(result))
for c in result:
    print(c)