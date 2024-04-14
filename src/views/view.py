import time
from ..model.modelo import Usuario
from ..controller.dao import UsuarioDAO
import tkinter as tk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

# ---------------------------------------------------------------------------------------- CADASTRO ---------------------------------------------------------------------------------------- #


class Cadastro(ctk.CTk):
    def __init__(self, login):
        super().__init__()
        self.layout_cadastro()
        self.sistema_cadastro()
        self.login = login

    # Definindo o layout da pagina
    def layout_cadastro(self):
        width = 500
        height = 510
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.title('Formulário Cadastro')
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)

    # configurações da GUI
    def sistema_cadastro(self):

        # Função para voltar para o botão de fazer login
        def voltar_ao_login():
            self.destroy()
            self.login.deiconify()

        # Função de cadastrar usuários no banco de dados
        def cadastrar_usuario():
            email_text = email.get()
            nome_text = nome.get()
            senha_text = senha.get()

            if not nome_text or not email_text or not senha_text :

                # message indicating that the fields were not properly filled in

                CTkMessagebox(title="Error", message="Todos os campos precisão ser preenchidos", icon="warning", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
            elif '@' not in email_text or "." not in email_text:

                # message indicating that the email provided is not valid

                CTkMessagebox(title="Error", message="O E-Mail digitado não é valido", icon="cancel", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
            else:

                # message indicating that the registration was successfully completed

                usuario = Usuario(nome=nome_text, email=email_text, senha=senha_text)
                dao = UsuarioDAO()
                dao.inserir_usuario(usuario)
                CTkMessagebox(message="Usuário cadastrado com sucesso!", icon="check", option_1="Ok", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
                nome.delete(0, ctk.END)
                email.delete(0, ctk.END)
                senha.delete(0, ctk.END)

        # ----------------------------------------------------- BACKGROUND OF PAGE ---------------------------------------------------- #

        background = ctk.CTkFrame(self, width=500, height=510, fg_color='#030711', corner_radius=0).place(x=0, y=0)

        # -------------------------------------------------------- FONT STYLES -------------------------------------------------------- #
        font_msg = ctk.CTkFont(family="Fira Code Nerd Font", size=17)
        font_titulo = ctk.CTkFont(family="Fira Code Nerd Font", size=30, weight='bold')
        font_labels = ctk.CTkFont(family='Fira Code Nerd Font', size=18, weight='bold')
        font_entry = ctk.CTkFont(family='Fira Code Nerd Font', size=18)
        font_button_cadastro = ctk.CTkFont(family='Fira Code Nerd Font', size=16)

        # ------------------------------------------------------- PAGE ELEMENTS ------------------------------------------------------- #

        # ----------------- TITLE ----------------- #
        titulo_background = ctk.CTkFrame(self, width=460, height=60, bg_color="#030711", fg_color="#071631", corner_radius=20)
        titulo = ctk.CTkLabel(self, text_color="#fff", text="CADASTRO", font=font_titulo, bg_color="#071631")

        # ---------------- ENTRY'S ---------------- #
        label_nome = ctk.CTkLabel(self, text_color='#546885', text="Nome:", font=font_labels, bg_color="#030711")
        nome = ctk.CTkEntry(self, text_color='#807f80', fg_color="#141824", width=440, height=50, corner_radius=14, bg_color='#030711', placeholder_text="Digite seu nome", font=font_entry)

        label_email = ctk.CTkLabel(self, text_color='#546885', text="E-Mail:", font=font_labels, bg_color='#030711')
        email = ctk.CTkEntry(self, text_color='#807f80', fg_color="#141824", width=440, height=50, corner_radius=14, bg_color='#030711', placeholder_text="Digite seu email", font=font_entry)

        label_senha = ctk.CTkLabel(self, text_color='#546885', text="Senha:", font=font_labels, bg_color='#030711')
        senha = ctk.CTkEntry(self, text_color='#807f80', show="*", fg_color='#141824', width=440, height=50, corner_radius=14, bg_color='#030711', placeholder_text="Digite sua senha", font=font_entry)

        button = ctk.CTkButton(self, hover_color='#0d295c',width=200, height=50, font=font_labels, text="cadastrar", corner_radius=10, bg_color="#030711", fg_color="#071631", command=cadastrar_usuario)
        button_voltar = ctk.CTkButton(self, width=100, hover=False, height=50, text_color="lightblue", font=font_button_cadastro, text="Ja tem conta?\n Faça Login", bg_color="#030711", fg_color="#030711", command=voltar_ao_login)

        # ---------------- TITLE-ALIGNMENT --------------- #
        titulo_background.place(x=20, y=20)
        titulo.place(x=165.9, y=33)

        # ----------------- FORM-ALIGNMENT ----------------#
        # NAME
        label_nome.place(x=30, y=98)
        nome.place(x=30, y=130)

        # E-MAIL
        label_email.place(x=30, y=200)
        email.place(x=30, y=231)

        # PASSWORD
        label_senha.place(x=30, y=301)
        senha.place(x=30, y=332)

        # BUTTON
        button.place(x=260, y=422)
        button_voltar.place(x=70, y=422)


# ----------------------------------------------------------------------------------------- LOGIN ------------------------------------------------------------------------------------------ #


class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_login()
        self.sistema_login()

    def layout_login(self):
        width = 500
        height = 470
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.title('Formulário de Login')
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)

    def sistema_login(self):

        def btn_cadastro():
            self.withdraw()
            cadastro = Cadastro(self)
            cadastro.mainloop()
            pass

        def logar():
            email_text = email.get()
            senha_text = senha.get()
            font_msg = ctk.CTkFont(family="Fira Code Nerd Font", size=17)

            if not email_text or not senha_text :
                # message indicating that the fields were not properly filled in
                CTkMessagebox(title="Error", message="Todos os campos precisão ser preenchidos", icon="warning", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
                email.delete(0, tk.END)

            elif '@' not in email_text or "." not in email_text:
                # message indicating that the email provided is not valid
                CTkMessagebox(title="Error", message="O E-Mail digitado não é valido", icon="cancel", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
            else:
                dao = UsuarioDAO()
                teste = dao.autenticar_usuario(email=email_text, senha=senha_text)
                if teste:
                    # message indicating that the login was successfully completed
                    CTkMessagebox(message="Login efetuado com sucesso", icon="check", option_1="Ok", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')
                    email.delete(0, ctk.END)
                    senha.delete(0, ctk.END)
                else:
                    CTkMessagebox(message="E-Mail ou senha incorretos", icon="cancel", option_1="Ok", fg_color="#040b1b", bg_color='#030711', font=font_msg, button_color="#140064", button_hover_color='#30216D')

        # ----------------------------------------------------- BACKGROUND OF PAGE ---------------------------------------------------- #

        background = ctk.CTkFrame(self, width=500, height=510, fg_color='#030711', corner_radius=0).place(x=0, y=0)

        # -------------------------------------------------------- FONT STYLES -------------------------------------------------------- #

        font_titulo = ctk.CTkFont(family="Fira Code Nerd Font", size=30, weight='bold')
        font_labels = ctk.CTkFont(family='Fira Code Nerd Font', size=18, weight='bold')
        font_entry = ctk.CTkFont(family='Fira Code Nerd Font', size=18)
        font_button_cadastro = ctk.CTkFont(family='Fira Code Nerd Font', size=16)

        # ------------------------------------------------------- PAGE ELEMENTS ------------------------------------------------------- #

        # ------------------ TITLE ------------------ #
        titulo_background = ctk.CTkFrame(self, width=460, height=100, bg_color="#030711", fg_color="#071631", corner_radius=15)
        titulo = ctk.CTkLabel(self, text_color="#fff", text="LOGIN", font=font_titulo, bg_color="#071631")

        # ------------------ ENTRY'S ------------------ #

        label_email = ctk.CTkLabel(self, text_color='#546885', text="E-Mail:", font=font_labels, bg_color='#030711')
        email = ctk.CTkEntry(self, text_color='#807f80', fg_color="#141824", width=440, height=60, corner_radius=14, bg_color='#030711', placeholder_text="Digite seu email", font=font_entry)

        label_senha = ctk.CTkLabel(self, text_color='#546885', text="Senha:", font=font_labels, bg_color='#030711')
        senha = ctk.CTkEntry(self, text_color='#807f80', show="*", fg_color='#141824', width=440, height=60, corner_radius=14, bg_color='#030711', placeholder_text="Digite sua senha", font=font_entry)

        button_login = ctk.CTkButton(self, hover_color='#0d295c', width=200, height=50, font=font_labels, text="ENTRAR", corner_radius=10, bg_color="#030711", fg_color="#071631", command=logar)
        button_cadastro = ctk.CTkButton(self, width=100, hover=False, height=50, text_color="lightblue", font=font_button_cadastro, text="cadastrar-se", corner_radius=10, bg_color="#030711", fg_color="#030711", command=btn_cadastro)

        # ---------------- TITLE-ALIGNMENT --------------- #
        titulo_background.place(x=20, y=-15)
        titulo.place(x=200, y=25)

        # ---------------- FORM-ALIGNMENT ---------------- #

        # E-MAIL
        label_email.place(x=30, y=120)
        email.place(x=30, y=151)

        # PASSWORD
        label_senha.place(x=30, y=231)
        senha.place(x=30, y=262)

        # BUTTON
        button_login.place(x=260, y=372)
        button_cadastro.place(x=80, y=372)
