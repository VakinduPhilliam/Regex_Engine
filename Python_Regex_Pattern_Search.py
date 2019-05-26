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
# Pattern.search(string[, pos[, endpos]]). 
# Scan through string looking for the first location where this regular expression produces a match, and return a corresponding match object.
# Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.
# 
# The optional second parameter pos gives an index in the string where the search is to start; it defaults to 0. This is not completely equivalent to
# slicing the string; the '^' pattern character matches at the real beginning of the string and at positions just after a newline, but not necessarily
# at the index where the search is to start.
# 
# The optional parameter endpos limits how far the string will be searched; it will be as if the string is endpos characters long, so only the characters
# from pos to endpos - 1 will be searched for a match. If endpos is less than pos, no match will be found; otherwise, if rx is a compiled regular expression
# object, rx.search(string, 0, 50) is equivalent to rx.search(string[:50], 0).
# 

pattern = re.compile("d")
pattern.search("dog")     # Match at index 0

# OUTPUT: '<re.Match object; span=(0, 1), match='d'>'

pattern.search("dog", 1)  # No match; search doesn't include the "d"
