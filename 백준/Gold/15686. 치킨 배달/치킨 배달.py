# 0(빈칸), 1(집), 2(치킨집)
# 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값

# 입력은 N,M으로 받음
# N * N 의 맵
# M개의 치킨 집 만듦
# 도시의 치킨집 중에 M개를 고르고, 나머지 폐업
# 그 중에 가장 치킨 거리가 적은 값

import sys
from itertools import combinations

input = sys.stdin.readline

n,m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]

# 치킨거리를 구하는 함수
# return 값이 그 경우의 수에서의 치킨거리
# 치킨집의 경우의 수에 따라 치킨거리를 구함
def get_chicken_distance(selected_chickens):
    total_distance = 0
    for h in home:
        min_distance = float('inf')
        for c in selected_chickens:
            min_distance = min(min_distance, abs(h[0]-c[0]) + abs(h[1]-c[1]))
        total_distance += min_distance
    return total_distance

# 치킨거리의 최솟값을 min을 통하여 출력

# 집과 치킨집의 index 값을 넣음.
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

# 모든 조합에서의 최솟값, 이렇게 따로 빼서 하기
min_chcken_distance = float('inf')

for selected in combinations(chicken,m):
    min_chcken_distance = min(min_chcken_distance, get_chicken_distance(selected))
print(min_chcken_distance)
