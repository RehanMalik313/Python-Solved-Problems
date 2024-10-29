#Task06:
# Using the song “10 green bottles”, display the lines “There are [num] green bottles hanging on the wall, [num] green bottles hanging on the wall, and if 1 green bottle should accidentally fall”. Then ask the question “how many green bottles will be hanging on the wall?” If the user answers correctly, display the message “There will be [num] green bottles hanging on the wall”. If they answer incorrectly, display the message “No, try again” until they get it right. When the number of green bottles gets down to 0, display the message “There are no more green bottles hanging on the wall”. 

num = 10
while num > 0:
    print(f'There are {num} green bottles hanging on the wall')
    print(f'{num} green bottles hanging on the wall')
    print(f'and if 1 green bottle should accidentally fall')
    num = num - 1
    ask = int(input("How many green bottles will be hanging in the wall?: "))

    if ask == num:
        print(f'There will be {num} green bottles hanging on the wall')
    else: 
        while ask != num:
            ask = int(input('No, try again: '))
print('There are no green bottles hanging on the wall!')