import streamlit as st
import openai

# Configurar la clave de la API de OpenAI
api_key = st.sidebar.text_input("Enter your OpenAI API key", type="password")

if not api_key:
    st.warning("Please enter a valid API key to continue.")
else:
    openai.api_key = api_key
    # Continuar con el resto del código que utiliza la clave de API



# Crear la interfaz de usuario
st.title("Mejorador de Prompts")
prompt = st.text_area("Ingresa el prompt:", value="Your task is to optimize prompts by analyzing the original prompts and creating new prompts that clearly communicate the desired outcome and provide specific guidelines for the type of response required. Your optimized prompts should encourage creativity, originality, and accuracy in the generated responses. Please focus on creating prompts that are clear, concise, and specific to the task at hand.")
if st.button("Generar Mejora"):
    # Generar la mejora del prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    improved_prompt = response.choices[0].text.strip()

    # Mostrar la mejora del prompt
    st.write("Mejora del prompt:")
    st.write(improved_prompt)
