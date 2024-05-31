n,m=map(int,input().split())
matrix=[]
for i in range(n):
    matrix.append([])
print(matrix)
for i in range(m):
    u,v=map(int,input().split())
    matrix[u].append(v)
    matrix[v].append(u)
print(matrix)
