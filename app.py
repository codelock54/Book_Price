import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Path del modelo y LabelEncoders preentrenados
MODEL_PATH = "models/rf_model.pkl"
ENCODERS_PATH = "models/encoders.pkl"  # Archivo para guardar los LabelEncoders

# Cargar el modelo y los LabelEncoders
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

with open(ENCODERS_PATH, "rb") as enc_file:
    encoders = pickle.load(enc_file)


# Función de predicción
def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1, -1)
    preds = model.predict(x)
    return preds


# Aplicación principal
def main():
    # Título de la aplicación
    st.markdown(
        "<h1 style='text-align: center; color: #181082;'>SISTEMA DE PREDICCIÓN DE PRECIO DE LIBRO</h1>",
        unsafe_allow_html=True,
    )

    # Entradas de usuario
    title = st.text_input("Título del libro:")
    author = st.text_input("Autor del libro:")
    genre = st.text_input("Género del libro:")
    category = st.text_input("Categoría del libro:")
    year = st.text_input("Año de publicación:", value="0")
    rating = st.text_input("Puntuación:", value="0")
    reviews = st.text_input("Reviews:", value="0")

    if st.button("Predecir Precio"):

        try:
            # Convertir entradas categóricas usando los LabelEncoders
            title_encoded = encoders["Title"].transform([title])[0]
            author_encoded = encoders["Author"].transform([author])[0]
            genre_encoded = encoders["Genre"].transform([genre])[0]
            category_encoded = encoders["BookCategory"].transform([category])[0]

            # Convertir entradas numéricas a float
            year = float(year)
            rating = float(rating)
            reviews = float(reviews)

            # Crear el array de entrada y realizar la predicción
            x_in = [
                title_encoded,
                author_encoded,
                genre_encoded,
                category_encoded,
                year,
                rating,
                reviews,
            ]

            pred = model_prediction(x_in, model)
            st.success(f"EL PRECIO DEL LIBRO ES: ${pred[0]:.2f}".upper())

        except ValueError as e:

            st.error(f"Error en la entrada: {e}")


if __name__ == "__main__":
    main()
