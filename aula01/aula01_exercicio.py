# --- Importar o Streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title('Meu Perfil')

# --- Cabeçalho com as boas vindas --- #
st.header('Seja bem-vindo ao meu site! 👋')

# --- Subcebeçalho com o nome --- #
st.subheader('Sou o Antony!')

# --- Usar o st.markdown() para as informações do perfil --- #
st.markdown('''
Sou formado em **Tecnologia em Processamento de Dados**, **MBA em Gestão de Banco de Dados Oracle** e **Pós-Graduação em Ciência de Dados e Big Analytics** 🖥️
Gosto muito de *Python*, *Banco de Dados* e *Engenharia e Análise de Dados*!
As áreas que gosto de estudar são:
* Análise de dados;
* Inteligência artificial;
* Banco de Dados;
* Engenharia de Dados;
* Análise de Dados no Futebol;
* E claro, **Streamlit**!
''')

# --- Usar o st.write() --- #
st.write('Espero que tenha gostado do meu perfil!')