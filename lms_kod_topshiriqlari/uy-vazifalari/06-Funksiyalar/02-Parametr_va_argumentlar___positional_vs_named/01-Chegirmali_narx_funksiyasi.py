def chegirmali(narx, foiz):
    chegirma = narx * foiz // 100
    return narx - chegirma
narx = int(input())
foiz = int(input())
print(chegirmali(narx, foiz))