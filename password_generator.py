import random


def gen_password():
    print('welcome To Your Password Generator')

    chars = 'abcdAbc123%&^'
    password = ''

    while True:
    # number = int(input('Amount of passwords to generate: '))
        length = int(input('Your password length: '))

        print('\nHere is your password: ')
        
        for c in range(length):
            password += random.choice(chars) 
        print(password)
        
        gen_another_pwd = input('Do you need another password (Yes or No): ')
        if gen_another_pwd == 'Yes':
            continue
        elif gen_another_pwd == 'No':
            break
    
    return password    

print(gen_password())
       