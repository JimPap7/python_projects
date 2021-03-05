import argparse
from collections import deque 
g = {}


parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the number of repetitions")
parser.add_argument("y", type=String, help="the filename")
parser.add_argument("-c", "--verbose", action="store_true")
parser.add_argument("-r", "--Radius",nargs = ?, default ="d")

args = parser.parse_args()

input_filename = args.y
Num = args.x
IF args.Radius != D:
    Limit = args.Radius


with open(input_filename) as graph_input:
    for line in graph_input:
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        g[nodes[0]].append(nodes[1])
        g[nodes[1]].append(nodes[0])

Final = {}

if args.Radius !=D:
   InfPoints = {}
   flag = true
   Theta = getTheta(Limit,G)
   InfPoints = CalcPoints(G,Theta)

    for i in range(1,num + 1):
        MaxInf = getMax(InfPoints,true)
        Final[MaxInf] = InfPoints[MaxInf]
        S =  getAll(g, node,limit)  
        G = UpdateGraph(G, MaxInf)
        InfPoints = UpdatePoints(S,InfPoints,Theta,MaxInf)      
elif args.verbose:
    flag = false
    For i in range(1,num + 1):
        MaxInf = getMax(G, false)
        Final[MaxInf] = len(G[MaxInf])
        UpdateVectors(G, MaxInf)

For key in Final:
    print(key, Final[key])





def getTheta(Limit,G):
     c = {}
     For key in G:
           c[key] = Perimeter(g, key,limit)
     return c



def UpdatePoints(S,InfPoints, Theta,MaxInf):
       del InfPoints[MaxInf]
       For z in S:
             For k in Theta[z]:
                   sum += (len(G[k]) - 1)
              InfPoints[z] = (len(G[z]) - 1) * sum
        return InfPoints











def CalcPoints(G,Theta):
     sum = 0
     InfPoints = {}
     For key in G:
           p = len(G[key]) - 1
           for x in Theta:
               sum += (len(G[x]) - 1)
           InfPoints[key] = p * sum
           sum = 0
      return InfPoints
               





Def getMax(G,flag):
      max = -1
      For key in G:
             if flag:
                 k = g[key]
             else:
                 k = len(g[key])
             if k > max:
                   max = k
                   maxVector = key
             elif k = max and MaxVector < key:
                   maxVector = key
       return MaxVector



       

Def UpdateGraph(G MaxInf):
     List = G[MaxInf]
     del G[MaxInf]
     For key in List:
              G[key].remove(MaxInf)
     return G
       
def Perimeter(g, node,limit):
    
    q = deque()
    
    visited = [ False for k in g.keys() ]
    inqueue = [ False for k in g.keys() ]
    q.append("A")
    q.appendleft(node)
    inqueue[node] = True
    r = 0
    while not (len(q) == 0):
        c = q.pop()
        if c = "a":
            r += 1
            q.appendleft("a")
            if r == limit:
                 return q
        else:
            inqueue[c] = False
            visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v]:
                q.appendleft(v)
                inqueue[v] = True

def getAll(g, node,limit):
    
    q = deque()
    list = []
    visited = [ False for k in g.keys() ]
    inqueue = [ False for k in g.keys() ]
    q.append("A")
    q.appendleft(node)
    inqueue[node] = True
    r = 0
    while not (len(q) == 0) and R < Limit + 2:
        c = q.pop()
        if c = "a":
            r += 1
            q.appendleft("a")
        else:
            inqueue[c] = False
            visited[c] = True
        for v in g[c]:
            if not visited[v] and not inqueue[v]:
                list.append(v)
                q.appendleft(v)
                inqueue[v] = True
     return list         
