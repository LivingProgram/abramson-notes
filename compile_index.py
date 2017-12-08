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
    elif key == 'img':
        return parse_img(value)
def parse_global_key(key, value):
    if key == 'proof':
        return parse_global_proof(value)
    elif key == 'proofsum':
        return parse_global_proofsum(value)
    else:
        raise ValueError('global key not recognized')

def extract_special_command(data, command_name): # commands must always use {} and start with backslash, and be unique
    if data.count('\\{}{{'.format(command_name)) == 1:
        start_idx = data.find('\\{}{{'.format(command_name))
        counter = 0
        for idx, char in enumerate(data.split('\\{}{{'.format(command_name))[-1]):
            if char == '{':
                counter+=1
            if char == '}':
                counter-=1
            if counter == -1:
                end_b_idx = idx
                break
        end_idx = start_idx+2+len(command_name) + end_b_idx +1 # start to end yields \\b{aasdfasd}
        unstripped = data[start_idx:end_idx]
        data = data.replace(unstripped, '')
        value = unstripped[2+len(command_name):len(unstripped)-1]
        return data, value # return data stripped of specified command's value 
    else:
        assert data.count('\\{}{{'.format(command_name)) <= 1 # commands can only be used once
        return None, None 

def parse_global_proof(value): # creates proof, can support multiple proofs
    new_lines = []
    new_lines.append('      <p>\n')
    new_lines.append('        <strong>Theorem Proof:</strong>\n')
    for line in value:
        if isinstance(line, dict):
            key, value_1 = list(line.items())[0]
            if key == 'lemma': # very similar to parse_theorem code
                for dict_1 in value_1:
                    key_1, value_2 = list(dict_1.items())[0]
                    if key_1 == 'statement':
                        lemma_statement = value_2
                        global lemma_counter # refer to global lemma_counter variable
                        new_lines.append('      <p><a id="lemma_{}" href="#lemma_{}"><strong>Lemma:</strong></a> {}</p>\n'.format(lemma_counter,lemma_counter,lemma_statement))
                        lemma_counter += 1 # id for keeping track of all lemmas on entire page
                    else:
                        lemma_proof_lines = parse_global_key(key_1, value_2) # return lines of lemma proof
                        lemma_proof_lines = [line.replace('Theorem Proof:','Lemma Proof:') for line in lemma_proof_lines] # start lemma proofs with 'Lemma Proof:'
                        new_lines += lemma_proof_lines
                        new_lines.insert(len(new_lines)-1,'        <strong>Theorem Proof Continued:</strong>\n')
            else:
                # global_key parse for images within proofs
                new_lines += parse_global_key(key, value_1)
        else:
            assert line.count('\\e ') <= 1 # line can have at most one explanation, i.e. a single '\e '
            if line.count('\\e ') == 1:
                line,line_explanation = line.split('\\e ')
            else:
                line_explanation = None # must make it none or else it will be the previous line's explanation
            # here you can do something with the explanation for specific lines of the proof


            if line[0:3] == '\\t ': # append pure text proof lines
                assert line.count('\\t ') <= 1 # line should only have one of these special strings
                new_lines.append('        '+ line.split('\\t ')[1] + '\n')
            else: # append math proof lines
                new_lines.append('        $${}$$\n'.format(line))
    new_lines.append('      </p>\n')
    return new_lines
def parse_global_proofsum(value): # add option for a proof summary
    new_lines = []
    new_lines.append('      <p><strong>Proof Summary:</strong></p>\n')
    new_lines.append('      <ul>\n')
    for line in value:
        new_lines.append('        <li>{}</li>\n'.format(line))
    new_lines.append('      </ul>\n')
    return new_lines

def parse_title1(value): # 'Inverse Function Applications'
    new_lines = []
    new_lines.append('      <h3><a id="{}" href="#{}">{}</a></h3>\n'.format(value.lower().replace(" ", "_"),value.lower().replace(" ", "_"),value))
    return new_lines
def parse_def(value): # takes the first bolded only
    new_lines = []
    assert value.find('\\b{') != -1 # make sure you have something bolded
    start_idx = value.find('\\b{')
    # grab everything after '\\b{' and iteratively look at each char, add 1 a counter if it is a '(' and subtract 1 from counter if it is a ')'
    # every loop over char, check to make sure counter == -1, if it =-1 then that ')' has to be the idx of the close of the '\\b{'
    p_counter = 0
    for idx, char in enumerate(value.split('\\b{')[-1]):
        if char == '{':
            p_counter+=1
        if char == '}':
            p_counter-=1
        if p_counter == -1:
            end_p_idx = idx
            break
    end_idx = start_idx+3 + end_p_idx +1
    term = value[start_idx+3:end_idx-1]
    data, explanation = extract_special_command(value,'e')
    if data != None: # only if explanation exists append it
        new_lines.append('      <p><a id="def_{}" href="#def_{}"><strong>Def:</strong></a> {}</p>\n'.format(term,term,data[:start_idx]+'<strong>'+term+'</strong>'+data[end_idx:]))
        new_lines.append('      <p>\n')
        new_lines.append('        ' + explanation + '\n')
        new_lines.append('      </p>\n')
    else:
        new_lines.append('      <p><a id="def_{}" href="#def_{}"><strong>Def:</strong></a> {}</p>\n'.format(term,term,value[:start_idx]+'<strong>'+term+'</strong>'+value[end_idx:]))
    return new_lines
def parse_theorem(value): # assumes you give one name, statement, does not require proof, but strict order of name, statement, proofs
    new_lines = []
    all_proof_lines = []
    for dict_1 in value: # unpacking dictionary values
        assert len(dict_1) == 1
        key, value_1 = list(dict_1.items())[0]
        if key == 'name':
            theorem_name = value_1
        elif key == 'statement':
            theorem_statement = value_1
        else:
            all_proof_lines += parse_global_key(key, value_1)
            
    # if the name has a single capital letter it is a named theorem 
    uppers = [l for l in theorem_name if l.isupper()]
    if uppers != []:
        simplified_name = theorem_name.replace(' ', '_').lower()
        new_lines.append('      <p><a id="{}" href="#{}"><strong>{}:</strong></a> {}</p>\n'.format(simplified_name,simplified_name,theorem_name,theorem_statement))
    else:
        # add generic theorem tag
        new_lines.append('      <p><a id="{}" href="#{}"><strong>Theorem:</strong></a> {}</p>\n'.format(theorem_name,theorem_name,theorem_statement)) 
    new_lines += all_proof_lines
    return new_lines
def parse_p(value):
    new_lines = []
    for line in value:
        new_lines.append('      <p>\n')
        new_lines.append('        ' + line + '\n')
        new_lines.append('      </p>\n')
    return new_lines
def parse_img(value): # add image stored in github and image explanation
    new_lines = []
    for dict_1 in value:
        key, value_1 = list(dict_1.items())[0]
        if key == 'src':
            new_lines.append('      <img src="{}">\n'.format(value_1))
        elif key == 'explanation':
            new_lines.append('      <p>\n')
            new_lines.append('        <strong>Image Explanation: </strong>{}\n'.format(value_1))
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
    dict_0_keys_list = ['title1','def','theorem','p','img']
    global lemma_counter # create counter to give lemmas unique ids
    lemma_counter = 0
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