# Schemas

⬆️ [Voltar para o Readme principal](../../README.md)

## Sumário

- [user.py](#userpy)
- [token.py](#tokenpy)

## user.py

O arquivo `user.py` contém as classes e esquemas que representam os usuários na API. Elas são utilizadas como entrada e saída de dados para as rotas de usuários.

- `UserBase`: Representa os campos básicos de um usuário, como `name` e `email`.
- `UserCreate`: Estende `UserBase` e adiciona o campo `password` para criação de usuários.
- `UserResponse`: Contém os dados de um usuário retornados para o cliente, incluindo o `access_token`.
- `AuthRequest`: Utilizado para autenticação, contendo `email` e `password`.

## token.py

O arquivo `token.py` contém as classes que representam os tokens de acesso na API. Elas são utilizadas como entrada e saída de dados para as rotas de autenticação.
