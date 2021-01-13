import csv
from datetime import datetime

class Csv:

    def __init__(self, file_path):
        self.__file_path = file_path

    def extract_csv_data(self):

        data = []
        close_price = []
        open_price = []
        min_value = []
        max_price = []

        with open(self.__file_path) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if datetime.fromtimestamp(row[0][:9]) >= '2012-01-01' and datetime.fromtimestamp(row[0][:9]) <= '2018-01-01':
                    if 'NaN' not in row:
                        open_price.append(row[1])
                        close_price.append(row[2])
                        min_value.append(row[3])
                        max_value.append(row[4])
                        #print(', '.join(row))

        return open_price, close_price

    def transform_timestamp_to_data(self):
        pass

class Candle:
    
    def __init__(self, period, open_value, close_value, max_value, min_value):
        self.period = period
        self.open_value = open_value
        self.close_value = close_value
        self.max_value = max_value
        self.min_value = min_value
    
    def draw_candle_graph(self):
        pass

class Indicador:

    def __init__(self, numero_periodos, desvio_padrao=0):
        self.numero_periodos = numero_periodos
        self.desvio_padrao = desvio_padrao
    
    def calculate_simple_moving_average(self):
        pass

def main():
    arquivo_csv = Csv('bitstamp.csv')

    open_price, close_price = arquivo_csv.extract_csv_data()

    candles = Candle(open_price, close_price)

if __name__ == '__main__':
    main()
