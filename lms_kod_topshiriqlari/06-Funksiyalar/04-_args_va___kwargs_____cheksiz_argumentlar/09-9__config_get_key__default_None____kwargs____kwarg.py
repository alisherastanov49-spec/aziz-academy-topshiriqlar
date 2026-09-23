def config_get(key, default=0, **kwargs):
    return kwargs.get(key, default)

if __name__ == '__main__':
    key = input().strip()
    n = int(input().strip())
    
    kwargs = {}
    for _ in range(n):
        k, v = input().split()
        kwargs[k] = int(v) 
        
    print(config_get(key, default=0, **kwargs))