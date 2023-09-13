import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API

# Configurar el título de la aplicación
st.title('Optimización de Prompt')

# Obtener el prompt del usuario
prompt = st.text_area('Ingrese el prompt que desea optimizar', height=200)

# Generar texto optimizado utilizando OpenAI GPT-3
if st.button('Generar Optimización'):
    # Llamar a la API de OpenAI para generar texto optimizado
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    
    # Mostrar el texto optimizado generado por OpenAI GPT-3
    st.subheader('Texto Optimizado')
    st.write(response.choices[0].text.strip())
