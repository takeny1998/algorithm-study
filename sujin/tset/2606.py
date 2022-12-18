n = int(input())
k = int(input())

graph = {i : list() for i in range(1,n+1)}
visited = [0] * (n+1)
cnt = 0

for _ in range(k):
    x, y = map(int, input().split())
    graph[x] = graph.get(x) + [y]
    graph[y] = graph.get(y) + [x]

def dfs(graph):
    cnt = 0
    stack = [1]
    
    while stack:
        current_node = stack.pop()
        visited[current_node]  = True  
        cnt += 1           
        
        for next_node in graph[current_node]:
            if not visited[next_node]: 
                stack.append(next_node)
    print("cnt",cnt)
    return visited

result = dfs(graph)
# for i in result:
#     if i:
#         cnt += 1

# print(cnt-1)
    

    