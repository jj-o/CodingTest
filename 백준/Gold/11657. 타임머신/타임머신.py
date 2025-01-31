import sys
inf = sys.maxsize
input = sys.stdin.readline

v,e = map(int,input().split())
edges = []
distance = [inf]*(v+1)

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

def bford(start):
    distance[start] = 0
    for i in range(v):
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur_node] != inf and distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                if i == v-1:
                    return True
    return False

negative = bford(1)
if negative:
    print(-1)
else:
    for i in range(2,v+1):
        if distance[i]==inf:
            print('-1')
        else:
            print(distance[i])