# Modelos

⬆️ [Voltar para o Readme principal ](../../README.md)

## Sumário

- [Keras Model](#keras-model)
- [User](#user)
- [Notas sobre o banco de dados](../db/README.md#nota-sobre-o-banco-de-dados)

### Keras Model

O arquivo `keras_model.py` contém as funções para prever imagens com o modelo de Keras. A classe `Predictor` é responsável por carregar o modelo de Keras e realizar predições com imagens. Sim, Keras não é um modelo de banco de dados, mas aqui está! 🤔
A pasta `models` também precisa do arquivo `model.keras` gerado em `notebooks/training.ipynb` para funcionar corretamente. Lembre-se de mover o arquivo `model.keras` para essa pasta quando tiver terminado o treinamento do modelo.

### User

O arquivo `user.py` contém a classe `User` que representa a tabela de usuários no banco de dados. A classe tem os campos `id`, `name`, `email` e `password`, e a senha é armazenada de forma segura usando hash.

## Conexão com o Banco de Dados

Os modelos são conectados ao banco de dados através da classe `Base` importada de [app/db/database.py](../db/README.md). Essa classe fornece uma conexão e mapeamento para as tabelas do banco de dados.
