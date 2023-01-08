m, n = map(int,input().split())

li = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)]for _ in range(m)] # -1로 이루어진 li와 같은 크기 

dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == m -1 and y == n -1:
        return 1
    if dp[x][y] == -1: # 탐색하지 않았다면
        dp[x][y] = 0  # 0으로 바꾸고 아래 탐색 코드 실행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0<= ny < n:
                if li[x][y] > li[nx][ny]: # 현재 위치보다 다음 탐색할 위치가 크다면
                    dp[x][y] += dfs(nx, ny)
                    dfs(nx,ny)
    return dp[x][y]
                
print(dfs(0,0))

