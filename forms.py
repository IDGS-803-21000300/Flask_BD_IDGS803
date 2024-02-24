
from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UsersForm (Form):

    nombre = StringField("nombre", [validators.DataRequired(message='el campo es requerido'),
                                    validators.length(min=4, max=10,message= 'Ingresa el nombre valido y arriba la fiera')]) 
    
    
    aPaterno = StringField("aPaterno", [validators.DataRequired(message= 'Ingresa el apellido pa'),
                                        validators.Length(min = 4, max= 10, message='Ingresa un apellido de de 4 a 10 caracteres')]) 
    
    
    aMaterno = StringField("aMaterno", [validators.DataRequired(message= 'Ingresa el apellido pa'),
                                        validators.Length(min = 4, max= 10, message='Ingresa un apellido de 4 a 10 caracteres')]) 
    
    
    edad = IntegerField("edad", [validators.DataRequired(message= 'Ingresa una edad pa'),
                                        validators.number_range(min=1, max=100, message='Valor No Valido')]) 
    
    correo = EmailField("correo ", [validators.email(message='Ingresa un correo valido')]) 


