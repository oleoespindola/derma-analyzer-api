# derma-analyzer-api

## Descrição

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
- [CRUD](app/crud/README.md)

### Treinamento do modelo

- [Notebooks](notebooks/README.md)

## Ferramentas Utilizadas

- Python 3.10
- FastAPI
- SQLAlchemy
- Pydantic
- TensorFlow

## Endpoints

- [POST /token](#post-token)
- [POST /users](#post-users)
- [GET /users/{email}](#get-usersemail)
- [POST /predict](#post-predict)

### POST /token

Endpoint para gerar um token de acesso. Recebe um JSON no corpo da requisição com o campo `secret`. Exemplo de JSON:

```json
{
  "secret": "your_secret_key"
}
```

Exemplo de Resposta:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Status Code de Sucesso: 200 OK

### POST /users

Endpoint para criar usuários. Recebe um JSON no corpo da requisição com os campos `name`, `email` e `password`. Exemplo de JSON:

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "password": "securepassword123"
}
```

Status Code de Sucesso: 201 Created
> Requer autenticação com Bearer Token.

### GET /users/{email}

Endpoint para obter informações de um usuário específico. O email do usuário deve ser passado no corpo da requisição. Retorna um JSON com os campos `id`, `name` e `email`. Exemplo de Resposta:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

Status Code de Sucesso: 200 OK
> Requer autenticação com Bearer Token.

### POST /predict

Endpoint para fazer previsões de imagens de pele. Recebe um arquivo de imagem em formato JPEG ou PNG no corpo da requisição. A imagem deve ser quadrada (1x1) para melhores resultados. Retorna um JSON com a probabilidade de que a imagem seja um caso de melanoma. Não requer autenticação. Exemplo de Resposta:

```json
{
  "prediction": "85.67%"
}
```

Status Code de Sucesso: 200 OK



