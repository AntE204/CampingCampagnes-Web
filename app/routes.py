from app import app
from flask import render_template
from .forms import InscriptionForm, ConnexionForm

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    form = InscriptionForm()
    popup = None

    if form.validate_on_submit():
        nom = form.nom.data
        prenom = form.prenom.data
        email = form.email.data
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