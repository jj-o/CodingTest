# 해야할 일 각각의 중요도 산정, 중요도가 높은 일부터
# 중요도는 M만큼 감소, 중요도가 K 이하가 되면 그 일은 완료한 것으로 간주
# 송이가 모든 일을 끝낼 때까지 며칠이 걸리는지
# 모든 일을 끝낼 때까지 송이가 일별로 느낀 만족감
# i번 일이 가지는 중요도

import sys
import math
import heapq
input = sys.stdin.readline

n,m,k = map(int,input().split())
d = [int(input()) for _ in range(n)]

max_heap = [-p for p in d]
heapq.heapify(max_heap)

y=0
ys = []

while max_heap:
    p = -heapq.heappop(max_heap)
    if p>k:
        y = math.floor(y/2)+p
        p = p-m
        ys.append(y)
        if p>k:
            heapq.heappush(max_heap,-p)
        
print(len(ys))
for y in ys:
    print(y)