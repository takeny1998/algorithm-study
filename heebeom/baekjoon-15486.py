import sys 
input = sys.stdin.readline 

def solution():
    # dp 테이블의 값은 해당 날짜까지 얻을 수 있는 돈의 최댓값임
    # 테이블의 길이는 N + 1임, 왜냐하면 돈은 그 다음날에 받을 수 있기 때문
    dp = [0 for _ in range(N + 1)]

    max_value = 0
    
    for index, (cost, money) in enumerate(counsel):
        # 현재 dp 테이블의 값은, 현재값과 이전 최댓값 중에 큰 값임
        max_value = max(dp[index], max_value)

        # dp 테이블에 마칠때 (현재 최대금액 + 상담금액)
        # (현재까지 얻은 최대 돈 + 현재 상담을 끝내고 받은 돈)과 기존 최댓값 비교
        if (index + cost) <= N:
            dp[index + cost] = max(max_value + money, dp[index + cost])

    return max(dp)


N = int(input())
counsel = []

for _ in range(N):
    cost, money = map(int, input().split())
    counsel.append((cost, money))

print(solution())