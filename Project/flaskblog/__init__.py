from flask import Flask


app = Flask(__name__)

from flaskblog import routes
from flaskblog.errors.handlers import errors
app.register_blueprint(errors)