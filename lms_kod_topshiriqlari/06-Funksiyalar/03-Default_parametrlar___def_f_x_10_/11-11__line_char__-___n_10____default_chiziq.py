import sys
def line(char='-', n=10):
    print(char * n)
args = sys.stdin.read().split()
if len(args) == 0:
    line()
elif len(args) == 1:
    if args[0].isdigit():
        line(n=int(args[0]))
    else:
        line(char=args[0])
else:
    line(char=args[0], n=int(args[1]))