# derma-analyzer-api

## Ferramentas Utilizadas

- **Python 3.10**
  - A versão utilizado do Python é 3.10, versões mais recentes do Python possuem problemas de compatibilidade com o TensorFlow.
    ‌**Será necessário estudar possível problemas de segurança devido à versão antiga utilizada do Python.**

## Importações

---

```
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
```

Evita problemas na importação do TensorFlow

## Modelo

---

### Data Generation

- `rescale=1./255`
  - Normaliza os pixels das imagens de 0–255 para 0–1 (padrão em redes neurais)
- `validation_split=0.2`
  - Separa 20% do dataset para as validações.
- `rotation_range=20`
  - Gira a imagem aleatoriamente até 20°
- `zoom_range=0.2`
  - Dá zoom aleatório até 20%.
- \`horizontal_flip=True\``
  - Inverte a imagem na horizontal ocasionalmente (para simular imagens diferentes).

### Train Data

- `batch_size=32`
  - Vai treinar com pacotes de 32 imagens por vez.
- `class_mode='binary'`
  - Como só temos duas classes (melanoma e benigno), usamos binário
- `subset='training'`
  - Diz que é a parte de **treino, dos 80% do dataset.**

### Validadion Data

- `subset='training'`
  - Diz que é a parte da **validação, dos 20% do dataset.**

## Model

```
tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
```

- `32` → número de **filtros** (pensa como detectores de padrões: bordas, formas, etc.)
- `(3,3)` → tamanho do filtro (vai olhar janelas de 3x3 pixels)
- `activation='relu'` → função de ativação que deixa o modelo **não-linear** (ignora valores negativos)
- `input_shape=(224,224,3)` → formato da imagem de entrada:
  - 224x224 pixels
  - 3 canais (RGB)

‌

```
tf.keras.layers.MaxPooling2D(2,2),
```

- Agora com **64 filtros** (mais complexidade → detecta padrões mais abstratos)
- Também com janelas 3x3
- ReLU de novo para ativação

‌

```
tf.keras.layers.Flatten()
```

Transforma o resultado da imagem (formato matriz 2D) em um vetor 1D (linear). Isso é necessário para conectar com as camadas densas (fully connected) a seguir.

‌

```
tf.keras.layers.Dense(128, activation='relu')
```

- 128 **neurônios**
- Cada neurônio está conectado a **todos os valores anteriores**

‌

```
tf.keras.layers.Dropout(0.5)
```

> Durante o treinamento, **desliga aleatoriamente 50% dos neurônios** dessa camada.

- Serve para **evitar overfitting** (evitar que memorize exemplos específicos do treino)
- Força o modelo a aprender de forma mais robusta e generalista

‌

```
tf.keras.layers.Dense(1, activation='sigmoid')
```

- Um único neurônio, porque estamos fazendo **classificação binária** (0 ou 1)
- `sigmoid` transforma a saída em um valor entre 0 e 1 → probabilidade de ser da **classe positiva** (ex: `malignant`)

‌

```
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

- `optimizer='adam'` → algoritmo que ajusta os pesos
- `loss='binary_crossentropy'` → função de perda ideal para **classificação binária**
- `metrics=['accuracy']` → queremos monitorar a **acurácia** enquanto