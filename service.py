from session import Session
from utils import Response, match_password, hash_password, login_required,is_admin
from db import cur,commit
from models import User,UserRole,TodoType
import logging





logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",filename="todo.log",filemode="a")



session = Session()

@commit
def register(username,password,email ): 
    if session.check_session():
        return Response('You already created account',404)



    check_users_if_not_exists = "select * from users where username = %s;"
    cur.execute(check_users_if_not_exists,(username,))
    user_data = cur.fetchone()
    if user_data:
        return Response('This user already exists',404)
    
    hashed_password = hash_password(password)

    data = (username,hashed_password,email, UserRole.USER.value)
    insert_user_query = ('insert into users(username,password,email,role) values(%s,%s,%s,%s)')
    cur.execute(insert_user_query,data)

    cur.execute('select * from users where username = %s;',(username,))
    user_data = cur.fetchone()
    user = User.from_tuple(user_data)



    session.add_session(user)
    logging.info('Refistered')
    return Response('You successfully registered')     
   

 



def login(username : str, password : str):
    user = session.check_session()
    if user:
        logging.warning('Attempt to enter another acc when session is activate')
        return Response('You already logged in' , 404)
    
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    
    user_data = cur.fetchone()
    if not user_data:
        logging.warning('Failed attempt to log in!')
        return Response('User not found',404)
    
    
    user = User.from_tuple(user_data)

    if not match_password(password,user.password):
        logging.warning('Wrong password')
        return Response('Password wrong',404)
    
    session.add_session(user)
    logging.info('Logged in!')
    return Response('You successfully logged in.')
    



def log_out():
    user = session.check_session()
    if not user:
        logging.warning('Attempt to log out from deactivated session')
        return Response("You're not logged in." , 404)
    
    session.logout_session()
    logging.info('Logged out')
    return Response('You succesfully loged out')



# sherzod
    


    # title : str
    # user_id : int
    # description : str | None = None
    # todo_type : TodoType = TodoType.PERSONAL.value
    # created_at : None = None
    # id : int | None = None


    
@login_required
@is_admin
@commit
def add_todo(title, todo_type, description):
    user_id = session.check_session().id 
    todo_data = (user_id, title, todo_type, description)

    insert_todo_query = 'insert into todos(user_id, title, todo_type, description) values(%s, %s, %s, %s)'
    cur.execute(insert_todo_query, todo_data)
    logging.info('Todo added')
    return 




@login_required
def show_user_todo():
    

    user_id = session.check_session().id 
    get_info =  'select * from todos where user_id = %s'
    cur.execute(get_info,(user_id,))
    
    check_todos = cur.fetchone()

    if not check_todos:
        logging.warn('Try to check unexisted todos!')
        return Response('You dont have any todos',404)


    query = ( 'select title,description,todo_type  from todos where user_id = %s ')
    cur.execute(query,(user_id,))
    datas = cur.fetchone()
    logging.info('Showed todos')
    return datas



# add_todo('blabla',TodoType.PERSONAL.value,'hi')
    

    
