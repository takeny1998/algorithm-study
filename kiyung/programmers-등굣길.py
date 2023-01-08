def solution(m, n, puddles):
    # 이 문제에서 puddles의 좌표 등 행렬의 좌표 전체가 일반적인 좌표계와 반대방향으로 구성 되어있다고 함.
    puddles = [[q,p] for [p,q] in puddles] # puddles 좌표 반대로
    dp = [[0]* (m+1) for _ in range(n+1)] # dp 행렬 생성
    dp[1][1] = 1 # 점의 위치 (시작위치)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue
            if [i,j] in puddles: # 웅덩이 위치의 경우 값은 0
                dp[i][j] = 0
            else:                # 현재 칸은 왼쪽 칸, 위 칸의 합산
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]


