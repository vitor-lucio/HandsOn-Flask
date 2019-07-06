from flask import (render_template, request, Blueprint, url_for, redirect, flash, abort)
from flask_login import current_user, login_user, logout_user
from flask_bcrypt import Bcrypt

from administer.usuarios.models import Admin
from administer.usuarios.forms import AdicionarUserForm, LoginForm, EditarUserForm
from administer import db
from administer.funcionarios.models import Funcionario
from administer.funcionarios.forms import funcionario_form

usuarios = Blueprint('usuarios', __name__, template_folder="templates")