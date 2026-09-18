import streamlit as st
import pandas as pd

def crear_tabla(num1, num2):
    valor1 = int(num1)
    valor2 = int(num2)
    resultado = valor1*valor2

    dato = [{"numero1": valor1,
            "numero2":valor2, 
            "resultado": resultado}]

    df_tabla = pd.DataFrame(dato)

def tabla():
    with st.form("tablas", clear_on_submit=True):
        st.title('formulario tablas')
        num1 = st.number_input("numero 1", step = 1)
        num2 = st.number_input("numero 2", step = 1)
        btn_enviar = st.form_submit_button("evaluar")

    if btn_enviar:
        if num1 and num2:
            st.spinner("cargando...")
            st.dataframe(crear_tabla(num1,num2))