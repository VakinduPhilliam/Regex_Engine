# Python Regex
# re — Regular expression operations.
# This module provides regular expression matching operations similar to those found in Perl.
# Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes).
# However, Unicode strings and 8-bit strings cannot be mixed: that is, you cannot match a Unicode string with a byte pattern or vice-versa; similarly,
# when asking for a substitution, the replacement string must be of the same type as both the pattern and the search string.
# Regular expressions use the backslash character ('\') to indicate special forms or to allow special characters to be used without invoking their
# special meaning. This collides with Python’s usage of the same character for the same purpose in string literals; for example, to match a literal
# backslash, one might have to write '\\\\' as the pattern string, because the regular expression must be \\, and each backslash must be expressed
# as \\ inside a regular Python string literal.
#
# Writing a Tokenizer:
# 
# A tokenizer or scanner analyzes a string to categorize groups of characters. This is a useful first step in writing a compiler or interpreter.
# 
# The text categories are specified with regular expressions. The technique is to combine those into a single master regular expression and to loop over
# successive matches:
# 

import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}

    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    line_num = 1
    line_start = 0

    for mo in re.finditer(tok_regex, code):

        kind = mo.lastgroup
        value = mo.group()

        column = mo.start() - line_start

        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)

        elif kind == 'ID' and value in keywords:
            kind = value

        elif kind == 'NEWLINE':
            line_start = mo.end()

            line_num += 1

            continue

        elif kind == 'SKIP':
            continue

        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')

        yield Token(kind, value, line_num, column)

statements = '''

    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;

    ENDIF;
'''

for token in tokenize(statements):
    print(token)
