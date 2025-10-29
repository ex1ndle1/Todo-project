from service import login,register,log_out,add_todo,show_user_todo
from models import TodoType
from utils import Response
from session import Session
import logging


session = Session()


logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",filename="todo.log",filemode="a")



while True:
    choice = input(""" 
1: login
2: register
3:log out
4:add todo
5:show todos
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
     
    elif choice == "4":
       
       try:  
        title =  input('''enter todo's title: ''')
        todo_type = input('''
enter todo type:
1.Personal
2.Working
enter:  ''')
        if todo_type == "1":
           todo_type = TodoType.PERSONAL.value

        elif todo_type == '2':
           todo_type = TodoType.WORKING.value

        else:
           print(Response('invalid choice',404))
           break


        descriptoin = input('enter description: ')
        
        print(add_todo(title,todo_type,descriptoin))
        
        


       except ValueError as e:
          print(f'Error: {e}')
    elif choice == '5':
       print(show_user_todo())

    elif choice == 'q':
        break
    
    




# title,todo_type,description