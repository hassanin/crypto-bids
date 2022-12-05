from flask import Blueprint
from json import dumps,loads
from dataclasses import asdict
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models.database import Person
# engine = create_engine("sqlite://", echo=True)
engine = create_engine(
    "postgresql://crypto:magical_password@localhost:5432/cryptoDb",
    isolation_level = "REPEATABLE READ"
)
user_page = Blueprint('user',__name__)
from models.user import User
user1 = User(name='Mohamed',email="Mohamed@123.com",age=30)
@user_page.route('hello')
def userHello():
    return dumps(asdict(user1))
    # return user1.to_json()


@user_page.route('hello2')
def userHello2():
    return 'Hello User2'


@user_page.route('hello3')
def ListUsers():
    with Session(engine) as session:
        stmt = select(Person)
        for user in session.scalars(stmt):
            print(user.name)
    return 'Hello User3'

@user_page.route('hello4/name/<name>/age/<age>')
def AddUser(name: str, age:int):
    print("user name is and age is",name,age)
    person = Person(name=name,age=age)
    with Session(engine) as session:
        session.add(person)
        session.commit()
    return 'Hello User4'


