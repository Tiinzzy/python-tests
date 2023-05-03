def extract_indexes(data):
    unique_indexes = []
    for d in data:
        if d["\ufeffIndex"] not in unique_indexes:
            unique_indexes.append(d["\ufeffIndex"])
    print(unique_indexes)