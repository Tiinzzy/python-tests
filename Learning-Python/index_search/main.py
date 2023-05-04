from process import extract_indexes
from draw_graph import DrawGraph
import sys
import csv
import math
import pandas as pd


def easy_process(file_name):
    df = pd.read_csv(file_name)
    index_ids = df.Index.unique()
    df.Volume = df.Volume.apply(lambda x: 0 if math.isnan(x) else int(x))
    for idx in index_ids:
        df[df.Index == idx].to_csv('./easy_output/' + idx + '.csv', index=False)


def read_csv(file):
    content = []
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        headers = [(lambda x: x.replace('\ufeff', ''))(x) for x in headers]

        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)

    return content


def direct_processing(file_name):
    try:
        data = read_csv(file_name)
        extract_indexes(data)
    except Exception as e:
        print(e)
        print("Can not open " + file_name + " file!")


def split_files():
    direct_processing(sys.argv[1])
    easy_process(sys.argv[1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py -split indexData.csv")
        print("       python main.py -chart NYA.csv")
    else:
        if sys.argv[1] == '-split':
            direct_processing(sys.argv[2])
            easy_process(sys.argv[2])
        elif sys.argv[1] == '-chart':
            print('I have to draw chart for ', sys.argv[2])
            path = '/home/tina/Documents/python/python-tests/Learning-Python/index_search/extracted_data/' + sys.argv[2]

            new_chart = DrawGraph(path)
            new_chart.graph()
