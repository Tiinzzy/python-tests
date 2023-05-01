from yaml.loader import SafeLoader
import yaml
import sys


def process_yaml(yaml_filename):
    with open(yaml_filename) as f:
        data = yaml.load(f, Loader=SafeLoader)
        print(data)


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
