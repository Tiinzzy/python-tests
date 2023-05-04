import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, graph_data):
        self.__graph_data = graph_data

    def graph(self):
        df = pd.read_csv(self.__graph_data)
        # print(df)

        x_axis_date = df.Date.unique()
        y_axis_open = df.High.to_numpy()
        y_axis_close = df.Low.to_numpy()
        #
        x_points = np.array(x_axis_date)
        y_point_1 = np.array(y_axis_open)
        y_point_2 = np.array(y_axis_close)

        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        ax1.plot(x_points, y_point_1, 'b-')
        ax2.plot(x_points, y_point_2, 'r-')

        plt.show()


