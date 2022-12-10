# 모눈종이 M,N 만들기
# 입력받은 왼쪽아래 좌표 오른쪽 위 좌표 계산해서 1로 변경
# 0으로 된 곳의 영역의 넓이를 list에 더하기
import sys
#dfs python재귀 제한
sys.setrecursionlimit(10000)

#왼쪽 아래좌표, 오른쪽 위의 좌표를 받아 직사각형 그리기
def drawRectangle(x,y,nx,ny,arr):    
    for i in range(y, ny):
        for j in range(x, nx):
            arr[M-1-i][j] = 1
    return arr

#dfs알고리즘
def dfs(x, y):
    global area
    visited[x][y] = True
    directions = [(1,0), (-1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if not arr[nx][ny] and not visited[nx][ny]:
            area += 1
            dfs(nx,ny)

M, N, K = map(int,input().split())

arr = [[0 for i in range(N)] for i in range(M)]
visited = [[False for i in range(N)] for i in range(M)]
result = []
cnt = 0

for _ in range(K):
    x, y, nx, ny = map(int, input().split())
    arr = drawRectangle(x, y, nx, ny, arr)

for i in range(M):
    for j in range(N):
        #방문하지 않고, 0인 곳을 탐색
        if not visited[i][j] and not arr[i][j]:
            # 면적값은 area에 결과값은 cnt에 받기
            cnt += 1
            area = 0
            dfs(i, j)
            result.append(area+1)
print(cnt)
print(*sorted(result))