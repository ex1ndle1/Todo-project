import psycopg2
import os
from dotenv import load_dotenv
from utils import hash_password
from models import UserRole

load_dotenv() 


db_info = {
    "database":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "host":os.getenv("DB_HOST"),
    "password":os.getenv("DB_PASSWORD"),
    "port":os.getenv("DB_PORT")
}


conn = psycopg2.connect(**db_info)
cur = conn.cursor()




def commit(func):
    def wrapper(*args,**kwrags):
        result = func(*args,**kwrags)
        conn.commit()
        return result
    return wrapper




# DRY  => Don't repeat yourself


def create_user_table():
    user_query = """
            drop table if exists users cascade;
            create table if not exists users(
            id serial primary key,
            username varchar(255) not null unique,
            password varchar(255) not null,
            role varchar(15) default 'user',
            email varchar(255) ,
            created_at timestamptz default now()     
    );    
    """
    cur.execute(user_query)

def create_todo_table():
    todo_query = """create table if not exists todos(
            id serial primary key,
            title varchar(255) not null,
            description text,
            todo_type varchar(20) default 'personal',
            user_id int references users(id),
            created_at timestamptz default now()    
        );    
    """
    cur.execute(todo_query)
    
    

@commit
def init():
    create_user_table()
    create_todo_table()
    



@commit
def insert_user():
     insert_user_query = 'insert into users'

@commit
def insert_admin():
    insert_admin_query = '''insert into users(username,password,role)
    values(%s,%s,%s);
    '''
    data = ('admin',hash_password('admin123'),UserRole.ADMIN.value)
    cur.execute(insert_admin_query,data)


