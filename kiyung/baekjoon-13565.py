import sys
sys.setrecursionlimit(10**6)

def test(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if n > nx >=0 and m > ny >=0:            
            # print('진입')
            if li[nx][ny] == 0:
                li[nx][ny] = 3
                test(nx, ny)

# 입출력
n, m = map(int, input().split())

# map
li = [[0]*m for _ in range(n)]

# li에 집어넣기
for x in range(n):
    a = input()
    for y in range(m):
        li[x][y] = int(a[y])

for x in range(n):
    for y in range(m):
        if li[x][y] == 0:
            conut = 0
            test(0,y)

print('YES') if 3 in li[len(li)-1] else print('NO')