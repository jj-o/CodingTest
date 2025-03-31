# 달빛 ㅕ우, 달빛 늑대대
# 1부터 N까지 번호가 붙은 N개의 나무 그루터기
# 그루터기들 사이에 M개의 오솔길
# 어떤 두 그루터기 사이에 두 개 이상의 오솔길이 나 있는 경우는 없다
# 달빛 여우와 달빛 늑대는 각자 가장 빠르게 달빛이 비치는 그루터기까지 다다를 수 있는 경로로 이동
# 달빛 여우가 달빛 늑대보다 먼저 도착할 수 있는 그루터기
import sys
import heapq
input = sys.stdin.readline

INF = int(1e18)
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, d = map(int, input().split())
    # 거리 * 2로 저장 (늑대가 나눗셈하는 거 방지)
    graph[a].append((b, d * 2))
    graph[b].append((a, d * 2))

# 여우
def dijkstra_fox():
    dist = [INF] * (n + 1)
    dist[1] = 0
    q = [(0, 1)]

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for nxt, d in graph[now]:
            if dist[nxt] > dist[now] + d:
                dist[nxt] = dist[now] + d
                heapq.heappush(q, (dist[nxt], nxt))
    return dist

# 늑대
def dijkstra_wolf():
    # 0: 빠르게 달린 후 (다음은 느리게), 1: 느리게 달린 후 (다음은 빠르게)
    dist = [[INF] * (n + 1) for _ in range(2)]
    dist[0][1] = 0
    q = [(0, 1, 0)]  # (cost, node, status)

    while q:
        cost, now, state = heapq.heappop(q)
        if dist[state][now] < cost:
            continue
        for nxt, d in graph[now]:
            if state == 0:  # 빠르게 달리는 경우 (속도 2배 → 시간 절반)
                new_cost = cost + d // 2
                if dist[1][nxt] > new_cost:
                    dist[1][nxt] = new_cost
                    heapq.heappush(q, (new_cost, nxt, 1))
            else:  # 느리게 달리는 경우 (속도 0.5배 → 시간 2배)
                new_cost = cost + d * 2
                if dist[0][nxt] > new_cost:
                    dist[0][nxt] = new_cost
                    heapq.heappush(q, (new_cost, nxt, 0))
    return dist

fox = dijkstra_fox()
wolf = dijkstra_wolf()

answer = 0
for i in range(2, n + 1):
    if fox[i] < min(wolf[0][i], wolf[1][i]):
        answer += 1

print(answer)
### 문제 요약 - `N`개의 노드 (1~N번 그루터기) - `M`개의 간선 (오솔길, 양방향) - 여우: 일반적인 다익스트라 - 늑대: 짝수 턴엔 속도 2배 (시간은 거리/2), 홀수 턴엔 속도 절반 (시간은 거리×2) - 여우가 늑대보다 빨리 도착할 수 있는 노드의 수를 구해야 함 --- ### 주요 아이디어 - **여우**는 일반 다익스트라로 한 번만 수행. - **늑대**는 **두 가지 상태** (빠른 속도, 느린 속도)를 가지므로 **2차원 거리 배열**로 다익스트라. --- ### 정답 코드 ```python import sys import heapq input = sys.stdin.readline INF = int(1e18) n, m = map(int, input().split()) graph = [[] for _ in range(n + 1)] for _ in range(m): a, b, d = map(int, input().split()) # 거리 * 2로 저장 (늑대가 나눗셈하는 거 방지) graph[a].append((b, d * 2)) graph[b].append((a, d * 2)) # 여우 def dijkstra_fox(): dist = [INF] * (n + 1) dist[1] = 0 q = [(0, 1)] while q: cost, now = heapq.heappop(q) if dist[now] < cost: continue for nxt, d in graph[now]: if dist[nxt] > dist[now] + d: dist[nxt] = dist[now] + d heapq.heappush(q, (dist[nxt], nxt)) return dist # 늑대 def dijkstra_wolf(): # 0: 빠르게 달린 후 (다음은 느리게), 1: 느리게 달린 후 (다음은 빠르게) dist = [[INF] * (n + 1) for _ in range(2)] dist[0][1] = 0 q = [(0, 1, 0)] # (cost, node, status) while q: cost, now, state = heapq.heappop(q) if dist[state][now] < cost: continue for nxt, d in graph[now]: if state == 0: # 빠르게 달리는 경우 (속도 2배 → 시간 절반) new_cost = cost + d // 2 if dist[1][nxt] > new_cost: dist[1][nxt] = new_cost heapq.heappush(q, (new_cost, nxt, 1)) else: # 느리게 달리는 경우 (속도 0.5배 → 시간 2배) new_cost = cost + d * 2 if dist[0][nxt] > new_cost: dist[0][nxt] = new_cost heapq.heappush(q, (new_cost, nxt, 0)) return dist fox = dijkstra_fox() wolf = dijkstra_wolf() answer = 0 for i in range(2, n + 1): if fox[i] < min(wolf[0][i], wolf[1][i]): answer += 1 print(answer) ``` --- ### 추가 팁 - 거리 비교 시 늑대는 두 상태 중 **더 짧은 거리**를 기준으로 비교해야 함. - 입력이 많을 수 있으니 `sys.stdin.readline` 사용. - `d * 2`로 모든 거리 저장해서 늑대의 나눗셈/곱셈 연산을 `// 2` 또는 `* 2`로 처리해 부동소수점 문제 회피. 필요하면 시각화나 예시도 만들어줄게요.