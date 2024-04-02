import firebase_admin
from firebase_admin import credentials, db

import pandas as pd
import statistics as stats

import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

from utils import insertSimulado, getMean
from simulados import simulados

class Betinho():

    def __init__(self, mode):
        self.name = "Betinho"
        self.mode = mode
        self.initialize()


    def initialize(self):
        if self.mode == "start":
            cred = credentials.Certificate("key.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://herbert2024-be557-default-rtdb.firebaseio.com/',
                'storageBucket': 'gs://herbert2024-be557.appspot.com'
            }) 
        elif self.mode == "get":
            firebase_admin.get_app()

        self.ref = db.reference("/students")
        self.students = self.ref.get()
    
    def getStudents(self):
        students_dict = {}

        for student_id, student_data in self.students.items():
            students_dict[student_id] = student_data.nome

        return students_dict

    def adicionarSimulado(self, nome_simulado):
        for student_id, student_data in self.students.items():
            try:
                gabarito_student = simulados[nome_simulado]["Gabaritos_Alunos"][student_id]
                insertSimulado(student_id, student_data, nome_simulado, gabarito_student, simulados[nome_simulado]["Gabarito"], self.ref)
                print(f"Inserido com sucesso | {student_data['nome']}")
            except:
                print(f"Erro ao inserir o estudante: {student_id} | {student_data['nome']}")

    def deleteSimulado(self, nome_simulado):
        for student_id, student_data in self.students.items():
            try:
                if nome_simulado in student_data["Simulados"]:
                    del student_data["Simulados"][nome_simulado]
                    self.ref.child(student_id).update(student_data)
                    print(f"Simulado '{nome_simulado}' deletado com sucesso para {student_data['nome']}")
                else:
                    print(f"O simulado '{nome_simulado}' não foi encontrado para {student_data['nome']}")
            except Exception as e:
                print(f"Erro ao deletar o simulado '{nome_simulado}' para o estudante {student_id}: {e}")

    def getDataFrame(self, nome_simulado):
        df = []
        for student_id, student_data in self.students.items():
            try:
                student = student_data["Simulados"][nome_simulado]["Acertos"]
                student["Nome"] = student_data["nome"]
                student["Periodo"] = student_data["periodo"]
                student["Genero"] = student_data["genero"]

                df.append(student) 
            except:
                continue
        
        df = pd.DataFrame(df)
        # Calculando os valores

        return df
    
    def getStudentsDF(self):
        #student = self.students[nome_estudante]

#        df = []
        nomes = []
        ids = []
        for student_id, student_data in self.students.items():
            try:
                student = {}
                nomes.append(student_data["nome"])
                ids.append(student_id)
                # df.append(student) 
            except:
                continue
        
        return nomes, ids

    def analisarEstudante(self, id, simulado):
        student = self.students[id]
        disciplinas = student["Simulados"][simulado]["Acertos"].keys()
        acertos = student["Simulados"][simulado]["Acertos"].values()
        erros = list(student["Simulados"][simulado]["Erros"])

        sorted_values = sorted(zip(disciplinas, acertos), key=lambda x: x[1], reverse=True)
        disciplinas, acertos = zip(*sorted_values)

        fig_acertos = px.bar(x=disciplinas, y=acertos, title="Acertos por Disciplina", labels={"x": "Disciplina", "y": "Acertos"},
                             color=disciplinas)

        # Erros 
        erros = pd.DataFrame(erros)
        erros = erros.value_counts().reset_index()
        erros.columns = ["Conteudo", "Quantidade"]

        fig_erros = px.bar(erros, x="Conteudo", y="Quantidade", color="Quantidade", title="Lista de conteúdos com erros")

        return student, [fig_acertos, fig_erros]

    def analisarSimulado(self, nome_simulado):
        df = []
        for student_id, student_data in self.students.items():
            try:
                student = student_data["Simulados"][nome_simulado]["Acertos"]
                student["Nome"] = student_data["nome"]
                student["Periodo"] = student_data["periodo"]
                student["Genero"] = student_data["genero"]

                df.append(student) 
            except:
                continue
        
        df = pd.DataFrame(df)
        # Calculando os valores

        df_stats = df[["Biologia", "Filosofia", "Física", "Geografia", "História", "Literatura", "Matemática", "Português", "Química", "Sociologia", "Total"]]

        min_values = df_stats.min().tolist()
        max_values = df_stats.max().tolist()
        mean_values = [round(value) for value in df_stats.mean().tolist()]
        
        # Informações
        print(f"Quantidade de Participantes: {len(df)}")
        
        # Tabela de valores
        data_table = [
            ["Medida", "Biologia", "Filosofia", "Física", "Geografia", "História", "Literatura", "Matemática", "Português", "Química", "Sociologia", "Total"],
            ["Mínimo"] + min_values,
            ["Média"] + mean_values,
            ["Máximo"] + max_values,
        ]

        colorscale = [[0, '#EF3E36'],[.5, '#FFD1D1'],[1, '#ffffff']]

        fig_table = ff.create_table(data_table, colorscale=colorscale)
        fig_table.show()

        # Barras de Pontuação Geral
        fig_scatter_total = px.bar(df, x="Total", y="Total", hover_data=["Nome"], color="Genero", title="Histograma de Acertos Totais")
        fig_scatter_total.show()

        # Matriz de Dispersão 1
#        df_matrix_1 = df[["Total", "Matemática", "Física", "Química", "Biologia"]]
        fig_matrix_1 = px.scatter_matrix(df, ["Total", "Matemática", "Física", "Química", "Biologia"], hover_data=["Nome", "Periodo"],  title="Matriz de Dispersão (Exatas e Natureza)")
        fig_matrix_1.show()

        # Matriz de Dispersão 2
        fig_matrix_2 = px.scatter_matrix(df, ["Total", "História", "Geografia", "Português", "Literatura", "Sociologia", "Filosofia"], hover_data=["Nome", "Periodo"], title="Matriz de Dispersão (Humanas e Linguagens)")
        fig_matrix_2.show()

        # Histograma por periodos
        fig_hist_periodo = px.histogram(df, x="Total", color="Periodo", facet_col="Periodo")

        fig_hist_periodo.update_layout(
            title="Distribuição das notas dos alunos por período",
            xaxis_title="Nota Total",
            yaxis_title="Contagem",
            bargap=0.1
        )

        fig_hist_periodo.show()

        # Scatter Por periodos
        fig_scatter = px.scatter(df, x="Periodo", y="Total", hover_data=["Nome"], color="Genero", title="Distribuição de acertos Totais (Periodo e Sexo)")
        fig_scatter.show()

        # Boxplot
        fig_box = px.box(df, x="Periodo", y="Total", color="Genero")
        fig_box.show()

        # Gerar acertos
        erros_list = []

        for student_id, student_data in self.students.items():
            try:
                erros = student_data["Simulados"][nome_simulado]["Erros"]
                erros_list.extend(erros)
            except:
                continue

        erros_serie = pd.Series(erros_list) 
        erros_serie = erros_serie.value_counts().reset_index()
        erros_serie.columns = ["Conteudo", "Quantidade"]

        fig_erros = px.bar(erros_serie, x="Conteudo", y="Quantidade", title="Indice de Erros por Conteudo")
        fig_erros.show()

        return fig_table