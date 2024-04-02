import firebase_admin
import streamlit as st
from firebase_admin import credentials, db
import pandas as pd
from Betinho import Betinho
from simulados import simulados
from Plano import Plano

betinho = Betinho(mode="get")

planos = {
    "Matemática": {
        "Matemática Básica": {
            "Conteudos": ["Adição e Subtração", "Multiplicação e Divisão", "Frações", "Potenciação", "Radiciação", "Potência de 10 e Notação Científica", "Regra de 3 Simples e Composta", "Porcentagem", "Razão e Proporção", "Máximo Dividor Comum (MDC)", "Múltiplos e MMC", "Conjuntos numéricos"]
        },
        "Matemática Básica II": {
            "Conteudos": ["Conjuntos Numéricos", "Produtos Notáveis", "Equação do Primeiro Grau", "Equação do Segundo Grau", "Números Primos, Fatoração e Divisores", "Juros Simples", "Juros Compostos", "Teoria das Funções", "Teoria dos Conjuntos", "Função do 1º Grau", "Função do 2º Grau", "Introdução à Geometria Plana"]
        },
        "Matemática Intermediaria": {
            "Conteudos": ["Função Inversa", "Função Composta", "Função Exponencial", "Função Modular", "Retas Paralelas e Transversais", "Teorema de Tales", "Quadriláteros Notáveis", "Polígonos", "Introdução à Trigonometria", "Introdução à Sequências", "Medidas de Centralidade e Dispersão"]
        }
    }
}

nomes, ids = betinho.getStudentsDF()

estudante = st.selectbox("Selecione o Estudante", nomes)
simulado = st.selectbox("Simulados", simulados.keys())
btn_analyze = st.button("Analisar")

if btn_analyze:

    plano = Plano()

    try:
        id = ids[nomes.index(estudante)]
        data, graphs = betinho.analisarEstudante(id, simulado)

        for graph in graphs:
            st.plotly_chart(graph)

        st.title("Montar plano de estudos")

        for disciplina in planos.keys():
            st.subheader(disciplina)

            planos_selecionados = st.multiselect(f"Selecione os planos de {disciplina}", planos[disciplina].keys())            
                
            st.divider()
        
    except:
        st.error("Falha ao processar.")
