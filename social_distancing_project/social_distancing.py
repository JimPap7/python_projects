
# coding: utf-8

# In[ ]:


import math, argparse, sys, random

def calculateNewCircle(centers,Cm, Cn,r):
    nx = Cn[0]
    ny = Cn[1]
    mx = Cm[0]
    my = Cm[1]
    dx = nx - mx
    dy = ny - my
    d = math.sqrt(dx ** 2 + dy ** 2)
    r1 = centers[Cm] + r
    r2 = centers[Cn] + r
    l = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * (d ** 2))
    e = math.sqrt((r1 ** 2 / d ** 2) - l ** 2)
    kx = round(mx + l * dx - e* dy,2)
    ky = round(my + l * dy + e* dx,2)
    return (kx, ky)

def DistanceFromLine(c,line):
    ux = line[0][0]
    uy = line[0][1]
    nx = line[1][0]
    ny = line[1][1]
    cx = c[0]
    cy = c[1]
    l2 = (ux - nx) ** 2 + (uy - ny) ** 2
    if l2 == 0:
        d = round(math.sqrt((ux - cx) ** 2 + (uy - cy) ** 2),2)
        return d
    t = ((cx - ux) * (nx - ux) + (cy - uy) * (ny - uy)) / l2
    t = max(0, min(1,t))
    px = ux + t * (nx - ux)
    py = uy + t * (ny - uy)
    d = round(math.sqrt((px - cx) ** 2 + (py - cy) ** 2),2)
    return d

def FindMinDist(front):
    minv = sys.maxsize
    for x in front:
        if front[x][2] == 1: # Is alive 
            if front[x][3] < minv:
                minv = front[x][3]
                minCircle = x
            elif front[x][3] == minv:
                if front[x][1] < front[minCircle][1]:
                    minCircle = x
    return minCircle

def findprobCircle(front,Ci,Cn,Cm,r):
  min = sys.maxsize
  a = (None,None)
  probList = []
  probCircle = None
  for x in front:
      x1 = x[0]
      y1 = x[1]
      x2 = Ci[0]
      y2 = Ci[1]
      dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      tmp1 = round(dist,2)
      tmp2 = round(float(r + storeCenters[x]),2)
      if tmp1 < tmp2 and x != Cn and x != Cm:
          probList.append(x)
  p = len(front) - 2
  for x in probList:
      s = 0
      z = Cn
      while z != x:
         z = front[z][0]
         s +=1        
      if s > math.ceil(p / 2) and  len(front) - (s+1) < min:
           a = (x,1)
           min = len(front) - (s+1)
      elif s <= math.ceil(p / 2) and s <= min:
           a = (x,2)
           min = s
  return a

parser = argparse.ArgumentParser()
parser.add_argument("-items","--items", "-ITEMS", "--ITEMS", dest="ITEMS", type=int)
parser.add_argument("-radius","--radius", "-RADIUS", "--RADIUS", dest="RADIUS",type=int)
parser.add_argument("--min_radius", dest="MIN_RADIUS",type=int)
parser.add_argument("--max_radius", dest="MAX_RADIUS",type=int)
parser.add_argument("-boundary", "--boundary", "-BOUNDARY", "--BOUNDARY",dest="BOUNDARY",type=str)
parser.add_argument("-seed","--seed", "-SEED", "--SEED",dest="SEED",type=int)
parser.add_argument("output_file",type=str)

args = parser.parse_args()
max_items = sys.maxsize
Title = args.output_file

if args.ITEMS:    
    max_items = args.ITEMS
    
if args.RADIUS:
    r = args.RADIUS
    r1, r2 = r,r
    
if args.SEED:
    random.seed(args.SEED)
    
if args.MIN_RADIUS and args.MAX_RADIUS:
    q = args.MIN_RADIUS
    w = args.MAX_RADIUS
    r1 = random.randint(q,w)
    r2 = random.randint(q,w)
    
lines = []

if args.BOUNDARY:
    bounds = args.BOUNDARY
    with open(bounds) as graph_input:
        for line in graph_input:
            nodes = [float (x) for x in line.split()]
            if len(nodes) != 4:
                continue
            x = (nodes[0], nodes[1])
            y = (nodes[2], nodes[3])
            z = (x,y)
            lines.append(z)
            
            
storeCenters = {}
front = {}
rad = r1 + r2
C1 = (0,0)
C2 = (rad,0)
storeCenters[C1]=r1
storeCenters[C2]=r2
front[C1] = (C2,1,1,0)
front[C2] = (C1,2,1,rad)
backup_front = {}
min_dis_cir= set()
s = 2
t = 2
if args.MIN_RADIUS and args.MAX_RADIUS:
     r = random.randint(q,w)
        
        
while t > 0   and s < max_items: #STEP 2
    Cm = FindMinDist(front)
    backupCircle = Cm
    min_dis_cir.add(Cm)
    flag = True
    Cn = front[Cm][0]
    Ci = calculateNewCircle(storeCenters, Cm, Cn, r)
    (Cj,section) = findprobCircle(front,Ci,Cn,Cm,r)
    while Cj is not None: #STEP 3
            if section == 1:
                stop = front[Cj][0]           
                while stop != Cn:
                    if stop not in backup_front:
                         backup_front[stop] = front[stop]
                    pv = front[stop][0]
                    del front[stop]
                    stop = pv
                    t -= 1
                if Cj not in backup_front:
                    backup_front[Cj] = front[Cj]
                front[Cj] = (Cn,front[Cj][1],front[Cj][2],front[Cj][3])
                Cm = Cj
            else:
                stop = front[Cm][0]
                while stop != Cj:
                    if stop not in backup_front:
                        backup_front[stop] = front[stop]
                    pv = front[stop][0]
                    del front[stop]
                    stop = pv
                    t -= 1
                if Cm not in backup_front:
                    backup_front[Cm] = front[Cm]
                Cn=Cj
                front[Cm] = (Cj,front[Cm][1],front[Cm][2],front[Cm][3])
            Ci = calculateNewCircle(storeCenters, Cm, Cn, r)
            (Cj,section) = findprobCircle(front,Ci,Cn,Cm,r)
    for z in lines:
        DistFromLine = DistanceFromLine(Ci,z)
        if DistFromLine < r:
            Ci = None
            break
    if Ci is not None:
        s += 1
        t += 1
        storeCenters[Ci] = r
        distFromStart = round(math.sqrt(Ci[0] ** 2 + Ci[1] ** 2),2)
        front[Ci] = (Cn, s , 1, distFromStart)
        front[Cm] = (Ci,front[Cm][1],front[Cm][2],front[Cm][3])
        for o in min_dis_cir:
            if o in front:
                front[o] = (front[o][0],front[o][1],1,front[o][3])
        min_dis_cir.clear()
        if args.MIN_RADIUS and args.MAX_RADIUS:
            r = random.randint(q,w)
    else:
        for x in backup_front:
            if x not in min_dis_cir:
                front[x] = (backup_front[x][0], backup_front[x][1],1,backup_front[x][3])
                t += 1
            else:
                front[x] = (backup_front[x][0], backup_front[x][1],0,backup_front[x][3])
                t  -= 1
        front[backupCircle] = (front[backupCircle][0], front[backupCircle][1], 0, front[backupCircle][3])
    t = len(front) - len(min_dis_cir)
    backup_front.clear()
    
    
f = open(Title, 'w')

for x in storeCenters:
     f.write('{:.2f} {:.2f} {:d}\n'.format(x[0],x[1],storeCenters[x]))
        
        
if args.BOUNDARY:
    for x in lines:
        f.write('{:.2f} {:.2f} {:.2f} {:.2f}\n'.format(x[0][0],x[0][1],x[1][0],x[1][1]))
        
f.close()

print(s)

