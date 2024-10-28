# Book Price Prediction App 📚

Este proyecto utiliza machine learning para predecir el precio de libros basándose en características como el título, el autor, el género y la categoría del libro. La aplicación está desarrollada en Python utilizando Streamlit como frontend, y puedes acceder a ella en el siguiente enlace: [Book Price Prediction App](https://bookprice-2yjhujkac5jssqyirxg2ba.streamlit.app/).

## Descripción del Proyecto

La aplicación permite ingresar información relevante sobre un libro, y, mediante un modelo de machine learning preentrenado, calcula y muestra el precio estimado. Este modelo fue entrenado en un dataset que contiene variables categóricas y numéricas, las cuales son convertidas a valores numéricos mediante codificación y normalización.

## Características

- **Input de Características del Libro**: Se ingresan valores para las características del libro, incluidas variables categóricas como `Título`, `Autor`, `Género` y `Categoría`.
- **Codificación de Variables Categóricas**: Las variables categóricas son transformadas usando `LabelEncoder` para ser utilizadas en el modelo.
- **Predicción de Precio**: Basándose en los valores ingresados, el modelo genera una predicción de precio.
- **Interfaz Amigable**: La aplicación está diseñada en Streamlit para una fácil interacción.

## Estructura del Proyecto

- `app.py`: Script principal de Streamlit que carga el modelo, toma los inputs y genera la predicción.
- `models/rf_model.pkl`: Archivo del modelo preentrenado (Random Forest).
- `models/encoders.pkl`: Archivo que contiene los encoders para las variables categóricas.
- `requirements.txt`: Lista de dependencias para el entorno del proyecto.

## Instalación y Ejecución

Para correr la aplicación localmente:

1. Clonar el repositorio y navegar al directorio del proyecto:
   ```bash
   git clone https://github.com/codelock54/Book_Price
   cd BookPricePrediction

   pip install -r requirements.txt

   streamlit run app.py
   
   ```
