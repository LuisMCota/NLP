import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from src.simulacion import Simulacion
import time

st.title("Simulación Animada de Modelos de Espines")
st.write("Visualiza cómo evoluciona la red de espines a lo largo de los ciclos de simulación.")

# Parámetros de simulación
L = st.number_input("Tamaño de la red (L)", min_value=10, max_value=100, value=20)
modelo = st.selectbox("Selecciona el modelo", ("Ising", "Potts"))
temperatura = st.slider("Temperatura (T)", min_value=0.1, max_value=5.0, value=2.0)
campo_h = st.slider("Campo magnético (solo para Ising)", min_value=-5.0, max_value=5.0, value=0.0)
ciclos = st.number_input("Número de ciclos de Monte Carlo", min_value=10, max_value=500, value=50)

# Ejecutar simulación
if st.button("Ejecutar y visualizar simulación"):
    simulacion = Simulacion(L, modelo, temperatura, ciclos, campo_h)
    
    # Configuración inicial de la visualización
    st.write("Evolución de la red de espines:")
    fig, ax = plt.subplots()
    img = ax.imshow(simulacion.obtener_red(), cmap="coolwarm", interpolation="nearest")
    ax.set_title("Red de Espines (Azul = -1, Rojo = +1)")
    st_plot = st.pyplot(fig)  # Crea un espacio en Streamlit para actualizar la visualización
    
    # Ciclo para actualizar la visualización en tiempo real
    for _ in range(ciclos):
        simulacion.paso()
        img.set_array(simulacion.obtener_red())
        st_plot.pyplot(fig)  # Actualiza la visualización en Streamlit
        time.sleep(0.1)  # Pausa entre cuadros para emular animación
    
    st.write("Simulación completada.")
