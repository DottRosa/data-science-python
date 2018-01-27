import re
from utils.connection import Connection
import utils.output as out
import utils.pickling as pick

conn = Connection()

sites = open("sites.txt", 'r')
mails = {}
regex = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
regexAt = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*\[at\](?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
regexAt2 = "[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)* \[at\] (?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

for site in sites:
    print("Elaboro ", site)
    html = conn.getpage(site)
    mails[site] = set(re.findall(r""+regex+"", html) + re.findall(r""+regexAt+"", html) + re.findall(r""+regexAt2+"", html))

print("\n\nRisutalti: ")
out.printhash(mails)

if len(mails.items()) > 0 and input("Salvare in .pickle? INVIO per rifiutare, qualsiasi tasto e poi INVIO per accettare: "):
    pick.savepickle("mails.pickle", mails)
