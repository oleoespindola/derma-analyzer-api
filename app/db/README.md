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

O banco de dados é um banco Postgres hospedado no Supabase, que fornece uma camada de abstração para o banco de dados. Além disso, estou usando o Cloudinary para armazenar as imagens enviadas, o que permite que eu possa escalar a aplicação sem me preocupar com o armazenamento de arquivos.
