from collections import deque

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

def bfs_path(graph,start,end,path = [],visited = set()):
    path = [start]
    q = deque([(start,path)])
    
    while q:
        (node,path) = q.popleft()
        visited.add(node)
        if node == end:
            return path
        for i in graph[node]:
            if i not in visited:
                q.append((i,path+[i]))
                visited.add(i)

def dfs_path_iterative(graph,start,end,path =[] ,visited =set()):
    stack = [(start,[start])]
    while stack:
        (node,path) = stack.pop()
        if node == end:
            return path
        for i in graph[node]:
            if i not in visited:
                stack.append((i,path+[i]))
                visited.add(i)
    
def dfs_path_recursive(graph,start,end, path =[] ,visited =set()):
    visited.add(start)
    if start == end:
        print(path) 
    if not path:
        path.append(start)
    for i in graph[start]-visited:
        if i not in visited:
            visited.add(i)
            dfs_path_recursive(graph, i, end,path + [i],visited)


print(bfs_path(graph,"0","3"))
print(dfs_path_iterative(graph, "0", "2"))
dfs_path_recursive(graph,"0","2")