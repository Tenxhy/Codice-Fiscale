import datetime
from datetime import datetime
import pandas as pd
from CalcoloCodice import CalcoloCodice

comuni = pd.read_excel(r".\data\Elenco-comuni-italiani.xlsx", header=None)
comuniDict = comuni.to_dict()
checkdigit = pd.read_excel(r".\data\CheckDigitDatabase.xlsx", header=None)
checkDict = checkdigit.to_dict()

print("""
#################################################################
#\t\t    CALCOLO CODICE FISCALE     \t\t\t#
#################################################################""".strip())
print("#")

#Richiesta del cognome e verifica della sua validità

check = 0
cognome = ""
while check == 0:
  cognome = input("# Inserisca un cognome valido  ").strip().upper()
  check = 1
  for i in cognome:
    if not (ord(i) >= 65 and ord(i) <= 90 or ord(i) == 32):
      check = 0

#Richiesta del nome e verifica della sua validità

check = 0
nome = ""
while check == 0:
  nome = input("# Inserisca un nome valido  ").strip().upper()
  check = 1
  for i in nome:
    if not ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) == 32)):
      check = 0

#Richiesta della data di nascita e verifica della sua validità

check = 0
data = ""
while check == 0:
  data = input("# Inserisca una data valida con format GG/MM/AAAA  ")
  check = 1
  if len(data) == 10:
    for i in data:
      if not (ord(i) >= 47 and ord(i) <= 57):
        check = 0

    if data[2] != "/" or data[5] != "/":
      check = 0
    else:
      anno_attuale = datetime.now().year
      mese_attuale = datetime.now().month
      giorno_attuale = datetime.now().day
      anno = int(data[-4:])
      mese = int(data[3:5])
      giorno = int(data[:2])

      if anno <= 1900 or (mese > mese_attuale and anno > anno_attuale and giorno > giorno_attuale):
        check = 0
      elif mese < 1 or mese > 12:
        check = 0
      elif (mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12):
        if giorno < 1 or giorno > 31:
          check = 0
      elif (mese == 4 or mese == 6 or mese == 9 or mese == 11):
        if giorno < 1 or giorno > 30:
          check = 0
      elif (mese == 2):
        if giorno < 1 or giorno >28:
          check = 0
        if anno%4==0 and (anno%100!=0 or anno%400==0):
          if mese == 2 and (giorno >= 1 or giorno <= 29):
            check = 1
  else:
    check = 0

anno = str(data[-4:])
mese = int(data[3:5])
giorno = str(data[:2])

#Richiesta del luogo di nascita e verifica della sua validità

check = 0
luogo = ""
while check == 0:
  luogo = input("# Inserisca il luogo di nascita  ")
  check = 1
  trovato = luogo in comuni[0].values
  if not trovato:
    check = 0

#Richiesta del sesso e verifica della sua validità

check = 0
sesso = ""
while check == 0:
  sesso = input("# Inserisca il sesso, M o F  ").strip().upper()
  check = 1
  if sesso != "M" and sesso != "F":
    check = 0


#Calcolo del codice fiscale

calcolo = CalcoloCodice(comuniDict, checkDict)

codice = calcolo.calcola(nome, cognome, sesso, giorno, mese, anno, luogo)

print("#")
print(f"# Il suo codice fiscale è {codice}")
print("#")
