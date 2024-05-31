def initiateDFSTraversal(node, visited, matrix, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in matrix[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, matrix, result)
 
def dfstraversal(matrix,n):
    visited=[False]*n
    result=[]
    for node in range(n):
        if visited[node]==False:
            initiateDFSTraversal(node,visited,matrix,result)
    print("bfs traversal is:",result)


n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append([])
print(matrix)
for i in range(m):
    u,v=map(int,input().split())
    matrix[u].append(v)
    matrix[v].append(u)
dfstraversal(matrix,n)
