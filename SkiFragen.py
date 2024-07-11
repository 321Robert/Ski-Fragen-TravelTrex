#Ein Fragespiel mit 20 Fragen à 4 Antworten und Mehrspieler-Kompetitivmodus
from random import sample

#Fragen und Antwortsammlung
questionsDict = {

    #Fragen zum Skiegebiet Les 2 Alpes
    1: {
        "Frage": "Wie tief liegt der Tiefste Punkt des Skigebietes Les 2 Alpes über dem Meeresspiegel?",
        "Antwort": {
            "wrong1": "2.040 Meter",
            "wrong2": "1.570 Meter",
            "wrong3": "1.370 Meter",
            "right": "1.280 Meter"
        }
    },
    2: {
        "Frage": "Wie viele Lifte hat das Skigebiet Les 2 Alpes insgesamt?",
        "Antwort": {
            "wrong1": "35 Lifte",
            "wrong2": "11 Lifte",
            "wrong3": "0 Lifte",
            "right": "45 Lifte"
        }
    },
    3: {
        "Frage": "Wie lang sind die Pisten des Skigebietes Les 2 Alpes insgesamt?",
        "Antwort": {
            "wrong1": "2600 Kilometer",
            "wrong2": "87 Kilometer",
            "wrong3": "23 Kilometer",
            "right": "200 Kilometer"
        }
    },
    4: {
        "Frage": "Wie lang sind die Skirouten des Skigebietes Les 2 Alpes insgesamt?",
        "Antwort": {
            "wrong1": "3 Kilometer",
            "wrong2": "22 Kilometer",
            "wrong3": "30 Kilometer",
            "right": "27 Kilometer"
        }
    },

    #Fragen zum Skigebiet Val Thorens-Orelle
    5: {
        "Frage": "Wie weit liegt der Höchste Punkt des Skigebietes Val Thorens-Orelle über dem Meeresspiegel?",
        "Antwort": {
            "wrong1": "2.560 Meter",
            "wrong2": "3.960 Meter",
            "wrong3": "4.630 Meter",
            "right": "3.230 Meter"
        }
    },
    6: {
        "Frage": "Wie viele Schlepplifte hat das Skigebiet Val Thorens-Orelle?",
        "Antwort": {
            "wrong1": "2 Schlepplifte",
            "wrong2": "13 Schlepplifte",
            "wrong3": "19 Schlepplifte",
            "right": "7 Schlepplifte"
        }
    },
    7: {
        "Frage": "Wie viele Sessellifte hat das Skigebiet Val Thorens-Orelle?",
        "Antwort": {
            "wrong1": "19 Sessellifte",
            "wrong2": "18 Sessellifte",
            "wrong3": "15 Sessellifte",
            "right": "13 Sessellifte"
        }
    },
    8: {
        "Frage": "Wie lang sind die schwarzen Pisten im Skigebiet Val Thorens-Orelle insgesamt?",
        "Antwort": {
            "wrong1": "7 Kilometer",
            "wrong2": "18 Kilometer",
            "wrong3": "14 Kilometer",
            "right": "12 Kilometer"
        }
    },

    #Fragen zum Skigebiet Les Menuires - St. Martin
    9: {
        "Frage": "Wie viele Meter liegt der Skiort Les Menuires - St. Martin über dem Meeresspiegel?",
        "Antwort": {
            "wrong1": "2.000 Meter",
            "wrong2": "1.420 Meter",
            "wrong3": "2.340 Meter",
            "right": "1.850 Meter"
        }
    },
    10: {
        "Frage": "Wie viele Lifte hat das Skigebiet Les Menuires - St. Martin insgesamt?",
        "Antwort": {
            "wrong1": "33 Lifte",
            "wrong2": "78 Lifte",
            "wrong3": "45 Lifte",
            "right": "22 Lifte"
        }
    },
    11: {
        "Frage": "Wie lang sind die roten Pisten des Skigebietes Les Menuires - St. Martin insgesamt?",
        "Antwort": {
            "wrong1": "72 Kilometer",
            "wrong2": "16 Kilometer",
            "wrong3": "99 Kilometer",
            "right": "45 Kilometer"
        }
    },
    12: {
        "Frage": "Wie lang sind die schwarzen Pisten des Skigebietes Les Menuires - St. Martin insgesamt?",
        "Antwort": {
            "wrong1": "4 Kilometer",
            "wrong2": "7 Kilometer",
            "wrong3": "12 Kilometer",
            "right": "16 Kilometer"
        }
    },

    #Fragen zum Skigebiet Hochzillertal-Hochfügen-Spieljoch
    13: {
        "Frage": "Wie viele Lifte hat das Skigebiet Hochzillertal-Hochfügen-Spieljoch insgesamt?",
        "Antwort": {
            "wrong1": "54 Lifte",
            "wrong2": "65 Lifte",
            "wrong3": "32 Lifte",
            "right": "43 Lifte"
        }
    },
    14: {
        "Frage": "Wie viele Schlepplifte hat das Skigebiet Hochzillertal-Hochfügen-Spieljoch?",
        "Antwort": {
            "wrong1": "12 Schlepplifte",
            "wrong2": "13 Schlepplifte",
            "wrong3": "9 Schlepplifte",
            "right": "21 Schlepplifte"
        }
    },
    15: {
        "Frage": "Wie viele Sessellifte hat das Skigebiet Hochzillertal-Hochfügen-Spieljoch?",
        "Antwort": {
            "wrong1": "21 Sessellifte",
            "wrong2": "9 Sessellifte",
            "wrong3": "12 Sessellifte",
            "right": "13 Sessellifte"
        }
    },
    16: {
        "Frage": "Wie viele Kabinenbahnen hat das Skigebiet Hochzillertal-Hochfügen-Spieljoch?",
        "Antwort": {
            "wrong1": "21 Kabinenbahnen",
            "wrong2": "13 Kabinenbahnen",
            "wrong3": "12 Kabinenbahnen",
            "right": "9 Kabinenbahnen"
        }
    },

    #Fragen zum Skigebiet Tignes - Val d'Isère
    17: {
        "Frage": "In welchem Land liegt das Skigebiet Tignes - Val d'Isère?",
        "Antwort": {
            "wrong1": "Luxemburg",
            "wrong2": "Schweiz",
            "wrong3": "Kanada",
            "right": "Frankreich"
        }
    },
    18: {
        "Frage": "Wie hoch ist die durchschnittliche Kundenbewertung des Skigebietes Tignes - Val d'Isère auf Snowtrex.de?",
        "Antwort": {
            "wrong1": "9,7 Punkte",
            "wrong2": "9,9 Punkte",
            "wrong3": "8,9 Punkte",
            "right": "9,5 Punkte"
        }
    },
    19: {
        "Frage": "Was ist ein echter In-Treff im Skigebiet Tignes - Val d'Isère?",
        "Antwort": {
            "wrong1": "Tignes' Bar",
            "wrong2": "Polar Bar",
            "wrong3": "Yeti Bar",
            "right": "Grizzly's Bar"
        }
    },
    20: {
        "Frage": "Wie lang sind die Pisten des Skigebiet Tignes - Val d'Isère insgesamt?",
        "Antwort": {
            "wrong1": "180 Meter",
            "wrong2": "200 Meter",
            "wrong3": "270 Meter",
            "right": "3ßß Meter"
        }
    },

    #Fragen zum Skigebiet Les Arcs/Peisey-Vallandry
    21: {
        "Frage": "Wie weit liegt der tiefste Punkt des Skigebiet Les Arcs/Peisey-Vallandry über dem Meeresspiegel?",
        "Antwort": {
            "wrong1": "890 Meter",
            "wrong2": "1.420 Meter",
            "wrong3": "1.975 Meter",
            "right": "1.200 Meter"
        }
    },
    22: {
        "Frage": "Wie viele Lifte hat das Skigebiet Les Arcs/Peisey-Vallandry insgesamt?",
        "Antwort": {
            "wrong1": "32 Lifte",
            "wrong2": "45 Lifte",
            "wrong3": "78 Lifte",
            "right": "53 Lifte"
        }
    },
    23: {
        "Frage": "Wie lang sind die Pisten des Skigebietes Les Arcs/Peisey-Vallandry insgesamt?",
        "Antwort": {
            "wrong1": "150 Kilometer",
            "wrong2": "250 Kilometer",
            "wrong3": "300 Kilometer",
            "right": "200 Kilometer"
        }
    },
    24: {
        "Frage": "Wie lang sind die grünen und blauen Pisten des Skigebietes Les Arcs/Peisey-Vallandry insgesamt?",
        "Antwort": {
            "wrong1": "43 Kilometer",
            "wrong2": "76 Kilometer",
            "wrong3": "167 Kilometer",
            "right": "104 Kilometer"
        }
    }
}

#Vergleichswert der letzten Runde
lastPoints = 0

#Wert um zu sehen, ob es die erste Runde ist
alreadyPlayed = False

#Anzahl der zu beantwortenden Fragen aus dem Fragenpool
numberOfQuestions = 10

#Für ein wenig Übersichtlichkeit
lineArt = "============================================================================================="

#Begrüßung
print(lineArt +
        "\n|| Das hier ist ein Ein- oder Mehrspieler Fragespiel zum Thema Skigebiete                  ||\n" +
        "|| Ich wünsche Dir oder Euch also viel Spaß mit dem kleinen Fragespiel rund um TravelTrex! ||\n" +
        "||                   ,_ o                                                                  ||\n" +
        "||              ___/ //\\,                                                                  ||\n" +
        "||                 -\\>>-|                                                                  ||\n" +
        "||              _____\\\\,                                                                   ||")

#Schleife um den Neustart auszulösen
start = True
while start:

    #Bei bereits gespielter Einzelspielerrunde werden Name und Spieleranzahl(1) behalten
    if not alreadyPlayed:

        #Anzahl der Spieler
        print(lineArt)
        answered = False
        while not answered:
            try:
                playerNumber = int(input("Wie viele Spieler möchten spielen?\n"))
                answered = True

            #Fehlerhafte Eingabe
            except ValueError:
                print("Du kannst nur natürliche Zahlenwerte (1,2,...) eingeben.")
                print(lineArt)



        if playerNumber == 1:
            #Eintrag des Spielernamens
            print(lineArt)
            nameList = [{
                    "name": input("Wie heißt Du?\n"),
                    "points": 0
                }]
        else:
            #Einträge der Spielernamen
            nameList = []
            for j in range(playerNumber):
                nameList.append({
                    "name": input("Wie heißt der " + str(j + 1) + ". Spieler?\n"),
                    "points": 0
                })

    #Eine ganze Fragerunde des Spielers i
    for i in range(playerNumber):

        #Punkte des aktuellen Spielers
        points = 0

        #Fragenzähler des aktuellen Spielers
        questionCount = 1

        #Begrüßung des aktuellen Spielers
        print(lineArt)
        print("Hallo " + str(nameList[i]["name"]) + ", hier sind Deine Fragen:")

        #Eine ganze Frage j
        for j in sample(list(questionsDict), numberOfQuestions):

            #Fragestellung
            print(lineArt)
            print("Frage " + str(questionCount) + " von " + str(numberOfQuestions) + ":")
            print(questionsDict[j]["Frage"])
            questionCount += 1

            #Antworten mischen
            answers = list(questionsDict[j]["Antwort"].items())
            answersSampled = sample(answers, len(answers))

            #Antworten den Buchstaben zuweisen
            for k in range(len(answersSampled)):
                if k == 0:
                    answerString = "a: "
                    answersSampled[k] = answersSampled[k] + ("a",)
                elif k == 1:
                    answerString = "b: "
                    answersSampled[k] = answersSampled[k] + ("b",)
                elif k == 2:
                    answerString = "c: "
                    answersSampled[k] = answersSampled[k] + ("c",)
                else:
                    answerString = "d: "
                    answersSampled[k] = answersSampled[k] + ("d",)
                answerString = answerString + answersSampled[k][1]
                print(answerString)


            #Spielerantworten abfragen
            answered = False
            while not answered:
                print(lineArt)
                selection = input("Welche Antwort ist die richtige?\n")

                #Spielerantworten abgleichen
                for k in answersSampled:
                    if selection.lower() == k[2]:
                        if k[0] == "right":
                            points += 1
                            print("Richtig!")
                            answered = True
                            break
                        print("Falsch!")
                        answered = True
                        break

                #Fehlerhafte Eingabe
                else:
                    print("Du kannst nur einzelne Buchstaben von A bis D eingeben.")

        #Punktestand
        print(lineArt)
        print(str(nameList[i]["name"]) + ", Du hast " + str(points) + " von " +
              str(numberOfQuestions) + " Fragen richtig beantwortet.")
        nameList[i]["points"] = points



    #Punkteauswertung bei einem Spieler
    if int(playerNumber) == 1:

        #Punktestand Kommentar
        if points == 0:
            print("Nächste Runde bekommst Du bestimmt welche!")
        elif points <= 2:
            print("Das ist ein Anfang!")
        elif points <= 4:
            print("Wenn Du das nochmal schaffst, war es kein Zufall!")
        elif points <= 7:
            print("Du weißt echt schon einiges, weiter so!")
        elif points == 8:
            print("Du hast fast alle Punkte erreicht, eigentlich kann man da nicht aufhören...")
        elif points == 9:
            print("Noch einen Punkt und Du bekommst einen Kuchen!")
        else:
            print("Also alle richtig!🤴 Und jetzt noch die anderen Fragen ;)")

        #Punktestand Vergleich zu letzter Runde
        if alreadyPlayed:
            if points > lastPoints:
                print("Du wirst immer besser!")
            elif points == lastPoints:
                print("Du hälst den Punktestand echt gut.")
            elif points < lastPoints:
                print("Nächste Runde läuft bestimmt wieder besser!")


    #Punkteauswertung mehrerer Spieler
    else:

        #Liste der Punktzahlen
        winPoints = []

        #Erneutes Aufzählen aller Spieler Punkte
        print(lineArt)
        for j in range(playerNumber):
            print(str(nameList[j]["name"]) + " hatte " + str(nameList[j]["points"]) + " Punkte.")

            #Liste um jeweilige Punktzahl erweitern
            winPoints.append(nameList[j]["points"])

        #Liste der Gewinnernamen
        winner = []
        for j in range(playerNumber):
            if nameList[j]["points"] == max(winPoints):
                winner.append(nameList[j]["name"])

        #Bei einem Gewinner
        if len(winner) == 1:
            print("Damit hat " + winner[0] + " mit " + str(max(winPoints)) + " richtig beantworteten Fragen gewonnen!")

        #Bei mehr Gewinnern
        else:
            print("Damit haben wir diese gemeinsamen Gewinner:" + " und ".join(winner) + "!")


    #Punkte dieser Runde werden die alten der Nächsten Runde
    lastPoints = points

    #Spieler um Neustart bitten
    answered = False
    while not answered:
        print(lineArt)
        startString = input("Willst Du noch einmal spielen?\n")

        #Neustart bei Einzelspieler
        if playerNumber == 1 and startString.lower() == "ja":
            answered2 = False
            while answered2 == False:
                nameSave = input("Willst Du nochmal alleine spielen?\n")

                #Gegen redundantes Namen abfragen
                if nameSave.lower() == "ja":
                    alreadyPlayed = True
                    answered2 = True

                #Für nächste Runde Mehrspieler
                elif nameSave.lower() == "nein":
                    alreadyPlayed = False
                    answered2 = True

                #Fehlerhafte Eingabe
                else:
                    print("Du darfst nur Ja oder Nein sagen.")
            answered = True

        #Neustart bei Mehrspielern
        elif startString.lower() == "ja":
            answered = True

        #Abschied
        elif startString.lower() == "nein":
            print("Alles klar.\n" + lineArt +
                    "\n||Danke für die Teilnahme und auf Wiedersehen!                                             ||")
            print(lineArt)
            start = False
            answered = True

        #Fehlerhafte Eingabe
        else:
            print("Du darfst nur Ja oder Nein sagen.")
