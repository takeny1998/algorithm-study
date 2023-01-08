import sys
input = sys.stdin.readline

n = int(input()) # 퇴사 D-n
date, pay = [], []

dp = [0 for _ in range(n + 1)]

for i in range(n): # 리스트에 다 담기
    t, p = map(int, input().split()) 
    date.append(t)
    pay.append(p)
money = 0
for i in range(n): #0~6
    if date[i] + i <= n:
        # dp[i+date[i]-1] = pay[i]
        dp[i+date[i]] = max(dp[i+date[i]], dp[i] + pay[i])
    dp[i+1] = max(dp[i], dp[i+1])
print(max(dp))
