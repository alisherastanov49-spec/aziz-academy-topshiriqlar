secret = 5
attempts = 0
while True:
        guess = int(input().strip())
        attempts += 1
        if guess < secret:
            continue
        elif guess > secret:
            continue
        else:
            print(attempts)
            break
            

          