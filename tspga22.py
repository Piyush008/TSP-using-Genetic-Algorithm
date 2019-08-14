# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:50:45 2019

@author: KIIT
"""

import numpy as np
import matplotlib.pyplot as plt
from random import random
from crossoverodx import odx


#n is the no. of cities and cm is the cost matrix
n=22
cm=[]
f=open('22cities.txt')
for x in range(22):
    cm.append(list(int(y) for y in f.readline().split()))


#function to calculate cost
def cost(seq):
    cost=0;
    for x in range(len(seq)-1):
        cost+=(cm[seq[x]][seq[x+1]])
    return cost
    
#generating random permutations and m is no of parents/Initialization 
m=10
p=[]
for x in range(m):
    p.append((np.random.permutation(n)).tolist())
    for y in range(x):
        while(np.array_equal(p[y],p[x])):
            p[x]=np.random.permutation(n).tolist()

#ng is the number of generations
avg=[]
ng=50000
for generations in range(ng):
    #cost calculation/Fitness assignment
    cp=[]
    for x in range(m):
        cp.append(cost(p[x]))
    
    #printing the cost of current gen
    print("GEN ",generations,":",cp)
    
    avg.append(np.mean(cp))
    
    #Selection
    c=[[]]*m
    for x in range(int(m/2)):
        p1=p2=0
        while(p1==p2):
            tp1,tp2=(int(random()*100)%m),(int(random()*100)%m)
            tp3,tp4=(int(random()*100)%m),(int(random()*100)%m)
            while(tp1==tp2):
                tp2=(int(random()*100)%m)
            while(tp3==tp4):
                tp4=(int(random()*100)%m)
                p1=tp1 if cost(p[tp1])>cost(p[tp2]) else tp2
                p2=tp3 if cost(p[tp3])>cost(p[tp4]) else tp4
        c[2*x],c[2*x+1]=odx(p[p1],p[p2])
    
    
    #Mutation mut is the mutation ratio
    mut=0.5
    nom=int(mut*m)
    for x in range(nom):
        s1=s2=0
        while(s1==s2):
            s1,s2=(int(random()*100)%n),(int(random()*100)%n)
        mn=int(random()*100)%m
        c[mn][s1],c[mn][s2]=c[mn][s2],c[mn][s1]
    
    
    #Cost for child    
    cc=[]
    for x in range(m):
        cc.append(cost(c[x]))
    
    
    #Next generation
    tempc=cc+cp
    tempp=c+p
    nextgen=[x for _,x in sorted(zip(tempc,tempp))]
    p=nextgen[:m]
    
    
    
#final cost
print("Cost: ",cost(p[0]))
genx=[x for x in range(ng)]
plt.plot(genx,avg)
plt.xlabel("Generations")
plt.ylabel("Avg Cost")
plt.title("22 cities")
plt.show()