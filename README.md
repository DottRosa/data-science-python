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
Il programma si collega a tutti i siti specificati nel file di testo sites.txt, elabora l'html ed estrapola tutti gli indirizzi email presenti. L'espressione regolare tiene anche conto di indirizzi email privi della '@' ma con la dicitura '[at]'. Al termine della ricerca, se c'è almeno un risultato, la struttura dati può essere salvata in un file .pickle per usi futuri. Un esempio di esecuzione:

```python
Risutalti: 
http://www.units.it

	{'ateneo@pec.units.it'}
https://www.uniud.it

	{'urp@uniud.it'}
https://www.uniud.it/it/didattica/contatti-e-sedi

	{'studenti@uniud.it', 'segreteria.biotecnologie@uniud.it', 'segreteria.scienze@uniud.it', 'segreteria.ingegneria@uniud.it', 'cort@uniud.it', 'segreteria.formazione@uniud.it', 'segreteria.medicina@uniud.it', 'amce@postacert.uniud.it', 'segreteria.lettere@uniud.it', 'segreteria.agraria@uniud.it', 'segreteria.giurisprudenza@uniud.it', 'segreteria.cepo@uniud.it', 'segreteria.lingue@uniud.it', 'segreteria.cego@uniud.it', 'urp@uniud.it', 'segreteria.economia@uniud.it'}
http://www.sedefvg.rai.it/dl/portali/site/articolo/ContentItem-cf26ae7b-1f49-4a6a-ae1f-fad4a732d46a.html

	{'daniela.grison@rai.it', 'mario.mirasola@rai.it', 'piero.pieri@rai.it', 'marina.devescovi@rai.it', 'dario.caroli@rai.it', 'p.pieri@rai.it', 'stefania.demaria@rai.it', 'c.brugnetta@rai.it', 'd.caroli@rai.it', 'd.picoi@rai.it', 'f.toffoli@rai.it', 'maria.pedone@rai.it', 'luigi.zannini@rai.it', 'gioia.meloni@rai.it', 'daniela.picoi@rai.it', 'massimo.gobessi@rai.it', 'fulvio.toffoli@rai.it', 'assunta.cannata@rai.it', 'tgrfvg@rai.it', 'claudia.brugnetta@rai.it', 'a.cannata@rai.it', 'maddalena.lubini@rai.it', 'l.zannini@rai.it', 'tiziana.toglia@rai.it', 'd.grison@rai.it', 'a.busletta@rai.it', 'm.mirasola@rai.it', 'alessandra.busletta@rai.it'}
http://www.regione.fvg.it/rafvg/cms/RAFVG/
	{'regione.friuliveneziagiulia@certregione.fvg.it'}
```
