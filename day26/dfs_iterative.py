def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for neighbor in reversed(graph[node]):
                stack.append(neighbor)



graph = {
    0:[1,2],
    1:[3],
    2:[4],
    3:[],
    4:[]
}

print("\nDFS Iterative:")
dfs_iterative(graph,0)