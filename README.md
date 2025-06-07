# derma-analyzer-api

🧑🏾‍⚕️ A Derma Analyzer API é uma aplicação web que utiliza técnicas de aprendizado de máquina para analisar imagens de pele e detectar possíveis casos de melanoma.

## Sumário

- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Endpoints](#endpoints)

### Documentação por Módulos

- [Modelos](app/models/README.md)
- [Esquemas](app/schemas/README.md)
- [Rotas da API](app/api/routes/README.md)
- [Banco de Dados](app/db/README.md)
- [Autenticação e Segurança](app/core/README.md)
- [UTILS](app/utils/README.md)

### Treinamento do modelo

- [Notebooks](notebooks/README.md)

## Ferramentas Utilizadas

- Python 3.10
- FastAPI
- SQLAlchemy
- Pydantic
- TensorFlow

## Endpoints

- [POST /predict](#post-predict)
- [POST /users/new](#post-usersnew)
- [POST /users/auth](#post-usersauth)
- [GET /users/current](#get-userscurrent)
- [POST /users/predict](#post-userspredict)
- [POST /users/feedback](#post-usersfeedback)

---
### GET /

Endpoint para verificar se a API está online.

Status Code de Sucesso: 200 OK

---

### POST /predict

> Rota pública

Endpoint para fazer predições com o modelo de Keras. Recebe um arquivo de imagem como entrada e retorna um JSON com a probabilidade de que a imagem seja um caso maligno de câncer de pele.

#### Exemplo de Requisição

```http
Content-Type: multipart/form-data
```

#### Exemplo de Corpo da Requisição

```plaintext
file: [sua-imagem-aqui]
```

#### Exemplo de Resposta

```json
{
  "prediction": "85.00%"
}
```

Status Code de Sucesso: 200 OK

---

### POST /users/new

> Requer api-key

Endpoint para criar usuários. Recebe um JSON no corpo da requisição com os campos `name`, `email` e `password`.

#### Exemplo de Requisição

```http
api-key: sua-api-key-aqui
```

#### Exemplo de Corpo da Requisição

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "securepassword123"
}
```

#### Exemplo de Resposta

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "sub": 1,
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Status Code de Sucesso: 200 OK

---

### POST /users/auth

> Requer api-key

Endpoint para autenticar usuários. Recebe um JSON no corpo da requisição com os campos `email` e `password`.

#### Exemplo de Requisição

```http
api-key: sua-api-key-aqui
```

#### Exemplo de Corpo da Requisição

```json
{
  "email": "johndoe@example.com",
  "password": "securepassword123"
}
```

#### Exemplo de Resposta

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "sub": 1,
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Status Code de Sucesso: 200 OK

---

### GET /users/current

> Requer api-key e Bearer token

Endpoint para obter as informações do usuário autenticado.

#### Exemplo de Requisição

```http
api-key: sua-api-key-aqui
Authorization: Bearer seu-token-aqui
```

#### Exemplo de Resposta

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "sub": 1,
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Status Code de Sucesso: 200 OK

---

### POST /users/predict

> Requer api-key e Bearer token

Endpoint para enviar uma imagem para análise. Recebe um arquivo de imagem no corpo da requisição, enviado com o tipo de conteúdo `multipart/form-data` e o nome do campo `file`.

#### Exemplo de Requisição

```http
api-key: sua-api-key-aqui
Authorization: Bearer seu-token-aqui
Content-Type: multipart/form-data
```

#### Exemplo de Corpo da Requisição

```plaintext
file: [sua-imagem-aqui]
```

#### Exemplo de Resposta

```json
{
  "predict": "0.85"
}
```

Status Code de Sucesso: 200 OK

---

### POST /users/feedback

> Requer api-key e Bearer token

Endpoint para enviar feedback sobre a análise de imagem. Recebe um JSON no corpo da requisição com os campos `analysis_id` e `feedback`.

> 💡 TRUE para análises positivas e FALSE para negativas

#### Exemplo de Requisição

```http
api-key: sua-api-key-aqui
Authorization: Bearer seu-token-aqui
```

#### Exemplo de Corpo da Requisição

```json
{
  "analysis_id": 1,
  "feedback": true
}
```

#### Exemplo de Resposta

```json
{
  "message": "Feedback saved"
}
```

Status Code de Sucesso: 200 OK

