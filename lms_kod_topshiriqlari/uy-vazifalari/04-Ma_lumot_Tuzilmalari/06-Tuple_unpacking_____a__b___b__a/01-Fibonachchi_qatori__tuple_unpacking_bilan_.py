n = int(input())
a, b = 0, 1
fib_sequence = []
for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b
print(*fib_sequence)