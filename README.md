# ML_TP1
# 🏠 House Price Prediction - Linear Regression from Scratch

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

Este proyecto implementa un sistema de **Predicción de Precios de Viviendas** utilizando técnicas de Machine Learning. El núcleo del proyecto es una implementación propia (custom) de **Regresión Lineal**, desarrollada puramente con `NumPy` sin depender de librerías de alto nivel como Scikit-Learn para el entrenamiento.

El objetivo principal es predecir el valor de mercado de propiedades inmobiliarias basándose en características como área, ubicación (latitud/longitud), antigüedad y amenities, aplicando técnicas de regularización y optimización matemática.

## 🚀 Características Principales

* **Core ML Propio**: Implementación de la clase `LinearReg` desde cero.
* **Métodos de Entrenamiento**:
    * **Gradient Descent (GD)**: Optimización iterativa.
    * **Ecuación Normal (Pseudo-inversa)**: Solución analítica exacta.
* **Regularización**: Soporte para **L1 (Lasso)** y **L2 (Ridge)** para evitar overfitting.
* **Feature Engineering**: Transformación de coordenadas geográficas en variables binarias (`lat_bin`, `lon_bin`) para capturar tendencias de precios por zona.
* **Validación**: Selección de hiperparámetros ($\lambda$) mediante Cross-Validation.

## 🛠️ Tecnologías Utilizadas

* **Python 3**: Lenguaje principal.
* **NumPy**: Cálculo matricial y vectorial para la implementación de los algoritmos.
* **Pandas**: Manipulación y limpieza del dataset.
* **Matplotlib / Seaborn**: Análisis exploratorio de datos (EDA) y visualización.
* **Jupyter Notebook**: Entorno de experimentación y reporte.

## 📂 Estructura del Proyecto

```text
HOUSE-PRICE-PREDICTION/
│
├── data/
│   ├── raw/
│   │   ├── casas_dev.csv       # Datos de entrenamiento/validación
│   │   ├── casas_test.csv      # Datos de prueba
│   │   └── vivienda_Amanda.csv # Caso de uso específico
│   └── processed/              # Datos normalizados y limpios
│
├── models.py                   # 🧠 Lógica Core: Clase LinearReg
├── Entrega_TP1.ipynb           # Notebook con EDA, entrenamiento y pruebas
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Documentación
