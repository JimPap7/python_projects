import sys



def create_pq():
    return []

def add_last(pq, c):
    pq.append(c)

def root(pq):
    return 0

def set_root(pq, c):
    if len(pq) == 0:
        pq = [c]
    else:
        pq[0] = c

def get_data(pq, p):
    a = pq[p]
    return a[0]

def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]

def parent(p):
    return (p - 1) // 2

def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]


def extract_last_from_pq(pq):
    return pq.pop()



def has_children(pq, p):
    return 2*p + 1 < len(pq)



def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c
        exchange(pq, i, j)
        i = j
    return c

def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i) < get_data(pq, parent(i)):
        p = parent(i)
        exchange(pq, i, p)
        i = p

def kCores(G):
    mh = create_pq()
    d = []
    p = []
    core = []
    for x in range(len(G)):
        d.append(len(G[x]))
        p.append(d[x])
        core.append(0)
        pn = [p[x], x]
        insert_in_pq(mh, pn)
    while len(mh) > 0:
        t = extract_min_from_pq(mh)
        core[t[1]] = t[0]
        if len(mh) != 0:
            for x in G[t[1]]:
                d[x] = d[x] - 1
                opn = [p[x], x] 
                p[x] = max(t[0], d[x])
                npn = [p[x], x]
                UpdatePQ(mh, opn, npn)
    return core


def UpdatePQ(mh, opn, npn):
    t=len(mh)-1
    k=-1
    while t>0 and k==-1:
        if mh[t] == opn:
            k=t
            break
        t = t-1
    if k!=-1:
        mh[k]=npn
        if npn < opn:
            while(k != 0 and get_data(mh, parent(k)) > get_data(mh, k)):
                mh[k],mh[parent(k)] = (mh[parent(k)],mh[k])
                k=parent(k)
        elif npn > opn:
            while has_children(mh, k):
                j = min(children(mh, k), key=lambda x: get_data(mh, x))
                if get_data(mh, k) < get_data(mh, j):
                    break
                exchange(mh, k, j)
                k=j
    
    
    
    

input_filename = sys.argv[1]
g = {}

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


k = kCores(g)

for x in range(len(k)):
    print(x,  " ",  k[x])
