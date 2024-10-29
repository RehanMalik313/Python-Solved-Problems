#Task05:
#Ask the user to enter a number between 10 and 20. If they enter a value under 10, display the message “Too low” and ask them to try again. If they enter a value above 20, display the message “Too high” and ask them to try again. Keep repeating this until they enter a value that is between 10 and 20 and then display the message “Thank you”.

num = int(input("Enter a number between 10 or 20: "))
max_attempts = 3
count = 1

while num < 10 or num > 20:
    if count == max_attempts:
        print('Too many attempts, Try Later!')
        break 

    if num < 10:
        print('Too low')
    else:
        print('Too high')
    count += 1    

    num = int(input('Try Again: '))

if 10 < num < 20:
    print("Thank you.")


