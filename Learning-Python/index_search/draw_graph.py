import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class DrawGraph:
    def __init__(self, graph_data, file_name):
        self.__graph_data = graph_data
        self.__file_name = file_name

    def single_graph(self):
        chart_name = self.__file_name.replace('.csv', '')
        df = pd.read_csv(self.__graph_data, parse_dates=['Date'])
        df = df.sort_values(by=['Date'])
        df = df.set_index(df.Date)

        plt.figure(figsize=(20, 12))
        plt.scatter(x=df.index, y=df.Low, s=0.1)
        plt.grid(True)
        plt.scatter(x=df.index, y=100 + df.High, s=0.1)
        plt.xlabel('Date', labelpad=15)
        plt.ylabel('Highest & Lowest Price', labelpad=15)
        plt.title('The highest and lowest price of ' + chart_name, pad=30)

        plt.plot([1, 2, 3])
        plt.plot([5, 6, 7])
        plt.legend(['Low', 'High'])
        plt.savefig('./easy_output/' + chart_name + '-1-image.png', dpi=300)
        plt.show()
        plt.close()

    def double_comparison_graph(self):
        chart_name = self.__file_name.replace('.csv', '')
        df = pd.read_csv(self.__graph_data, parse_dates=['Date'])
        df = df.sort_values(by=['Date'])
        df = df.set_index(df.Date)

        plt.figure(1, figsize=(20, 10))
        plt.subplot(211)
        plt.scatter(x=df.index, y=df.High, s=0.1, c='steelblue')
        plt.title('The highest price of ' + chart_name, pad=15)
        plt.grid(True)
        plt.xlabel('Date', labelpad=15)
        plt.ylabel('Highest Price', labelpad=15)
        plt.plot([1, 2, 3])
        plt.legend(['Highest'])

        plt.subplot(212)
        plt.scatter(x=df.index, y=df.Low, s=0.1, c='red')
        plt.title('The lowest price of ' + chart_name, pad=15)
        plt.grid(True)
        plt.xlabel('Date', labelpad=15)
        plt.ylabel('Lowest Price', labelpad=15)
        plt.plot([5, 6, 7])
        plt.legend(['Lowest'])

        plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1)
        plt.savefig('./easy_output/' + chart_name + '-2-image.png', dpi=300)
        plt.show()
        plt.close()

    def quadruple_comparison_graph(self):
        chart_name = self.__file_name.replace('.csv', '')
        df = pd.read_csv(self.__graph_data, parse_dates=['Date'])
        df = df.sort_values(by=['Date'])
        df = df.set_index(df.Date)

        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.set_size_inches(10, 5)
        fig.suptitle('The highest, lowest, opening & closing price of ' + chart_name)

        ax1.scatter(x=df.index, y=df.High, s=0.1, label="Highest Price")
        ax1.grid(True)
        ax1.legend(loc='upper left')

        ax2.scatter(x=df.index, y=df.Low, c='orange', s=0.1, label="Lowest Price")
        ax2.grid(True)
        ax2.legend(loc='upper left')

        ax3.scatter(x=df.index, y=df.Open, c='green', s=0.1, label="Opening Price")
        ax3.grid(True)
        ax3.legend(loc='upper left')

        ax4.scatter(x=df.index, y=df.Close, c='red', s=0.1, label="CLosing Price")
        ax4.grid(True)
        ax4.legend(loc='upper left')

        for ax in fig.get_axes():
            ax.label_outer()

        plt.savefig('./easy_output/' + chart_name + '-4-image.png', dpi=300)
        plt.show()
        plt.close()
