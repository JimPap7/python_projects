
# coding: utf-8

# In[ ]:


import pprint,argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("-p", "--verbose", action="store_true")


Polyo={}

SDep = int(input("Enter number of squares : "))
S = 1
T = 2 - SDep
for A in range(T, 0):
    for L in range(1, S+1):
        X = A
        Y = L
        s = X+1
        t = Y+1
        B = (s,Y)
        K = (X,t)
        D = (X,Y)
        if D not in Polyo.keys():
            Polyo[D] = []
        Polyo[D].insert(0,B)               
        Polyo[B] = []
        Polyo[B].insert(1,D)
        if L != S:
            if K not in Polyo.keys():
                Polyo[K] = []
            Polyo[D].insert(1,K)
            Polyo[K].append(D)
    S+= 1
S = SDep
for A in range(0,SDep):
    for L in range(0, S):
        X = A
        Y = L
        s = X+1
        t = Y+1
        B = (s,Y)
        K = (X,t)
        D = (X,Y)
        if D not in Polyo.keys():
            Polyo[D] = []
        if L != S-1:
            Polyo[D].insert(0,B)
            Polyo[B] = []
            Polyo[B].append(D)
            Polyo[D].insert(1,K)
            if K not in Polyo.keys():
                Polyo[K] = []
            Polyo[K].append(D)
    S-= 1

print(Polyo[(0,0)])
        
    


# In[ ]:


ff
dd

