import heapq
import sys
input = sys.stdin.readline

n = int(input())
s = []

for i in range(n):
    d, r = map(int,input().split())
    s.append((d,r))
    
s.sort()
heap = []

for d, ramens in s:
    heapq.heappush(heap,ramens)
    if len(heap) > d:
        heapq.heappop(heap)

print(sum(heap))