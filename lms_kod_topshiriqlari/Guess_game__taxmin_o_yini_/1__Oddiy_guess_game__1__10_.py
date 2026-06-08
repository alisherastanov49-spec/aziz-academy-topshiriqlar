secret = 7
attempts = 0
while True:
    try:
        guess = int(input())
        attempts += 1
        if guess < secret:
            print("Low")
        elif guess > secret:
            print("High")
        else:
            print("Correct")
            break
    except:
        break