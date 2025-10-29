import datetime as dt
from ppdc_timed_generator import Generador

gen = Generador(dt.time(7, 0), dt.time(20, 0))
print(gen)
