from modules.aluno import Aluno
from modules.mysql import MySQL

banco = MySQL()

banco.connect()

aluno = Aluno("Emanuella",
              "emanuella@gmail.com",
              "98765432110",
              "031905002764",
              "Rua Paineira, Eldorado, 1300"
              )
query = aluno.cadastrar()
print(query)

banco.execute_query(query)

banco.disconnect()