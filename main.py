from flask import Flask, render_template, request, Response
import forms 
from flask import flash
from flask import g, redirect
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig
from models import db
from models import Alumnos

app = Flask (__name__)
# app.secret_key = 'quiere que le ponga musica pa que baile hasta abajo la bebe'
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/index", methods = ["GET", "POST"])
def index():
    alum_form = forms.UsersForm2(request.form)

    if request.method == "POST" and alum_form.validate():
         alum = Alumnos(nombre = alum_form.nombre.data,
                        apaterno = alum_form.aPaterno.data,
                        email = alum_form.email.data)
         db.session.add(alum)
         db.session.commit()
         alum_form = Alumnos.query.all()
         return render_template('ABC_Completo.html', form = alum_form)
    
    return render_template('index.html', form = alum_form)

@app.route("/abc_completo", methods = ["GET", "POST"])
def alum():
     alum_form = Alumnos.query.all()
     return render_template('ABC_Completo.html', form = alum_form)

@app.route("/eliminar", methods = ["GET", "POST"])
def eliminar():
    alum_form = forms.UsersForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum_form.id.data = request.args.get('id')
        alum_form.nombre.data = alum1.nombre
        alum_form.aPaterno.data = alum1.apaterno
        alum_form.email.data = alum1.email              
    if request.method == 'POST':
        id = alum_form.id.data
        alum = Alumnos.query.get(id)
        db.session.delete(alum)
        db.session.commit()
        return redirect('ABC_Completo')
    return render_template('eliminar.html', form = alum_form)
    

@app.route("/modificar")
def modificar():
    alum_form = forms.UsersForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum_form.id.data = request.args.get('id')
        alum_form.nombre.data = alum1.nombre
        alum_form.aPaterno.data = alum1.aPaterno
        alum_form.email.data = alum1.email              
    if request.method == 'POST':
        id = alum_form.id.data
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum1.nombre = alum_form.nombre.data
        alum1.apaterno = alum_form.apaterno.data
        alum1.email = alum_form.email.data
        db.session.add(alum1)
        db.session.commit()
        return redirect('ABC_Completo')
    return redirect('modificar.html', form = alum_form)

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