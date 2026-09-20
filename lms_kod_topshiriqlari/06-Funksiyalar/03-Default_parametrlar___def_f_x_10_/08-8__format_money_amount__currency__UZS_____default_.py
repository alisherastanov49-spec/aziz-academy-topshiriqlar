import sys
def format_money(amount, currency='UZS'):
    return f"{amount} {currency}"
data =sys.stdin.read().split()
if data:
    if len(data) == 1:
        print(format_money(data[0]))
    else:
        print(format_money(data[0], data[1]))
        