def uzunlik_ok(p):
    return len(p) >= 8
def raqam_bor(p):
    for ch in p:
        if ch in "0123456789":
            return True
    return False
def kuch(p):
    if uzunlik_ok(p) and raqam_bor(p):
        return "kuchli"
    return "zaif"
p = input()
print(kuch(p))