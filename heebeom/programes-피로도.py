def permutations(arr:list, d:int):
    for i in range(len(arr)):
        if d == 1:
            yield [arr[i]]
        else:
            for next in permutations(arr[:i] + arr[i+1:], d - 1):
                yield [arr[i]] + next


def check_explore(
    order:list[int], 
    fatigue:int, 
    dungeons:list[list[int, int]]):

    order.reverse()

    while order:
        min_fatigue, cost_fatigue = dungeons[order.pop()]
        if fatigue < min_fatigue:
            return (DUNGEON_NUM - len(order) - 1)

        fatigue -= cost_fatigue

    return (DUNGEON_NUM - len(order))
        

def solution(k:int, dungeons:list[list[int, int]]):
    global DUNGEON_NUM
    DUNGEON_NUM = len(dungeons)
    answer:int = -1

    num_range:list[int] = list(range(DUNGEON_NUM))

    for order in permutations(num_range, DUNGEON_NUM):
        answer = max(answer, check_explore(order, k, dungeons))

    return answer