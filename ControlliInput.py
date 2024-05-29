from pandas import Series, DataFrame
from datetime import datetime

class ControlliInput:

    @staticmethod
    def check_parola(nome: str) -> bool:
        check = True
        for l in nome:
            if not ((ord(l) >= 65 and ord(l) <= 90) or (ord(l) == 32)):
                check = False
        return check

    @staticmethod
    def check_luogo(luogo: str, comuni: DataFrame) -> bool:
        check = True
        trovato = luogo in comuni[0].values
        if not trovato:
            check = False
        return check
    
    @staticmethod
    def check_sesso(sesso: str) -> bool:
        check = True
        if sesso != "M" and sesso != "F":
            check = False
        return check

    @staticmethod
    def check_data(data: str) -> bool:
        check = True
        if len(data) == 10:
            for i in data:
                if not (ord(i) >= 47 and ord(i) <= 57):
                    check = False

                if data[2] != "/" or data[5] != "/":
                    check = False
                else:
                    anno_attuale = datetime.now().year
                    mese_attuale = datetime.now().month
                    giorno_attuale = datetime.now().day
                    anno = int(data[-4:])
                    mese = int(data[3:5])
                    giorno = int(data[:2])

                    if ((anno <= anno_attuale - 130) or 
                        (anno > anno_attuale) or 
                        (anno == anno_attuale and mese > mese_attuale) or 
                        (anno == anno_attuale and mese == mese_attuale and giorno > giorno_attuale)):
                            check = False
                    elif mese < 1 or mese > 12:
                        check = False
                    elif (mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12):
                        if giorno < 1 or giorno > 31:
                            check = False
                    elif (mese == 4 or mese == 6 or mese == 9 or mese == 11):
                        if giorno < 1 or giorno > 30:
                            check = False
                    elif (mese == 2):
                        if giorno < 1 or giorno >28:
                            check = False
                        if anno%4==0 and (anno%100!=0 or anno%400==0):
                            if mese == 2 and (giorno >= 1 or giorno <= 29):
                                check = True
        else:
            check = False

        return check