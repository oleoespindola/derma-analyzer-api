# Treinamento do Modelo

**Adendo**: o arquivo `modelos/keras_model.py` deve ser movido para a pasta `app/models` para ser usado na API.

## Configurações do Treinamento

Configurações do treinamento:

| Parâmetro | Valor |
| --- | --- |
| `rescale` | 1./255 |
| `validation_split` | 0.2 |
| `rotation_range` | 20 |
| `zoom_range` | 0.2 |
| `horizontal_flip` | True |
| `batch_size` | 32 |
| `class_mode` | 'binary' |
| `subset` | 'training' |

## Modelo

Modelo:

* Camada de entrada: **224x224x3**
* Camada de saída: **1** (binário)
* Camadas ocultas:
  * **ReLU**: 128 neurônios
  * **Dropout**: 50%
  * **Sigmoid**: 1 neurônio

## Resultados

(Em Breve)
