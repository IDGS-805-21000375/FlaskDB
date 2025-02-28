from flask_sqlalchemy import SQAlchemy
import datetime

db-SQAlchemy()
class Alumno(db.Model):
    __tablename__='alumnos'
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Colum(db.String(50))
    apaterno=db.Colum(db.String(50))
    email=db.Colum(db.String(50))
    created_date=db.Column(db.DateTime,default=datetime.datetime.now)