# 📚 Treinamento do Modelo

⬆️ [Voltar para o Readme principal ](../README.md)

## ⚙️ Configurações do Treinamento

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

> Mais informações no training.ipynb

## Adendos

Um dos modelos (ex: best_model.keras) deve ser escolhido, renomeado para `model.keras` e movido para a pasta `app/keras` para ser usado na API.

Treino utilizando o dataset [Melanoma Cancer Image Dataset](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset)
