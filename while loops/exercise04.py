#Task04:
#Create a variable called compnum and set the value to 50. Ask the user to enter a number. While their guess is not the same as the compnum value, tell them if their guess is too low or too high and ask them to have another guess. If they enter the same value as compnum, display the message “Well done, you took [count] attempts”. 


compnum = 50
guess = int(input("Enter a number: "))
max_attempts = 3
count = 1

while guess != compnum:
    if count == max_attempts:
        print('Too many attempts, Try Later!')
        break

    if guess > compnum:
        print('your guess is too high.')
    else:
        print("your guess is too low.")
    count += 1
    guess = int(input('Have another Guess: '))

if guess == compnum:
    print(f"Welldone, you took {count} attempts.")
        