# data-science-python

Una raccolta di programmi in linguaggio Python che utilizzano la Data Science per l'elaborazione dei dati e il loro utilizzo.

## name_generator
Utilizzando dei dataset reperiti online ho costruito un file .csv contenente oltre 4000 nomi italiani maschili e femminili e la loro frequenza per anno.
Il programma fonde due nomi casuali creandone uno nuovo. Un esempio:

```python
Numero di nomi da generare: 10
ALENORA
	['ALESSIO', 'ELEONORA']
ALEO
	['ALICE', 'LEO']
CARTIANO
	['CARMINE', 'CRISTIANO']
MICSINE
	['MICHAEL', 'YASSINE']
LAINA
	['LARA', 'MARINA']
BEATESSA
	['BEATRICE', 'VANESSA']
MOHORIA
	['MOHAMED', 'VICTORIA']
ENRIGI
	['ENRICO', 'LUIGI']
MAOLO'
	['MAYA', "NICOLO'"]
SIMIA
	['SIMONA', 'ASIA']
```

## mail_extractor
Il programma si collega a tutti i siti specificati nel file di testo sites.txt, elabora l'html ed estrapola tutti gli indirizzi email presenti. L'espressione regolare tiene anche conto di indirizzi email privi della '@' ma con la dicitura '[at]'. Al termine della ricerca, se c'è almeno un risultato, la struttura dati può essere salvata in un file .pickle per usi futuri.

## dictionary
Con questo progetto voglio creare un dizionario delle parole italiane (più di 600.000 parole). Tra le varie risorse sarà possibile accedere ai seguenti dizionari python:

...Chiave: la parola stessa; Valore: la lunghezza della parola
...Chiave: la lunghezza delle parole; Valore: array di parole della medesima lunghezza
...Chiave: la parola stessa; Valore: dizionario contente la lunghezza e la parola divisa in sillabe
...Chiave: il numero di sillabe delle parole; Valore: array di parole che hanno lo stesso numero di sillabe

All'interno della libreria verranno fornite diverse funzioni atte all'ottenimento di particolari informazioni riguardo le parole (per esempio ottenere tutte le parole la cui ultima sillaba è 'de').
Esempio di codice:

```python
from italianwords import Words
import utils.output as out

# Istanzio l'oggetto che accederà direttamente ai dizionari appropriati
words = Words()

# Tutte le parole che terminano con la sillaba 'de'
out.printlist(words.get_by_last_syllable("de"))

# Ottengo le sillabe della parola 'azalea'
print(words.get_syllables("azalea"))

```
