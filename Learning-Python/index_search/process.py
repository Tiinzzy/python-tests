import csv


def extract_indexes(data):
    unique_indexes = []
    for d in data:
        if d["Index"] not in unique_indexes:
            unique_indexes.append(d["Index"])

    get_collections(unique_indexes, data)


def get_collections(unique_indexes, data):
    finalized_data = {}
    for index in unique_indexes:
        finalized_data[index] = []

    for i in range(len(data)):
        row_list = list(data[i].values())
        finalized_data[row_list[0]].append(data[i])

    save_collections_as_csv(finalized_data, unique_indexes)


def save_collections_as_csv(data, file_names):
    columns = []
    for d in data:
        columns = list(data[d][0].keys())

    for i in range(len(file_names)):
        path = '/home/tina/Documents/python/python-tests/Learning-Python/index_search/extracted_data/' + \
               file_names[i] + '.csv'
        with open(path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(columns)
            for row in data[file_names[i]]:
                writer.writerow(list(row.values()))
