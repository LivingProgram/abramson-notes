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
    elif key == 'def':
        return parse_def(value)
    elif key == 'theorem':
        return parse_theorem(value)
    elif key == 'p':
        return parse_p(value)
def parse_title1(value): # 'Inverse Function Applications'
    new_lines = []
    new_lines.append('      <h3><a id="{}" href="#{}">{}</a></h3>\n'.format(value.lower().replace(" ", "_"),value.lower().replace(" ", "_"),value))
    return new_lines
def parse_def(value): # takes the first bolded only
    new_lines = []
    assert value.find('\\b(') != -1 # make sure you have something bolded
    start_idx = value.find('\\b(')
    #end_p_idx = value.split('\\b(')[-1].find(')')
    # grab everything after '\\b(' and iteratively look at each char, add 1 a counter if it is a '(' and subtract 1 from counter if it is a ')'
    # every loop over char, check to make sure counter == -1, if it =-1 then that ')' has to be the idx of the close of the '\\b('
    p_counter = 0
    for idx, char in enumerate(value.split('\\b(')[-1]):
        if char == '(':
            p_counter+=1
        if char == ')':
            p_counter-=1
        if p_counter == -1:
            end_p_idx = idx
            break
    end_idx = start_idx+3 + end_p_idx +1
    term = value[start_idx+3:end_idx-1]
    new_lines.append('      <p><a id="def_{}" href="#def_{}"><strong>Def:</strong></a> {}</p>\n'.format(term,term,value[:start_idx]+'<strong>'+term+'</strong>'+value[end_idx:]))
    return new_lines
def parse_theorem(value): # assumes you give one name, statement, and proof
    new_lines = []
    for dict_1 in value: # unpacking dictionary values
        assert len(dict_1) == 1
        key, value_1 = list(dict_1.items())[0]
        if key == 'name':
            theorem_name = value_1
        elif key == 'statement':
            theorem_statement = value_1
        elif key == 'proof':
            proof_lines = value_1
    new_lines.append('      <p><a id="{}" href="#{}"><strong>Theorem:</strong></a> {}</p>\n'.format(theorem_name,theorem_name,theorem_statement))
    new_lines.append('      <p>\n')
    new_lines.append('        <strong>Proof:</strong>\n')
    for line in proof_lines:
        assert line.count('\\e ') <= 1 # line can have at most one explanation, i.e. a single '\e '
        if line.count('\\e ') == 1:
            line,line_explanation = line.split('\\e ')
        else:
            line_explanation = None # must make it none or else it will be the previous line's explanation
        # here you can do something with the explanation for specific lines of the proof


        if line[0:3] == '\\t ': # append pure text proof lines
            assert line.count('\\t ') <= 1 # line should only have one of these special strings
            new_lines.append(line.split('\\t ')[1] + '\n')
        else: # append math proof lines
            new_lines.append('        $${}$$\n'.format(line))
    new_lines.append('      </p>\n')
    return new_lines
def parse_p(value):
    new_lines = []
    for line in value:
        new_lines.append('      <p>\n')
        new_lines.append('      ' + line + '\n')
        new_lines.append('      </p>\n')
    return new_lines

if __name__ == '__main__':
    with open("./index_data.mybad", 'r') as stream:
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
    dict_0_keys_list = ['title1','def','theorem','p']
    for dict_0 in data: # 0 space indent dictionaries
        assert len(dict_0) == 1 # make sure there is only one key, value pair per dict_0
        key, value = list(dict_0.items())[0]
        assert key in dict_0_keys_list # make sure key is recognizable
        for key_type in dict_0_keys_list:
            if key == key_type:
                new_lines = parse_key(key,value)
        all_new_lines += new_lines
    # insert new lines
    html_lines = html_lines[:div_start_idx+1] + all_new_lines + html_lines[div_end_idx:]

    # write the new list of lines to the file
    with open("./index.html", "w") as html_file:
        html_lines = "".join(html_lines)
        html_file.write(html_lines)