import bcrypt
from session import Session
import logging


session = Session()

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s",filename="todo.log",filemode="a")


def hash_password(raw_password : str):
    encoded_password = raw_password.encode('utf-8') # b'admin'
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded_password,salt).decode()


def match_password(raw_passowrd : str, encoded_password:str):
    raw_passowrd = raw_passowrd.encode()
    return bcrypt.checkpw(raw_passowrd,encoded_password.encode())


class Response:
    def __init__(self,message,status_code = 200):
        self.message = message
        self.status_code = status_code
        
    def __str__(self):
        return f'{self.message} =  {self.status_code}'
    



def is_admin(func):
    def wrapper(*args,**kwargs):
        if session.session.role != 'admin':
            logging.warning('Someone with out admin permissions try to access!')
            return Response('Only admin user can be changed'),logging.warning('Someone with out admin permissions try to access!')
        
        return func(*args,**kwargs)
    return wrapper




def login_required(func):
    def wrapper(*args,**kwargs):
        check_session = session.check_session()
        if not check_session:
            logging.warning('Someone tried to log in!')
            return Response('You must logg in',404),logging.warning('Someone with out admin permissions try to access!')
        
        result =  func(*args,**kwargs)
        return result
    
    return wrapper





#print(bcrypt.hashpw('123'.encode('utf-8'),bcrypt.gensalt()))

#print(bcrypt.checkpw('123'.encode('utf-8'),'$2b$12$kDRi04moqEQMs2Y6LoaV7u6Hh.59Na/uEJVG8eJJpkZHPWkLVCFjS'.encode('utf-8')))