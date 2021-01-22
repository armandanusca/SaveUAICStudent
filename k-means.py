import math

import pandas as pd
import numpy as np

# the hyperparameter for K-Means Algorithm
k = 3

# hardcoded problem data
inst = np.array([
    [0.25, 0.50],
    [0.50, 0.35],
    [0.25, 0.50],
    [1.00, 0.35],
    [1.40, 0.70],
    [0.50, 0.85],
    [0.25, 1.00],
    [0.75, 1.00],
    [0.35, 1.25],
    [0.85, 1.25],
    [3.25, 0.50],
    [3.50, 0.35],
    [3.00, 1.00],
    [3.25, 0.85],
    [3.45, 0.85],
    [3.75, 0.85],
    [3.25, 1.10],
    [3.00, 3.25],
    [3.25, 3.00],
    [3.10, 3.50],
    [1.00, 2.50],
    [1.20, 2.40],
    [1.25, 2.50],
    [1.50, 2.50],
    [0.65, 2.75],
    [1.20, 2.75],
    [1.37, 2.75],
    [1.00, 3.00],
    [1.10, 3.20],
    [0.85, 3.35],
])


def dist(p1, p2):
    return math.sqrt(pow(p1[0]-p2[0], 2)+pow(p1[1]-p2[1], 2))
def column(matrix, i):
    return [row[i] for row in matrix]

#algoritmul

#initializez centroizii random
centr=np.random.randn(2, k)
clus=[]

#linia0,1 suma coordonate
#linia 2 nr instante, fac media
newclus=[]

D=None
trigger = True

while trigger:
    clus = newclus
    #calculez matricea distanta
    for i in range(k):
        for j in range(inst.shape[0]):
            D[i][j]=dist(inst[j],centr[i])

    #determin clusterele
    #pe fiecare coloana, calculez minimul, iar linia conform minmului devine culoarea/ clusterul din care instanta face parte
    for i in range(inst.shape[0]):
        minpos = column(D, 1).index(min(column(D, 1)))
        clus[i]=minpos
    
    map_clus_inst = {}
    for num, clsut in enumerate(clus):
        map_clus_inst[clsut].append(num)

    clust_pos=[]
    #pozitionez centroidul in mijlocul clusterului format
    for clus_list in map_clus_inst:
        list_clust = map_clus_inst[clus_list].tolist()
        i_sum = 0
        for i_inst in list_clust:
            coordinates = inst[i_inst]
            i_sum += coordinates
        clust_pos[clus_list] = i_sum / len(list_clust)
    #fac media pe fiecare culoare si memorez in newclus

    for i in range(k):
        for j in range(inst.shape[0]):
            D[i][j]=dist(inst[j],clust_pos[i])   
    
    for i in range(inst.shape[0]):
        minpos = column(D, 1).index(min(column(D, 1)))
        newclus[i]=minpos
    
    trigger = (clus != newclus)

print(clust_pos)