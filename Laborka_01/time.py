import calendar
from time import process_time
start = process_time()

calendar = calendar.month(4288, 5)
print("Kalendarz dla miesiąca maj, roku pańskiego 4288 :) ")
print(calendar)

end = process_time() - start
print("Czas wykonywania programu wyniósł " + str(end) + "s")