import streamlit as st
import pandas as pd
import numpy as np

st.image("images/neurona.jpg", width=360)

st.header("¡Hola neurona!")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

with tab1:
    st.subheader("Una neurona con una entrada y un pes5o")

    w = st.slider("Peso", 0.0, 5.0)
    x = st.number_input("Introduzca el valor de la entrada")
  
    if st.button("Calcular la salida", "b1"):
        st.text(f"La salida de la neurona es {x * w}")

with tab2:
    col1, col2 = st.columns(2)

    with col1:
       st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
       w0 = st.slider("s1", 0.0, 5.0, label_visibility="collapsed")
       st.markdown("Entrada x<sub>0</sub>", unsafe_allow_html=True)
       x0 = st.number_input("i1", label_visibility="collapsed")

    with col2:
       st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
       w1 = st.slider("s2", 0.0, 5.0, label_visibility="collapsed")
       st.markdown("Entrada x<sub>1</sub>", unsafe_allow_html=True)
       x1 = st.number_input("i2", label_visibility="collapsed")
    
    if st.button("Calcular la salida", "b2"):
        st.text(f"La salida de la neurona es {x0 * w0 + x1 * w1}")

with tab3:
    col1, col2, col3 = st.columns(3)

    with col1:
       st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
       w0 = st.slider("s3", 0.0, 5.0, label_visibility="collapsed")
       st.markdown("Entrada x<sub>0</sub>", unsafe_allow_html=True)
       x0 = st.number_input("i3", label_visibility="collapsed")

    with col2:
       st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
       w1 = st.slider("s4", 0.0, 5.0, label_visibility="collapsed")
       st.markdown("Entrada x<sub>1</sub>", unsafe_allow_html=True)
       x1 = st.number_input("i4", label_visibility="collapsed")

    with col3:
       st.markdown("Peso w<sub>2</sub>", unsafe_allow_html=True)
       w2 = st.slider("s5", 0.0, 5.0, label_visibility="collapsed")
       st.markdown("Entrada x<sub>2</sub>", unsafe_allow_html=True)
       x2 = st.number_input("i5", label_visibility="collapsed")
   
    b = st.number_input("Introduzca el valor del sesgo")
        
    if st.button("Calcular la salida", "b3"):
        st.text(f"La salida de la neurona es {x0 * w0 + x1 * w1 + x2 * w2 + b}")