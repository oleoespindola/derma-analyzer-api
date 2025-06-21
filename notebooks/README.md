# Treinamento do Modelo

**Adendo**: o arquivo `modelos/keras_model.py` deve ser movido para a pasta `app/models` para ser usado na API.

## Configurações do Treinamento

Configurações do treinamento:

| Parâmetro | Valor | Descrição |
| --- | --- | --- |
| `rescale` | 1./255 | Normaliza as imagens para valores entre 0 e 1 |
| `validation_split` | 0.2 | Define a porcentagem de imagens para validação |
| `rotation_range` | 20 | Gira as imagens em até 20 graus |
| `zoom_range` | 0.2 | Aplica um zoom de até 20% nas imagens |
| `horizontal_flip` | True | Aplica flip horizontal nas imagens |
| `batch_size` | 32 | Tamanho do lote de imagens para treinamento |
| `class_mode` | 'binary' | Define o tipo de problema como binário (0 ou 1) |
| `subset` | 'training' | Define que as imagens devem ser usadas para treinamento |

## Modelo

Modelo:

* Camada de entrada: **224x224x3**
* Camada de saída: **1** (binário)
* Camadas ocultas:
  * **ReLU**: 128 neurônios
  * **Dropout**: 50%
  * **Sigmoid**: 1 neurônio

## Resultados

Treino utilizando o dataset [Melanoma Cancer Image Dataset](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset) + [Skin Cancer Malignant vs. Benign](https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign)

### Acurácia

![Acuracia](https://github.com/oleoespindola/derma-analyzer-api/blob/feature/auth/notebooks/charts/Acur%C3%A1ria%20-%20Dataset%20Public%20Image.png?raw=true)

### Loss

![Loss](https://github.com/oleoespindola/derma-analyzer-api/blob/feature/auth/notebooks/charts/Loss%20-%20Dataset%20Public%20Image.png?raw=true)
