import csv
import random as random
import utils.output as out

with open("names.csv", 'r', encoding="utf8") as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    names = []
    for row in file:
        names.append(row[1])
    del names[0]

    n = input("Numero di nomi da generare: ")
    results = {}
    for i in range(0, int(n)):
        indexA = random.randint(0, len(names)-1)
        indexB = random.randint(0, len(names) - 1)

        firstPart = names[indexA][:int(len(names[indexA])/2)]
        lastPart = names[indexB][int(len(names[indexB]) / 2):]

        results[firstPart+lastPart] = [names[indexA], names[indexB]]

    out.printhash(results)
