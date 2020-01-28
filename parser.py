# File to user=defined string parser

'''
===========================================
|    Author : Yokesh                      |
|    Email  : y.subramanian@keele.ac.uk   |
===========================================
args in: file_name, type = 'file_type', delete = [], start = [], end = [], both = [], lower_case = boolean
file_name : Name of the file with extension as string
path   : only specify if the file is in a different directory, input as string
type   : 'txt' or 'pdf'
delete : Removes the char everywhere in the string_list
start  : Removes the char at the start of string_list but not everywhere, ideal for ['-else', '.html'] = ['else', 'html']
end    : Removes the char at the end of string_list but not everywhere, ideal for ['more,' 'done.'] = ['more', 'done']
both   : Removes the char at either ends. If both is defined, start and end lists are redundant
No packages required unless you wish to parse strings from pdf, then the only requirement is the package 'tika'
Note: tika requires java 7+ to run
pdf_text_extract courtesy: tika Dev team
'''

import pdf_parser as pdf


def parser(file_name, path = None, type = None, delete = None, start = None, end = None, both = None, lower_case = True):

    if type is None or type not in ['txt', 'pdf']:
        return "Error: pass a valid file type ---> 'txt' or 'pdf'"

    path, error = path_finder(file_name, path)
    if error:
        return 0

    delete, start, end, both = initialize(delete, start, end, both)
    string_list = string_strip(path, type)
    analyse_string(string_list, delete, start, end, lower_case)

    print_list(string_list)
    return string_list


# Sorting out file path
def path_finder(file_name, path):
    if path is None:
        path = file_name
    else:
        path = path + '\\' + file_name

    error = False
    try:
        f = open(path)
        f.close()
    except IOError as e:
        print("\nError : Don't panic, just check your file path or name\n", e)
        error = True
    return path, error

# Make sufficient changes to the replace char controls
def initialize(delete, start, end, both):
    if delete is not None:
        if both is None:
            for char in delete:
                if char in start:
                    start.remove(char)
                if char in end:
                    end.remove(char)
        else:
            for char in delete:
                if char in both:
                    both.remove(char)
            start = []
            end = []
            for char in both:
                start.append(char)
                end.append(char)
    elif both is not None:
        start = []
        end = []
        for char in both:
            start.append(char)
            end.append(char)

    return delete, start, end, both


# Strip lines into individual strings
def string_strip(path, type):

    if type == 'txt':
        raw_data = open(path, "r").read()
    else:
        raw_data = pdf.pdf_parser(path)

    raw_list = raw_data.splitlines()
    string_list = []
    for i in raw_list:
        if len(i) != 0:
            string_list.extend(i.split())
    return string_list


# Analyse and filter strings
def analyse_string(string_list, delete, start, end, lower_case):
    delete_items = []  # To delete null items in the string_list

    # If there is something in delete list
    if delete is not None:
        for i in range(0, len(string_list)):
                for char in delete:
                    string_list[i] = string_list[i].replace(char, '')

    # Main loop
    for i in range(0, len(string_list)):
        skip_item = False  # skip all loops

        # skip null or number items
        if len(string_list[i]) == 0 or string_list[i].isdigit():
            skip_item = True
            delete_items.append(i)
        elif not skip_item:
            # end char removal
            while string_list[i][-1] in end:
                string_list[i] = string_list[i][:-1]
                if len(string_list[i]) == 0:
                    skip_item = True
                    delete_items.append(i)
                    break
            # start char removal
            if not skip_item:
                while string_list[i][0] in start:
                    string_list[i] = string_list[i][1:]
                    if len(string_list[i]) == 0:
                        skip_item = True
                        delete_items.append(i)
                        break

    string_list = delete_null_items(string_list, delete_items)
    if lower_case:
        list_lower(string_list)

    return string_list


# Sorting is redundant since iteration through an ascending loop
def delete_null_items(string_list, delete_items):
    if len(delete_items) > 0:
        offset = 0
        for i in delete_items:
            del string_list[int(i) - offset]
            offset += 1
    return string_list


# Switch all strings to lowercase, reduces space complexity in case of something like Trie
def list_lower(string_list):
    for i in range(0, len(string_list)):
        string_list[i] = string_list[i].lower()
    return string_list


# Print items in a list line-by-line
def print_list(string_list, index = None, sep = None):

    if index is None and sep is None:
        for i in range(0, len(string_list)):
            print("list[%d]:" % i, "---->", string_list[i])
    else:
        for i in range(0, len(string_list)):
            print("list[%d]:" % i, sep, string_list[i])

    return 0


# A substitute for copy.copy()
def copy(input_list):
    output_list = []
    for item in input_list:
        output_list.append(item)
    return output_list


if __name__ == "__main__":
    Path = 'some_dir'
    parser('file_name', path = Path, type = 'pdf', both = [',', '.', '-'])
