import os
import csv
import time
import datetime

class Csv:

    def __init__(self, file_path):
        self.__file_path = file_path

    def extract_csv_data(self):

        data = []
        close_price = []
        open_price = []
        min_value = []
        max_value = []
        
        with open(self.__file_path) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if row[0] >= str(time.mktime(datetime.datetime.strptime('2012-01-01', "%Y-%m-%d").timetuple())) and row[0] <= str(time.mktime(datetime.datetime.strptime('2020-01-01', "%Y-%m-%d").timetuple())):
                    if 'NaN' not in row:
                        open_price.append(row[1])
                        close_price.append(row[2])
                        min_value.append(row[3])
                        max_value.append(row[4])
                        #print(', '.join(row))

        return open_price, close_price, min_value, max_value

class Candle:
    
    def __init__(self, date, frequency, open_value, close_value, max_value, min_value):
        self.date = date
        self.frequency = frequency
        self.open_value = open_value
        self.close_value = close_value
        self.max_value = max_value
        self.min_value = min_value
    
    def draw_candle_graph(self):
        pass

    def get_candle(self):
        return(f'O preço de abertura do candle foi {self.open_value}, o preço de fechamento do candle foi {self.close_value}')

class Indicador:

    def __init__(self, numero_periodos, desvio_padrao=0):
        self.numero_periodos = numero_periodos
        self.desvio_padrao = desvio_padrao
    
    def calculate_simple_moving_average(self):
        i = 0
        moving_averages = []
        while i < len(numbers) - self.numero_periodos + 1:
            this_window = numbers[i : i + self.numero_periodos]
            window_average = sum(this_window) / self.numero_periodos
            moving_averages.append(window_average)
            i += 1

def main():
    arquivo_csv = Csv('bitstamp.csv')

    open_price, close_price, min_value, max_value = arquivo_csv.extract_csv_data()

    candles = Candle(1255448, 5, open_price, close_price, min_value, max_value)
    print(candles.get_candle())

if __name__ == '__main__':
    main()
