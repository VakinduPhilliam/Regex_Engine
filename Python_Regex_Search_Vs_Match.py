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
# search() vs. match()
# Python offers two different primitive operations based on regular expressions: re.match() checks for a match only at the beginning of the string, while
# re.search() checks for a match anywhere in the string (this is what Perl does by default).
# 
# For example:
# 

re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match

# OUTPUT: <re.Match object; span=(2, 3), match='c'>

# 
# Regular expressions beginning with '^' can be used with search() to restrict the match at the beginning of the string:
# 

re.match("c", "abcdef")    # No match
re.search("^c", "abcdef")  # No match

re.search("^a", "abcdef")  # Match


# OUTPUT: '<re.Match object; span=(0, 1), match='a'>'
 
#
# Note however that in MULTILINE mode match() only matches at the beginning of the string, whereas using search() with a regular expression beginning
# with '^' will match at the beginning of each line.
# 

re.match('X', 'A\nB\nX', re.MULTILINE)  # No match
re.search('^X', 'A\nB\nX', re.MULTILINE)  # Match

# OUTPUT: '<re.Match object; span=(4, 5), match='X'>'
