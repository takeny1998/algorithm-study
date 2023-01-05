#검은색 - 전류 차단/ 흰색 - 전류 통함
# 전류는 섬유 물질의 가장 바깥쪽 흰색 격자들에 공급

import sys
#python 재귀 제한
sys.setrecursionlimit(100000)

#dfs
def dfs(x, y):
    global result
    visited[x][y] = True
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    # print("x,y",x,y)
    if x == (M-1):
        result = True
        return

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if not visited[nx][ny] and not arr[nx][ny]:
            dfs(nx, ny)

arr = list()
M, N = map(int, input().split())
visited = [[False for i in range(N)] for i in range(M)]

#그래프 만들기
for _ in range(M):
    arr.append(list(map(int, list(input()))))

#inline부터 시작해야하기 때문에 첫쨋줄만 검사
for j in range(N):
    result = False
    if not arr[0][j] and not visited[0][j]:
        dfs(0,j)
        #False일 경우 다른 줄 검사
        if not result:
            continue
        #True일 경우 결과값 바로 출력
        break

if result:
    print("YES")
else:
    print("NO")