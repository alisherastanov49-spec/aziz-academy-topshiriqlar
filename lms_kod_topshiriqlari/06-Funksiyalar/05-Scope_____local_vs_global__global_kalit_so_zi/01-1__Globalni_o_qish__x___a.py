import sys 

x = 10 

def add_to_global(a):
    return x + a 

if __name__ == '__main__':
    a = int(sys.stdin.read())
    print(add_to_global(a))