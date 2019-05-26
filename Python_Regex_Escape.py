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
# re.escape(pattern). 
# Escape special characters in pattern. This is useful if you want to match an arbitrary literal string that may have regular expression metacharacters
# in it.
#
# For example:
# 

print(re.escape('python.exe'))

# OUTPUT: 'python\.exe'

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"

print('[%s]+' % re.escape(legal_chars))

# OUTPUT: '[abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+'

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))

# OUTPUT: '/|\-|\+|\*\*|\*'
