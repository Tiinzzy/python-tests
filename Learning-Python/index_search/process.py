def extract_indexes(data):
    unique_indexes = []
    for d in data:
        if d["\ufeffIndex"] not in unique_indexes:
            unique_indexes.append(d["\ufeffIndex"])

    save_in_separate_files(unique_indexes, data)


def save_in_separate_files(unique_indexes, data):
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
