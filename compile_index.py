import yaml
from pprint import pprint

def convert_to_yaml(stream):
    # insert a - in front of every line
    yaml_string = ''
    for line in stream:
        leading_spaces = len(line) - len(line.lstrip(' '))
        yaml_string += line[:leading_spaces] + '- ' + line[leading_spaces:]
    return yaml_string

def parse_key(key,value):
    if key == 'title1':
        return parse_title1(value)
    if key == 'def':
        return parse_def(value)
    if key == 'theorem':
        return parse_theorem(value)
def parse_title1(value): # 'Inverse Function Applications'
    new_lines = []
    new_lines.append('      <h3><a id="{}" href="#{}">{}</a></h3>\n'.format(value.lower().replace(" ", "_"),value.lower().replace(" ", "_"),value))
    return new_lines
def parse_def(value): # takes the first bolded only
    new_lines = []
    assert value.find('\\b(') != -1 # make sure you have something bolded
    start_idx = value.find('\\b(')
    end_idx = start_idx+3 + value.split('\\b(')[-1].find(')')+1
    term = value[start_idx+3:end_idx-1]
    new_lines.append('      <p><a id="def_{}" href="#def_{}">Def:</a> {}</p>\n'.format(term,term,value[:start_idx]+'<strong>'+term+'</strong>'+value[end_idx:]))
    return new_lines
def parse_theorem(value):
    return ['theorem']

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
    all_new_lines = []
    dict_0_keys_list = ['title1','def','theorem']
    for dict_0 in data: # 0 space indent dictionaries
        assert len(dict_0) == 1 # make sure there is only one key, value pair per dict_0
        key, value = list(dict_0.items())[0]
        assert key in dict_0_keys_list # make sure key is recognizable
        for key_type in dict_0_keys_list:
            if key == key_type:
                new_lines = parse_key(key,value)
        all_new_lines += new_lines
    pprint(all_new_lines)
    # insert new lines
    html_lines = html_lines[:div_start_idx+1] + all_new_lines + html_lines[div_end_idx:]

    pprint(html_lines)
    # write the new list of lines to the file
    with open("./index.html", "w") as html_file:
        html_lines = "".join(html_lines)
        html_file.write(html_lines)