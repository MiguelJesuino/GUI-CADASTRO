try:
    import sys
    sys.path.append(r"../src")
except ModuleNotFoundError:
    ...

from controller.connection import connection_factory
import mysql.connector


class UsuarioDAO:
    def __init__(self):
        self.connection_factory = connection_factory()

    def inserir_usuario(self, usuario):
        global cursor
        conexao = None

        try:
            conexao = self.connection_factory.open_connect()

            # check if the connection was conditional
            if conexao is not None:
                cursor = conexao.cursor()

                # Consulta SQL para inserir um novo usuário
                query = "INSERT INTO Usuario (nome, email, password) VALUES (%s, %s, %s)"
                valores = (usuario.nome, usuario.email, usuario.senha)

                # Execute the SQL query in the database
                cursor.execute(query, valores)
                conexao.commit()

                print("Usuário inserido com sucesso!")
            else:
                print("A conexão não foi estabelecida corretamente.")

        except mysql.connector.Error as err:
            print(f"Falha ao inserir usuário: {err}")

        finally:
            if conexao is not None and conexao.is_connected():
                cursor.close()
                conexao.close()

    def autenticar_usuario(self, email, senha):
        global cursor
        conexao = None

        try:
            conexao = self.connection_factory.open_connect()

            if conexao is not None:
                cursor = conexao.cursor(dictionary=True)
                query = "SELECT * FROM Usuario WHERE email = %s AND password = %s"
                valores = (email, senha)
                cursor.execute(query, valores)
                usuario = cursor.fetchone()

                if usuario:
                    return True
                else:
                    return False

            else:
                print("A conexão não foi estabelecida corretamente.")
                return None

        except mysql.connector.Error as err:
            print(f"Falha ao autenticar usuário: {err}")
            return None

        finally:
            if conexao is not None and conexao.is_connected():
                cursor.close()
                conexao.close()

