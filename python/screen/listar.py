from modules.mysql import MySQL
from modules.aluno import Aluno
 
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem
)
 
class Listar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()
 
        self.configurar_janela()
        self.criar_componentes()
        self.carregar_dados()
 
    def configurar_janela(self):
        self.janela.setWindowTitle("Listagem de Alunos")
 
        # Tema visual azul neon suave
        self.janela.setStyleSheet("""
 
            QWidget{
                background-color: #1c1f26;
                color: #e6e6e6;
                font-size: 14px;
                font-family: Segoe UI, Arial;
            }
 
            QTableWidget{
                background-color: #232834;
                border: 2px solid #1e90ff;
                border-radius: 10px;
                gridline-color: #2f3747;
                selection-background-color: #1e90ff;
                selection-color: white;
            }
 
            QHeaderView::section{
                background-color: #2a3342;
                border: none;
                padding: 6px;
                color: #dce9ff;
                font-weight: bold;
            }
 
            QPushButton{
                background-color: #2a3342;
                border: 2px solid #1e90ff;
                border-radius: 16px;
                color: #dce9ff;
                padding: 10px;
                margin-top: 10px;
                font-weight: bold;
            }
 
            QPushButton:hover{
                border: 2px solid #00b7ff;
                background-color: #313b4f;
            }
 
            QPushButton:pressed{
                background-color: #222a38;
                border: 2px solid #4dc4ff;
            }
        """)
 
        screen = self.app.primaryScreen().geometry()
        largura = int(screen.width() * 0.6)
        altura = int(screen.height() * 0.7)
 
        self.janela.resize(largura, altura)
        self.janela.setLayout(self.layout)
 
    def criar_componentes(self):
 
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "CPF", "Telefone", "Matricula"]
        )
 
        self.layout.addWidget(self.tabela)
 
        botao_atualizar = QPushButton("Atualizar")
        self.layout.addWidget(botao_atualizar)
 
        botao_atualizar.clicked.connect(self.carregar_dados)
 
    def carregar_dados(self):
 
        self.banco.connect()
        alunos = Aluno.listar(self.banco)
        self.banco.disconnect()
 
        self.tabela.setRowCount(len(alunos))
 
        for linha, aluno in enumerate(alunos):
            self.tabela.setItem(linha, 0, QTableWidgetItem(str(aluno["id"])))
            self.tabela.setItem(linha, 1, QTableWidgetItem(aluno["nome"]))
            self.tabela.setItem(linha, 2, QTableWidgetItem(aluno["email"]))
            self.tabela.setItem(linha, 3, QTableWidgetItem(aluno["cpf"]))
            self.tabela.setItem(linha, 4, QTableWidgetItem(aluno["telefone"]))
 
            if aluno["matricula"] == True:
                self.tabela.setItem(linha, 5, QTableWidgetItem("True"))
            else:
                self.tabela.setItem(linha, 5, QTableWidgetItem("False"))