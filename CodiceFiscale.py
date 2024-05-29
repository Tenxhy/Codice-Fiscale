import colorama
from datetime import datetime
import pandas as pd
from CalcoloCodice import CalcoloCodice
from ControlliInput import ControlliInput

comuni = pd.read_excel(r".\data\Elenco-comuni-italiani.xlsx", header=None)
comuniDict = comuni.to_dict()
checkdigit = pd.read_excel(r".\data\CheckDigitDatabase.xlsx", header=None)
checkDict = checkdigit.to_dict()

def main() -> None:

  print(f"""
  #################################################################
#\t\t    {str(colorama.Fore.CYAN)}CALCOLO CODICE FISCALE{str(colorama.Style.RESET_ALL)}     \t\t\t#
#################################################################""".strip())
  print("#")

  # Richiesta del cognome e verifica della sua validità
  cognome = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire un cognome valido:  " + colorama.Style.RESET_ALL).strip().upper()
  while not ControlliInput.check_parola(cognome):
    print("# " + colorama.Fore.RED + "Il cognome può contenere solo lettere" + colorama.Style.RESET_ALL)
    cognome = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire un cognome valido:  " + colorama.Style.RESET_ALL).strip().upper()

  # Richiesta del nome e verifica della sua validità
  nome = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire un nome valido:  " + colorama.Style.RESET_ALL).strip().upper()
  while not ControlliInput.check_parola(nome):
    print("# " + colorama.Fore.RED + "Il nome può contenere solo lettere" + colorama.Style.RESET_ALL)
    nome = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire un nome valido:  " + colorama.Style.RESET_ALL).strip().upper()

  # Richiesta della data di nascita e verifica della sua validità
  data = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire una data valida con format GG/MM/AAAA:  " + colorama.Style.RESET_ALL)
  while not ControlliInput.check_data(data):
    data_minima = datetime.now().year - 130
    print("# " + colorama.Fore.RED + f"La data deve corrispondere al formato GG/MM/AAAA e deve essere compresa tra il {data_minima} e oggi" + colorama.Style.RESET_ALL)
    data = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire una data valida con format GG/MM/AAAA:  " + colorama.Style.RESET_ALL)

  anno = str(data[-4:])
  mese = int(data[3:5])
  giorno = str(data[:2])

  # Richiesta del luogo di nascita e verifica della sua validità
  luogo = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire il luogo di nascita:  " + colorama.Style.RESET_ALL)
  while not ControlliInput.check_luogo(luogo, comuni):
    print("# " + colorama.Fore.RED + "Il luogo di nascita non è valido" + colorama.Style.RESET_ALL)
    luogo = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire il luogo di nascita:  " + colorama.Style.RESET_ALL)

  # Richiesta del sesso e verifica della sua validità
  sesso = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire il sesso, M o F:  " + colorama.Style.RESET_ALL).strip().upper()
  while not ControlliInput.check_sesso(sesso):
    print("# " + colorama.Fore.RED + "Il sesso può essere solo M o F" + colorama.Style.RESET_ALL)
    sesso = input("# " + colorama.Fore.LIGHTBLUE_EX + "Inserire il sesso, M o F:  " + colorama.Style.RESET_ALL).strip().upper()

  # Calcolo del codice fiscale
  calcolo = CalcoloCodice(comuniDict, checkDict)
  codice = calcolo.calcola(nome, cognome, sesso, giorno, mese, anno, luogo)

  print("#")
  print("# " + colorama.Fore.GREEN + "Il suo codice fiscale è " + colorama.Fore.YELLOW + f"{codice}" + colorama.Style.RESET_ALL)
  print("#")
  print("#################################################################")
  input("Premere INVIO per uscire...")

if __name__ == "__main__":
  main()
