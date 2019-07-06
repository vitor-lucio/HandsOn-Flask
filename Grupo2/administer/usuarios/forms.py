from flask_wtf import FlaskForm
from wtforms import(SelectField, DateField, IntegerField, PasswordField, SubmitFile, StringField)
from flask_wtf.file import (FileField, FileAllowed)
from wtforms.validators import (DataRequired, Email, EqualTo, Length)

class AdicionarUserForm(FlaskForm):

    nome = StringField("Nome: ", validators=(DataRequired(message="Campos Obrigatorios"), Length(min=8,max=130),message="Minimo: 8    Maximo: 130"))
    email = StringField("Email: ", validators=(DataRequired(message="Campos Obrigatorios"), Email(message="Digite um email válido")))
    username = StringField("Username: ", validators=[DataRequired(message="Campos Obrigatorios"), Length(min=8,max=130),message="Minimo: 8    Maximo: 130"])
    data_nasc = DateField("Nascimento: ", format="%d-%m-%Y", validator=(DataRequired))
    foto = FileField("Foto: ", validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    senha = PasswordField("Senha: ", validators=[DataRequired(), EqualTo("conf-senha",message="As senhas precisam ser iguais"), Length(min=8,max=150,message="Mínimo 8 e máximo 150")]
    conf_senha = PasswordField("Confirme a senha: ", validators=[DataRequired(), Length(min=8,max=150,message="Mínimo 8 e máximo 150")]