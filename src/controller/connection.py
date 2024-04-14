import mysql.connector


class connection_factory():
    def __init__(self):
        self.host = '127.0.0.1'
        self.usuario = '{seu nome de usuario}'
        self.senha = '{sua senha}'
        self.banco_de_dados = 'formulario'
        self.conn = None

    # Abrir a conexão com mysql
    def open_connect(self):
        try:
            # Estabelecendo a conexão
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco_de_dados
            )

            if self.conn.is_connected():
                print("Conexão ao MySQL bem-sucedida!")
            return self.conn

        except Exception as e:
            print(f"Falha na conexão ao MySQL: {e}")

    # Fechar a Conexão com mySQL
    def close_connection(self, cursor=None):
        try:
            if self.conn is not None and self.conn.is_connected:
                self.conn.close()
            if cursor is not None:
                cursor.close()

        except Exception as e:
            print(f"Falha ao fechar a conexão com o banco de dados -> ", e)


