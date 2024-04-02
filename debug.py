import firebase_admin
from firebase_admin import credentials, db
import pandas as pd

disciplinas = {
            "Matemática": {
                "Matemática Básica": {
                    "Matemática Básica": False,
                    "Adição e Subtração": False,
                    "Multiplicação e Divisão": False,
                    "Frações": False,
                    "Potenciação": False,
                    "Radiciação": False,
                    "Racionalização de Denominadores": False,
                    "Produtos Notáveis": False,
                    "Potência de 10 e Notação Científica": False,
                    "Conjuntos Numéricos": False,
                    "Fatoração de Expressões Algébricas": False,
                    "Sistema de Numeração decimal": False,
                    "Equação do Primeiro Grau": False,
                    "Equação do Segundo Grau": False,
                    "Números Primos, Fatoração e Divisores": False,
                    "Múltiplos e MMC": False,
                    "Máximo Dividor Comum (MDC)": False,
                    "Razão e Proporção": False,
                    "Grandezas Diretamente Proporcionais": False,
                    "Grandezas Inversamente Proporcionais": False,
                    "Regra de 3 Simples e Composta": False,
                    "Porcentagem": False,
                    "Juros Simples": False,
                    "Juros Compostos": False,
                },
                "Conjuntos e Funções": {
                    "Funções": False,
                    "Conjuntos numéricos": False,
                    "Teoria dos Conjuntos": False,
                    "Função do 1º Grau": False,
                    "Função Inversa": False,
                    "Função Composta": False,
                    "Função do 2º Grau": False,
                    "Função Exponencial": False,
                    "Função Logarítmica": False,
                    "Função Modular": False
                },
                "Geometria": {
                    "Geometria": False,
                    "Introdução à Geometria Plana": False,
                    "Retas Paralelas e Transversais": False,
                    "Teorema de Tales": False,
                    "Pontos Notáveis de Triângulos": False,
                    "Quadriláteros Notáveis": False,
                    "Polígonos": False,
                    "Circulo e Circunferência": False,
                    "Introdução à Geometria Analítica": False,
                    "Cônicas": False,
                    "Geometria Espacial": False,
                    "Poliedros": False,
                    "Prismas, Paralelepípedos e Cubos": False,
                    "Cilindro e Cones": False,
                    "Troncos de Cone, Pirâmides e Semelhança de Sólidos": False,
                    "Esferas": False,
                    "Projeção Ortogonal e Planificação de Sólidos": False
                },
                "Trigonometria": {
                    "Trigonometria": False,
                    "Introdução à Trigonometria": False,
                    "Transformações Trigonométricas": False,
                    "Função Trigonométrica": False,
                    "Circulo Trigonométrico": False
                },
                "Sequências": {
                    "Sequências": False,
                    "Introdução à Sequências": False,
                    "Progressão Aritmética": False,
                    "Progressão Geométrica": False,
                },
                "Estatística e Combinatória": {
                    "Estatística e Combinatória": False,
                    "Medidas de Centralidade e Dispersão": False,
                    "Principio Fundamental da Contagem": False,
                    "Permutação e Arranjo": False,
                    "Combinação": False,
                    "Probabilidade": False,
                    "Probabilidade Condicional": False
                },
                "Sistemas Lineares": {
                    "Sistemas Lineares": False,
                    "Introdução à Sistemas Lineares": False,
                    "Escalonamento e Regra de Cramer": False,
                },
                "Outros": {
                    "Matrizes": False,
                    "Números Complexos": False,
                    "Polinômios": False
                }
            },
            "Biologia": {
                "Bioquímica": {
                    "Bioquímica": False,
                    "Níveis de Organização": False,
                    "Sais Minerais": False,
                    "Carboidratos e Lipídios": False,
                    "Proteínas e Enzimas": False,
                    "Ácidos Nucleicos": False
                },
                "Ecologia": {
                    "Ecologia": False,
                    "Introdução à Ecologia": False,
                    "Dinâmica Populacional, Cadeias alimentares e Pirâmide Ecológica": False,
                    "Relações Ecológicas": False,
                    "Sucessão Ecológica e Zonação": False,
                    "Ciclos Biogeoquímicos": False,
                    "Biociclos e Biomas": False,
                    "Desequilíbrios Ecológicos": False
                },
                "Citologia": {
                    "Citologia": False,
                    "Tipos de Células e Membrana Plasmática": False,
                    "Transporte em Membrana": False,
                    "Citoplasma, Organelas e Estruturas celulares": False,
                    "Respiração Celular aeróbica e anaeróbica": False,
                    "Fermentação": False,
                    "Fotossíntese e Quimiossíntese": False,
                    "Síntese de Proteinas": False,
                    "Ciclo Celular e Mitose": False,
                    "Meiose e Gametogênese": False
                },
                "Origem da Vida e Evolução": {
                    "Origem da Vida e Evolução": False,
                    "Origem da Vida": False,
                    "Características dos seres vivos": False,
                    "Evolução": False,
                    "Especiação": False
                },
                "Histologia Humana": {
                    "Histologia Humana": False,
                    "Tecido Epitelial": False,
                    "Tecidos Conectivos e Adiposo": False,
                    "Tecidos Conectivos Cartilaginoso e Ósseo": False,
                    "Tecidos Conectivos Hematopoiético e Sanguíneo": False,
                    "Tecido Muscular": False,
                    "Tecido Nervoso": False
                },
                "Genética": {
                    "Genética": False,
                    "Conceitos de Genética": False,
                    "Primeira lei de Mendel": False,
                    "Heredogramas e Cruzamento-Teste": False,
                    "Sistema ABO e Eritoblastose Fetal": False,
                    "Sistema Rh, Sistema MN e Efeito Bombaim": False,
                    "Genética do sexo e sistema de determinação de sexo": False,
                    "Segunda Lei de Mendel": False,
                    "Linkage": False,
                    "Expressividade e Interação Gênica": False,
                    "Pleiotropia e Genética de Populações": False,
                    "Mutações e Engenharia Genética": False
                },
                "Fisiologia": {
                    "Fisiologia": False,
                    "Sistema Digestório": False,
                    "Sistema Respiratório": False,
                    "Sistema Circulatório Humano": False,
                    "Sistema Circulatório dos Vertebrados": False,
                    "Sistema Imunológico e Linfático": False,
                    "Sistema Excretor": False,
                    "Sistema Nervoso": False,
                    "Órgãos dos Sentidos": False,
                    "Sistema Endócrino": False,
                    "Sistema Reprodutor": False
                },
                "Seres Vivos": {
                    "Seres Vivos": False,
                    "Classificação dos Seres Vivos": False,
                    "Taxonomia": False,
                    "Virus e Viroses": False,
                    "Reino Fungi": False,
                    "Reino Protista e Protozooses": False,
                    "Poríferos e cnidários": False,
                    "Platelmintos e nematelmintos": False,
                    "Verminoses": False,
                    "Protocordados e vertebrados": False,
                    "Métodos contraceptivos": False,
                    "Mamíferos": False,
                    "Fisiologia comparada e evolução dos seres vivos": False,
                    "Ciclos reprodutivos no Reino Plantae": False,
                    "Briófitas e pteridófitas": False,
                    "Gimnospermas e angiospermas": False,
                    "Evolução das plantas, tipos de polinização e": False,
                    "morfologia externa de plantas": False,
                    "Fitormônios": False,
                    "Histologia vegetal": False,
                    "Fitocromos e classificação complementar de plantas": False,
                    "Anel de Malpighi, transpiração e estômatos": False
                },
                "Embriologia": {
                    "Embriologia": False,
                    "Embriogênese do anfioxo": False,
                    "Tipos de gêmeos e classificação dos animais": False,
                    "Destino dos folhetos embrionários e anexos embrionários": False,
                    "Tipos de ovos e segmentações": False,
                }
            },
            "Química": {
                "Físico-Química": {
                    "Físico-Química": False,
                    "Gráficos e Conceitos de Termoquimica": False,
                    "Cálculo de Varição de Entalpia": False,
                    "Entropia e Energia de Gibbs": False,
                    "Cinética Química": False,
                    "Kc e Kp em Equilíbrio Químico": False,
                    "Equilíbrio Iônico": False,
                    "Equilíbrio Iônico da Água e Hidrólise Salina": False,
                    "Solução Tampão e Kps": False,
                    "Pilhas e Bateria": False,
                    "Eletrólise": False
                },
                "Química Orgânica": {
                    "Química Orgânica": False,
                    "Postulados de Kekulê": False,
                    "Classificação e Hibridização do Carbono": False,
                    "Classificação de Cadeias Carbônicas": False,
                    "Hidrocarbonetos e Nomenclatura de Compostos Orgânicos": False,
                    "Hidrocarbonetos Alifáticos e Cíclicos e Regra Geral de Nomenclatura": False, 
                    "Aldeído, éster, sal orgânico e anidrido": False,
                    "Éter, nitrila, ácido sulfônico, tiocomposto, amina e amida": False,
                    "Haletos orgânicos": False,
                    "Isomeria plana": False,
                    "Isomeria geométrica": False,
                    "Isomeria óptica": False,
                    "Propriedades físicas dos compostos orgânicos": False,
                    "Acidez e basicidade de compostos orgânicos": False,
                    "Polímeros de adição": False,
                    "Polímeros de condensação": False,
                    "Reações orgânicas de substituição": False,
                    "Reações orgânicas de adição": False
                },
                "Química Ambiental": {
                    "Química Ambiental": False,
                    "Bioquímica": False,
                    "Recursos Orgânicas": False
                }
            },
            "Física": {
                "Termologia": {
                    "Termologia": False,
                    "Unidades de medida e conversões": False,
                    "Termometria": False,
                    "Dilatometria": False,
                    "Calorimetria": False,
                    "Gases perfeitos": False,
                    "Máquinas térmicas e propagação de calor": False,
                    "Leis da termodinâmica": False
                },
                "Mecânica": {
                    "Mecânica": False,
                    "Movimento uniforme": False,
                    "Movimento uniformemente variado": False,
                    "Lançamento vertical e queda livre": False,
                    "Lançamento horizontal e lançamento oblíquo": False,
                    "Cinemática vetorial": False,
                    "Movimento circular uniforme": False,
                    "Vetores em dinâmica": False,
                    "Leis de Newton": False,
                    "Principais forças da dinâmica": False,
                    "Força de atrito": False,
                    "Força em trajetórias curvilíneas": False,
                    "Equilíbrio de ponto material e equilíbrio de corpos": False,
                    "extensos": False,
                    "Hidrostática": False,
                    "Hidrodinâmica": False,
                    "Trabalho e energia": False,
                    "Partículas em movimento": False,
                    "Gravitação universal": False,
                    "Movimento harmônico simples (MHS)": False
                },
                "Eletricidade": {
                    "Eletricidade": False,
                    "Carga total, processos de eletrização e lei de Coulomb": False,
                    "Campo elétrico, força elétrica e campo elétrico uniforme": False,
                    "Potencial elétrico e trabalho da força elétrica": False,
                    "Corrente elétrica e leis de Ohm": False,
                    "Geradores elétricos e resistores elétricos": False,
                    "Curto-circuito, potência elétrica e receptores elétricos": False,
                    "Medidores elétricos, ponte de Wheatstone e ponte de fio": False,
                    "Leis de Kirchhoff": False,
                    "Capacitadores": False,
                    "Magnetismo e Fontes de Campo Magnético": False,
                    "Força Magnética e Indução Eletromagnética": False,
                },
                "Ondulatória": {
                    "Ondulatória": False,
                    "Estrutura e classificações de onda": False,
                    "Reflexão refração de ondas": False,
                    "Equação de onda unidimensional, velocidade e": False,
                    "intensidade de onda": False,
                    "Difração e interferência de ondas": False,
                    "Experimento de Young e refração de ondas na praia": False,
                    "Acústica": False,
                    "Ondas estacionárias": False,
                    "Efeito Doppler, batimento, polarização e ressonância": False
                },
                "Óptica": {
                    "Óptica": False,
                    "Conceitos gerais em óptica geométrica": False,
                    "Reflexão e imagem em espelhos planos": False,
                    "Reflexão e imagem em espelhos esféricos": False,
                    "Refração da luz": False,
                    "Lentes esféricas": False,
                    "Óptica da visão e instrumentos ópticos": False
                }
            },
            "História": {
                "Idade Antiga": {
                    "Idade Antiga": False,
                    "Cronologia da História e Mesopotâmia": False,
                    "Egito e Fenícios": False,
                    "Persas e Hebreus": False,
                    "Grécia Antiga": False,
                    "Roma Antiga": False
                },
                "Idade Média": {
                    "Idade Média": False,
                    "Imperios Medievais": False,
                    "Alta Idade Média e Baixa Idade Média": False
                },
                "Idade Moderna": {
                    "Idade Moderna": False,
                    "Formação dos Estados Nacionais Modernos": False,
                    "Renascimento Artístico e Cultural": False,
                    "Reforma Protestante": False,
                    "Expansão Marítimo Comercial": False,
                    "Civilizações Pré-Colombianas": False,
                    "América Espanhola e Revoluções Inglesas do Século XVII": False,
                    "Revolução Industrial e Iluminismo": False,
                    "Colonização e Independência das 13 Colônias": False,
                    "Expansão Territorial dos EUA e EUA no Século XIX": False,
                    "Revolução Francesa": False
                }, 
                "Idade Contemporânea": {
                    "Idade Contemporânea": False,
                    "Era Napoleônica": False,
                    "Independência da América Espanhola": False,
                    "Imperialismo Norte-Americano": False,
                    "Unificação Italiana e Unificação Alemã": False,
                    "Segunda Revolução Industrial e Neocolonialismo": False,
                    "Revolução Mexicana": False,
                    "Populismo na América Latina e América Latina no": False,
                    "Século XX": False,
                    "Primeira Guerra Mundial": False,
                    "Revolução Russa e Regimes Totalitários": False,
                    "Segunda Guerra Mundial": False,
                    "Mundo Pós Segunda Guerra": False
                },
                "História do Brasil": {
                    "História do Brasil": False,
                    "Colonização do Brasil e Economia Açucareira": False,
                    "Expansão Territorial no Brasil Colônia": False,
                    "Revoltas Nativistas e Movimentos Emancipacionistas": False,
                    "Periodo Joanino": False,
                    "Primeiro Reinado no Brasil": False,
                    "Período Regencial no Brasil": False,
                    "Segundo Reinado no Brasil": False,
                    "República Velha no Brasil": False,
                    "Governo Vargas": False,
                    "Eurico Gaspar Dutra e Segundo Governo Vargas": False,
                    "Conflitos Sociais e Revoltas na República Velha": False,
                    "Café Filho e Juscelino Kubitschek": False,
                    "Jânio Quadros e João Goulart": False,
                    "Regime Militar": False,
                    "Brasil Contemporâneo": False
                },
            },
            "Geografia": {
                "População em Geografia": {
                    "População em Geografia": False,
                    "Conceitos em Geografia e Introdução à Demografia": False,
                    "Pirâmides Etárias, Transição Demográfica e": False,
                    "Teorias Demográficas": False
                },
                "Indústria e Economia": {
                    "Indústria e Economia": False,
                    "Primeira e Segunda Revoluções Industriais": False,
                    "Terceira e Quarta Revoluções Industriais": False,
                    "Modelos Econômicos": False,
                    "A Velha e a Nova Ordem Mundial": False,
                    "Blocos Econômicos": False
                },
                "Sociedade e Espaço": {
                    "Sociedade e Espaço": False,
                    "Transportes": False,
                    "Energia": False,
                    "Urbanização": False,
                    "Problemas Ambientais": False,
                    "Migrações": False,
                    "Uso da Terra e Sistemas Agrícolas": False,
                    "Fatores Naturais e Uso da Terra no Brasil": False,
                    "Estrutura Agrária e Pecuária no Brasil": False,
                    "Mapa do Brasil": False,
                    "Industrialização Brasileira": False
                },
                "Geografia Física": {
                    "Geografia Física": False,
                    "Cartografia": False,
                    "Geomorfologia": False,
                    "Solos": False,
                    "Mineração": False,
                    "Climatologia": False,
                    "Hidrografia": False,
                    "Biogeografia": False
                },
                "Geografia Mundo": {
                    "Geografia Mundo": False,
                    "Estados Unidos": False,
                    "América Latina": False,
                    "Oriente Médio": False,
                    "África": False,
                    "Ásia": False,
                    "Geopolítica Contemporânea": False
                }
            },
            "Filosofia": {
                "Filosofia Antiga": {
                    "Filosofia Antiga": False,
                    "Mito e Filosofia": False,
                    "Pré-Socráticos e Sofistas": False,
                    "Sócrates": False,
                    "Platão": False,
                    "Aristóteles": False,
                    "Período Helenista": False
                },
                "Filosofia Medieval": {
                    "Filosofia Medieval": False,
                    "Filosofia Medieval": False,
                    "Moral e Ética": False
                },
                "Epistemologia": {
                    "Epistemologia": False,
                    "René Descartes e Racionalismo": False,
                    "John Locke e Empirismo": False,
                    "Francis Bacon e David Hume": False,
                    "Kant": False
                },
                "Filosofia Política": {
                    "Filosofia Política": False,
                    "Maquiavel, Adam Smith e Montesquieu": False,
                    "Contratualistas": False
                },
                "Filosofia Moderna": {
                    "Filosofia Moderna": False,
                    "Hegel e a Dialética": False,
                    "Utilitarismo e Estética": False,
                    "Espinoza e Pascal": False,
                    "Sartre e Existencialismo": False,
                    "Fenomenologia e Heidegger": False,
                    "Nietzsche": False,
                    "Schopenhauer e Kierkegaard": False,
                    "Michel Foucault": False,
                    "Hannah Arendt": False,
                    "Freud": False,
                    "Russel e Wittgenstein": False,
                    "Escola de Frankfurt": False,
                    "John Rawls": False,
                    "Jürgen Habermas": False,
                },
                "Sociologia": {
                    "Autores Clássicos": {
                        "Surgimento da Sociologia e Socialização": False,
                        "Positivismo e Auguste Comte": False,
                        "Karl Marx": False,
                        "Émile Durkheim": False,
                        "Max Weber": False,
                    },
                    "Cultura e Sociedade": {
                        "Cultura e Sociedade": False,
                        "Antropologia": False,
                        "Norbert Elias": False,
                        "Pierre Bordieu": False,
                        "Adorno, Horkheimer e Walter Benjamin": False
                    },
                    "Política e Sociedade": {
                        "Política e Sociedade": False,
                        "Cidadania, Tipos de Direitos e Estratificação Social": False,
                        "Tipos de Democracia, Partidos Políticos": False,
                        "Tipos de Eleição": False
                    },
                    "Sociologia Brasileira": {
                        "Sociologia no Brasil": False,
                        "Paulo Freire e Teorias Educacionais": False
                    },
                    "Autores Complementares": {
                        "Zigmunt Bauman": False,
                        "Simone de Beavouir": False
                    }
                }
            },
            "Português": {
                "Morfologia": {
                    "Morfologia": False,
                    "Substantivo, Adjetivo, Numeral e Artigo": False,
                    "Pronomes": False,
                    "Verbos": False,
                    "Vozes Verbais, Advérbio, Preposição, Interjeição": False,
                    "Palavra Denotativa": False,
                    "Estrutura e Formação de Palavras": False
                },
                "Sintaxe": {
                    "Sintaxe": False,
                    "Conceitos, Orações e Sujeitos": False,
                    "Adjunto Adnominal, Complemento Nominal e Vocativo": False,
                    "Aposto e Agenda da Passiva": False,
                    "Predicado, Predicativo e Adjunto Adverbial": False,
                    "Orações Coordenadas e Orações Subordinadas": False,
                    "Concordância Nominal": False,
                    "Concordância Verbal": False,
                    "Regência Verbal": False,
                    "Regência Nominal": False,
                    "Crase": False,
                    "Pontuação": False,
                    "Acentuação": False,
                    "Ortografia": False
                },
                "Semântica": {
                    "Semântica": False,
                    "Funções da Linguagem": False,
                    "Figuras de Linguagem": False,
                    "Variação Linguística": False,
                    "Gêneros e Tipos Textuais": False,
                    "Vícios da Linguagem": False
                }
            },
        }

desempenho = {
            "Matemática": {
                "Matemática Básica": {
                    "Matemática Básica": {"Erros": 0, "Acertos": 0},
                    "Adição e Subtração": {"Erros": 0, "Acertos": 0},
                    "Multiplicação e Divisão": {"Erros": 0, "Acertos": 0},
                    "Frações": {"Erros": 0, "Acertos": 0},
                    "Potenciação": {"Erros": 0, "Acertos": 0},
                    "Radiciação": {"Erros": 0, "Acertos": 0},
                    "Racionalização de Denominadores": {"Erros": 0, "Acertos": 0},
                    "Produtos Notáveis": {"Erros": 0, "Acertos": 0},
                    "Potência de 10 e Notação Científica": {"Erros": 0, "Acertos": 0},
                    "Conjuntos Numéricos": {"Erros": 0, "Acertos": 0},
                    "Fatoração de Expressões Algébricas": {"Erros": 0, "Acertos": 0},
                    "Sistema de Numeração decimal": {"Erros": 0, "Acertos": 0},
                    "Equação do Primeiro Grau": {"Erros": 0, "Acertos": 0},
                    "Equação do Segundo Grau": {"Erros": 0, "Acertos": 0},
                    "Números Primos, Fatoração e Divisores": {"Erros": 0, "Acertos": 0},
                    "Múltiplos e MMC": {"Erros": 0, "Acertos": 0},
                    "Máximo Dividor Comum (MDC)": {"Erros": 0, "Acertos": 0},
                    "Razão e Proporção": {"Erros": 0, "Acertos": 0},
                    "Grandezas Diretamente Proporcionais": {"Erros": 0, "Acertos": 0},
                    "Grandezas Inversamente Proporcionais": {"Erros": 0, "Acertos": 0},
                    "Regra de 3 Simples e Composta": {"Erros": 0, "Acertos": 0},
                    "Porcentagem": {"Erros": 0, "Acertos": 0},
                    "Juros Simples": {"Erros": 0, "Acertos": 0},
                    "Juros Compostos": {"Erros": 0, "Acertos": 0},
                },
                "Conjuntos e Funções": {
                    "Funções": {"Erros": 0, "Acertos": 0},
                    "Conjuntos numéricos": {"Erros": 0, "Acertos": 0},
                    "Teoria dos Conjuntos": {"Erros": 0, "Acertos": 0},
                    "Função do 1º Grau": {"Erros": 0, "Acertos": 0},
                    "Função Inversa": {"Erros": 0, "Acertos": 0},
                    "Função Composta": {"Erros": 0, "Acertos": 0},
                    "Função do 2º Grau": {"Erros": 0, "Acertos": 0},
                    "Função Exponencial": {"Erros": 0, "Acertos": 0},
                    "Função Logarítmica": {"Erros": 0, "Acertos": 0},
                    "Função Modular": {"Erros": 0, "Acertos": 0}
                },
                "Geometria": {
                    "Geometria": {"Erros": 0, "Acertos": 0},
                    "Introdução à Geometria Plana": {"Erros": 0, "Acertos": 0},
                    "Retas Paralelas e Transversais": {"Erros": 0, "Acertos": 0},
                    "Teorema de Tales": {"Erros": 0, "Acertos": 0},
                    "Pontos Notáveis de Triângulos": {"Erros": 0, "Acertos": 0},
                    "Quadriláteros Notáveis": {"Erros": 0, "Acertos": 0},
                    "Polígonos": {"Erros": 0, "Acertos": 0},
                    "Circulo e Circunferência": {"Erros": 0, "Acertos": 0},
                    "Introdução à Geometria Analítica": {"Erros": 0, "Acertos": 0},
                    "Cônicas": {"Erros": 0, "Acertos": 0},
                    "Geometria Espacial": {"Erros": 0, "Acertos": 0},
                    "Poliedros": {"Erros": 0, "Acertos": 0},
                    "Prismas, Paralelepípedos e Cubos": {"Erros": 0, "Acertos": 0},
                    "Cilindro e Cones": {"Erros": 0, "Acertos": 0},
                    "Troncos de Cone, Pirâmides e Semelhança de Sólidos": {"Erros": 0, "Acertos": 0},
                    "Esferas": {"Erros": 0, "Acertos": 0},
                    "Projeção Ortogonal e Planificação de Sólidos": {"Erros": 0, "Acertos": 0}
                },
                "Trigonometria": {
                    "Trigonometria": {"Erros": 0, "Acertos": 0},
                    "Introdução à Trigonometria": {"Erros": 0, "Acertos": 0},
                    "Transformações Trigonométricas": {"Erros": 0, "Acertos": 0},
                    "Função Trigonométrica": {"Erros": 0, "Acertos": 0},
                    "Circulo Trigonométrico": {"Erros": 0, "Acertos": 0}
                },
                "Sequências": {
                    "Sequências": {"Erros": 0, "Acertos": 0},
                    "Introdução à Sequências": {"Erros": 0, "Acertos": 0},
                    "Progressão Aritmética": {"Erros": 0, "Acertos": 0},
                    "Progressão Geométrica": {"Erros": 0, "Acertos": 0},
                },
                "Estatística e Combinatória": {
                    "Estatística e Combinatória": {"Erros": 0, "Acertos": 0},
                    "Medidas de Centralidade e Dispersão": {"Erros": 0, "Acertos": 0},
                    "Principio Fundamental da Contagem": {"Erros": 0, "Acertos": 0},
                    "Permutação e Arranjo": {"Erros": 0, "Acertos": 0},
                    "Combinação": {"Erros": 0, "Acertos": 0},
                    "Probabilidade": {"Erros": 0, "Acertos": 0},
                    "Probabilidade Condicional": {"Erros": 0, "Acertos": 0}
                },
                "Sistemas Lineares": {
                    "Sistemas Lineares": {"Erros": 0, "Acertos": 0},
                    "Introdução à Sistemas Lineares": {"Erros": 0, "Acertos": 0},
                    "Escalonamento e Regra de Cramer": {"Erros": 0, "Acertos": 0},
                },
                "Outros": {
                    "Matrizes": {"Erros": 0, "Acertos": 0},
                    "Números Complexos": {"Erros": 0, "Acertos": 0},
                    "Polinômios": {"Erros": 0, "Acertos": 0}
                }
            },
            "Biologia": {
                "Bioquímica": {
                    "Bioquímica": {"Erros": 0, "Acertos": 0},
                    "Níveis de Organização": {"Erros": 0, "Acertos": 0},
                    "Sais Minerais": {"Erros": 0, "Acertos": 0},
                    "Carboidratos e Lipídios": {"Erros": 0, "Acertos": 0},
                    "Proteínas e Enzimas": {"Erros": 0, "Acertos": 0},
                    "Ácidos Nucleicos": {"Erros": 0, "Acertos": 0}
                },
                "Ecologia": {
                    "Ecologia": {"Erros": 0, "Acertos": 0},
                    "Introdução à Ecologia": {"Erros": 0, "Acertos": 0},
                    "Dinâmica Populacional, Cadeias alimentares e Pirâmide Ecológica": {"Erros": 0, "Acertos": 0},
                    "Relações Ecológicas": {"Erros": 0, "Acertos": 0},
                    "Sucessão Ecológica e Zonação": {"Erros": 0, "Acertos": 0},
                    "Ciclos Biogeoquímicos": {"Erros": 0, "Acertos": 0},
                    "Biociclos e Biomas": {"Erros": 0, "Acertos": 0},
                    "Desequilíbrios Ecológicos": {"Erros": 0, "Acertos": 0}
                },
                "Citologia": {
                    "Citologia": {"Erros": 0, "Acertos": 0},
                    "Tipos de Células e Membrana Plasmática": {"Erros": 0, "Acertos": 0},
                    "Transporte em Membrana": {"Erros": 0, "Acertos": 0},
                    "Citoplasma, Organelas e Estruturas celulares": {"Erros": 0, "Acertos": 0},
                    "Respiração Celular aeróbica e anaeróbica": {"Erros": 0, "Acertos": 0},
                    "Fermentação": {"Erros": 0, "Acertos": 0},
                    "Fotossíntese e Quimiossíntese": {"Erros": 0, "Acertos": 0},
                    "Síntese de Proteinas": {"Erros": 0, "Acertos": 0},
                    "Ciclo Celular e Mitose": {"Erros": 0, "Acertos": 0},
                    "Meiose e Gametogênese": {"Erros": 0, "Acertos": 0}
                },
                "Origem da Vida e Evolução": {
                    "Origem da Vida e Evolução": {"Erros": 0, "Acertos": 0},
                    "Origem da Vida": {"Erros": 0, "Acertos": 0},
                    "Características dos seres vivos": {"Erros": 0, "Acertos": 0},
                    "Evolução": {"Erros": 0, "Acertos": 0},
                    "Especiação": {"Erros": 0, "Acertos": 0}
                },
                "Histologia Humana": {
                    "Histologia Humana": {"Erros": 0, "Acertos": 0},
                    "Tecido Epitelial": {"Erros": 0, "Acertos": 0},
                    "Tecidos Conectivos e Adiposo": {"Erros": 0, "Acertos": 0},
                    "Tecidos Conectivos Cartilaginoso e Ósseo": {"Erros": 0, "Acertos": 0},
                    "Tecidos Conectivos Hematopoiético e Sanguíneo": {"Erros": 0, "Acertos": 0},
                    "Tecido Muscular": {"Erros": 0, "Acertos": 0},
                    "Tecido Nervoso": {"Erros": 0, "Acertos": 0}
                },
                "Genética": {
                    "Genética": {"Erros": 0, "Acertos": 0},
                    "Conceitos de Genética": {"Erros": 0, "Acertos": 0},
                    "Primeira lei de Mendel": {"Erros": 0, "Acertos": 0},
                    "Heredogramas e Cruzamento-Teste": {"Erros": 0, "Acertos": 0},
                    "Sistema ABO e Eritoblastose Fetal": {"Erros": 0, "Acertos": 0},
                    "Sistema Rh, Sistema MN e Efeito Bombaim": {"Erros": 0, "Acertos": 0},
                    "Genética do sexo e sistema de determinação de sexo": {"Erros": 0, "Acertos": 0},
                    "Segunda Lei de Mendel": {"Erros": 0, "Acertos": 0},
                    "Linkage": {"Erros": 0, "Acertos": 0},
                    "Expressividade e Interação Gênica": {"Erros": 0, "Acertos": 0},
                    "Pleiotropia e Genética de Populações": {"Erros": 0, "Acertos": 0},
                    "Mutações e Engenharia Genética": {"Erros": 0, "Acertos": 0}
                },
                "Fisiologia": {
                    "Fisiologia": {"Erros": 0, "Acertos": 0},
                    "Sistema Digestório": {"Erros": 0, "Acertos": 0},
                    "Sistema Respiratório": {"Erros": 0, "Acertos": 0},
                    "Sistema Circulatório Humano": {"Erros": 0, "Acertos": 0},
                    "Sistema Circulatório dos Vertebrados": {"Erros": 0, "Acertos": 0},
                    "Sistema Imunológico e Linfático": {"Erros": 0, "Acertos": 0},
                    "Sistema Excretor": {"Erros": 0, "Acertos": 0},
                    "Sistema Nervoso": {"Erros": 0, "Acertos": 0},
                    "Órgãos dos Sentidos": {"Erros": 0, "Acertos": 0},
                    "Sistema Endócrino": {"Erros": 0, "Acertos": 0},
                    "Sistema Reprodutor": {"Erros": 0, "Acertos": 0}
                },
                "Seres Vivos": {
                    "Seres Vivos": {"Erros": 0, "Acertos": 0},
                    "Classificação dos Seres Vivos": {"Erros": 0, "Acertos": 0},
                    "Taxonomia": {"Erros": 0, "Acertos": 0},
                    "Virus e Viroses": {"Erros": 0, "Acertos": 0},
                    "Reino Fungi": {"Erros": 0, "Acertos": 0},
                    "Reino Protista e Protozooses": {"Erros": 0, "Acertos": 0},
                    "Poríferos e cnidários": {"Erros": 0, "Acertos": 0},
                    "Platelmintos e nematelmintos": {"Erros": 0, "Acertos": 0},
                    "Verminoses": {"Erros": 0, "Acertos": 0},
                    "Protocordados e vertebrados": {"Erros": 0, "Acertos": 0},
                    "Métodos contraceptivos": {"Erros": 0, "Acertos": 0},
                    "Mamíferos": {"Erros": 0, "Acertos": 0},
                    "Fisiologia comparada e evolução dos seres vivos": {"Erros": 0, "Acertos": 0},
                    "Ciclos reprodutivos no Reino Plantae": {"Erros": 0, "Acertos": 0},
                    "Briófitas e pteridófitas": {"Erros": 0, "Acertos": 0},
                    "Gimnospermas e angiospermas": {"Erros": 0, "Acertos": 0},
                    "Evolução das plantas, tipos de polinização e": {"Erros": 0, "Acertos": 0},
                    "morfologia externa de plantas": {"Erros": 0, "Acertos": 0},
                    "Fitormônios": {"Erros": 0, "Acertos": 0},
                    "Histologia vegetal": {"Erros": 0, "Acertos": 0},
                    "Fitocromos e classificação complementar de plantas": {"Erros": 0, "Acertos": 0},
                    "Anel de Malpighi, transpiração e estômatos": {"Erros": 0, "Acertos": 0}
                },
                "Embriologia": {
                    "Embriologia": {"Erros": 0, "Acertos": 0},
                    "Embriogênese do anfioxo": {"Erros": 0, "Acertos": 0},
                    "Tipos de gêmeos e classificação dos animais": {"Erros": 0, "Acertos": 0},
                    "Destino dos folhetos embrionários e anexos embrionários": {"Erros": 0, "Acertos": 0},
                    "Tipos de ovos e segmentações": {"Erros": 0, "Acertos": 0},
                }
            },
            "Química": {
                "Físico-Química": {
                    "Físico-Química": {"Erros": 0, "Acertos": 0},
                    "Gráficos e Conceitos de Termoquimica": {"Erros": 0, "Acertos": 0},
                    "Cálculo de Varição de Entalpia": {"Erros": 0, "Acertos": 0},
                    "Entropia e Energia de Gibbs": {"Erros": 0, "Acertos": 0},
                    "Cinética Química": {"Erros": 0, "Acertos": 0},
                    "Kc e Kp em Equilíbrio Químico": {"Erros": 0, "Acertos": 0},
                    "Equilíbrio Iônico": {"Erros": 0, "Acertos": 0},
                    "Equilíbrio Iônico da Água e Hidrólise Salina": {"Erros": 0, "Acertos": 0},
                    "Solução Tampão e Kps": {"Erros": 0, "Acertos": 0},
                    "Pilhas e Bateria": {"Erros": 0, "Acertos": 0},
                    "Eletrólise": {"Erros": 0, "Acertos": 0}
                },
                "Química Orgânica": {
                    "Química Orgânica": {"Erros": 0, "Acertos": 0},
                    "Postulados de Kekulê": {"Erros": 0, "Acertos": 0},
                    "Classificação e Hibridização do Carbono": {"Erros": 0, "Acertos": 0},
                    "Classificação de Cadeias Carbônicas": {"Erros": 0, "Acertos": 0},
                    "Hidrocarbonetos e Nomenclatura de Compostos Orgânicos": {"Erros": 0, "Acertos": 0},
                    "Hidrocarbonetos Alifáticos e Cíclicos e Regra Geral de Nomenclatura": {"Erros": 0, "Acertos": 0}, 
                    "Aldeído, éster, sal orgânico e anidrido": {"Erros": 0, "Acertos": 0},
                    "Éter, nitrila, ácido sulfônico, tiocomposto, amina e amida": {"Erros": 0, "Acertos": 0},
                    "Haletos orgânicos": {"Erros": 0, "Acertos": 0},
                    "Isomeria plana": {"Erros": 0, "Acertos": 0},
                    "Isomeria geométrica": {"Erros": 0, "Acertos": 0},
                    "Isomeria óptica": {"Erros": 0, "Acertos": 0},
                    "Propriedades físicas dos compostos orgânicos": {"Erros": 0, "Acertos": 0},
                    "Acidez e basicidade de compostos orgânicos": {"Erros": 0, "Acertos": 0},
                    "Polímeros de adição": {"Erros": 0, "Acertos": 0},
                    "Polímeros de condensação": {"Erros": 0, "Acertos": 0},
                    "Reações orgânicas de substituição": {"Erros": 0, "Acertos": 0},
                    "Reações orgânicas de adição": {"Erros": 0, "Acertos": 0}
                },
                "Química Ambiental": {
                    "Química Ambiental": {"Erros": 0, "Acertos": 0},
                    "Bioquímica": {"Erros": 0, "Acertos": 0},
                    "Recursos Orgânicas": {"Erros": 0, "Acertos": 0}
                }
            },
            "Física": {
                "Termologia": {
                    "Termologia": {"Erros": 0, "Acertos": 0},
                    "Unidades de medida e conversões": {"Erros": 0, "Acertos": 0},
                    "Termometria": {"Erros": 0, "Acertos": 0},
                    "Dilatometria": {"Erros": 0, "Acertos": 0},
                    "Calorimetria": {"Erros": 0, "Acertos": 0},
                    "Gases perfeitos": {"Erros": 0, "Acertos": 0},
                    "Máquinas térmicas e propagação de calor": {"Erros": 0, "Acertos": 0},
                    "Leis da termodinâmica": {"Erros": 0, "Acertos": 0}
                },
                "Mecânica": {
                    "Mecânica": {"Erros": 0, "Acertos": 0},
                    "Movimento uniforme": {"Erros": 0, "Acertos": 0},
                    "Movimento uniformemente variado": {"Erros": 0, "Acertos": 0},
                    "Lançamento vertical e queda livre": {"Erros": 0, "Acertos": 0},
                    "Lançamento horizontal e lançamento oblíquo": {"Erros": 0, "Acertos": 0},
                    "Cinemática vetorial": {"Erros": 0, "Acertos": 0},
                    "Movimento circular uniforme": {"Erros": 0, "Acertos": 0},
                    "Vetores em dinâmica": {"Erros": 0, "Acertos": 0},
                    "Leis de Newton": {"Erros": 0, "Acertos": 0},
                    "Principais forças da dinâmica": {"Erros": 0, "Acertos": 0},
                    "Força de atrito": {"Erros": 0, "Acertos": 0},
                    "Força em trajetórias curvilíneas": {"Erros": 0, "Acertos": 0},
                    "Equilíbrio de ponto material e equilíbrio de corpos": {"Erros": 0, "Acertos": 0},
                    "extensos": {"Erros": 0, "Acertos": 0},
                    "Hidrostática": {"Erros": 0, "Acertos": 0},
                    "Hidrodinâmica": {"Erros": 0, "Acertos": 0},
                    "Trabalho e energia": {"Erros": 0, "Acertos": 0},
                    "Partículas em movimento": {"Erros": 0, "Acertos": 0},
                    "Gravitação universal": {"Erros": 0, "Acertos": 0},
                    "Movimento harmônico simples (MHS)": {"Erros": 0, "Acertos": 0}
                },
                "Eletricidade": {
                    "Eletricidade": {"Erros": 0, "Acertos": 0},
                    "Carga total, processos de eletrização e lei de Coulomb": {"Erros": 0, "Acertos": 0},
                    "Campo elétrico, força elétrica e campo elétrico uniforme": {"Erros": 0, "Acertos": 0},
                    "Potencial elétrico e trabalho da força elétrica": {"Erros": 0, "Acertos": 0},
                    "Corrente elétrica e leis de Ohm": {"Erros": 0, "Acertos": 0},
                    "Geradores elétricos e resistores elétricos": {"Erros": 0, "Acertos": 0},
                    "Curto-circuito, potência elétrica e receptores elétricos": {"Erros": 0, "Acertos": 0},
                    "Medidores elétricos, ponte de Wheatstone e ponte de fio": {"Erros": 0, "Acertos": 0},
                    "Leis de Kirchhoff": {"Erros": 0, "Acertos": 0},
                    "Capacitadores": {"Erros": 0, "Acertos": 0},
                    "Magnetismo e Fontes de Campo Magnético": {"Erros": 0, "Acertos": 0},
                    "Força Magnética e Indução Eletromagnética": {"Erros": 0, "Acertos": 0},
                },
                "Ondulatória": {
                    "Ondulatória": {"Erros": 0, "Acertos": 0},
                    "Estrutura e classificações de onda": {"Erros": 0, "Acertos": 0},
                    "Reflexão refração de ondas": {"Erros": 0, "Acertos": 0},
                    "Equação de onda unidimensional, velocidade e": {"Erros": 0, "Acertos": 0},
                    "intensidade de onda": {"Erros": 0, "Acertos": 0},
                    "Difração e interferência de ondas": {"Erros": 0, "Acertos": 0},
                    "Experimento de Young e refração de ondas na praia": {"Erros": 0, "Acertos": 0},
                    "Acústica": {"Erros": 0, "Acertos": 0},
                    "Ondas estacionárias": {"Erros": 0, "Acertos": 0},
                    "Efeito Doppler, batimento, polarização e ressonância": {"Erros": 0, "Acertos": 0}
                },
                "Óptica": {
                    "Óptica": {"Erros": 0, "Acertos": 0},
                    "Conceitos gerais em óptica geométrica": {"Erros": 0, "Acertos": 0},
                    "Reflexão e imagem em espelhos planos": {"Erros": 0, "Acertos": 0},
                    "Reflexão e imagem em espelhos esféricos": {"Erros": 0, "Acertos": 0},
                    "Refração da luz": {"Erros": 0, "Acertos": 0},
                    "Lentes esféricas": {"Erros": 0, "Acertos": 0},
                    "Óptica da visão e instrumentos ópticos": {"Erros": 0, "Acertos": 0}
                }
            },
            "História": {
                "Idade Antiga": {
                    "Idade Antiga": {"Erros": 0, "Acertos": 0},
                    "Cronologia da História e Mesopotâmia": {"Erros": 0, "Acertos": 0},
                    "Egito e Fenícios": {"Erros": 0, "Acertos": 0},
                    "Persas e Hebreus": {"Erros": 0, "Acertos": 0},
                    "Grécia Antiga": {"Erros": 0, "Acertos": 0},
                    "Roma Antiga": {"Erros": 0, "Acertos": 0}
                },
                "Idade Média": {
                    "Idade Média": {"Erros": 0, "Acertos": 0},
                    "Imperios Medievais": {"Erros": 0, "Acertos": 0},
                    "Alta Idade Média e Baixa Idade Média": {"Erros": 0, "Acertos": 0}
                },
                "Idade Moderna": {
                    "Idade Moderna": {"Erros": 0, "Acertos": 0},
                    "Formação dos Estados Nacionais Modernos": {"Erros": 0, "Acertos": 0},
                    "Renascimento Artístico e Cultural": {"Erros": 0, "Acertos": 0},
                    "Reforma Protestante": {"Erros": 0, "Acertos": 0},
                    "Expansão Marítimo Comercial": {"Erros": 0, "Acertos": 0},
                    "Civilizações Pré-Colombianas": {"Erros": 0, "Acertos": 0},
                    "América Espanhola e Revoluções Inglesas do Século XVII": {"Erros": 0, "Acertos": 0},
                    "Revolução Industrial e Iluminismo": {"Erros": 0, "Acertos": 0},
                    "Colonização e Independência das 13 Colônias": {"Erros": 0, "Acertos": 0},
                    "Expansão Territorial dos EUA e EUA no Século XIX": {"Erros": 0, "Acertos": 0},
                    "Revolução Francesa": {"Erros": 0, "Acertos": 0}
                }, 
                "Idade Contemporânea": {
                    "Idade Contemporânea": {"Erros": 0, "Acertos": 0},
                    "Era Napoleônica": {"Erros": 0, "Acertos": 0},
                    "Independência da América Espanhola": {"Erros": 0, "Acertos": 0},
                    "Imperialismo Norte-Americano": {"Erros": 0, "Acertos": 0},
                    "Unificação Italiana e Unificação Alemã": {"Erros": 0, "Acertos": 0},
                    "Segunda Revolução Industrial e Neocolonialismo": {"Erros": 0, "Acertos": 0},
                    "Revolução Mexicana": {"Erros": 0, "Acertos": 0},
                    "Populismo na América Latina e América Latina no": {"Erros": 0, "Acertos": 0},
                    "Século XX": {"Erros": 0, "Acertos": 0},
                    "Primeira Guerra Mundial": {"Erros": 0, "Acertos": 0},
                    "Revolução Russa e Regimes Totalitários": {"Erros": 0, "Acertos": 0},
                    "Segunda Guerra Mundial": {"Erros": 0, "Acertos": 0},
                    "Mundo Pós Segunda Guerra": {"Erros": 0, "Acertos": 0}
                },
                "História do Brasil": {
                    "História do Brasil": {"Erros": 0, "Acertos": 0},
                    "Colonização do Brasil e Economia Açucareira": {"Erros": 0, "Acertos": 0},
                    "Expansão Territorial no Brasil Colônia": {"Erros": 0, "Acertos": 0},
                    "Revoltas Nativistas e Movimentos Emancipacionistas": {"Erros": 0, "Acertos": 0},
                    "Periodo Joanino": {"Erros": 0, "Acertos": 0},
                    "Primeiro Reinado no Brasil": {"Erros": 0, "Acertos": 0},
                    "Período Regencial no Brasil": {"Erros": 0, "Acertos": 0},
                    "Segundo Reinado no Brasil": {"Erros": 0, "Acertos": 0},
                    "República Velha no Brasil": {"Erros": 0, "Acertos": 0},
                    "Governo Vargas": {"Erros": 0, "Acertos": 0},
                    "Eurico Gaspar Dutra e Segundo Governo Vargas": {"Erros": 0, "Acertos": 0},
                    "Conflitos Sociais e Revoltas na República Velha": {"Erros": 0, "Acertos": 0},
                    "Café Filho e Juscelino Kubitschek": {"Erros": 0, "Acertos": 0},
                    "Jânio Quadros e João Goulart": {"Erros": 0, "Acertos": 0},
                    "Regime Militar": {"Erros": 0, "Acertos": 0},
                    "Brasil Contemporâneo": {"Erros": 0, "Acertos": 0}
                },
            },
            "Geografia": {
                "População em Geografia": {
                    "População em Geografia": {"Erros": 0, "Acertos": 0},
                    "Conceitos em Geografia e Introdução à Demografia": {"Erros": 0, "Acertos": 0},
                    "Pirâmides Etárias, Transição Demográfica e": {"Erros": 0, "Acertos": 0},
                    "Teorias Demográficas": {"Erros": 0, "Acertos": 0}
                },
                "Indústria e Economia": {
                    "Indústria e Economia": {"Erros": 0, "Acertos": 0},
                    "Primeira e Segunda Revoluções Industriais": {"Erros": 0, "Acertos": 0},
                    "Terceira e Quarta Revoluções Industriais": {"Erros": 0, "Acertos": 0},
                    "Modelos Econômicos": {"Erros": 0, "Acertos": 0},
                    "A Velha e a Nova Ordem Mundial": {"Erros": 0, "Acertos": 0},
                    "Blocos Econômicos": {"Erros": 0, "Acertos": 0}
                },
                "Sociedade e Espaço": {
                    "Sociedade e Espaço": {"Erros": 0, "Acertos": 0},
                    "Transportes": {"Erros": 0, "Acertos": 0},
                    "Energia": {"Erros": 0, "Acertos": 0},
                    "Urbanização": {"Erros": 0, "Acertos": 0},
                    "Problemas Ambientais": {"Erros": 0, "Acertos": 0},
                    "Migrações": {"Erros": 0, "Acertos": 0},
                    "Uso da Terra e Sistemas Agrícolas": {"Erros": 0, "Acertos": 0},
                    "Fatores Naturais e Uso da Terra no Brasil": {"Erros": 0, "Acertos": 0},
                    "Estrutura Agrária e Pecuária no Brasil": {"Erros": 0, "Acertos": 0},
                    "Mapa do Brasil": {"Erros": 0, "Acertos": 0},
                    "Industrialização Brasileira": {"Erros": 0, "Acertos": 0}
                },
                "Geografia Física": {
                    "Geografia Física": {"Erros": 0, "Acertos": 0},
                    "Cartografia": {"Erros": 0, "Acertos": 0},
                    "Geomorfologia": {"Erros": 0, "Acertos": 0},
                    "Solos": {"Erros": 0, "Acertos": 0},
                    "Mineração": {"Erros": 0, "Acertos": 0},
                    "Climatologia": {"Erros": 0, "Acertos": 0},
                    "Hidrografia": {"Erros": 0, "Acertos": 0},
                    "Biogeografia": {"Erros": 0, "Acertos": 0}
                },
                "Geografia Mundo": {
                    "Geografia Mundo": {"Erros": 0, "Acertos": 0},
                    "Estados Unidos": {"Erros": 0, "Acertos": 0},
                    "América Latina": {"Erros": 0, "Acertos": 0},
                    "Oriente Médio": {"Erros": 0, "Acertos": 0},
                    "África": {"Erros": 0, "Acertos": 0},
                    "Ásia": {"Erros": 0, "Acertos": 0},
                    "Geopolítica Contemporânea": {"Erros": 0, "Acertos": 0}
                }
            },
            "Filosofia": {
                "Filosofia Antiga": {
                    "Filosofia Antiga": {"Erros": 0, "Acertos": 0},
                    "Mito e Filosofia": {"Erros": 0, "Acertos": 0},
                    "Pré-Socráticos e Sofistas": {"Erros": 0, "Acertos": 0},
                    "Sócrates": {"Erros": 0, "Acertos": 0},
                    "Platão": {"Erros": 0, "Acertos": 0},
                    "Aristóteles": {"Erros": 0, "Acertos": 0},
                    "Período Helenista": {"Erros": 0, "Acertos": 0}
                },
                "Filosofia Medieval": {
                    "Filosofia Medieval": {"Erros": 0, "Acertos": 0},
                    "Filosofia Medieval": {"Erros": 0, "Acertos": 0},
                    "Moral e Ética": {"Erros": 0, "Acertos": 0}
                },
                "Epistemologia": {
                    "Epistemologia": {"Erros": 0, "Acertos": 0},
                    "René Descartes e Racionalismo": {"Erros": 0, "Acertos": 0},
                    "John Locke e Empirismo": {"Erros": 0, "Acertos": 0},
                    "Francis Bacon e David Hume": {"Erros": 0, "Acertos": 0},
                    "Kant": {"Erros": 0, "Acertos": 0}
                },
                "Filosofia Política": {
                    "Filosofia Política": {"Erros": 0, "Acertos": 0},
                    "Maquiavel, Adam Smith e Montesquieu": {"Erros": 0, "Acertos": 0},
                    "Contratualistas": {"Erros": 0, "Acertos": 0}
                },
                "Filosofia Moderna": {
                    "Filosofia Moderna": {"Erros": 0, "Acertos": 0},
                    "Hegel e a Dialética": {"Erros": 0, "Acertos": 0},
                    "Utilitarismo e Estética": {"Erros": 0, "Acertos": 0},
                    "Espinoza e Pascal": {"Erros": 0, "Acertos": 0},
                    "Sartre e Existencialismo": {"Erros": 0, "Acertos": 0},
                    "Fenomenologia e Heidegger": {"Erros": 0, "Acertos": 0},
                    "Nietzsche": {"Erros": 0, "Acertos": 0},
                    "Schopenhauer e Kierkegaard": {"Erros": 0, "Acertos": 0},
                    "Michel Foucault": {"Erros": 0, "Acertos": 0},
                    "Hannah Arendt": {"Erros": 0, "Acertos": 0},
                    "Freud": {"Erros": 0, "Acertos": 0},
                    "Russel e Wittgenstein": {"Erros": 0, "Acertos": 0},
                    "Escola de Frankfurt": {"Erros": 0, "Acertos": 0},
                    "John Rawls": {"Erros": 0, "Acertos": 0},
                    "Jürgen Habermas": {"Erros": 0, "Acertos": 0},
                },
                "Sociologia": {
                    "Autores Clássicos": {
                        "Surgimento da Sociologia e Socialização": {"Erros": 0, "Acertos": 0},
                        "Positivismo e Auguste Comte": {"Erros": 0, "Acertos": 0},
                        "Karl Marx": {"Erros": 0, "Acertos": 0},
                        "Émile Durkheim": {"Erros": 0, "Acertos": 0},
                        "Max Weber": {"Erros": 0, "Acertos": 0},
                    },
                    "Cultura e Sociedade": {
                        "Cultura e Sociedade": {"Erros": 0, "Acertos": 0},
                        "Antropologia": {"Erros": 0, "Acertos": 0},
                        "Norbert Elias": {"Erros": 0, "Acertos": 0},
                        "Pierre Bordieu": {"Erros": 0, "Acertos": 0},
                        "Adorno, Horkheimer e Walter Benjamin": {"Erros": 0, "Acertos": 0}
                    },
                    "Política e Sociedade": {
                        "Política e Sociedade": {"Erros": 0, "Acertos": 0},
                        "Cidadania, Tipos de Direitos e Estratificação Social": {"Erros": 0, "Acertos": 0},
                        "Tipos de Democracia, Partidos Políticos": {"Erros": 0, "Acertos": 0},
                        "Tipos de Eleição": {"Erros": 0, "Acertos": 0}
                    },
                    "Sociologia Brasileira": {
                        "Sociologia no Brasil": {"Erros": 0, "Acertos": 0},
                        "Paulo Freire e Teorias Educacionais": {"Erros": 0, "Acertos": 0}
                    },
                    "Autores Complementares": {
                        "Zigmunt Bauman": {"Erros": 0, "Acertos": 0},
                        "Simone de Beavouir": {"Erros": 0, "Acertos": 0}
                    }
                }
            },
            "Português": {
                "Morfologia": {
                    "Morfologia": {"Erros": 0, "Acertos": 0},
                    "Substantivo, Adjetivo, Numeral e Artigo": {"Erros": 0, "Acertos": 0},
                    "Pronomes": {"Erros": 0, "Acertos": 0},
                    "Verbos": {"Erros": 0, "Acertos": 0},
                    "Vozes Verbais, Advérbio, Preposição, Interjeição": {"Erros": 0, "Acertos": 0},
                    "Palavra Denotativa": {"Erros": 0, "Acertos": 0},
                    "Estrutura e Formação de Palavras": {"Erros": 0, "Acertos": 0}
                },
                "Sintaxe": {
                    "Sintaxe": {"Erros": 0, "Acertos": 0},
                    "Conceitos, Orações e Sujeitos": {"Erros": 0, "Acertos": 0},
                    "Adjunto Adnominal, Complemento Nominal e Vocativo": {"Erros": 0, "Acertos": 0},
                    "Aposto e Agenda da Passiva": {"Erros": 0, "Acertos": 0},
                    "Predicado, Predicativo e Adjunto Adverbial": {"Erros": 0, "Acertos": 0},
                    "Orações Coordenadas e Orações Subordinadas": {"Erros": 0, "Acertos": 0},
                    "Concordância Nominal": {"Erros": 0, "Acertos": 0},
                    "Concordância Verbal": {"Erros": 0, "Acertos": 0},
                    "Regência Verbal": {"Erros": 0, "Acertos": 0},
                    "Regência Nominal": {"Erros": 0, "Acertos": 0},
                    "Crase": {"Erros": 0, "Acertos": 0},
                    "Pontuação": {"Erros": 0, "Acertos": 0},
                    "Acentuação": {"Erros": 0, "Acertos": 0},
                    "Ortografia": {"Erros": 0, "Acertos": 0}
                },
                "Semântica": {
                    "Semântica": {"Erros": 0, "Acertos": 0},
                    "Funções da Linguagem": {"Erros": 0, "Acertos": 0},
                    "Figuras de Linguagem": {"Erros": 0, "Acertos": 0},
                    "Variação Linguística": {"Erros": 0, "Acertos": 0},
                    "Gêneros e Tipos Textuais": {"Erros": 0, "Acertos": 0},
                    "Vícios da Linguagem": {"Erros": 0, "Acertos": 0}
                }
            }
        }

simulados = {
    "Colmeias_Inicial": {
        "1": {"Resposta": "D", "Disciplina": "Português", "Conteudo": ["Funções da Linguagem", "Morfologia"]},
        "2": {"Resposta": "A", "Disciplina": "Português", "Conteudo": ["Morfologia", "Concordância Verbal"]},
        "3": {"Resposta": "A", "Disciplina": "Português", "Conteudo": ["Funções da Linguagem", "Variação Linguística"]},
        "4": {"Resposta": "C", "Disciplina": "Português", "Conteudo": ["Figuras de Linguagem", "Morfologia", "Verbos"]},
        "5": {"Resposta": "E", "Disciplina": "Português", "Conteudo": ["Morfologia", "Substantivo, Adjetivo, Numeral e Artigo"]},
        "6": {"Resposta": "D", "Disciplina": "Física", "Conteudo": ["Movimento uniforme", "Matemática Básica", "Porcentagem"]},
        "7": {"Resposta": "B", "Disciplina": "Física", "Conteudo": ["Ondulatória", "Movimento Uniforme"]},
        "8": {"Resposta": "E", "Disciplina": "Física", "Conteudo": ["Eletricidade", "Gráficos"]},
        "9": {"Resposta": "E", "Disciplina": "Matemática", "Conteudo": ["Geometria Espacial", "Volume"]},
        "10": {"Resposta": "A", "Disciplina": "Matemática", "Conteudo": ["Medidas de Centralidade e Dispersão", "Tabela"]},
        "11": {"Resposta": "B", "Disciplina": "Matemática", "Conteudo": ["Matemática Básica", "Adição e Subtração", "Potenciação", "Radiciação"]},
        "12": {"Resposta": "B", "Disciplina": "Matemática", "Conteudo": ["Porcentagem", "Matemática Financeira"]},
        "13": {"Resposta": "C", "Disciplina": "Matemática", "Conteudo": ["Função do 1º Grau", "Gráficos", "Tabela"]},
        "14": {"Resposta": "B", "Disciplina": "Geografia", "Conteudo": ["Conceitos em Geografia e Introdução à Demografia", "Migrações"]},
        "15": {"Resposta": "E", "Disciplina": "Geografia", "Conteudo": ["Industrialização Brasileira"]},
        "16": {"Resposta": "C", "Disciplina": "Geografia", "Conteudo": ["Energia"]},
        "17": {"Resposta": "C", "Disciplina": "História", "Conteudo": ["Governo Vargas"]},
        "18": {"Resposta": "B", "Disciplina": "História", "Conteudo": ["Idade Moderna"]},
        "19": {"Resposta": "B", "Disciplina": "História", "Conteudo": ["Segunda Guerra Mundial", "Autoritarismo"]},
        "20": {"Resposta": "A", "Disciplina": "Química", "Conteudo": ["Química Orgânica"]},
        "21": {"Resposta": "A", "Disciplina": "Química", "Conteudo": ["Química Orgânica", "Classificação e Hibridização do Carbono", "Classificação de Cadeias Carbônicas"]},
        "22": {"Resposta": "D", "Disciplina": "Química", "Conteudo": ["Equilíbrio Iônico"]},
        "23": {"Resposta": "D", "Disciplina": "Biologia", "Conteudo": ["Biociclos e Biomas", "Ecologia"]},
        "24": {"Resposta": "C", "Disciplina": "Biologia", "Conteudo": ["Saúde"]},
        "25": {"Resposta": "D", "Disciplina": "Biologia", "Conteudo": ["Citologia"]}
    }
}

# Iniciando
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://herbert2024-be557-default-rtdb.firebaseio.com/',
    'storageBucket': 'gs://herbert2024-be557.appspot.com'
}) 

ref = db.reference("/students")
students = ref.get()

def findStudent(key, students):
    student = students[key]

    return student

def converter_respostas(resposta_aluno):
    respostas_dict = {}
    for i, resposta in enumerate(resposta_aluno, start=1):
        respostas_dict[str(i)] = resposta

    return respostas_dict


def insertSimulado(student_id, estudante, nome_simulado, gabarito_student_str, gabarito_oficial, ref=ref):  

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

if students:
    for student_id, student_data in students.items():
        # Atualiza os atributos 'desempenho' e 'disciplinas' para cada aluno
        #student_data['desempenho'] = desempenho
        #student_data['disciplinas'] = disciplinas
        # student_data['nome'] = student_data["nome"].title()
        #ref.child(student_id).update(student_data)
        # estudante = findStudent(student_id, students)
        try:
            gabarito_estudante = student_data["Simulados"]["Colmeia_Inicial"]
            insertSimulado(student_id, student_data, "Colmeia_Inicial", gabarito_estudante, simulados["Colmeias_Inicial"])
        except:
            continue
        print(f"{student_data['nome']} - Check")

    print("Todos os alunos foram atualizados com sucesso!")
else:
    print("Não há alunos no banco de dados.")