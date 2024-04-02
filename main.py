import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
from Betinho import Betinho

betinho = Betinho()
#betinho.adicionarSimulado("Colmeias_Inicial")
#betinho.deleteSimulado("Colmeia_Inicial")

betinho.analisarSimulado("Colmeias_Inicial")