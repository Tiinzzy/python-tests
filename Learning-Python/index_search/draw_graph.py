import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, graph_data):
        self.__graph_data = graph_data

    def graph(self):
        df = pd.read_csv(self.__graph_data)
        print(df)

        x_axis_date = df.Date.unique()

        # xpoints = np.array(x_axis_date)
        # ypoints = np.array([3, 8, 1, 10])
        # plt.plot(xpoints, ypoints)
        # plt.show()
