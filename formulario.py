import streamlit as st

def formulario():
    st.title("formulario")
    st.divider()

    with st.form("contacto", clear_on_submit=True):
        st.header("contactenos")
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("nombre")
        with col2:
            email = st.text_input("email")
        descripcion = st.text_area("descripcion")
        btn_enviar = st.form_submit_button("cargar")

    if btn_enviar:
        st.toast(f"datos: {nombre}, correo: {email}")
        st.success(f"datos: {nombre}, correo: {email}\n{descripcion}")