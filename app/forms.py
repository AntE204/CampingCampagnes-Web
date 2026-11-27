from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Length, Optional, EqualTo

class InscriptionForm(FlaskForm):
    nom = StringField("Nom", validators=[
        InputRequired(message="Le nom est obligatoire."),
        Length(min=2, max=50)
    ])

    prenom = StringField("Prénom", validators=[
        InputRequired(message="Le prénom est obligatoire."),
        Length(min=2, max=50)
    ])

    email = EmailField("Email", validators=[
        InputRequired(message="L'email est obligatoire.")
    ])

    mdp = PasswordField("Mot de passe", validators=[
        InputRequired(message="Le mot de passe est obligatoire.")
    ])

    mdp_confirm = PasswordField("Confirmer ot de passe", validators=[
        InputRequired(message="La confirmation du mot de passe est obligatoire.")
    ])

    rue = StringField("Rue", validators=[
        InputRequired(message="La rue est obligatoire."),
        Length(min=2, max=50)
    ])

    ville = StringField("Ville", validators=[
        InputRequired(message="La ville est obligatoire."),
        Length(min=2, max=50)
    ])

    code_postal = StringField("Code postal", validators=[
        InputRequired(message="Le code postal est obligatoire."),
        Length(min=2, max=50)
    ])

    tel = StringField("Numéro de téléphone", validators=[
        Optional()
    ])

class ConnexionForm(FlaskForm):
    email = EmailField("Email", validators=[
        InputRequired(message="L'email est obligatoire.")
    ])

    mdp = PasswordField("Mot de passe", validators=[
        InputRequired(message="Le mot de passe est obligatoire.")
    ])

class ProfilForm(FlaskForm):
    nom = StringField("Nom", validators=[
        InputRequired(message="Le nom est obligatoire."),
        Length(min=2, max=50)
    ])

    prenom = StringField("Prénom", validators=[
        InputRequired(message="Le prénom est obligatoire."),
        Length(min=2, max=50)
    ])

    email = StringField("Email")

    rue = StringField("Rue", validators=[
        InputRequired(message="La rue est obligatoire."),
        Length(min=2, max=50)
    ])

    ville = StringField("Ville", validators=[
        InputRequired(message="La ville est obligatoire."),
        Length(min=2, max=50)
    ])

    code_postal = StringField("Code postal", validators=[
        InputRequired(message="Le code postal est obligatoire."),
        Length(min=2, max=50)
    ])

    tel = StringField("Numéro de téléphone", validators=[
        Optional(),
        Length(min=14, max=14)
    ])

    role = StringField("Rôle")