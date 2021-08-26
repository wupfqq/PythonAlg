def Dej(n,top,matr):
    state=[True for x in range(n)]
    dist=[10000 for x in range(n)]
    dist[top]=0
    for x in range(n):
        min_dist=1000000
        #di=-1
        for y in range(n):
            if dist[y]<min_dist and state[y]:
                min_dist=y
                di=y
        for a in range(n):
            if dist[di]+matr[di][a]<dist[a] and matr[di][a]:
                dist[a]=dist[di]+matr[di][a]
        state[di]=False
    return dist

gr_matrix=[[0,10,5,10, 0],
           [0, 0, 0,0,10],
           [0, 0, 0,15,30],
           [0, 0, 0, 0,10],
           [0, 0, 0, 0, 0]]

q=Dej(5,1,gr_matrix)   #если 0 или 10000 то пути неть
print(q)