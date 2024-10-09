from collections import deque

def solution(board):
    answer = 0
    
    R = len(board)
    C = len(board[0])
    
    for i in range(R):
        for j in range(C):
            if board[i][j]=='R':
                sr,sc = i,j
    
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    
    def bfs():
        visited = [[0]*C for i in range(R)]
        q = deque()
        q.append((sr,sc))
        visited[sr][sc] = 1

        while q:
            px,py = q.popleft()
            if board[px][py] == 'G':
                return visited[px][py]

            for i in range(4):
                nx,ny = px,py
                while True:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if 0<=nx<R and 0<=ny<C and board[nx][ny]=='D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx<0 or ny<0 or nx>=R or ny>=C:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] +1
                    q.append((nx,ny))
        return -1
    answer = bfs()
    if answer >0:
        answer -=1
    return answer