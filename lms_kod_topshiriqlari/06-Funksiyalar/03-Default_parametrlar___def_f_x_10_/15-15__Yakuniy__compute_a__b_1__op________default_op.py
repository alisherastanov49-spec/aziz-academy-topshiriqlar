import sys
def compute(a, b=1, op='+'):
    res = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}[op]
    return f"{res:.2f}" if op == '/' else res
args = sys.stdin.read().split()
nums = [int(x) for x in args if x.isdigit()]
ops = [x for x in args if x in '+-*/']
a = nums[0]
b = nums[1] if len(nums) > 1 else 1
op = ops[0] if ops else '+'
print(compute(a, b, op))