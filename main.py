from service import login,register,log_out

while True:
    choice = input("""
                
1: login
2: register
3:log out
q:quit      
choice : """)
    if choice == '1':
        username = input('username : ')
        password = input('password : ')
        
        result = login(username,password)
        
        print(result)
    
    elif choice == "2":
        new_user = input('enter username: ')
        new_password = input('enter your password: ')
        email = input('enter email: ')
        
        result = register(new_user,new_password,email)
        print(result)
    
    elif choice == "3":
        result = log_out()
        print(result)

    elif choice == 'q':
        break
    
    
    