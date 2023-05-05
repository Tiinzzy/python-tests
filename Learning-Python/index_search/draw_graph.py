import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, graph_data, file_name):
        self.__graph_data = graph_data
        self.__file_name = file_name

    def graph(self):
        chart_name = self.__file_name.replace('.csv', '')
        df = pd.read_csv(self.__graph_data, parse_dates=['Date'])
        df = df.sort_values(by=['Date'])
        df = df.set_index(df.Date)

        plt.figure(figsize=(20, 12))
        plt.scatter(x=df.index, y=df.Low, s=0.1)
        plt.grid(True)
        plt.scatter(x=df.index, y=100 + df.High, s=0.1)
        plt.xlabel('Date', labelpad=35)
        plt.ylabel('High', labelpad=35)
        plt.title('The highest and lowest price of ' + chart_name, pad=35)
        plt.show()

        # plt.figure(1, figsize=(20, 6))
        # plt.subplot(211)
        # plt.scatter(x=df.index, y=df.High, s=0.1, c='steelblue')
        # plt.xlabel('Date')
        # plt.ylabel('High')
        # plt.subplot(212)
        # plt.scatter(x=df.index, y=df.Low, s=0.1, c='red')
        # plt.xlabel('Date')
        # plt.ylabel('High')
        # plt.show()
