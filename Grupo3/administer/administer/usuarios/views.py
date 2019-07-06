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
@usuarios.route("/cadastro", methods=["POST", "GET"]) 
def adicionar():
    form_add = AdicionarUserForm(prefix="form_add")
	if form_add.validate_on_submit() and not Admin.query.filter_by(username=form_add.username.data).first() and not 

	  nome = form_add.nome.data
	  username = form_add.username.data
	  email = form_add.email.data
	  data_nasc = form_add.data_nascimento.data

	  bcript = Bcrypt()

	  hhash = bcript.generate_password_hash(form_add.senha.data)

	  avatar = adicionar_avatar(form_add.foto.data, username)

	  novo_user = Admin(nome, email, username, data_nasc, hhash, avatar)

	  db.session.add(novo_user)
	  db.session.commit()

	  flash("Agradecemos seu cadastro", "sucess")
	  
	  return redirect(url_for('principal.index'))

	  if Admin.query.filter_by(username = form_add.username.data).first():
		  flash(f"Esse nome de usuario ja existe", "warning")

	  if Admin.query.filter_by(email = form_add.email.data).first():
		  flash(f"Email ja cadastrado", "warning")

	  return redirect(url_for('principal.index'))


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