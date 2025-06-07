# UTILS

⬆️ [Voltar para o Readme principal](../../README.md)

## Sumário

- [Usuário](#usuário)

## Usuário

- O arquivo `user.py` contém as funções de serviços para usuários.
  - `new_user`: Cria um novo usuário no banco de dados e retorna o token de acesso do usuário.
  - `get_user_by_email`: Retorna um usuário com base no email fornecido.
  - `user_auth`: Verifica se o email e senha fornecidos pertencem a um usuário cadastrado e retorna o token de acesso.
  - `prediction`: Faz a análise com o modelo Keras, salva a imagem no storage da Cloudinary e armazena os dados de URL e previsão no banco Supabase.
  