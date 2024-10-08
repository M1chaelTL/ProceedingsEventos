from utils.repositorios.sqlAlchemy.UsuarioRepositorioImpl import UsuarioRepositorioImpl

class UsuarioServicio:
    def __init__(self, usuario = None):
        self.usuario_repositorio = UsuarioRepositorioImpl(usuario)
    def registrar_usuario(self):
        if not self.usuario_repositorio.verificar_usuario_bd():
            return False
        
        self.usuario_repositorio.agregar_usuario_bd()
        return True

    def loggear_usuario(self,email, contrasenia):
        self.usuario_repositorio.recuperar_usuario_by_email(email)

        if self.usuario_repositorio.consultar_usuario() is None:
            return False
        
        if self.usuario_repositorio.verificar_contrasenia(contrasenia):
            return True

        return False
    
    def obtener_id_usuario(self):
        return self.usuario_repositorio.consultar_usuario().id

    def es_admin(self):
        return self.usuario_repositorio.consultar_usuario().es_admin