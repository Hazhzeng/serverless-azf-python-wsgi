from flask import Flask

# Flask App
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    return 'Flask from Azure Functions ! Try: /user/awesome !'

@app.route('/user')
def user():
    return 'Query user from /user/<id>'

@app.route('/user/<int:user_id>')
def user_id(user_id: int):
    return f'User ID = int({user_id})'

@app.route('/user/<user_id>')
def user_id_str(user_id: str):
    return f'User ID = str({user_id})'
