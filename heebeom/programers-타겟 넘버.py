from itertools import product

def cal(numbers, signs):
    result = 0

    for i in range(len(numbers)):
        if signs[i] == 0:
            result += numbers[i]
        else:
            result += (numbers[i] * -1)
    
    return result


def solution(numbers, target):

    answer = 0

    for signs in product([0, 1], repeat = len(numbers)):
        if cal(numbers, signs) == target:
            answer += 1

    print(answer)
    return answer

solution([4, 1, 2, 1], 4)