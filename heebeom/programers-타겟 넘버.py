def dfs(idx, val, numbers, target):
    global answer
    if idx == len(numbers):
        if val == target:
            answer += 1
        return
    
    dfs(idx + 1, val + numbers[idx], numbers, target)
    dfs(idx + 1, val - numbers[idx], numbers, target)


def solution(numbers, target):
    global answer

    answer = 0
    
    dfs(0, 0, numbers, target)
    print(answer)
    return answer
