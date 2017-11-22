import yaml
from pprint import pprint

def convert_to_yaml(stream):
    # the rule is: if the line does not have a known key then it will be regarded as a list element
    yaml_string = ''
    for line in stream:
        if line.lstrip(' ').split(': ')[0] not in ALL_KEYS:
            leading_spaces = len(line) - len(line.lstrip(' '))
            yaml_string += line[:leading_spaces] + '- ' + line[leading_spaces:]
            #print(line[:leading_spaces] + '- ' + line[leading_spaces:])
        else:
            yaml_string += line
    return yaml_string
    

if __name__ == '__main__':
    ALL_KEYS = ['title1','def','theorem','name','statement','proof'] # list of known keys
    with open("./index_data.yaml", 'r') as stream:
        data = yaml.load(convert_to_yaml(stream)) # treats the first indent as dictionary, takes only unique keys
        # yaml.load each first indent separately 
        pprint(data)