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
# If the regular expression uses the (?P<name>...) syntax, the groupN arguments may also be strings identifying groups by their group name.
# If a string argument is not used as a group name in the pattern, an IndexError exception is raised.
# 
# An example:
# 

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
m.group('first_name')

# OUTPUT: 'Malcolm'

m.group('last_name')

# OUTPUT: 'Reynolds'

# 
# Named groups can also be referred to by their index:
# 

m.group(1)

# OUTPUT: 'Malcolm'

m.group(2)

# OUTPUT: 'Reynolds'
 
#
# If a group matches multiple times, only the last match is accessible:
# 

m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
m.group(1)                        # Returns only the last match.

# OUTPUT: 'c3'
