import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, graph_data):
        self.__graph_data = graph_data

    def graph(self):
        df = pd.read_csv(self.__graph_data, parse_dates=['Date'])
        df = df.sort_values(by=['Date'])
        df = df.set_index(df.Date)

        plt.figure(figsize=(20, 12))
        plt.scatter(x=df.index, y=df.Low, s=0.1)
        plt.grid(True)
        plt.scatter(x=df.index, y=100+df.High, s=0.1)
        plt.show()

        plt.figure(1, figsize=(20, 6))
        plt.subplot(211)
        plt.scatter(x=df.index, y=df.High, s=0.1, c='steelblue')
        plt.subplot(212)
        plt.scatter(x=df.index, y=df.Low, s=0.1, c='red')
        plt.show()
