import yaml
from pprint import pprint

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_spaces(line):
    return int(len(line) - len(line.lstrip(' ')))

if __name__ == '__main__':
    """
    with open("./index_data.yaml", 'r') as stream:
        lines_dict = {}
        for line_id, line in enumerate(stream.readlines()):
            # compile lines_dictionary with id = line number, space = number of inital spaces, line = 'str of line'
            num_spaces = len(line) - len(line.lstrip(' '))
            lines_dict[line_id]= [num_spaces, line]
        #pprint(lines_dict)
        # generate unique list of number of initial spaces
        spaces_list = []
        for line_id in lines_dict:
            spaces_list.append(lines_dict[line_id][0])
        spaces_set = set(spaces_list)
        # check that it has to be even, if not raise error there is an odd number
        for num_spaces in spaces_list:
            if num_spaces % 2 != 0:
                raise ValueError('odd number of spaces detected in indent')

        final_list = []
        spaces_list = sorted(spaces_set) # make sure number spaces are sorted
        spaces_list=[0] # for testing
        for num_spaces in spaces_list: # loop over list of number of inital spaces
            lines_list = []
            counter = 0
            for line_id in lines_dict:
                if lines_dict[line_id][0] == num_spaces:
                    if counter == 1: # if you find a line with space = number, and counter = 1, final_list.append({index:list}, index=line,list=0,counter=1
                        final_list.append({next_index:lines_list})
                        lines_list = []
                    # if you find a line with space = number, add 1 to counter, set index = line
                    counter = 1
                    next_index = lines_dict[line_id][1]
                else:
                    lines_list.append(lines_dict[line_id][1])
                    # if this is the last line, append
                    if line_id + 1 == len(lines_dict):
                        final_list.append({next_index:lines_list})
        # after compiling it, change all keys with empty lists into correct format
        #for key in final_list:
        #    if final_list[key] == []:
        #        new_key,data = key.split(': ')
        #        final_list
        #        final_list.remove(key)
            pprint(final_list)
                # then go into second indents, 
    """
    with open("./index_data.yaml", 'r') as stream:
        saved_stream = [] # need to do this or else you cannot loop multiple times over stream
        # generate unique list of number of initial spaces
        spaces_list = []
        for line in stream:
            spaces_list.append(get_spaces(line))
            saved_stream.append(line)
        spaces_set = set(spaces_list)

        # check that it has to be even, if not raise error there is an odd number
        for num_spaces in spaces_list:
            if num_spaces % 2 != 0:
                raise ValueError('odd number of spaces detected in indent')

        final_list = []
        spaces_list = sorted(spaces_set, reverse=True) # make sure lowest 
        spaces_list = spaces_list[1:] # remove the lowest layer
        spaces_list = [2]
        for num_spaces in spaces_list:
            lines_list = []
            counter = 0
            line_counter = 0
            total_lines = file_len('./index_data.yaml')
            for line in saved_stream: # this loop is not getting run, cannot loop over stream twice?
                line_counter += 1
                print(line_counter)
                if get_spaces(line) == num_spaces:
                    if counter == 1: 
                        if lines_list == []: # takes care of case when you do not have list
                            key,value = next_index.split(': ')
                            final_list.append({key:value})
                        else:
                            final_list.append({next_index:lines_list})
                            lines_list = []
                        next_index = line
                    else:
                        counter = 1
                    next_index = line
                elif get_spaces(line) < num_spaces:
                    if 'next_index' in globals():
                        final_list.append({next_index:lines_list}) # this break because first line triggers this
                        lines_list = []
                    final_list.append(line)
                else:
                    lines_list.append(line)

                if line_counter == total_lines:
                    if lines_list == []: # if you end on no lines list
                        key,value = line.split(': ')
                        final_list.append({key:value})
                    else: # if you end on nonempty lines list
                        final_list.append({next_index:lines_list})
        pprint(final_list)
                