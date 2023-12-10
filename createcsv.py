import csv
import arrow
import pandas as pd

def create_csv(valores: list):
    date = arrow.utcnow()
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    print(valores)
    with open(f'{year}{month}{day}rapmexspotop.csv', 'w') as file:
        df = pd.DataFrame(valores)
        df.to_csv(f'{month}{year}{day}toprapspoti.csv', index=False, header=False)
        # for key in valores.keys():
            # file.write("%s, %s\n" % (key, valores[key]))
