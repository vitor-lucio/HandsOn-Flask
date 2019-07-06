from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, IntegerField, PasswordField, SubmitField, StringField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, Length

class AdicionarUser_form(FlaskForm):
    nome = StringField("Nome:", validators=[DataRequired(message="Campo Obrigatório"), Length(min=3, max=120, message="O nome deve possuir entre 3 e 120 caracteres")])
    email = StringField("Email:", validator=[DataRequired(message="Campo Obrigatório"), Email(message="Email inválido")])
    username = StringField("Username:", validators=[DataRequired(message="Campo Obrigatório"), Length(min=3, max=120, message="O nome deve possuir entre 3 e 120 caracteres")])
    data_nac = DateField("Data de nascimento:", format="%Y-%m-%d", validators=[DataRequired(message="Campo Obrigatório")])
    foto = FileField("Foto:", format="%Y-%m-%d", validators=[DataRequired(message="Foto Obrigatória"), FileAllowed['jpg', 'jpeg', 'png']])
    senha = PasswordField("Senha:", validators=[DataRequired(message="Campo Obrigatório"), Length(min=3, max=120, message="O nome deve possuir entre 3 e 120 caracteres")]) 
    conf_senha = PasswordField("Confirmar senha:", validators=[DataRequired(message="Campo Obrigatório"), EqualTo('senha', message="As senhas devem ser iguais")]) 
    submit = SubmitField("Enviar")
