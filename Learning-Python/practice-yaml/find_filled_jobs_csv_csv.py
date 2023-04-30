import pandas as pd
import os.path
import sys


def row_to_str(row):
    result = []
    for c in row:
        result.append(str(c))
    return ','.join(result) + '\n'


def save_batch(batch, filename):
    with open(filename, 'a') as f:
        for row in batch:
            f.write(row_to_str(row))


def run(source_file, destination_file, batch_size, on_error):
    if not os.path.isfile(source_file) and on_error == 'stop':
        sys.exit("Bad source file path!")
    else:
        source_df = pd.read_csv(source_file)

    try:
        with open(destination_file, 'w') as f:
            f.write(','.join(source_df.columns) + '\n')
    except Exception as e:
        if on_error == 'stop':
            print(e)
            sys.exit("Can not create destination file!")

    batch = []
    batch_count = 0
    for index, row in source_df.iterrows():
        if row['Series_title_1'].startswith('Filled jobs'):
            batch.append(row)
            if len(batch) == batch_size:
                batch_count += 1
                try:
                    save_batch(batch, destination_file)
                except Exception as e:
                    if on_error == 'stop':
                        print(e)
                        sys.exit("problem writing data batch #" + str(batch_count))
                batch = []

    if len(batch) > 0:
        batch_count += 1
        save_batch(batch, destination_file)
