# numbers를 사용해서 -,+를 해서 target숫자로 만들기
# 1이상 1000이하일때 가능
from collections import deque

numbers = [1, 1, 1, 1, 1]
visited = [False] * len(numbers)
target = 3
print(visited)

def bfs(index):
    visited[index] = True
    current = numbers[index]
    
    for cal in "-","+":
        index += 1
        after = eval(str(current)+cal+str(numbers[index]))
        print(after)
        if after <= 0 or after >= 1000:
            continue
        if not visited[index]