

user_credentials = ('baba', '12kk')

while True:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == user_credentials[0] and password == user_credentials[1]:
        print(f'Welcome {username}')
        break
    else:
        print('Wrong credentials')
        
   
   


