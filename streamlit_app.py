import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API


def optimize_prompt(original_prompt):
    # Analizar el prompt original y crear un prompt optimizado
    optimized_prompt = "Your task is to generate a response that demonstrates creativity, originality, and accuracy. Please provide a detailed and specific answer that aligns with the desired outcome. Consider the guidelines provided and focus on clarity, conciseness, and relevance to the task at hand."

    return optimized_prompt

# Configurar el título de la aplicación
st.title('Optimización de Prompts')

# Obtener el prompt original del usuario
original_prompt = st.text_area('Ingrese el prompt original', height=200)

# Generar prompt optimizado
if st.button('Generar Prompt Optimizado'):
    optimized_prompt = optimize_prompt(original_prompt)
    
    # Mostrar el prompt optimizado
    st.subheader('Prompt Optimizado')
    st.write(optimized_prompt)
