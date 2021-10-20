from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
# pyside6-uic .\Gui_main5.ui -o Gui_main5.py
from DesignOrdner.Gui_main5 import Ui_MainWindow
import csv
import webbrowser

font = QtGui.QFont()
font.setPointSize(11)
file = open('ExelMappe1.CSV', newline='')

fragen_csv = csv.DictReader(file, delimiter=';')
glob = {"index": 0, "fragenNummer": 2, "eingabe": 3}


class Fragen():
    def __init__(self, frage, spalte1, spalte2, umgekehrteSpalte):
        self.frage = frage
        self.persönlichkeitsSpalte1 = spalte1
        self.persönlichkeitsSpalte2 = spalte2
        self.umgekehrtePersönlichkeitsSpalte = umgekehrteSpalte


fragen_feld = [
    Fragen("Das Leben gelingt, besser wenn man das Positive sieht, anstatt sich am Negativen aufzuhalten", 6, -1, -1)]
antwort_speicher_feld = []
rechner_liste = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# die fragenFeld Liste wird mit der csv Datei aufgefüllt
for item in fragen_csv:
    fragen_feld.append(Fragen(item['Frage'], int(item['spalte1']), int(item['spalte2']), int(item['umgekehrt'])))


# Testet ob die Eingabe ein integer ist und zwischen eisnchließlich 0 und 6 liegt
def richtige_eingabe_test(eingabe) -> bool:
    if eingabe.isnumeric():
        if int(eingabe) <= 6 and int(eingabe) >= 0:
            return True
        else:
            return False
    else:
        return False

# löscht den EingabeWert
def persönlichkeit_spalte_hinzufuegen(eingabe, spalte):
    if (spalte != -1):
        rechner_liste[spalte] += int(eingabe)


def umgekehrte_persoenlichkeit_hinzufuegen(eingabe, spalte):
    if (spalte != -1):
        rechner_liste[spalte] += fragen_wert_umkehren(int(eingabe))

    # speichert die Antwortwerte


def persoenlichkeit_spalte_abziehen(eingabe, spalte):
    if (spalte != -1):
        rechner_liste[spalte] -= int(eingabe)


def umgekehrte_persoenlichkeit_abziehen(eingabe, spalte):
    if (spalte != -1):
        rechner_liste[spalte] -= fragen_wert_umkehren(int(eingabe))


def ende():
    print("Ende")

    # Speichert die werte in die Passende spalte vom FragenRechner


def antwort_speichern(index, eingabe):
    if index <= len(fragen_feld):
        persönlichkeit_spalte_hinzufuegen(eingabe, fragen_feld[index].persönlichkeitsSpalte1)
        persönlichkeit_spalte_hinzufuegen(eingabe, fragen_feld[index].persönlichkeitsSpalte2)
        umgekehrte_persoenlichkeit_hinzufuegen(eingabe, fragen_feld[index].umgekehrtePersönlichkeitsSpalte)
        print(rechner_liste)
    else:
        ende()


def fragen_wert_umkehren(eingabe) -> int:
    zahl = int(eingabe)
    if zahl == 0:
        return 6
    elif zahl == 1:
        return 5
    elif zahl == 2:
        return 4
    elif zahl == 3:
        return 3
    elif zahl == 4:
        return 2
    elif zahl == 5:
        return 1
    elif zahl == 6:
        return 0


def typen_anzeigen():
    webbrowser.open_new(
        r'file://C:\Users\joshu\PycharmProjects\PersönlichkeitsTest\Enneagramm Kurzbeschreibung-gedreht.pdf')


# gibt den PersönlichkeitsTyp mit der hoechsten uebereinstimmung zurueck
def hoechsten_typ_geben() -> str:
    groeßterWert = 0
    groeßterWertIndex = 0
    for i in range(0, len(rechner_liste)):

        if (rechner_liste[i] > groeßterWert):
            groeßterWert = rechner_liste[i]
            groeßterWertIndex = i + 1

    return "Hoechste Übereinstimmung: Typ: " + str(groeßterWertIndex)


def ende(ausgabeString) -> str:
    ausgabeString = ""
    zähler = 0
    while (zähler < 8):
        ausgabeString += "Persönlichkeit Typ " + str(zähler + 1) + ") " + str(
            rechner_liste[zähler]) + "       Persönlichkeit Typ" + str(zähler + 2) + ") " + str(
            rechner_liste[zähler + 1]) + "\n"
        zähler += 2
    ausgabeString += "Persönlichkeit Typ 9) " + str(rechner_liste[8]) + "\n" + hoechsten_typ_geben()
    return ausgabeString


def rechen_feld_abziehen(frage, abzieh_wert):
    persoenlichkeit_spalte_abziehen(abzieh_wert, frage.persönlichkeitsSpalte1)
    persoenlichkeit_spalte_abziehen(abzieh_wert, frage.persönlichkeitsSpalte2)
    umgekehrte_persoenlichkeit_abziehen(abzieh_wert, frage.umgekehrtePersönlichkeitsSpalte)


class Frm_main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Persönlichkeit Test")
        self.fragenLabel.setText("1) " + fragen_feld[0].frage)
        self.fragenLabel.setFont(font)
        self.weiterButton.clicked.connect(self.weiter)
        self.zurueckButton.clicked.connect(self.zurueck)
        self.eingabeLabel.setText("3")
        self.horizontalSlider.setRange(0, 6)
        self.horizontalSlider.setSliderPosition(3)
        self.horizontalSlider.valueChanged.connect(self.eingabe_wert_setzen)
        self.progressBar.setValue(0)

    def eingabe_wert_setzen(self, eingabe):
        self.eingabeLabel.setText(str(eingabe))
        glob["eingabe"] = eingabe

    def weiter(self):
        eingabe = glob["eingabe"]
        if (glob["index"] < len(fragen_feld) - 1):

            self.fragenLabel.setText(str(glob["fragenNummer"]) + ") " + fragen_feld[glob["index"] + 1].frage)
            antwort_speichern(glob["index"], eingabe)
            glob["index"] += 1
            glob["fragenNummer"] += 1
            antwort_speicher_feld.append(eingabe)
            print(antwort_speicher_feld)
            self.progressBar.setValue(prozent_ermitteln(self))
            self.horizontalSlider.setSliderPosition(3)

        elif glob["index"] == len(fragen_feld) - 1:
            self.fragenLabel.setText("Du hast alle Fragen beantwortet :)")
            antwort_speichern(glob["index"], eingabe)
            self.weiterButton.setText("Ergebnis Anzeigen")
            glob["index"] += 1

        else:
            self.fragenLabel.setText(ende(""))
            self.weiterButton.setText("Typen Anzeigen")
            self.weiterButton.clicked.connect(typen_anzeigen)

    # Löscht die eingabe der Letzen Frage und zeigt sie wieder an (rückgängig Methode)
    def zurueck(self):
        if glob["index"] > 0 and glob["index"] < 115:
            glob["index"] -= 1
            glob["fragenNummer"] -= 1
            self.fragenLabel.setText(str(glob["fragenNummer"] - 1) + ") " + fragen_feld[glob["index"]].frage)
            rechen_feld_abziehen(fragen_feld[glob["index"]], antwort_speicher_feld.pop())
            print(antwort_speicher_feld)
            self.progressBar.setValue(prozent_ermitteln(self))


def prozent_ermitteln(self) -> int:
    print(glob["index"])
    return glob["index"] / 114 * 100


def main():
    app = QApplication()
    frm_main = Frm_main()
    frm_main.show()
    app.exec()


#if __name__ == "__main__":

main()

