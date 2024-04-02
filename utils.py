def converter_respostas(resposta_aluno):
    respostas_dict = {}
    for i, resposta in enumerate(resposta_aluno, start=1):
        respostas_dict[str(i)] = resposta

    return respostas_dict

def insertSimulado(student_id, estudante, nome_simulado, gabarito_student_str, gabarito_oficial, ref):  

    gabarito_student = converter_respostas(gabarito_student_str)

    simulado = {
        "Acertos": {"Total": 0, "Português": 0, "Literatura": 0, "Matemática": 0, "Física": 0, "Química": 0, "Biologia": 0, "História": 0, "Geografia": 0, "Filosofia": 0, "Sociologia": 0},
        "Gabarito": gabarito_student,
        "Erros": []
    }

    for i in gabarito_oficial.keys():
        if gabarito_oficial[i]["Resposta"] == gabarito_student[i]:
            simulado["Acertos"][gabarito_oficial[i]["Disciplina"]] += 1
            simulado["Acertos"]["Total"] += 1
            
            conteudos_questao = gabarito_oficial[i]["Conteudo"]
            disciplina = gabarito_oficial[i]["Disciplina"]

            for conteudo in conteudos_questao:
                for key in estudante["desempenho"][disciplina].keys():
                    if conteudo in estudante["desempenho"][disciplina][key].keys():
                        estudante["desempenho"][disciplina][key][conteudo]["Acertos"] += 1
        else:
            simulado["Erros"].extend(gabarito_oficial[i]["Conteudo"])

            conteudos_questao = gabarito_oficial[i]["Conteudo"]
            disciplina = gabarito_oficial[i]["Disciplina"]

            for conteudo in conteudos_questao:
                for key in estudante["desempenho"][disciplina].keys():
                    if conteudo in estudante["desempenho"][disciplina][key].keys():
                        estudante["desempenho"][disciplina][key][conteudo]["Erros"] += 1

    estudante["Simulados"][nome_simulado] = simulado

    ref.child(student_id).update(estudante)

    return 1

def getMean(df, disciplina, size=2):
    value = round(df[disciplina].mean(), size)
    return value