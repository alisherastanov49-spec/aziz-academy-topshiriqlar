secret = 8
attempts = 0

while attempts < 3:
    guess = int(input().strip())
    attempts += 1 
    
    if guess == secret:
        print("Correct")
        break
    elif attempts == 3:
        print("Game Over")