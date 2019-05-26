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
# Match.group([group1, ...]). 
#
# Returns one or more subgroups of the match. If there is a single argument, the result is a single string; if there are multiple arguments, the result
# is a tuple with one item per argument. Without arguments, group1 defaults to zero (the whole match is returned). If a groupN argument is zero, the
# corresponding return value is the entire matching string; if it is in the inclusive range [1..99], it is the string matching the corresponding
# parenthesized group. If a group number is negative or larger than the number of groups defined in the pattern, an IndexError exception is raised.
# If a group is contained in a part of the pattern that did not match, the corresponding result is None.
# If a group is contained in a part of the pattern that matched multiple times, the last match is returned.
 
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
m.group(0)       # The entire match

# OUTPUT: 'Isaac Newton'

m.group(1)       # The first parenthesized subgroup.

# OUTPUT: 'Isaac'

m.group(2)       # The second parenthesized subgroup.

# OUTPUT: 'Newton'

m.group(1, 2)    # Multiple arguments give us a tuple.

# OUTPUT: ('Isaac', 'Newton')
