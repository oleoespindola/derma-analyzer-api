# API Routes

⬆️ [Voltar para o Readme principal ](../../../README.md)

## Sumário

- [Keras Model](#keras-model)
- [Token](#token)
- [User](#user)

### Keras Model

O arquivo `keras_model.py` contém a rota para fazer predições com o modelo de Keras. A rota recebe um arquivo de imagem como entrada e retorna um JSON com a probabilidade de que a imagem seja um caso de melanoma.

### Token

O arquivo `token.py` contém as rotas para gerar e verificar tokens de acesso. A rota `POST /token` gera um token com base em um email e senha válidos, e a rota `GET /token` verifica se o token é válido.

### User

O arquivo `user.py` contém as rotas para criar, ler e atualizar usuários. A rota `POST /users` cria um novo usuário, a rota `GET /users` lista todos os usuários e a rota `GET /users/{id}` lista um usuário específico. A rota `PUT /users/{id}` atualiza um usuário específico.
