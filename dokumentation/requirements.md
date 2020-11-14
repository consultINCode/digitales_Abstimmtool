# Requirements

Enthält alle benötigen Funktionen die die Application abbilden soll.

## Persons
### getAllPersons()
Gibt alle Benutzer zurück die in der Anwendung hinterlegt sind.

### getAllPersonsCheckedIn()
Gibt alle als anwesend makierten Benutzer zurück.

### getAllPersonsCheckedOut()
Gibt alle als abwesend makierten Benutzer zurück.

### approveMinimalVoters()
Überprüft ob Mindesanzahl an Wähler für eine MV vorhanden sind

### createPerson(Person)
Bekommt als Parameter mehrer Werte um eine Person anzulegen.

### deletePerson(Person)
Entfernt einen Benutzer aus der Anwendung

### generatePassword()
Generiert ein Passwort für einen Benutzer

### resetPassword()
Zurücksetzen eines Passworts

### checkInForElectionRound(ElectionRound)
Anwesenheit für einen Wahlgang bestätigen

### checkOutFromElectionRound(ElectionRound)
Sich von einem Wahlgang abmelden

## Election Rounds

### createElectionRound()
Erstellt eine Wahlrunde

### getAllElectionRounds()
gibt alle Wahlrunden zurück

### getAllOpenElections()
git alle Wahlrunden zurück die aktive sind

### closeOpenElectionRound(ElectionRound)
Schließt eine Wahlrunde 

### CheckIfElectionRoundIsOpen()
Prüft ob die Wahlrunde noch offen ist

### addChoiceToELectionRound(Choice)
Fügt Wahlmöglichkeiten der Wahlrunde hinzu.

### getResultofElectionRound()
Gibt das Ergebnis der Wahlrunde zurück

## Has Voted

### setVote(ElectionRound, Person)
Person hat erfolgreich für diese Wahl abgestimmt

### getAllPersonsWhoVoted(ElectionRound)
Gibt alle Personen zurück die in der Wahlrunde schon gewählt haben

### getALlPersonsWhoHaveNotVoted(ElectionRound)
Gibt alle Personen zurück die noch Nicht gewählt haben

## Choices
### setPicture()
Ermöglicht ein Bild hochzuladen/ zu ändern

### createChoice(Choice)
Option erstellen

### deleteChoice(Choice)
Löscht eine Option

### updateChoice(Choice)
Option bearbeiten

### updateVotes(ChoiceId, Votes)
Zählt die Stimmen einer Option hoch

## Has_Choice

### createChoiceProxy(Sender, Receiver)
Stimmübertragung von Sender zu Receiver erstellen

### deleteChoiceProxy(ChoiceProxy)
Löscht eine Stimmübertragung

### updateChoiceProxy(Sender, Receiver)
Stimmübertragung für Sender bearbeiten und neuen Receiver eintragen

### checkChoiceProxy