import time
import datetime
localtime = time.localtime(time.time())

print(localtime)

minuta=60

godzina=60*minuta

dni=24*godzina

rok=365*dni

rokprzestepny=366*dni



print(rok)

print(rokprzestepny," sek")



narodziny=datetime(2001,6,29,19,30)

obecna=datetime.now() - narodziny

print (obecna.total_seconds())