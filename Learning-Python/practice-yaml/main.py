import sys
import yaml
from yaml.loader import SafeLoader

import find_filled_jobs_csv_csv as etl_csv


def process_yaml(yaml_filename):
    with open(yaml_filename) as f:
        data = yaml.load(f, Loader=SafeLoader)
        if data['source']['data_base_type'] == 'csv' and data['destination']['data_base_type'] == 'csv':
            etl_csv.run(data['source']['location'],
                        data['destination']['location'],
                        data['pump']['batch_size'],
                        data['pump']['on_error'])
        elif data['source']['data_base_type'] == 'mysql' and data['destination']['data_base_type'] == 'mongodb':
            pass


if __name__ == '__main__':

    if len(sys.argv) < 1:
        print("You need to pass the name of the config.yaml as the parameter.")
    else:
        yaml_file = sys.argv[1]
        try:
            process_yaml(yaml_file)
        except Exception as e:
            print(e)
            print("Can not open " + yaml_file + "file!")
