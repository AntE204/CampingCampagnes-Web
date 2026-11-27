from app import app
from flask import render_template, session, url_for, redirect, abort
from .forms import InscriptionForm, ConnexionForm, ProfilForm
from .help import is_logged, is_animateur

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
    if is_logged(session):
        return redirect(url_for("index"))
    
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
    if not is_logged(session):
        return redirect(url_for("inscription"))

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
    if not is_logged(session):
        return redirect(url_for("connexion"))

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

        # TODO modif du profil en DB

        popup = {
            "message": "Profil mis à jour.",
            "type": "primary"
        }

    return render_template("profil.html", form=form, popup=popup)

@app.route("/deconnexion")
def deconnexion():
    session.clear()
    return redirect(url_for("index"))

@app.route("/desinscription", methods=["DELETE"])
def desinscription():
    if not is_logged(session):
        return redirect(url_for("connexion"))
    
    if is_animateur(session):
        return redirect("index")
    
    # TODO supprimer le compte avec ID stocké en session

@app.route("/animations", methods=["GET", "POST"])
def animations():
    # TODO pouvoir s'inscrire uniquement si logged et pas animateur
    return render_template("animations.html")

@app.route("/agenda")
def agenda():
    if not is_logged(session):
        return redirect(url_for("connexion"))

    if is_animateur(session):
        return redirect(url_for("index"))

    # TODO récup anims où un campeur est inscrit (par ID en session)
    return render_template("agenda.html")

@app.route("/planning", methods=["GET", "POST"])
def planning():
    if not is_logged(session):
        return redirect(url_for("connexion"))

    if not is_animateur(session):
        return redirect(url_for("index"))

    # TODO récup des animations animées par animateur (avec ID en session)
    # pouvoir faire l'appel avec checkboxes
    return render_template("planning.html")