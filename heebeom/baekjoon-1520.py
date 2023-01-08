import sys
sys.setrecursionlimit(10**6)

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dfs(y, x):
    # 해당 위치가 도착점일 경우 1을 반환
    if (y, x) == (M - 1, N - 1):
        return 1

    # -1이 아닐 경우 >> 이미 탐색한 경우
    # 해당 위치의 경우의 수를 반환
    if dp[y][x] > -1:
        return dp[y][x]

    # 4방향으로 뻗어서, 도착하는 경우의 수를 탐색하기
    reachable = 0
    for direction in range(4):
        dy, dx = dyx[direction]
        ny, nx = y + dy, x + dx
        
        if (0 <= ny < M) and (0 <= nx < N):
            # 고도가 낮은 쪽으로만 진행
            if field[y][x] > field[ny][nx]:
                reachable += dfs(ny, nx)
    
    # 현재 dp 테이블을 갱신
    dp[y][x] = reachable
    return dp[y][x]


def solution():
    global dp

    # dp 테이블의 값은 현재 위치에서 도착 위치까지 가능한 경우의 수임
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    dfs(0, 0)

    # 시작 위치의 도착점까지 경우의 수가 정답임
    return dp[0][0]


M, N = map(int, input().split())
field = []

for _ in range(M):
    field.append(list(map(int, input().split())))

print(solution())