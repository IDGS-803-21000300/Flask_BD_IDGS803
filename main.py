from flask import Flask, render_template, request, Response
import forms 
from flask import flash
from flask import g, redirect
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig
from models import db

app = Flask (__name__)
# app.secret_key = 'quiere que le ponga musica pa que baile hasta abajo la bebe'
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/")
def index():
    escuela = "LA RONCHA"
    alumnos = ["Kevin", "Eduardo", "Messi", "Rels B"]
    return render_template("index.html", escuela = escuela, alumnos = alumnos)

#FLASH......

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Kevinsito'
    # if 'Kevinsito' not in g.nombre and request.endpoint not in ['/']:
    #     return redirect('/maestros.html')
    print('before_request')
 
@app.after_request
def after_request(response):
    print('ultimo')
    if 'Kevinsito' not in g.nombre and request.endpoint not in ['/']:
        return redirect('/maestros.html')
    return response

#TERMINA FLASH.......

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():

    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UsersForm(request.form)

    # alum_form = forms.UsersForm(request.form)

    if request.method == "POST" and alum_form.validate():
            print('Hola {}'.format(g.nombre))
            nom = alum_form.nombre.data
            apa = alum_form.aPaterno.data
            ama = alum_form.aMaterno.data

            mensaje = 'Bienvenido {}'.format(nom)
            flash(mensaje)

            print("Nombre : {}".format(nom))
            print("Paterno : {}".format(apa))
            print("Materno : {}".format(ama))

    return render_template("alumnos.html", form = alum_form, nom = nom, apa = apa, ama = ama)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
         db.create_all()

    app.run()