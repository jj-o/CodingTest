import sys
from collections import deque

input = sys.stdin.readline

def dfs(v):
    visited1[v] = True
    print(v, end=' ')
    
    for v_next in graph[v]:
        if not visited1[v_next]:
            dfs(v_next)

def bfs(v):

    q = deque([v])
    visited2[v] = True
    
    while q:
        node = q.popleft()
        print(node, end=' ')
        
        for next_v in graph[node]: # 현재노드 기준 (v아님)

            if not visited2[next_v]:
                q.append(next_v)
                visited2[next_v] = True
    

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)] # 이렇게 적어야함

for _ in range(m):
    v1, v2 = map(int,input().split())
    # graph[v1][v2] = graph[v2][v1] = 1
    graph[v1].append(v2)
    graph[v2].append(v1)

for g in graph:
    g.sort()

visited1 = [False]*(n+1)
dfs(v)
print()
visited2 = [False]*(n+1)
bfs(v)
