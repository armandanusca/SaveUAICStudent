import math

import numpy as np

# the hyperparameter for K-Means Algorithm
k =2

# hardcoded problem data
inst = np.array([
    [0.30, 1.75],
    [0.30, 2.00],
    [0.30, 2.25]
])



def dist(p1, p2):
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


def column(matrix, i):
    return [row[i] for row in matrix]

def getmincol(mat,col):
    poz=0
    minim=10000000
    for i in range(mat.shape[0]):
        if minim>mat[i][col]:
            minim=mat[i][col]
            poz=i
    return poz

# algoritmul
# Carol e prost
# initializez centroizii random, convenabil cu instantele alese
centr = np.random.randn(k, 2)%4
newcentr=np.zeros((k, 3))

# coloana 0,1 suma coordonate
# coloana 2 nr instante, fac media
newclus = [0]*inst.shape[0]
D = np.random.randn(k, inst.shape[0])
trigger = True

while trigger:
    clus = newclus
    # calculez matricea distanta
    for i in range(k):
        for j in range(inst.shape[0]):
            D[i][j] = dist(inst[j], centr[i])
    print(centr)
    # determin clusterele
    # pe fiecare coloana, calculez minimul, iar linia conform minmului devine culoarea/ clusterul din care instanta face parte
    for i in range(inst.shape[0]):
        clus[i]=getmincol(D,i)
        newcentr[clus[i]][2]=newcentr[clus[i]][2]+1
        newcentr[clus[i]][0]=newcentr[clus[i]][0]+inst[i][0]
        newcentr[clus[i]][1] = newcentr[clus[i]][1] + inst[i][1]
    print(clus)
    print(newcentr)
    # pozitionez centroidul in mijlocul clusterului format
    for i in range(k):
        if newcentr[i][2]!=0:
            centr[i][0]=newcentr[i][0]/newcentr[i][2]
            centr[i][1]=newcentr[i][1]/newcentr[i][2]
    # fac media pe fiecare culoare si memorez in newclus
    print(centr)
    for i in range(k):
        for j in range(inst.shape[0]):
            D[i][j] = dist(inst[j], centr[i])
    print(D)
    for i in range(inst.shape[0]):
        newclus[i] = getmincol(D,i)
    print(newclus)
    trigger = (clus != newclus)
    print(trigger)

#print(centr)