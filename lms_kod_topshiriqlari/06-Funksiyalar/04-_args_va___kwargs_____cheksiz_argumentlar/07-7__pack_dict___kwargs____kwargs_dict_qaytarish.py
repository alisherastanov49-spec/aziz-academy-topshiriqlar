def pack_dict(**kwargs):
    return kwargs
n = int(input())
data = {}
for _ in range(n):
    parts = input().split()
    key = parts[0]
    val_str = parts[1]
    if val_str.isdigit() or (val_str.startswith('-') and val_str[1:].isdigit()):
        val = int(val_str)
    else:
        val = val_str
    data[key] = val
print(pack_dict(**data))