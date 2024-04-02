class Plano():

    def __init__(self):
        self.plano = {
            "Matemática": [],
            "Física": [],
            "Química": [],
            "Biologia": [],
            "Geografia": [],
            "História": [],
            "Sociologia": [],
            "Filosofia": [],
            "Literatura": [],
            "Gramática": []
        }

    def insertConteudo(self, disciplina, conteudo):
        self.plano.disciplina.append(conteudo)