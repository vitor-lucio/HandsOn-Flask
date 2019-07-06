from flask_wtf import FlaskForm
from wtforms import (SelectField, DateField, IntegerField, PasswordField, SubmitField, StringField)
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length

class AdicionarUserForm(FlaskForm):

    nome = StringField("Nome", validators=[DataRequired(message="Campos Obrigatorio"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120")])
    email = StringField("Email", validators=[DataRequired(message="Campos Obrigatorio"), Email(message="Digite um e-mail valido")])
    username = StringField("username", validators=[DataRequired(message="Campos Obrigatorio"), Length(min=3, max=120, message="Minimo de 3 caracteres e máximo de 120")])
    data_nac = DateField("Data de nascimento", format="%Y-%m-%d", validators=[DataRequired()])
    foto = FileField("Foto", validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    senha = PasswordField("Senha", validators=[DataRequired(), EqualTo('conf_senha', message="As senhas precisam bater"), Length(min=3, max=250, message="Minimo de 3 caracteres e máximo de 250")])
    conf_senha = PasswordField("Confirmar senha", validators=[DataRequired(), Length(min=3, max=250, message="Minimo de 3 caracteres e máximo de 250")])
    submit = SubmitField("Enviar")
