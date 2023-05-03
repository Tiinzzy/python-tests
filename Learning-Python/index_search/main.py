from process import extract_indexes
import sys
import csv


def read_csv(file):
    content = []
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)

        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)

    return content


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Enter the name of config.yaml as the parameter.")
    else:
        file_name = sys.argv[1]
        try:
            data = read_csv(file_name)
            extract_indexes(data)
        except Exception as e:
            print(e)
            print("Can not open " + file_name + " file!")
