import logging

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi
from flask import Flask

# Flask App
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index_get():
    return 'Flask from Azure Functions ! GET: Index Page !'

@app.route('/user')
def user():
    return 'Query user from /user/<id>'

@app.route('/user/<int:user_id>')
def user_id(user_id: int):
    return f'User ID = int({user_id})'

@app.route('/user/<user_id>')
def user_id_str(user_id: str):
    return f'User ID = str({user_id})'


# Main Entry Point
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AzureFunctionsWsgi(app.wsgi_app).main(req, context)
