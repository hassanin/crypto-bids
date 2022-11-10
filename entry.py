from audioop import add
from flask import Flask
from mohamed import addTwo,sayHello
import sys
from routes.user import user_page
# from user import user_page


# adding Folder_2 to the system path
# sys.path.insert(0, './util')
from util import maths
x=5
print(x)
print("I am happy")
sayHello()
print(addTwo(4,5))
print(__name__)
r = maths.factorial(2)
print("r is ",r)
r12=[12,3,4]
for tr in r12:
    print(tr)
app = Flask(__name__)
# print(Flask.__version__)

app.register_blueprint(user_page,url_prefix='/user')
@app.route('/')
def index():
    return "Hello World From Flask"

app.run(host='0.0.0.0', port=5005)
