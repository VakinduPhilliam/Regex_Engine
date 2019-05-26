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
# Pattern.fullmatch(string[, pos[, endpos]]). 
# If the whole string matches this regular expression, return a corresponding match object. Return None if the string does not match the pattern; note
# that this is different from a zero-length match.
# 
# The optional pos and endpos parameters have the same meaning as for the search() method.
# 

pattern = re.compile("o[gh]")
pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".

pattern.fullmatch("ogre")     # No match as not the full string matches.
pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.

# OUTPUT: '<re.Match object; span=(1, 3), match='og'>'
