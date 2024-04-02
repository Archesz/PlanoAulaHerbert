import pandas as pd
import statistics as stats

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

def getTable(df):
    df_stats = df[["Biologia", "Filosofia", "Física", "Geografia", "História", "Literatura", "Matemática", "Português", "Química", "Sociologia", "Total"]]
    min_values = df_stats.min().tolist()
    max_values = df_stats.max().tolist()
    mean_values = [round(value) for value in df_stats.mean().tolist()]

    data_table = [
        ["", "Medida", "Biologia", "Filosofia", "Física", "Geografia", "História", "Literatura", "Matemática", "Português", "Química", "Sociologia", "Total"],
        ["", "Mínimo"] + min_values,
        ["", "Média"] + mean_values,
        ["", "Máximo"] + max_values,
    ]

    colorscale = [[0, '#EF3E36'],[.5, '#FFD1D1'],[1, '#ffffff']]

    fig_table = ff.create_table(data_table, colorscale=colorscale)
    fig_table.layout.width = 1000
    fig_table.update_annotations(xanchor="center")

    return fig_table

def getHistTotal(df, disciplina):
    fig_scatter_total = px.histogram(df, disciplina, color="Genero", title="Histograma de Acertos Totais",
                               labels={"Quantidade": "Acertos", "count": "Quantidade"}, nbins=20)
    return fig_scatter_total

def getHistPeriodo(df, disciplina):
    fig_hist_periodo = px.histogram(df, x=disciplina, color="Periodo", facet_col="Periodo")

    fig_hist_periodo.update_layout(
        title="Distribuição das notas dos alunos por período",
        xaxis_title="Nota Total",
        yaxis_title="Contagem",
        bargap=0.1
    )

    return fig_hist_periodo

def getScatterAll(df, disciplina):
    # Cria o gráfico de dispersão
    fig = px.scatter(df, y=disciplina, hover_data=["Nome"], color="Periodo", title="Distribuição das notas dos alunos")
     
    return fig

def getBox(df, disciplina):
    # Boxplot
    fig_box = px.box(df, x="Periodo", y=disciplina, title="Distribuição das notas dos alunos por periodo")
    return fig_box

def getErros(nome_simulado, students):
    erros_list = []

    for student_id, student_data in students.items():
        try:
            erros = student_data["Simulados"][nome_simulado]["Erros"]
            erros_list.extend(erros)
        except:
            continue

    erros_serie = pd.Series(erros_list) 
    erros_serie = erros_serie.value_counts().reset_index()
    erros_serie.columns = ["Conteudo", "Quantidade"]

    fig_erros = px.bar(erros_serie, x="Conteudo", y="Quantidade", title="Indice de Erros por Conteudo")
    return fig_erros