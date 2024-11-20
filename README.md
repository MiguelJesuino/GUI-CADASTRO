

# GUI-Cadastro
Este projeto é uma aplicação básica de formulário de cadastro desenvolvida em Python, integrada a um banco de dados MySQL. O programa permite o cadastro e login de usuários. A aplicação inclui uma interface gráfica simples, construída utilizando customtkinter. Foi criada com o objetivo de aprender um pouco mais sobre interfaces gráficas e operações CRUD com Python.

## Como Usar

Para usar este programa, você precisará dos seguintes requisitos:

- Python 3.12 instalado
- Banco de dados MySQL
  
    O banco de dados MySQL pode ser configurado localmente ou em um servidor remoto. Se você optar por configurar o banco de dados localmente, você pode usar o MySQL Workbench para administrar e visualizar o banco de dados. O MySQL Workbench é uma ferramenta de administração e modelagem de banco de dados desenvolvida pela Oracle. Você pode baixar o MySQL Workbench gratuitamente em [sua página oficial](https://www.mysql.com/products/workbench/).


### Execução
1. Clone o repositório para o seu ambiente local:
    git clone https://github.com/MiguelJesuino/GT-Cadastro
2. Dentro do diretório do projeto baixe as bibliotecas necessárias utilizando o comando `pip -r requirements.txt`
3. Utilize o arquivo SQL `formulario.sql` para criar o banco de dados
4. Modifique os dados no modulo `connection.py` utilizando suas informações referentes ao banco de dados
   
   ```python
       def __init__(self):
          self.host = '127.0.0.1'
          self.usuario = '{seu nome de usuario}'
          self.senha = '{sua senha}'
          self.banco_de_dados = 'formulario' # nome do banco de dados
          self.conn = None
   ```
   
5. execute o arquivo principal `main.py` para iniciar o programa

## Estrutura do Projeto

- `connection.py`: Contém a classe `Connection_Factory` responsável por estabelecer e fechar conexões com o banco de dados MySQL.
- `modelo.py`: Define a classe `Usuario` que representa um usuário do sistema.
- `dao.py`: Implementa a classe `UsuarioDAO` responsável por interagir com o banco de dados para realizar operações de inserção e autenticação de usuários.
- `view.py`: Contém as classes `Cadastro` e `Login` que definem a interface gráfica do programa usando customtkinter.
- `main.py`: Arquivo principal que inicia o programa.

## Melhorias Futuras

- Implementar um sistema de adiminstração de usuarios onde os usuarios possam ser classificados como admin ou usuario comum 
- Implementar funcionalidades adicionais, como edição e exclusão de usuários.
- Melhorar a segurança, como criptografar senhas armazenadas no banco de dados.


## Contribuição

Contribuições são bem-vindas! Este projeto foi desenvolvido para fins didáticos. fique à vontade para abrir uma issue ou enviar um pull request.
