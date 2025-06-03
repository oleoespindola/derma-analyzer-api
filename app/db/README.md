# Banco de Dados

⬆️ [Voltar para o Readme principal](../../README.md)

## Sumário

- [database.py](#databasepy)
- [base.py](#basepy)
- [Nota sobre o Banco de Dados](#nota-sobre-o-banco-de-dados)

## database.py

Contém a função `get_db` que retorna uma sessão do banco de dados. A sessão é gerenciada pelo FastAPI e é automaticamente fechada ao final de cada requisição.

## base.py

Contém a classe `Base` que é a base para todos os modelos do banco de dados. Ela fornece a conexão com o banco de dados e mapeia as tabelas.

## Nota sobre o Banco de Dados

O banco de dados não está incluído no repositório, apesar de ser um banco SQLite. Isso ocorre porque o banco de dados pode conter dados sensíveis ou configurações específicas do ambiente de desenvolvimento. No entanto, os scripts utilizados para criar e popular o banco de dados serão fornecidos em breve para que você possa recriar o ambiente localmente.
