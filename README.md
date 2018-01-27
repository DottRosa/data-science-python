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
