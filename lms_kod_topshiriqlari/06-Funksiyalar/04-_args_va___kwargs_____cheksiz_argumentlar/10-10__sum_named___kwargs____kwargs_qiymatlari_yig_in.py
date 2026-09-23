def sum_named(**kwargs):
    return sum(kwargs.values())

if __name__ == '__main__':
    n = int(input().strip())
    
    kwargs = {}
    for _ in range(n):
        k, v = input().split()
        kwargs[k] = int(v) 
        
    print(sum_named(**kwargs))