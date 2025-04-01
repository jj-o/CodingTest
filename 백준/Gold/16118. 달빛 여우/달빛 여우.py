# 달빛 ㅕ우, 달빛 늑대대
# 1부터 N까지 번호가 붙은 N개의 나무 그루터기
# 그루터기들 사이에 M개의 오솔길
# 어떤 두 그루터기 사이에 두 개 이상의 오솔길이 나 있는 경우는 없다
# 달빛 여우와 달빛 늑대는 각자 가장 빠르게 달빛이 비치는 그루터기까지 다다를 수 있는 경로로 이동
# 달빛 여우가 달빛 늑대보다 먼저 도착할 수 있는 그루터기


# 그래프 문제
# 다익스트라 

# 달빛 여우와 달빛 늑대는 1번 나무 그루터기에 산다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c*2))
    graph[b].append((a,c*2))
    
# fox_distance = [INF] * (n+1)
# fox_visited = [False] * (n+1)
# wolf_distance = [INF] * (n+1)
# wolf_visited = [False] * (n+1)

def dijkstra_fox():
    dist = [INF] * (n+1)
    dist[1] = 0
    q = [(0,1)]
    
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, d in graph[now]:
            if dist[nxt] > dist[now] + d:
                dist[nxt] = dist[now] + d
                heapq.heappush(q,(dist[nxt], nxt))
    return dist


def dijkstra_wolf():
    # 0: 빠르게 가기, 1: 느리게 가기
    dist = [[INF]*(n+1) for _ in range(2)]
    # 달빛 늑대는 출발할 때 오솔길 하나를 달빛 여우의 두 배의 속도로 달려가고
    # -> 처음에는 빨리 달림
    dist[0][1] = 0
    q = [(0,1,0)]
    
    while q:
        cost, now, state = heapq.heappop(q)
        if dist[state][now] < cost:
            continue
        for nxt, d in graph[now]:
            if state == 0:
                new_cost = cost + d//2
                if dist[1][nxt] > new_cost:
                    dist[1][nxt] = new_cost
                    heapq.heappush(q,(new_cost,nxt,1))
            else:
                new_cost = cost + d*2
                if dist[0][nxt] > new_cost:
                    dist[0][nxt] = new_cost
                    heapq.heappush(q,(new_cost, nxt, 0))
    return dist

# def dijkstra(start,k):
#     fox_distance[start] = 0
#     wolf_distance[start] = 0
#     for j in graph[start]:
#         fox_distance[j[0]] = j[1]
#         # 2배 빨리갓다가 1/2로 갔다가 하는 것을 어떻게 구현??
#         wolf_distance[j[0]] = k*j[1]
#     for _ in range(n-1):
#         fox_now, wolf_now = get_smallest_node()
#         fox_visited[fox_now] = True
#         wolf_visited[wolf_now] = True
#         for j in graph[fox_now]:
#             cost = fox_distance[fox_now] + j [1]

fox = dijkstra_fox()
wolf = dijkstra_wolf()

answer = 0
for i in range(2,n+1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1

print(answer)

        
