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

### POST /users

Endpoint para criar usuários. Recebe um JSON com os campos `name`, `email` e `password`.

### GET /users/{id}

Endpoint para obter informações de um usuário específico. Retorna um JSON com os campos `id`, `name` e `email`.

### POST /predict

Endpoint para fazer previsões de imagens de pele. Recebe um arquivo de imagem em formato JPEG ou PNG e retorna um JSON com a probabilidade de que a imagem seja um caso de melanoma.
