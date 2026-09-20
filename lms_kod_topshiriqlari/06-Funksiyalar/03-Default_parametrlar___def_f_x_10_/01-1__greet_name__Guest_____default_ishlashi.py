import sys
def greet(name='Guest'):
    return f"Hello, {name}!"
user_input = sys.stdin.read().strip()
if user_input:
    print(greet(user_input))
else:
    print(greet())