def narxli(narx, soliq=12):
    return narx + narx * soliq // 100
narx = int(input())
soliq = int(input())
print(narxli(narx))
print(narxli(narx, soliq))