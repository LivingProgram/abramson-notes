import yaml
from pprint import pprint

def convert_to_yaml(stream):
    # insert a - in front of every line
    yaml_string = ''
    for line in stream:
        leading_spaces = len(line) - len(line.lstrip(' '))
        yaml_string += line[:leading_spaces] + '- ' + line[leading_spaces:]
    return yaml_string
    

if __name__ == '__main__':
    with open("./index_data.yaml", 'r') as stream:
        data = yaml.load(convert_to_yaml(stream))
        pprint(data)