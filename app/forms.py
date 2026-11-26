from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired, Length

class ExampleForm(FlaskForm):
    nom = StringField("Nom de l'utilisateur", validators=[
        InputRequired(message="Le nom est obligatoire."),
        Length(min=2, max=50)
    ])
    prenom = StringField("Prénom de l'utilisateur", validators=[
        InputRequired(message="Le prénom est obligatoire."),
        Length(min=2, max=50)
    ])
    role = SelectField("Rôle", choices=[
        ("utilisateur", "Utilisateur"),
        ("administrateur", "Administrateur")
    ])
    submit = SubmitField("Se connecter")
