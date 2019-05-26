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
# Match.groups(default=None): 
#
# Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern.
# The default argument is used for groups that did not participate in the match; it defaults to None.
# 
# For example:
# 

m = re.match(r"(\d+)\.(\d+)", "24.1632")
m.groups()

# OUTPUT: ('24', '1632')

# 
# If we make the decimal place and everything after it optional, not all groups might participate in the match.
# These groups will default to None unless the default argument is given:
# 

m = re.match(r"(\d+)\.?(\d+)?", "24")
m.groups()      # Second group defaults to None.

# OUTPUT: ('24', None)

m.groups('0')   # Now, the second group defaults to '0'.

# OUTPUT: ('24', '0')
