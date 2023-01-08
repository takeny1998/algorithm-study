
def solution(m, n, puddles):
    # 필드 크기와 같은 DP 배열 생성하기
    # DP 배열의 값은 해당 위치까지 도달할 수 있는 경로의 수의 합임
    dp = [[-1 for _ in range(m)] for _ in range(n)]
    puddle_field = [[False for _ in range(m)] for _ in range(n)]
    
    # 물웅덩이는 지나갈 수 없음 = 도달할 수 없음
    # 그러므로 물웅덩이의 값은 0임
    for (x, y) in puddles:
        dp[y - 1][x - 1] = 0
        puddle_field[y - 1][x - 1] = True
    
    dp[0][0] = 1
     
    # 최좌상단에서 최우하단 밑에 도달할 수 있는 최소거리를 구하므로
    # (n, m)의 구할 경로는 [(n - 1, m)의 경로의 합 + (n, m - 1)의 경로의 합임]
    # 즉 dp[n][m] = dp[n - 1][m] + dp[n][m - 1]
    for y in range(n):
        for x in range(m):
            # 물웅덩이는 지나칠 수 없음
            if not puddle_field[y][x]:
                # 위 점화식 적용하기
                if y > 0:
                    dp[y][x] += dp[y - 1][x]
                if x > 0:
                    dp[y][x] += dp[y][x - 1]
                        
    return dp[n - 1][m - 1] % 1000000007