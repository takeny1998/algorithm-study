#등굣길
# 일부 지역 물에 잠김
# 오른쪽, 아래쪽만 움직임
def solution(m, n, puddles):
    #지도 생성 위, 아래를 더하면서 진행할것이라서 윗줄 옆줄 초기값 0 셋팅
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    #웅덩이 셋팅
    for deleteY, deleteX in puddles:
        dp[deleteY][deleteX] = -1

    #시작점 셋팅
    dp[1][1] = 1


    for y in range(1,n+1):
        for x in range(1, m+1):
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            # if puddles:
                # if y == puddles[0][0] and x == puddles[0][1]:
                    # del puddles[0]
                    # continue
            dp[y][x] += dp[y-1][x] + dp[y][x-1]
        
    return dp[n][m] % 1000000007
            
print(solution(4, 3, [[2,2]]))