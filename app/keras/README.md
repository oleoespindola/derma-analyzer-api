# Keras Model

⬆️ [Voltar para o Readme principal](../../README.md)

## Sumário

- [Carregar o modelo](#carregar-o-modelo)
- [Fazer previsões](#fazer-previsões)
- [Arquitetura](#arquitetura)

### Carregar o modelo

A função `load_model` carrega o modelo de Keras treinado em memória.

> ⚠️ Lembre-se de mover o arquivo `model.keras` para essa pasta quando tiver terminado o treinamento do modelo.

### Fazer previsões

A função `predict_image` recebe uma imagem de pele em formato JPEG ou PNG e retorna a probabilidade de que a imagem seja um caso de melanoma.

### Arquitetura

A arquitetura do modelo de Keras utilizada pode ser encontrada no [README do notebook de treinamento](../notebooks/training.ipynb).
