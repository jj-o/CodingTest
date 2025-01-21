# 수빈이 현재 점 N(0<=N<=10만)
# 동생 K(0<=K<10만)
# 수빈 위치가 X일 때 걷는다면, 1초 후 X-1, X+1
# 순간이동 1초 후 2*X
# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

from collections import deque

# q에 수빈이가 이동한 위치를 넣는 것은 맞는데, 동생의 위치와 맞는지를 어떻게 보지?

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == b:
            return array[v]
        for next_v in (v-1,v+1,2*v):
            if 0<= next_v < MAX and not array[next_v]: # not array i가 0이 아니라는 것?
                array[next_v] = array[v] +1
                q.append(next_v)

s,b = map(int,input().split())
MAX = 100001
array = [0] * MAX # visited 행렬을 안 두고 시간을 표시하기 위하여 [0] MAX 개를 둠
print(bfs(s))

