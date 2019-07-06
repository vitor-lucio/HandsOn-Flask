from flask import (render_template, request, Blueprint, url_for, redirect, request, flash, abort,
					make_response, jsonify)
from administer.funcionarios.forms import funcionario_form
from administer.funcionarios.models import Funcionario
from flask_login import LoginManager, current_user
from administer import login_required, db

funcionarios = Blueprint('funcionarios', __name__, template_folder='templates')



@login_required()
@funcionarios.route("/exibe_all")
def exibe_all():

	add_funcionario = funcionario_form()

	titulo = "Todos funcionários"
	setor = [("0", "Equipe administrativo"), ("1", "Desenvolvedor"), ("2", "Equipe projetos"), ("3", "Equipe RH"), ("4", "Equipe marketing"), ("5", "Equipe presidencia"), ("6", "Equipe Negocios")]
	setor = dict(setor)

	page = request.args.get('page', 1, type=int)
	funcionarios = Funcionario.query.paginate(page=page, per_page=12)
	return render_template("todos_funcionarios.html", setor=setor, titulo=titulo, funcionarios=funcionarios, add_funcionario=add_funcionario)

@login_required()
@funcionarios.route("/meus_funcionarios")
def meus_funcionarios():

	add_funcionario = funcionario_form()

	titulo = "Meus funcionários"
	setor = [("0", "Equipe administrativo"), ("1", "Desenvolvedor"), ("2", "Equipe projetos"), ("3", "Equipe RH"), ("4", "Equipe marketing"), ("5", "Equipe presidencia"), ("6", "Equipe Negocios")]
	setor = dict(setor)

	page = request.args.get('page', 1, type=int)
	funcionarios = Funcionario.query.filter_by(admin_id=current_user.id).paginate(page=page, per_page=12)
	
	return render_template("todos_funcionarios.html", setor=setor, titulo=titulo, funcionarios=funcionarios, add_funcionario=add_funcionario)

@login_required()
@funcionarios.route("/exibe/<int:id>")
def exibe(id):
	
	add_funcionario = funcionario_form()
	funcionario = Funcionario.query.get_or_404(id)

	return render_template("funcionario.html", add_funcionario=add_funcionario, funcionario=funcionario)
