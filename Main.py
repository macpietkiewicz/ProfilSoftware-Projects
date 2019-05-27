'''README
By program mógł działać należy ze strony podanej w zadaniu 
pobrać plik csv z danymi, zmienić jego nazwę na 'file.csv' oraz
umieścić go w katalogu razem z niniejszym skryptem.
Skrypt pisany był w środowisku PyCharm i tam też radziłbym testować program.
By wyszukać interesujące nas informacje należy zmodyfikować zmienne początkowe w każdej pętli z osobna (Year, Place,A,B).
'''



Nazwa_Pliku = 'file.csv'


#Zadanie 1
with open(Nazwa_Pliku) as File:
    Year = '2015'
    Place = 'Polska'
    Values = []
    for Line in File:
        Line = Line.split(';')
        if Line[3] >= Year and Line[1] == 'przystąpiło' and Line[0] == Place:
            Values.append(Line[4].rstrip('\n'))

    Sum = 0
    for Value in Values:
        Sum = Sum + int(Value)
    Average = Sum/len(Values)
    print(Average)


#Zadanie 2
with open(Nazwa_Pliku) as File:
    Year = '2015'
    Place = 'Polska'
    ValuesDict = {}
    PassedDict = {}
    ResultsDict = {}
    for Line in File:
        Line = Line.split(';')
        if Line[1] == 'przystąpiło' and Line[0] == Place:
            ValuesDict[Line[3]] = Line[4]
        elif Line[1] == 'zdało' and Line[0] == Place:
            PassedDict[Line[3]] = Line[4]

    for Key in ValuesDict.keys():
        ResultsDict[Key] = int(PassedDict[Key])/int(ValuesDict[Key])*100
    print(ResultsDict)


#Zadanie 3
with open(Nazwa_Pliku) as File:
    Year = '2012'
    Tekst = []
    Number = 0
    Passed = 0
    Results = {}
    Naj = 0
    for Line in File:
        Line = Line.split(';')
        Tekst.append(Line)
    for i, Line in enumerate(Tekst):
        if i == 0:
            Place = Tekst[1][0]
        if Line[0] == Place and Line[3] == Year:
            if Line[1] == 'przystąpiło':
                Number = Number + int(Line[4])
            elif Line[1] == 'zdało':
                Passed = Passed + int(Line[4])
        if i % 36 == 0 and i > 0:
            Results[Place] = Passed/Number
            Number = 0
            Passed = 0
            if i < len(Tekst) - 1:
                Place = Tekst[i + 1][0]

    Naj = 0
    Place = ''
    for Element in Results.keys():
        if Results[Element] > Naj:
            Place = Element
            Naj = Results[Element]
    print(Year + ' - ' + Place)


#Zadanie 5
with open(Nazwa_Pliku) as File:
    A = 'Lubelskie'
    B = 'Dolnośląskie'
    Results = {}
    Years = []
    Tekst = []
    for Line in File:
        Line = Line.split(';')
        Tekst.append(Line)
    for i in range(2010, 2019):
        Years.append(str(i))
    for Year in Years:
        NumberA, NumberB, PassedA, PassedB = 0, 0, 0, 0
        for Line in Tekst:
            if Line[0] == A and Line[3] == Year:
                if Line[1] == 'przystąpiło':
                    NumberA = NumberA + int(Line[4])
                elif Line[1] == 'zdało':
                    PassedA = PassedA + int(Line[4])
            elif Line[0] == B and Line[3] == Year:
                if Line[1] == 'przystąpiło':
                    NumberB = NumberB + int(Line[4])
                elif Line[1] == 'zdało':
                    PassedB = PassedB + int(Line[4])
        if PassedA / NumberA > PassedB / NumberB:
            Results[Year] = A
        else:
            Results[Year] = B

    print(Results)
