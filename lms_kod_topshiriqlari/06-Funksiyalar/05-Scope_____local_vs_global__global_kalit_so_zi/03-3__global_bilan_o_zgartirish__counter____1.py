import sys 

counter = 0 

def inc():
    global counter
    counter += 1
    return counter

if __name__ == '__main__':
    n = int(sys.stdin.read())
    for _ in range(n):
        print(inc())