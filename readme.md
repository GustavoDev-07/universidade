# Projeto Universidade

Modelagem em Orientação à Objetos
das Entidades Alunos, Cursos e Turmas.

## Caso de Uso
```mermaid
flowchart LR
    Usuário([Secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Alunos))

    Usuário --> UC1
    Usuário --> UC2
    Usuário --> UC3
```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno {
        - nome
        - email
        - cpf
        - telefone
        - endereço
        - matrícula
        + cadastrar()
        + editar()
        + transferir()
    }
```

## Diagrama de Sequência - **Cadastro**
```mermaid
sequenceDiagram 
    participant UI as TelaCadastro 
    participant Entidade as Aluno 
    participant DB as MySQL 
    participant Banco as MySQL Server 

    UI ->> Entidade: cria Aluno(...) 
    UI ->> DB: connect() 
    UI ->> Entidade: cadastrar(DB) 
    Entidade ->> DB: execute_query(INSERT) 
    DB ->> Banco: Envia SQL 
    Banco -->> DB: Confirmação 
    DB -->> Entidade: lastrowid 
    UI ->> DB: disconnect()
```
## Diagrama de Sequência - **Listagem**
```mermaid
sequenceDiagram
    participant UI as TelaListagem
    participant Entidade as Aluno
    participant DB as MySQL
    participant Banco as MySQL Server

    UI ->> DB: connect()
    UI ->> Entidade: listar(DB)
    Entidade ->> DB: execute_query(SELECT)
    DB ->> Banco: Envia SQL (SELECT)
    Banco -->> DB: Retorna registros
    DB -->> Entidade: lista de alunos
    Entidade -->> UI: lista de alunos
    UI ->> UI: preencher QTableWidget
    UI ->> DB: disconnect()
```

# Funções MySQL

- CREATE - Cria tabelas dentro da base de dados.
- INSERT - Cria registros dentro das tabelas.
- SELECT - Permite visualizar os dados dentro das tabelas. Também permite filtrar os dados que quer visualizar.
- ALTER - Altera a estrutura das tabelas, adicionando ou removendo atributos(campos).
- UPDATE - Atualiza registros dentro da tabelas.
- DROP - Exclui a tabela ou a base de dados inteira.
- DELETE - Exclui registros dentro das tabelas.

## Conceitos MySQL

- Banco de Dados: Programa hospedado na máquina com objetivo de persistir dados fisicamente no HD.
- Base de Dados: Conjunto de tabelas.
- Tabelas: Conjunto de Registros.
- Registros: Uma linha na tabela, contendo a informação dos seus atributos.
- Atributos: Uma das caracteristicas da tabela (Colunas). 

## Bicliotecas Python

Este é um projeto desktop, utilizando as tecnologias:

- Python
- PySide6
- PyInstaller

## Dependências
- **VSCode:** IDE (Interface de Desenvolvimento).
- **Mermaid:** Linguagem para confecção de Diagramas em documentos MD(Mark Down).
- **Material Icon Theme:** Tema para colorir as pastas.
- **Git Lens:** Interface gráfica para o versionamento git integrada ao VSCode.
- **MySQL:** SGBD (Sistema Gerenciador de Banco de Dados). Permite conectar o usuário com o servidor MySQL, possibilitando criar bases de dados, tabelas, incluir e modificar atributos e registros.