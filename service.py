from session import Session
from utils import Response, match_password, hash_password
from db import cur,commit
from models import User,UserRole


session = Session()

@commit
def register(username,password,email ): 
    check_users_if_not_exists = "select * from users where username = %s;"
    cur.execute(check_users_if_not_exists,(username,))
    user_data = cur.fetchone()
    if user_data:
        return Response('This user already exists',404)
    
    hashed_password = hash_password(password)

    data = (username,hashed_password,email, UserRole.USER.value)
    insert_user_query = ('insert into users(username,password,email,role) values(%s,%s,%s,%s)')
    cur.execute(insert_user_query,data)

    return Response('You successfully registered')     
    



def login(username : str, password : str):
    user = session.check_session()
    if user:
        return Response('You already logged in' , 404)
    
    get_user_by_username = '''select * from users where username = %s;'''
    cur.execute(get_user_by_username,(username,))
    
    user_data = cur.fetchone()
    if not user_data:
        return Response('User not found',404)
    
    
    user = User.from_tuple(user_data)

    if not match_password(password,user.password):
        return Response('Password wrong',404)
    
    session.add_session(user)
    return Response('You successfully logged in.')
    


def log_out():
    user = session.check_session()
    if not user:
        return Response("You're not logged in." , 404)
    
    session.logout_session()
    return Response('You succesfully loged out')


    
# sherzod
    
    
    
