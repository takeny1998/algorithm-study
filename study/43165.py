# numbers를 사용해서 -,+를 해서 target숫자로 만들기
# 1이상 1000이하일때 가능
from collections import deque

numbers = [1, 2, 3, 4, 5]

target = 3

def dfs(idx, result):
    visited = [False] * len(numbers)
    stack = []

    for cal in "-","+":
        totalNum += int(cal+str(numbers[index]))
        # if index == (len(numbers)-1):
        dfs(string)
        dfs(string) 
        # print("cal+number[index]: ",cal,numbers[index])
        # print("total: ",totalNum)
        # if not visited[index]:
        #     dfs(totalNum, index+1)
    # print(total)

total = ""
dfs(0,0)
