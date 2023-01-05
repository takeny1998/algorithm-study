import sys
sys.setrecursionlimit(1000)

#깊이 우선 탐색 
def dfs(start):
    stack = [start]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while stack:
        x, y = stack.pop()
        visited[x][y] = True
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if ground[nx][ny] and not visited[nx][ny]:
                stack.append((nx,ny))

#사용자 입력
t = int(input())
for _ in range(t):
    M, N, K = map(int,input().split())

    #가로, 세로 맞는 2차원 배열 선언 
    ground = [[0 for i in range(M)] for i in range(N)]
    visited = [[False for i in range(M)] for i in range(N)]

    #밭 만들기
    for _ in range(K):
        y, x = map(int,input().split())
        ground[x][y] = 1

    result = 0
    #밭에서 1이고 방문하지 않은곳에 dfs
    for i in range(N):
        for j in range(M):
            if ground[i][j] and not visited[i][j]:
                result += 1
                dfs((i,j)) 
    print(result)

    
