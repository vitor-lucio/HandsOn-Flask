from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort)
from administer.usuarios.models import Admin
from administer.usuarios.forms import AdicionarUserForm, LoginForm, EditarUserForm
from flask_login import LoginManager, current_user, login_user, logout_user
from administer import login_required
from administer.usuarios.avatar import adicionar_avatar
from flask_bcrypt import Bcrypt
from administer import db
from administer.funcionarios.models import Funcionario
from administer.funcionarios.forms import funcionario_form

usuarios = Blueprint('usuarios', __name__,template_folder='templates/usuarios')

#ADICIONAR

#LOGIN

#LOGOUT

@usuarios.route("/dashboard", methods=["POST", "GET"])
@login_required()
def dashboard():
	totalSetor =[]
	add_funcionario = funcionario_form()

	funcionarios = Funcionario.query.filter_by(admin_id=current_user.id)
	for func in funcionarios:
		totalSetor.append(func.setor)
	
	tabela = [totalSetor.count('0'),totalSetor.count('1'),totalSetor.count('2'),totalSetor.count('3'),totalSetor.count('4'),totalSetor.count('5'),totalSetor.count('6')]

	return render_template("dashboard.html", add_funcionario=add_funcionario, tabela=tabela)

@login_required()
@usuarios.route("/perfil", methods=["POST", "GET"])
def perfil():
	
	add_funcionario = funcionario_form()
	editar_user = EditarUserForm()

	if editar_user.validate_on_submit(): 
		bcript = Bcrypt()		
		current_user.nome = editar_user.nome.data
		current_user.username = editar_user.username.data
		current_user.email = editar_user.email.data
		current_user.data_nasc = editar_user.data_nascimento.data

		current_user.hhash = bcript.generate_password_hash(editar_user.senha.data)

		current_user.avatar = adicionar_avatar(editar_user.foto.data, editar_user.username.data) 
		db.session.commit()

		flash("Dados atualizados!","success")

	return render_template("perfil.html", add_funcionario=add_funcionario, editar_user=editar_user)