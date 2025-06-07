# API Routes

⬆️ [Voltar para o Readme principal](../../../README.md)

## Sumário

- [Keras Model](#keras-model)
- [User](#user)

### Keras Model

O arquivo `keras_model.py` contém a rota para fazer predições com o modelo de Keras. A rota recebe um arquivo de imagem como entrada e retorna um JSON com a probabilidade de que a imagem seja um caso caso maligno de cancer de pele.

> ⚠️ **Essa rota é publica e não precisa de autenticação.**

### User

O arquivo `user.py` contém as rotas relacionadas aos usuários. As seguintes funcionalidades estão disponíveis:

- **Criação de Usuário**: A rota `POST /users/new` permite criar um novo usuário e retorna um token bearer.
- **Autorização de Usuário**: A rota `POST /users/auth` autoriza um usuário existente e também retorna um token bearer.
- **Obtenção do Usuário Atual**: A rota `GET /users/current` obtém as informações do usuário autenticado.
- **Predição de Imagem**: A rota `POST /users/predict` permite que um usuário autenticado envie uma imagem para análise e receba um JSON com a probabilidade de que a imagem seja um caso maligno de câncer de pele.
