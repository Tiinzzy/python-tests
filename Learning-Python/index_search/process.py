def extract_indexes(data):
    unique_indexes = []
    for d in data:
        if d["\ufeffIndex"] not in unique_indexes:
            unique_indexes.append(d["\ufeffIndex"])

    save_in_separate_files(unique_indexes, data)


def save_in_separate_files(unique_indexes, data):
    finalized_data = {}
    for i in range(len(data)):
        data[i]["\ufeffIndex"]
        for index in unique_indexes:
            if data[i]["\ufeffIndex"] == index:
                finalized_data[index] = data[i]
    print(finalized_data)
