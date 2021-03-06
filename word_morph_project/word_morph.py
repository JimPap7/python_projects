import sys
import editdistance
from collections import deque

input_dictionary = sys.argv[1]
start_word = sys.argv[2]
finish_word = sys.argv[3]
Distance = editdistance.eval(start_word, finish_word)
g = {}

def IsEmpty(g):
   if len(g) == 0:
      return true
   else:
      return false

def SetRoot(g, node):
   g[node] = []

def GetRoot(g):
   return list(g.keys())[0]

def GetChildNode(bk, Ldistance, parent):
    for (u, w) in bk[parent]:
       if u == Ldistance:
          return w
    return null

def AddChildNode(parent, Ldistance, bk, node):
   bk[parent].append((Ldistance, node))
   bk[node] = [] 

def BKInsertTree(g, Inode):
   if IsEmpty(g):
      SetRoot(g, node)
   node = GetRoot(g)
   while node != null:
       Ldistance = editdistance.eval(node, nodeI)
       parent = node
       node = GetChildNode(bk, Ldistance, node)
       if node == null:
           AddChildNode(parent, Ldistance, bk, Inode)

with open(input_dictionary) as graph_input:
    for line in graph_input:
       node = line.strip()
       if node:
          BKInsertTree(g, node)


def CreateSet():
    return set()

def CreateQueue():
    return deque()

def Enqueue(to_check, s):
    to_check.leftappend(s)

def Dequeue(to_check):
    to_check.pop()


def IsQueueEmpty(to_check):
    if len(to_check) == 0:
       return true
    else:
       return false


def AddToSet(results, k):
    results.add(k)


def BKsearch(r, bk, word):  
    results = CreateSet()
    to_check = CreateQueue()
    Enqueue(to_check, GetRoot(bk))
    while not IsQueueEmpty(to_check):
        node = Dequeue(to_check)
        dist = editdistance.eval(word, node)
        if dist <= r:
            AddToSet(results, (node, dist))
        l = dist - r
        s = dist + r
        for (u, w) in bk[node]:
            if u <= s and u >= l:
                Enqueue(to_check, w)
    return results

s = BKsearch(Distance, g, finish_word)
t = {}
f = {}
for x in s:
    BKInsertTree(t, x[0])
    f[x[0]] = x[1]
k = {}
for x in s:
    h = x[0]
    k[h] = []
    r = BKsearch(1, t, h)
    for g in r:
        if g[0] != h:
            k[h].append((g[0], f[g[0]]))


def dijkstra_Star(k, start_word, finish_word):
    dist = {}
    pred = {}
    Open_Set = {}
    for x in k.keys():
        dist[x] = MAX_INT
        pred[x] = None
        Open_Set[x] = MAX_INT
    Open_Set[start_word] = 0
    dist[start_word] = 0
    el_in_q = 1
    current = ""
    while el_in_q != 0 and current !=  finish_word:
        current = min(Open_Set, key = lambda x: Open_Set.get(x))
        el_in_q -= 1
        Open_Set[current] = MAX_INT
        if current == finish_word:
            return get_path(pred, current)
        for (x, e) in k[current]:
            if dist[x] == MAX_INT:
                el_in_q += 1 
            if dist[x] > dist[current] + E:
                dist[x] = dist[current] + E
                pred[x] = current
                Open_Set[k] = dist[k]
    return pred   
    
     






pred = dijkstra_Star(k,start_word, finish_word)



def get_path(pred, current):
    total_path = [current]
    while pred[current] != None:
        current = pred[current]
        total_path.append(current)
    return total_path[:-1]


if pred is None:
   print(start_word)
else:
   TotalPath = get_path(pred, start_word)
   for x in TotalPath:
      print(x, end = ', ')


