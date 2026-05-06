# African Economic Crisis — Neural Network Analysis
**Africa AI Hub | Week 6 Task**

## Dataset
- **Source:** Kaggle — Africa Economic Banking and Systemic Crisis Data
- **Size:** 1059 rows × 14 columns
- **Countries:** 13 African countries (1860–2014)
- **Target:** Banking Crisis — binary classification (crisis / no crisis)

## What This Notebook Covers
1. Data loading, cleaning and exploration (Pandas)
2. Feature engineering and train/test split
3. Scikit-learn baseline — Random Forest Classifier
4. Keras Sequential Neural Network
   - Input layer → Dense(64, ReLU) → Dense(1, Sigmoid)
   - Trained over 50 epochs
   - Loss and accuracy curves plotted
5. Model comparison: Random Forest vs Neural Network
6. Experiments:
   - Added extra hidden layer (64 → 32)
   - Increased neurons to 128
   - Added Dropout(0.3)

## Results
| Model | Accuracy |
|---|---|
| Random Forest | XX% |
| Base Neural Network (64) | XX% |
| NN + Extra Layer | XX% |
| NN + 128 Neurons | XX% |
| NN + Dropout 0.3 | XX% |

## Key Finding
> Neural networks are not always the best tool.
> For structured tabular data like this dataset,
> Random Forest performed competitively with far less complexity.

## Tools Used
| Tool | Purpose |
|---|---|
| Pandas | Data loading and cleaning |
| NumPy | Numerical operations |
| Scikit-learn | Baseline ML model |
| TensorFlow/Keras | Neural network |
| Matplotlib | Loss curves and charts |

## Files
- `african_crisis_nn.ipynb` — Main notebook
- `loss_curves.png` — Training loss and accuracy plots
- `model_comparison.png` — All models compared

## Author
Built as part of the Africa AI Hub Data Science Programme
