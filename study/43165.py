# numbers를 사용해서 -,+를 해서 target숫자로 만들기
# 1이상 1000이하일때 가능


def solution(numbers, target):
    #index를 넘어가는 로직이기때문에 마지막에 0 추가
    numbers.append(0)

    #초기값 설정
    stack = [(0,0)]
    answer = 0

    #dfs
    while stack:
        index, result = stack.pop()
        #만약 주어진 배열의 index를 넘어갈때 결과값을 보고 answer에 추가 
        if index == (len(numbers))-1:
            if result == target:
                answer += 1
            continue
        #index가 넘어가지 않을 경우 그대로 반복
        else:
            stack.append((index+1, result - numbers[index]))
            stack.append((index+1, result + numbers[index]))
    return answer


numbers = [4, 1, 2, 1]
target = 4

# numbers = [1, 1, 1, 1, 1]
# target = 3
print(solution(numbers, target))


    