import csv


def extract_indexes(data):
    unique_indexes = []
    for d in data:
        if d["\ufeffIndex"] not in unique_indexes:
            unique_indexes.append(d["\ufeffIndex"])

    get_collections(unique_indexes, data)


def get_collections(unique_indexes, data):
    finalized_data = {}
    for index in unique_indexes:
        finalized_data[index] = []

    for i in range(len(data)):
        row_list = list(data[i].values())
        if unique_indexes[0] in row_list:
            finalized_data[unique_indexes[0]].append(data[i])
        elif unique_indexes[1] in row_list:
            finalized_data[unique_indexes[1]].append(data[i])
        elif unique_indexes[2] in row_list:
            finalized_data[unique_indexes[2]].append(data[i])
        elif unique_indexes[3] in row_list:
            finalized_data[unique_indexes[3]].append(data[i])
        elif unique_indexes[4] in row_list:
            finalized_data[unique_indexes[4]].append(data[i])
        elif unique_indexes[5] in row_list:
            finalized_data[unique_indexes[5]].append(data[i])
        elif unique_indexes[6] in row_list:
            finalized_data[unique_indexes[6]].append(data[i])
        elif unique_indexes[7] in row_list:
            finalized_data[unique_indexes[7]].append(data[i])
        elif unique_indexes[8] in row_list:
            finalized_data[unique_indexes[8]].append(data[i])
        elif unique_indexes[9] in row_list:
            finalized_data[unique_indexes[9]].append(data[i])
        elif unique_indexes[10] in row_list:
            finalized_data[unique_indexes[10]].append(data[i])
        elif unique_indexes[11] in row_list:
            finalized_data[unique_indexes[11]].append(data[i])
        elif unique_indexes[12] in row_list:
            finalized_data[unique_indexes[12]].append(data[i])
        elif unique_indexes[13] in row_list:
            finalized_data[unique_indexes[13]].append(data[i])

    save_collections_as_csv(finalized_data, unique_indexes)


def save_collections_as_csv(data, file_names):
    columns = []
    for d in data:
        columns = list(data[d][0].keys())

    for i in range(len(file_names)):
        path = '/home/tina/Documents/python/python-tests/Learning-Python/index_search/extracted_data/' + file_names[
            i] + '.csv'
        with open(path, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(columns)
            for row in data[file_names[i]]:
                writer.writerow(list(row.values()))
