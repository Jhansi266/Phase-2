def initiatedbfstraversal(node,visited,matrix,result):
    Q = [node]
    visited[node] = True 
 
    while len(Q) > 0:
        curr = Q.pop(0)
        result.append(curr)
        for neighbour in matrix[curr]:
            if visited[neighbour] == False:
                visited[neighbour] = True 
                Q.append(neighbour)

def bfstraversal(matrix,n):
    visited=[False]*n
    result=[]
    for node in range(n):
        if visited[node]==False:
            initiatedbfstraversal(node,visited,matrix,result)
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
bfstraversal(matrix,n)
