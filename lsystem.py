import argparse
import json
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="Enter the L-grammar")
parser.add_argument("output_file", nargs='?', help="Output File")
parser.add_argument("-m", action="store_true", help="display Tree")
args = parser.parse_args()


 

with open(args.input_file) as json_file:
    try:
        data = json.load(json_file)
    except ValueError as e:
        print("invalid json file")
        sys.exit(1)


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


if args.m:
    print(mystr)

    
if args.output_file is  None:
    sys.exit(0)
    
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
    elif mystr[i] == "F":
         x = l[0] + step_length * math.cos(math.radians(angle))
         y = l[1] + step_length * math.sin(math.radians(angle))
         x = round(x,2)
         y = round(y,2)
         result = (x,y)
         k.append((l,result))
         l = result
    i += 1

file = open(args.output_file,"w")
for s in k:
    a = ''.join(str(s[0]))
    b = ''.join(str(s[1]))
    file.write(a + " " + b + "\n")
file.close()
