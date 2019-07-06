from flask import Flask
# 
import os
# Bibliotecas
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Páginas


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


######### Config DB ############
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
Migrate(app, db)



######### Cadastro BluePrints ############
from administer.principal.views import principal
app.register_blueprint(principal)
from administer.usuarios.views import usuarios
app.register_blueprint(usuarios, url_prefix="/usuarios")
#app.register_blueprint(funcionarios, url_prefix="/funcionarios")

