def bulid_stats(*args, **kwargs):
    return {
        'count': len(args), 
        'min': min(args) if args else None, 
        'max': max(args) if args else None, 
        'sum': sum(args), 
        'extra_keys': sorted(kwargs.keys()),
        'extra_sum': sum(kwargs.values())
    }
    
nums = [int(t) for t in input().split()]
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
    
print(bulid_stats(*nums, **data))
       
