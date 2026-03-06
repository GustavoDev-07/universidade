from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton
)

from screen.cadastrar import Cadastro
from screen.listar import Listar

import sys


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.layout = QVBoxLayout()

        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)
        self.janela.setStyleSheet("""
            QWidget {
                background-color: #1c1f26;
                color: #e6e6e6;
                font-size: 14px;
                font-family: Segoe UI, Arial;
            }
        """)

        self.criar_botoes()

        self.janela.show()

    def criar_botoes(self):
        botao_listar = QPushButton("Listar")
        botao_listar.setMinimumHeight(45)

        botao_listar.setStyleSheet("""
            QPushButton {
                background-color: #2a3342;
                border: 2px solid #1e90ff;
                border-radius: 16px;
                color: #dce9ff;
                padding: 10px;
            }

            QPushButton:hover {
                border: 2px solid #00b7ff;
                background-color: #313b4f;
            }

            QPushButton:pressed {
                background-color: #222a38;
                border: 2px solid #4dc4ff;
            }
        """)

        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)

        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.setMinimumHeight(45)

        botao_cadastrar.setStyleSheet("""
            QPushButton {
                background-color: #3a2a2a;
                border: 2px solid #ff2a2a;
                border-radius: 16px;
                color: #ffe3e3;
                padding: 10px;
            }

            QPushButton:hover {
                border: 2px solid #ff4d6d;
                background-color: #463030;
            }

            QPushButton:pressed {
                background-color: #2e2020;
                border: 2px solid #ff7a7a;
            }
        """)

        self.layout.addWidget(botao_cadastrar)
        botao_cadastrar.clicked.connect(self.abrir_cadastro)

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastro(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())