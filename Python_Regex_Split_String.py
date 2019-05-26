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
# re.split(pattern, string, maxsplit=0, flags=0). 
# Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned
# as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element
# of the list.
 
re.split(r'\W+', 'Words, words, words.')

# OUTPUT: ['Words', 'words', 'words', '']

re.split(r'(\W+)', 'Words, words, words.')

# OUTPUT: ['Words', ', ', 'words', ', ', 'words', '.', '']

re.split(r'\W+', 'Words, words, words.', 1)

# OUTPUT: ['Words', 'words, words.']

re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)

# OUTPUT: ['0', '3', '9']
 
#
# If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string.
# The same holds for the end of the string:
# 

re.split(r'(\W+)', '...words, words...')

# OUTPUT: ['', '...', 'words', ', ', 'words', '...', '']
 
#
# That way, separator components are always found at the same relative indices within the result list.
# 
# Empty matches for the pattern split the string only when not adjacent to a previous empty match.
# 

re.split(r'\b', 'Words, words, words.')

# OUTPUT: ['', 'Words', ', ', 'words', ', ', 'words', '.']

re.split(r'\W*', '...words...')

# OUTPUT: ['', '', 'w', 'o', 'r', 'd', 's', '', '']

re.split(r'(\W*)', '...words...')

# OUTPUT: ['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', ''
