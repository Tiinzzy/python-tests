from yaml.loader import SafeLoader
from transfer import get_mysql_data, insert_in_mongodb
import yaml
import sys


def process_yaml(yaml_filename):
    with open(yaml_filename) as f:
        data = yaml.load(f, Loader=SafeLoader)

        mysql_host = data['source']['host']
        mysql_port = data['source']['port']
        mysql_schema = data['source']['schema']
        mysql_table = data['source']['table']

        mongodb_host = data['destination']['host']
        mongodb_port = data['destination']['port']
        mongodb_schema = data['destination']['schema']
        mongodb_collection = data['destination']['collection']

        batch_size = data['pump']['batch_size']
        batch_error = data['pump']['on_error']

        result = get_mysql_data(mysql_table)
        insert_in_mongodb(result)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print("Enter the name of config.yaml as the parameter.")
    else:
        yaml_file = sys.argv[1]
        try:
            process_yaml(yaml_file)
        except Exception as e:
            print(e)
            print("Can not open " + yaml_file + " file!")
