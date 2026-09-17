import sys
print(f"{'Mahsulot'.ljust(10)}{'Soni'.rjust(6)}\n{'-' * 16}")
data = sys.stdin.read().split()[1:]
for nom, soni in zip(data[::2], data[1::2]):
    print(f"{nom.ljust(10)}{soni.rjust(6)}")