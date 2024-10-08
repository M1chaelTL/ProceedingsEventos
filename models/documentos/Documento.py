# models/documentos/Documento.py
from utils.repositorios.sqlAlchemy.conexionBd import db

class Documento(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    resumen = db.Column(db.Text, nullable=False)
    datos = db.Column(db.Text, nullable=False)
    conclusion = db.Column(db.Text, nullable=False)
    num_pag = db.Column(db.Integer, nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('evento.id'), nullable=False)
    autores = db.Column(db.String(50), nullable=False)

    def __init__(self, resumen, datos, conclusion, num_pag, evento_id, autores):
        self.resumen = resumen
        self.datos = datos
        self.conclusion = conclusion
        self.num_pag = num_pag
        self.evento_id = evento_id
        self.autores = autores



    @staticmethod
    def crear_documento(resumen, datos, conclusion, num_pag, evento_id, autores):
        try:
            nuevo_documento = Documento(resumen, datos, conclusion, num_pag, evento_id, autores)
            db.session.add(nuevo_documento)
            db.session.commit()
            return nuevo_documento
        except Exception as e:
            db.session.rollback()
            raise e
