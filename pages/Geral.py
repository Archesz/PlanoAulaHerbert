import streamlit as st
from Betinho import Betinho
from simulados import simulados
import graphs as pg

st.set_page_config(layout="wide")

disciplinas = ["Total", "Matemática", "Física", "Química", "Biologia", "Geografia", "História", "Filosofia", "Sociologia", "Literatura", "Português"]

betinho = Betinho(mode="get")

st.title("Sistema de Análise de Simulados")

simulado = st.selectbox("Selecione o Simulado", simulados.keys())

df_simulado = betinho.getDataFrame(simulado)

#st.text(f"Simulado: {simulados_select} | Questões: {len(simulados[simulados_select.keys()])}\nNúmero de Alunos: {len(df_simulado)}")

table = pg.getTable(df_simulado)
st.plotly_chart(table) 


disciplina_1 = st.selectbox("Selecione a Disciplina", disciplinas)

col1, col2 = st.columns(2)

with col1:
    histTotal = pg.getHistTotal(df_simulado, disciplina_1)
    st.plotly_chart(histTotal)

with col2:
    histPeriodos = pg.getHistPeriodo(df_simulado, disciplina_1)
    st.plotly_chart(histPeriodos)

disciplina_2 = st.selectbox("Selecione a disciplina", disciplinas)

scatterAll = pg.getScatterAll(df_simulado, disciplina_2)
st.plotly_chart(scatterAll,  use_container_width=True)

boxplot = pg.getBox(df_simulado, disciplina_2)
st.plotly_chart(boxplot, use_container_width=True)

erros = pg.getErros(simulado, betinho.students)
st.plotly_chart(erros, use_container_width=True)
