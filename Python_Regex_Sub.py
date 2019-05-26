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
# re.sub(pattern, repl, string, count=0, flags=0). 
# Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl.
# If the pattern isn’t found, string is returned unchanged. repl can be a string or a function; if it is a string, any backslash escapes in it are
# processed.
# That is, \n is converted to a single newline character, \r is converted to a carriage return, and so forth. Unknown escapes such as \& are left alone.
# Backreferences, such as \6, are replaced with the substring matched by group 6 in the pattern.
#
# For example:
# 

re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
           r'static PyObject*\npy_\1(void)\n{',
           'def myfunc():')

# OUTPUT: 'static PyObject*\npy_myfunc(void)\n{'
 
#
# If repl is a function, it is called for every non-overlapping occurrence of pattern. The function takes a single match object argument, and returns the
# replacement string.
#
# For example:
# 

def dashrepl(matchobj):

        if matchobj.group(0) == '-': return ' '

        else: return '-'

    re.sub('-{1,2}', dashrepl, 'pro----gram-files')

# OUTPUT: 'pro--gram files'

re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)

# OUTPUT: 'Baked Beans & Spam'
