def cheg(narx, foiz):
    return narx * (100 - foiz) // 100
def sol(narx):
    return narx + narx * 12 // 100
narx, foiz = [int(x) for x in input().split()]
print(sol(cheg(narx, foiz)))