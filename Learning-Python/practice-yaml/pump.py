from yaml.loader import SafeLoader
from transfer import get_mysql_data, insert_in_mongodb, get_csv_data, insert_in_mysql, get_mongodb_documents, \
    insert_in_mysql_from_mongodb
import yaml
import sys


def process_yaml(yaml_filename):
    with open(yaml_filename) as f:
        data = yaml.load(f, Loader=SafeLoader)

        if yaml_filename == 'pump-config-2.yaml':
            mysql_host = data['source']['host']
            mysql_port = data['source']['port']
            mysql_user = data['source']['user']
            mysql_password = data['source']['password']
            mysql_schema = data['source']['schema']
            mysql_table = data['source']['table']

            mongodb_host = data['destination']['host']
            mongodb_port = data['destination']['port']
            mongodb_schema = data['destination']['schema']
            mongodb_collection = data['destination']['collection']

            batch_size = data['pump']['batch_size']
            batch_error = data['pump']['on_error']

            documents = get_mysql_data(mysql_table, mysql_host, mysql_port, mysql_user, mysql_password, mysql_schema)
            insert_in_mongodb(documents, mongodb_host, mongodb_port, mongodb_schema, mongodb_collection)

        elif yaml_filename == 'pump-config-3.yaml':
            csv_location = data['source']['location']

            mysql_host = data['destination']['host']
            mysql_port = data['destination']['port']
            mysql_user = data['destination']['user']
            mysql_password = data['destination']['password']
            mysql_schema = data['destination']['schema']
            mysql_table = data['destination']['database']

            data = get_csv_data(csv_location)
            insert_in_mysql(data, mysql_schema, mysql_table, mysql_host, mysql_port, mysql_user, mysql_password)

        elif yaml_filename == 'pump-config-4.yaml':
            mongodb_host = data['source']['host']
            mongodb_port = data['source']['port']
            mongodb_schema = data['source']['schema']
            mongodb_collection = data['source']['collection']

            data = get_mongodb_documents(mongodb_host, mongodb_port, mongodb_schema, mongodb_collection)
            insert_in_mysql_from_mongodb(data)


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
