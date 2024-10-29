#Task03:
#Ask for the name of somebody the user wants to invite to a party. After this, display the message “[name] has now been invited” and add 1 to the count. Then ask if they want to invite somebody else. Keep repeating this until they no longer want to invite anyone else to the party and then display how many people they have coming to the party. 


count = 0
while True:  
    name = input("Enter invitee's name: ")
    print(f'{name} has been invited to the party!')
    count += 1
    ask = input('Do you want to invite somebody else?(y/n): ')

    if ask == 'n':
       break 
        
print(f"The total invitees are {count}")



#Another Solution:

again= "y"
count= 0

while again == 'y':
    name = input("Enter the name of soemone to whom you want to invite: ")
    print(f"{name} has been invited to the party!")
    count= count + 1 
    again = input("Is there anyone else to whom you wnat to invite?(y/n): ")
print(f'You have {count} invitees in the party.')






