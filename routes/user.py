from flask import Blueprint
from json import dumps,loads
from dataclasses import asdict
user_page = Blueprint('user',__name__)
from models.user import User
user1 = User(name='Mohamed',email="Mohamed@123.com",age=30)
@user_page.route('hello')
def userHello():
    return dumps(asdict(user1))


@user_page.route('hello2')
def userHello2():
    return 'Hello User2'

