import logging

import azure.functions as func
from azf_wsgi import AzureFunctionsWsgi
from .flaskapp import app


# Main Entry Point
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AzureFunctionsWsgi(app.wsgi_app).main(req, context)
