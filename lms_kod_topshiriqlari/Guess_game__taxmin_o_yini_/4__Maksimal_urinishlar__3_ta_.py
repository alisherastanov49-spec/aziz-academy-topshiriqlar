secret = 7
max_attempts = 3
attempts = 0
while atempts < max_attempts:
    guess = int(input())
    attempts += 1
    if guess == secret:
        print("Correct")
        break
    elif attempts == max_attempts:
        print("Game Over")