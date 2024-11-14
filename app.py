import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.simulacion import Simulacion
import imageio
from io import BytesIO

st.title("Simulación de Modelos de Espines con Animación GIF")
st.write("Ejecuta la simulación y visualiza un GIF animado del comportamiento de la red de espines.")

# Parámetros de simulación
L = st.number_input("Tamaño de la red (L)", min_value=10, max_value=100, value=20)
modelo = st.selectbox("Selecciona el modelo", ("Ising", "Potts"))
temperatura = st.slider("Temperatura (T)", min_value=0.1, max_value=5.0, value=2.0)
campo_h = st.slider("Campo magnético (solo para Ising)", min_value=-5.0, max_value=5.0, value=0.0)
ciclos = st.number_input("Número de ciclos de Monte Carlo", min_value=10, max_value=500, value=50)

# Ejecutar simulación
if st.button("Ejecutar simulación y crear GIF"):
    simulacion = Simulacion(L, modelo, temperatura, ciclos, campo_h)
    
    # Lista para almacenar cada imagen de estado de la red como array
    frames = []

    # Ciclo para capturar cada estado de la red
    for _ in range(ciclos):
        simulacion.paso()  # Ejecutar un paso de la simulación

        # Crear la figura y capturar el estado actual
        fig, ax = plt.subplots()
        img = ax.imshow(simulacion.obtener_red(), cmap="coolwarm", interpolation="nearest")
        ax.set_title("Red de Espines (Azul = -1, Rojo = +1)")

        # Guardar el cuadro en memoria como una imagen PNG
        buf = BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        frames.append(imageio.v2.imread(buf))  # Lee el contenido del buffer en `frames`
        buf.close()
        plt.close(fig)  # Cerrar la figura para liberar memoria

    # Crear el GIF en un `BytesIO` en memoria
    gif_buffer = BytesIO()
    imageio.mimsave(gif_buffer, frames, format="GIF", duration=0.1)  # Crear el GIF en memoria
    gif_buffer.seek(0)

    # Mostrar el GIF en Streamlit
    st.image(gif_buffer, caption="Animación de la Simulación", use_column_width=True)
