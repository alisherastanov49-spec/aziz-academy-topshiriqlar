import sys 

x = 5 

def safe_add(a):
    y = a + x
    return y 

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        a = int(input_data[0])
        print(safe_add(a))
        
if __name__ == '__main__':
    main()