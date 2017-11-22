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

    # open html file with all its lines
    with open("./index.html", "r") as html_file:
        html_lines = html_file.readlines()

    # delete all the lines starting from '    <div class="section">' to the very next '    </div>', there should not be any '    </div>' inbetween
    # get the indexes of the div section for now, later remove it
    div_start_idx = 0
    for idx, line in enumerate(html_lines):
        if line == '    <div class="section">\n':
            div_start_idx = idx
        if div_start_idx != 0:
            if line == '    </div>\n':
                div_end_idx = idx
                break

    # create new lines
    new_lines = ['a','b','c']
    
    # insert new lines
    html_lines = html_lines[:div_start_idx+1] + new_lines + html_lines[div_end_idx:]

    # write the new list of lines to the file
    #with open("./index.html", "w") as html_file:
    #    html_lines = "".join(html_lines)
    #    html_file.write(html_lines)