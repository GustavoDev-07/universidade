from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL( 
              '127.0.0.1',
              'root'
              '',
              'universidade'
              )

banco.connect()

consulta = Aluno.listar(banco)

aluno = Aluno("Emanuella",
              "emanuella@gmail.com",
              "98765432110",
              "031905002764",
              "Rua Paineira, Eldorado, 1300"
              )
query = aluno.cadastrar(banco)
print(query)

banco.execute_query(query)

banco.disconnect()