from flask import Flask

app = Flask(__name__) # __name__ - predifined python variable ; name of the module it is used in

from app import routes