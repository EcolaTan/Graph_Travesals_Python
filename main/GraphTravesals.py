from collections import deque

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

def bfs(graph,start):
    q = deque([start])
    visited = set(start)

    while q:
        node = q.popleft()
        print(node, end = " ")
        for i in graph[node]:
            if i not in visited:
                visited.add(i)
                q.append(i)
    print()

def dfs_iterative(graph,start,visited = set()):
    stack = [start]

    while stack:
        node = stack.pop()
        visited.add(node)
        for i in graph[node]:
            if i not in visited:
                stack.append(i)
    return visited
            

def dfs_recursive(graph,start,visited = set()):
    visited.add(start)

    for i in graph[start]:
        if i not in visited:
            dfs_recursive(graph, i,visited)
    return visited


bfs(graph,"0")
print(dfs_recursive(graph, "0"))
print(dfs_iterative(graph, "0"))
    
