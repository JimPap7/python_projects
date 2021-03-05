import argparse
import json
import math
import sys


 
#
# Define the find grammar module
#
def find_grammar(input_fl):

    lines = []
    min_x = sys.maxsize
    min_y = sys.maxsize
    max_x = -min_x
    max_y = -min_y
    step  = 0

    with open(input_fl) as input_file:
        for line in input_file:
            points = line.strip().split(') (')
            point_1 = [ float(x) for x in points[0][1:].split(',') ]
            point_2 = [ float (x) for x in points[1][:-1].split(',') ]
            min_x = min(min_x, min(point_1[0], point_2[0]))
            min_y = min(min_y, min(point_1[1], point_2[1]))        
            max_x = max(max_x, max(point_1[0], point_2[0]))
            max_y = max(max_y, max(point_1[1], point_2[1]))
            max_dx = abs(point_1[0] - point_2[0])
            max_dy = abs(point_1[1] - point_2[1])
            step   = max(step, abs(max_dx - max_dy))
            lines.append([point_1, point_2])

    S=""
    prv_angle = 0;

    dictA = {}
    dictC = {}
    dictB = {}
    listA = []
    listB = []
    reverse = {}
    reverse["F"] = "G"
    reverse["G"] = "F"
    reverse["-"] = "+"
    reverse["+"] = "-"

    for x in lines:
        x1 = x[0][0]
        y1 = x[0][1]
        x2 = x[1][0]
        y2 = x[1][1]
        dx = x2 - x1
        dy = y2 - y1

        new_angle = math.degrees(math.atan2(dy, dx))

        angle = new_angle - prv_angle
        if angle > 180:
            angle = 180 - angle
        if angle < -180:
            angle = 360 + angle

        if angle > 0:
            S += "+"
        elif angle < 0:
            S += "-"


        center_X = x1 + (x2 - x1) / 2
        center_Y = y1 + (y2 - y1) / 2

        if x2 > x1:
            center_left  = (center_X, y1 + step / 2)
            center_right = (center_X, y1 - step/2)
        elif x2 < x1:
            center_right = (center_X, y1 + step / 2)
            center_left  = (center_X, y1 - step / 2)
        elif y2 > y1:
            center_left  = (x1 - step / 2 ,center_Y)
            center_right = (x1 + step / 2 ,center_Y)
        elif y2 < y1: 
            center_right = (x1 - step / 2 ,center_Y) 
            center_left  = (x1 + step / 2 ,center_Y)


        if center_right[0] * center_right[1] > 0  and center_right[0] <= max_x and center_right[1] <= max_y:
            if center_right not in dictC:
                listA.append((center_right, 'G'))
            else:
                listB.append((center_right, 'G'))


        if center_left[0] * center_left[1] > 0  and center_left[0] <= max_x and center_left[1] <= max_y:
            if center_left not in dictC:
                listA.append((center_left, 'F'))
            else:
                listB.append((center_left, 'F'))

        if len(listA) > 0:
            S = S + str((listA[0])[1])
            dictA[str(x)] = len(S) - 1
            dictC[listA[0][0]] = x
            if len(listA) == 2 or len(listB) > 0:
                if len(listA) == 2:
                    dictB[str(x)] = (listA[1])[0]
                else:
                    dictB[str(x)] = (listB[0])[0] 

        else:
            fixed = True
            l = 0
            while fixed:
                conflict = True
                t = S
                t = t + listB[l][1]
                k = len(t) - 1
                sc = listB[l][0]
                h = sc
                j  = str(dictC[sc])
                while conflict:
                    if str(j) in dictB:
                        sc = dictB[str(j)]
                        p = dictA[str(j)]
                        t = t[:p] + reverse[t[p]] + t[(p + 1):]
                        if dictB[str(j)] in dictC:
                            j = dictC[sc]
                        else:
                            conflict = False
                            fixed = False
                            S = t
                            dictC[h] = x
                            dictA[str(x)] = k
                    else:
                        conflict = False
                        l = l + 1
        listA.clear()
        listB.clear()    
        prv_angle = new_angle

    new_angle = 0
    angle = new_angle - prv_angle
    if angle > 0:
        S += "+"
    elif angle < 0:
        S += "-"

    sl = len(S) - 1
    t = ''
    while sl > -1:
        t = t + reverse[S[sl]]
        sl -= 1

    print(S)
    print(t)
#
# End of find grammar
#

#
# Define the parse grammar module
#
def parse_grammar(switch, input_fl, output_fl):

    with open(input_fl) as json_file:
        try:
            data = json.load(json_file)
        except ValueError as e:
            print(input_fl + " is not a valid json file")
            return


    axiom = data["axiom"]
    left_angle = data["left_angle"]
    right_angle = data["right_angle"]
    step_length = data["step_length"]
    order = data["order"]
    step_length = data["step_length"]
    start_angle = data["start_angle"]
    rules = data["rules"]



    mystr = axiom
    for rep in range(order):
        new_str = []
        for i in range(len(mystr)):
            ch = mystr[i]
            if ch in rules:
                new_str.append(rules[ch])
            else:
                new_str.append(ch)
        mystr = ''.join(new_str)


    if switch:
        print(mystr)


    if output_fl is  None:
        return

    i = 0
    c = []
    k = []
    l = (0,0)
    lk = []

    angle = start_angle
    while i != len(mystr):
        if mystr[i] == "-":
            angle = angle - left_angle
        elif mystr[i] == "+":
            angle = angle + right_angle
        elif mystr[i] == "[":
                lk.append((l,angle))
        elif mystr[i] == "]":
                 l,angle = lk.pop()
        elif mystr[i] <= "L":
             x = l[0] + step_length * math.cos(math.radians(angle))
             y = l[1] + step_length * math.sin(math.radians(angle))
             x = round(x,2)
             y = round(y,2)
             result = (x,y)
             k.append((l,result))
             l = result
        i += 1

    file = open(output_fl,"w")
    for s in k:
        a = ''.join(str(s[0]))
        b = ''.join(str(s[1]))
        file.write(a + " " + b + "\n")
    file.close()
#
# End of parse grammar
#



parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Enter the L-grammar")
parser.add_argument("output_file", nargs='?', help="Output File")
parser.add_argument("-m", action="store_true", help="display Tree")
parser.add_argument("-d", action="store_true", help="find grammar")
args = parser.parse_args()


if args.m and args.d:
    print("Enter -m OR -d switch")
    sys.exit()
    
if args.output_file is not None and args.d:
    print("usage: lsystem.py -d input_file")
    print("lsystem.py: error: -d switch accept only one file name")
    sys.exit()
    
if args.d:
    find_grammar(args.input_file)
else:
    parse_grammar(args.m, args.input_file, args.output_file)

    
   
