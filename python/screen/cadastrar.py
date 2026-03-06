from modules.mysql import MySQL
from modules.aluno import Aluno

from PySide6.QtWidgets import(
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)

class Cadastro():
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()
        
        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()
    
    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastro Aluno")

        # Tema visual (mesma paleta do botão cadastrar)
        self.janela.setStyleSheet("""

            QWidget{
                background-color: #1c1f26;
                color: #e6e6e6;
                font-size: 14px;
                font-family: Segoe UI, Arial;
            }

            QLabel{
                margin-top: 6px;
                color: #ffdede;
            }

            QLineEdit{
                background-color: #2a2222;
                border: 2px solid #ff2a2a;
                border-radius: 10px;
                padding: 6px;
                color: #ffffff;
            }

            QLineEdit:focus{
                border: 2px solid #ff4d6d;
                background-color: #332626;
            }

            QPushButton{
                background-color: #3a2a2a;
                border: 2px solid #ff2a2a;
                border-radius: 16px;
                color: #ffe3e3;
                padding: 10px;
                margin-top: 10px;
                font-weight: bold;
            }

            QPushButton:hover{
                border: 2px solid #ff4d6d;
                background-color: #463030;
            }

            QPushButton:pressed{
                background-color: #2e2020;
                border: 2px solid #ff7a7a;
            }
        """)

        # 🔹 Ajusta dinamicamente ao tamanho da tela
        screen = self.app.primaryScreen().availableGeometry()
        largura = int(screen.width() * 0.4)
        altura = int(screen.height() * 0.6)

        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)

    def criar_componentes(self):
        componentes = {
            "nome": "Digite seu nome:",
            "email": "Digite seu email:",
            "cpf": "Digite seu cpf:",
            "telefone": "Digite seu telefone:",
            "endereco": "Digite seu endereco:"
        }
        
        for chave, texto in componentes.items():
            label = QLabel(texto)
            campo = QLineEdit()
            
            self.layout.addWidget(label)
            self.layout.addWidget(campo)
            
            self.campos[chave] = campo
            
        botao_cadastro = QPushButton("Cadastrar")
        self.layout.addWidget(botao_cadastro)
        
        botao_cadastro.clicked.connect(self.cadastrar)
        
    # 🔹 MÉTODO SEPARADO DE VALIDAÇÃO
    def validar_campos(self):
        nome = self.campos["nome"].text().strip()
        email = self.campos["email"].text().strip()
        cpf = self.campos["cpf"].text().strip()
        telefone = self.campos["telefone"].text().strip()
        endereco = self.campos["endereco"].text().strip()

        # Campos vazios
        if not all([nome, email, cpf, telefone, endereco]):
            raise ValueError("Todos os campos devem ser preenchidos.")

        # CPF deve conter apenas números e ter 11 dígitos
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("CPF deve conter 11 números.")

        # Telefone deve conter apenas números
        if not telefone.isdigit():
            raise ValueError("Telefone deve conter apenas números.")

        return True
        
    def cadastrar(self):
        try:
            # Primeiro valida
            self.validar_campos()

            aluno = Aluno(
                self.campos["nome"].text(),
                self.campos["email"].text(),
                self.campos["cpf"].text(),
                self.campos["telefone"].text(),
                self.campos["endereco"].text()
            )

            self.banco.connect()
            aluno.cadastrar(self.banco)

            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno Cadastrado!"
            )

            self.limpar_campos()
            
        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao Cadastrar: {e}"
            )
            
        finally:
            self.banco.disconnect()
            
    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()