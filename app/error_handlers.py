from app import app
from flask import render_template

@app.errorhandler(400)
def forbidden(error):
    print(error)
    return render_template("400.html"), 400

@app.errorhandler(403)
def forbidden(error):
    print(error)
    return render_template("403.html"), 403

@app.errorhandler(404)
def not_found(error):
    print(error)
    return render_template("404.html"), 404
