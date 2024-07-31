# routes/controlador/home.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.documentos.Actividad import Actividad
from models.documentos.Noticias import Noticias

home = Blueprint('home', __name__, template_folder='../templates/vista/HTML')

@home.route('/')
def home_page():
    cronograma = Actividad.query.all()
    noticias = Noticias.query.all()
    return render_template('vista/assets/HTML/home.html', cronograma=cronograma, noticias=noticias)

