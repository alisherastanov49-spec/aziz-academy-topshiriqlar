import sys
def make_user(name, role='student'):
    return f"name={name}, role={role}"
args = sys.stdin.read().split()
if len(args) == 1:
    print(make_user(args[0]))
elif len(args) >= 2:
    print(make_user(args[0], args[1]))