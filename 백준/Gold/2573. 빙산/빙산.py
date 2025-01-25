import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

# 동서남북 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt():
    """빙산 높이를 감소시키는 함수"""
    melted = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if field[x][y] > 0:
                sea_count = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
                        sea_count += 1
                melted[x][y] = max(0, field[x][y] - sea_count)  # 녹은 후 음수가 되지 않도록 처리
    return melted

def count_icebergs():
    """빙산 덩어리 개수를 세는 함수 (BFS 기반)"""
    visited = [[False] * m for _ in range(n)]
    count = 0

    for x in range(n):
        for y in range(m):
            if field[x][y] > 0 and not visited[x][y]:
                count += 1
                queue = deque([(x, y)])
                visited[x][y] = True
                while queue:
                    cx, cy = queue.popleft()
                    for k in range(4):
                        nx, ny = cx + dx[k], cy + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and field[nx][ny] > 0:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    return count

def all_melted():
    """모든 빙산이 녹았는지 확인"""
    for x in range(n):
        for y in range(m):
            if field[x][y] > 0:
                return False
    return True

# 시뮬레이션 시작
year = 0
while True:
    # 빙산 덩어리 개수 확인
    num_icebergs = count_icebergs()
    if num_icebergs >= 2:  # 두 덩어리 이상으로 분리되면 종료
        print(year)
        break
    if all_melted():  # 모든 빙산이 녹으면 0 출력
        print(0)
        break
    # 빙산 녹이기
    field = melt()
    year += 1