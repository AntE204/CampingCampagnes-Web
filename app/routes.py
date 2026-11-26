from app import app
from flask import render_template
from .forms import InscriptionForm, ConnexionForm, ProfilForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    form = InscriptionForm()
    popup = None

    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        email = form.email.data
        mdp = form.mdp.data
        mdp_confirm = form.mdp_confirm.data
        ville = form.ville.data
        rue = form.rue.data
        code_postal = form.code_postal.data
        tel = form.tel.data

        popup = {
            "message": "TODO",
            "type": "warning"
        }

        # TODO insérer en DB, check si email existe déjà

    return render_template("inscription.html", form=form, popup=popup)

@app.route("/connexion", methods=["GET", "POST"])
def connexion():
    form = ConnexionForm()
    popup = None

    if form.validate_on_submit():
        email = form.email.data
        mdp = form.mdp.data

        popup = {
            "message": "TODO",
            "type": "warning"
        }

        # TODO check les creds avec DB

    return render_template("connexion.html", form=form, popup=popup)

@app.route("/profil", methods=["GET", "POST"])
def profil():
    form = ProfilForm()
    popup = None

    # TODO récupération des infos en DB
    form.nom.data = "nom"
    form.prenom.data = "prénom"
    form.email.data = "email@ok.com"
    form.ville.data = "ville"
    form.rue.data = "rue"
    form.code_postal.data = "0550002D"
    form.tel.data = "06 07 08 09 10"
    form.role.data = "administrateur"

    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        ville = form.ville.data
        rue = form.rue.data
        code_postal = form.code_postal.data
        tel = form.tel.data

        popup = {
            "message": "Profil mis à jour.",
            "type": "primary"
        }

    return render_template("profil.html", form=form, popup=popup)

@app.route("/desinscription", methods=["DELETE"])
def desinscription():
    ...

@app.route("/animations", methods=["GET", "POST"])
def animations():
    ...

@app.route("/agenda")
def agenda():
    ...

@app.route("/planning", methods=["GET", "POST"])
def planning():
    ...