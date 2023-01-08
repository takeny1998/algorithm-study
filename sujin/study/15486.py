# 상담 N일동안 최대한 많은 상담
# 상담 완료 기간 T/ 상담을 했을 때 받을 수 있는 금액 P
# 가치 구하기, 배낭문제와 같음
import sys 

n = int(sys.stdin.readline())
t, p = [], []
dp = [0] * (n+1)

for _ in range(n):
    ti, pi = map(int, sys.stdin.readline().split())
    t.append(ti)
    p.append(pi)

k = 0
for i in range(n):
    k = max(k, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])

print(max(dp))
    


    
