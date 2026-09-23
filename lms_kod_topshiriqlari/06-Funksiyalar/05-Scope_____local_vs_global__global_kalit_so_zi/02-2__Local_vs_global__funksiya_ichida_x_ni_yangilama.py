import sys 

x = 7 

def f(a):
    x = a 
    return x + 1 

if __name__ == '__main__':
    a =  int(sys.stdin.read())
    print(f(a))
    print(x)
