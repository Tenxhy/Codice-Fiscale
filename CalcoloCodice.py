class CalcoloCodice:
    '''Classe per il calcolo del codice fiscale di una persona a partire dai suoi dati anagrafici'''
    def __init__(self, comuniDict: dict, checkDict: dict):
        '''Inizializza la classe CalcoloCodice

        Parametri
        ---
        comuniDict : dict
            Dizionario contenente i comuni italiani
        checkDict : dict
            Dizionario contenente i valori per il calcolo del check digit
        '''

        self.comuniDict = comuniDict
        self.checkDict = checkDict

    def __calcolo_nome(self, nome: str) -> str:
        compnom = ""
        check = 0
        for  i in nome:
            if not(i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
                compnom = compnom+i

        if len(compnom)<4:
            for  i in nome:
                if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                    compnom = compnom+i

            check = 1
            compnom = compnom+"XXX"

        if check == 0:
            comp2 = compnom[:1]+compnom[2:4]
        else:
            comp2 = compnom[:3]

        return comp2
    
    def __calcolo_cognome(self, cognome: str) -> str:
        compcogn = ""
        for  i in cognome:
            if not(i == "A" or i == "E" or i == "I" or i == "O" or i == "U"):
                compcogn = compcogn+i

        for  i in cognome:
            if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
                compcogn = compcogn+i

        compcogn = compcogn+"XXX"
        comp1 = compcogn[:3]

        return comp1
    
    def __calcolo_data(self, giorno: str, mese: int, anno: str, sesso: str) -> str:
        if sesso == "M":
            compgiorno = giorno
        else:
            compgiorno = str(int(giorno)+40)

        compmese = ""

        if mese == 1:
            compmese = "A"
        elif mese == 2:
            compmese = "B"
        elif mese == 3:
            compmese = "C"
        elif mese == 4:
            compmese = "D"
        elif mese == 5:
            compmese = "E"
        elif mese == 6:
            compmese = "H"
        elif mese == 7:
            compmese = "L"
        elif mese == 8:
            compmese = "M"
        elif mese == 9:
            compmese = "P"
        elif mese == 10:
            compmese = "R"
        elif mese == 11:
            compmese = "S"
        elif mese == 12:
            compmese = "T"

        companno = str(anno[2:])

        comp3 = companno+compmese+compgiorno

        return comp3
    
    def __calcolo_luogo(self, luogo: str) -> str:
        comuniDict = self.comuniDict
        compluogoNum = [value for value, nomeLuogo in comuniDict[0].items() if nomeLuogo == luogo][0]

        comp4 = comuniDict[1][compluogoNum]

        return comp4
    
    def __calcolo_valore_check(self, codice: str) -> str:
        checkDict = self.checkDict
        compcheckNum = int()
        compSomma = int()
        nomeChar = ""
        tot = 0

        for c in codice:
            tot = tot+1
            nomeChar = c
            if tot%2 != 0:
                compcheckNum = int([value for value, nomeChar in checkDict[2].items() if nomeChar == c][0])
                compSomma = compSomma+checkDict[3][compcheckNum]
            else:
                compcheckNum = int([value for value, nomeChar in checkDict[0].items() if nomeChar == c][0])
                compSomma = compSomma+checkDict[1][compcheckNum]

        compSomma = compSomma%26
        comp5 = checkDict[5][compSomma]

        return comp5

    def calcola(self, nome: str, cognome: str, sesso: str, giorno: str, mese: int, anno: str, luogo: str) -> str:
        '''Calcola il codice fiscale di una persona a partire dai suoi dati anagrafici

        Parametri
        ---
        nome : str
            Nome della persona
        cognome : str
            Cognome della persona
        sesso : str
            Sesso della persona (M o F)
        giorno : str
            Giorno di nascita della persona (formato DD)
        mese : int
            Mese di nascita della persona (formato MM)
        anno : str
            Anno di nascita della persona (formato YYYY)
        luogo : str
            Luogo di nascita della persona
        
        Restituisce
        ---
        Codice Fiscale della persona : str
        '''
        comuniDict = self.comuniDict
        checkDict = self.checkDict

        comp1 = self.__calcolo_cognome(cognome)
        comp2 = self.__calcolo_nome(nome)
        comp3 = self.__calcolo_data(giorno, mese, anno, sesso)
        comp4 = self.__calcolo_luogo(luogo)
        comp5 = self.__calcolo_valore_check(comp1+comp2+comp3+comp4)

        codice = comp1+comp2+comp3+comp4+comp5
        return codice
    
    def __str__(self) -> str:
        return f"CalcoloCodice(comuniDict={self.comuniDict}, checkDict={self.checkDict})"
