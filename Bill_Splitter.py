amount_str = input("Enter the total bill amount: ")
if amount_str.isdigit() or (amount_str.startswith('-') and amount_str[1:].isdigit()):
    amount_str = int(amount_str)
else:
    print('Please enter a valid whole number for bill amount.')
    exit()
if amount_str <= 0:
    print('Invalid bill amount')
    exit()
if amount_str > 0:
    num_members = input('Enter the number of memebers :')
    if num_members.isdigit() or (num_members.startswith('-') and num_members[1:].isdigit()):
        num_members = int(num_members)
    else:
        print('please enter a valid whole number for number of members.')
        exit()
    if num_members <= 0 :
        print('Invalid input')
        exit()
    elif num_members > 0:
        per_person_amount = round(amount_str/num_members, 2)
        print('Per person amount to pay is :', per_person_amount)
