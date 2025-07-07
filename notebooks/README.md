# 📚 Treinamento do Modelo

**Adendo**: o arquivo `modelos/keras_model.py` deve ser movido para a pasta `app/models` para ser usado na API.

## ⚙️ Configurações do Treinamento

Configurações do treinamento:

| Parâmetro | Valor | Descrição |
| --- | --- | --- |
| `rescale` | 1./255 | Normaliza as imagens para valores entre 0 e 1 |
| `validation_split` | 0.15 | Define a porcentagem de imagens para validação |
| `rotation_range` | 30 | Gira as imagens em até 30 graus |
| `zoom_range` | 0.3 | Aplica um zoom de até 30% nas imagens |
| `horizontal_flip` | True | Aplica flip horizontal nas imagens |
| `batch_size` | 32 | Tamanho do lote de imagens para treinamento |
| `class_mode` | 'binary' | Define o tipo de problema como binário (0 ou 1) |
| `input_size` | (224, 224, 3) | Tamanho das imagens de entrada |
| `model_base` | MobileNetV2 | Modelo pré-treinado utilizado como base |
| `optimizer` | Adam com Cosine Decay | Otimizador com agendamento de taxa de aprendizado |
| `callbacks` | EarlyStopping, ModelCheckpoint | Estratégias para evitar overfitting e salvar o melhor modelo |

## Modelo

Arquitetura do modelo utilizada (Transfer Learning):

* **Camada de entrada**: Imagem RGB com dimensão 224x224x3
* **Base**: MobileNetV2 pré-treinada no ImageNet, com pesos congelados inicialmente
* **Camadas adicionais:**
  * **Data Augmentation**: Flip horizontal, rotação, zoom e translação aleatória
  * **GlobalAveragePooling2D**: Reduz as dimensões e evita overfitting
  * **Dense**: 128 neurônios com ativação ReLU
  * **Dropout**: 50% para reduzir overfitting
  * **Dense** final: 1 neurônio com ativação Sigmoid para saída binária

## Resultados

Treino utilizando o dataset [Melanoma Cancer Image Dataset](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset)

### Acurácia

![Acuracia](https://github.com/oleoespindola/derma-analyzer-api/blob/feature/auth/notebooks/charts/Acur%C3%A1ria%20-%20Dataset%20Public%20Image.png?raw=true)

### Loss

![Loss](https://github.com/oleoespindola/derma-analyzer-api/blob/feature/auth/notebooks/charts/Loss%20-%20Dataset%20Public%20Image.png?raw=true)

