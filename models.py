from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Importar desde flask_sqlalchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Puedes cambiar la URI según tu base de datos
db = SQLAlchemy(app)

class Alumnos(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.now)  # Corregir el tipo de columna
