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
## Dependências
- **VSCode:** IDE (Interface de Desenvolvimento).
- **Mermaid:** Linguagem para confecção de Diagramas em documentos MD(Mark Down).
- **Material Icon Theme:** Tema para colorir as pastas.
- **Git Lens:** Interface gráfica para o versionamento git integrada ao VSCode.