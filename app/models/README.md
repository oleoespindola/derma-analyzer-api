# Modelos

⬆️ [Voltar para o Readme principal ](../../README.md)

## Sumário

- [User](#user)
- [Image Analysis](#image-analysis)
- [Notas sobre o banco de dados](../db/README.md#nota-sobre-o-banco-de-dados)

### User

O arquivo `user.py` contém a classe `User` que representa a tabela de usuários no banco de dados. A classe tem os campos `id`, `name`, `email` e `password`, e a senha é armazenada de forma segura usando hash.

### Image Analysis

O arquivo `image_analysis.py` contém a classe `ImageAnalysis` que representa a tabela de resultados de análise de imagem no banco de dados. A classe tem os campos `id`, `user_id`, `image_url`, `prediction` e `created_at`.

## Conexão com o Banco de Dados

Os modelos são conectados ao banco de dados através da classe `Base` importada de [app/db/database.py](../db/README.md). Essa classe fornece uma conexão e mapeamento para as tabelas do banco de dados.

