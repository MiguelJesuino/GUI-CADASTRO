class Usuario:
    def __init__(self, email, senha, nome=None):
        self.nome = nome
        self.email = email
        self.senha = senha