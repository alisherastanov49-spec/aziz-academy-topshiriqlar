import math 
import sys 

def apply_op(op, *args):
    if op == 'sum':
        return sum(args)
    elif op == 'prod':
        return math.prod(args)
    
lines = sys.stdin.read().splitlines()
if lines:
    op = lines[0].strip()
    args = [int(x) for x in lines[1].split()]
    print(apply_op(op, *args))