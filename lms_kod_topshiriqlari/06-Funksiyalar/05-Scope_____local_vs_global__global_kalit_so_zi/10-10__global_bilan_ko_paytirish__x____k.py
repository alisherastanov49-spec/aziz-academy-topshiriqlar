import sys 

x = 2 

def mul_global(k):
    global x 
    x *= k 
    return x 

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        for i in range(1, n + 1):
            k = int(input_data[i])
            print(mul_global(k))
            
if __name__ == '__main__':
    main()