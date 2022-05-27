import re
import sys
import glob
import os
from pathlib import Path

errors = {
    1: "Too long",
    2: "Indentation is not a multiple of four",
    3: "Unnecessary semicolon",
    4: "At least two spaces required before inline comments",
    5: "TODO found",
    6: "More than two blank lines used before this line"
}


def main():
    name = sys.argv[1]
    if name.endswith('.py'):
        check_file(name)
    else:
        directory = Path(name)

        files = sorted(directory.glob('*.py'))
        for file in files:
            check_file(file)


def check_file(filename):
    empty_line_counter = 0
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file.readlines()):
            check_line(filename, line_number + 1, line)


def check_line(filename, number_of_line, line):
    for err in checkers:
        if checkers[err](line):
            print(f'{filename}: Line {number_of_line}: S00{err} {errors[err]}')


# Error S001 Too long
def check_length(line):
    return len(line) > 79


# Error S002 Indentation
def check_indentation(line):
    indentation = re.match(" +", line)
    if indentation:
        if indentation and len(indentation.group()) % 4 != 0:
            return True
    return False


# Error S003 Unnecessary semicolon
def check_semicolon(line):
    inside = re.search(r"'([^('].*)'", line)
    in_comment = re.search(r"#.*;", line)

    if inside:
        if ';' not in inside.group():
            if ';' in line and not in_comment:
                return True
    elif not in_comment and ';' in line:
        return True


# Error S004 Less than two spaces before inline comments
def check_comments(line):
    if line.find('#') != -1:
        # Check if inline comment
        if not line[:line.find('#')].isspace() and not line.find('#') == 0:
            if line[line.index('#') - 2:line.index('#')] != '  ':
                return True


# Error S005 TODO found
def check_todo(line):
    match = re.search(r"#.*todo", line, flags=re.IGNORECASE)
    if match:
        return True


# Error S006 More than two blank lines preceding a code line
def check_blank_lines(line):
    global empty_line_counter

    line_empty = line.rstrip('\n') == ""
    if not line_empty and empty_line_counter > 2:
        empty_line_counter = 0
        return True
    if line_empty:
        empty_line_counter += 1


checkers = {
    1: check_length, 2: check_indentation, 3: check_semicolon,
    4: check_comments, 5: check_todo, 6: check_blank_lines
}

if __name__ == '__main__':
    main()
