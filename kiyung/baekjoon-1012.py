import sys
sys.setrecursionlimit(10000)

#출력 정리
def map_list(): 
    line = 0
    for i in li:
        print(line, i)
        line += 1

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):  #0,0 // 1,0, //-1,0, // 0,1 // 0,-1
        nx = x + dx[i]
        ny = y + dy[i]

        if m > nx >= 0 and n > ny >= 0:
            if li[nx][ny] == 1:
                li[nx][ny] = -1
                dfs(nx,ny)
               

t = int(input())
result = []
for p in range(t):
    # map
    m,n,k = map(int, input().split())
    li = [[0] * n for i in range(m)]
    x1, y1 = 0, 0
    cnt = 0

    for i in range(k):
        x, y = map(int, input().split())
        li[x][y] = 1
        #맵 출력
        # map_list()

    for x in range(m):
        for y in range(n):
            if li[x][y] == 1:
                dfs(x,y) # 좌표 넘김
                cnt += 1
    result.append(cnt)
for i in result: print(i)
# print(t)
# print(m,n,k)