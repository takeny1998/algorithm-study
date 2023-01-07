# 내리막길
# dfs로 구현 
# 도착할 경우 남아있는 stack 저장
# visited를 초기화 한 후 stack에 있는 경우의 수를 다시 출발

M, N = map(int, input().split(" "))
array = []
for _ in range(M):
    array.append(list(map(int, input().split())))
    
dp = [[-1 for _ in range(N)] for _ in range(M)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x,y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if array[x][y] > array[nx][ny]:
                    dp[x][y] += dfs(nx, ny)
    
    return dp[x][y]



print(dfs(0,0))

            