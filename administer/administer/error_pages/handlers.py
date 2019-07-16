from flask import Blueprint,render_template
from administer.funcionarios.forms import funcionario_form 

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
	add_funcionario = funcionario_form()
	return render_template('error_pages/404.html', add_funcionario=add_funcionario) , 404

@error_pages.app_errorhandler(403)
def error_403(error):
	add_funcionario = funcionario_form()
	return render_template('error_pages/403.html', add_funcionario=add_funcionario) , 403